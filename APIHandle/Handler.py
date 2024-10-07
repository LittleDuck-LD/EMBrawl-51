import os
import flask,json,requests
from flask import request

from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging
from Classes.Utils.Helpers import Helpers
from Database.DatabaseHandler import DatabaseHandler

from flask_cors import CORS

apiPort = 13005
api = flask.Flask(__name__) 

def isLoginEffective(tag:str,token:str,playerData):
    
    if "APIToken" not in playerData:
        return False
    if playerData["APIToken"] == int(token):
        return True
    else:
        return False
def cf_verify(token,client_ip):
    url = "https://challenges.cloudflare.com/turnstile/v0/siteverify"
    form_data = {
        "secret": "0x4AAAAAAAi865n3MjBy88H_l1D_R3SFS-w",
        "response": token,
        "remoteip": client_ip,
    }
    resp = requests.post(url, json=form_data)
    if resp.status_code != 200:
        print("response err, verify failed")
        return False
    resp_json = json.loads(resp.content)
    if resp_json["success"]:
        return True
    else:
        print("verify failed:", resp_json)
    return False

def map_stats(stats):
    json_list = {
        "3v3": 1, "unk": 2, "trophies": 3, "highesttrophies": 4, "heros_count": 5, 
        "sd_wins": 8, "RoboRumble": 9, "dsd_wins": 11, "RaidBoss": 12, "PowerPlayPoints": 13, 
        "PowerPlayRank": 14, "championship": 15, "SuperCity": 16, "TeamRanked": 17, 
        "SoloRanked": 18, "ClubLeague": 19, "Fame": 20, "exp": 21, "HighestRank": 22, 
        "CurRank": 23, "CurrentRankScore":24, "HiggestRankScore":25, "MasterRank":26, "RegYear":27, "stars": 10000
    }
    
    result = {}
    
    for key, value in json_list.items():
        for stat in stats:
            if stat[0] == value:
                result[key] = stat[1]
                break
                
    return result
# 实例化api，把当前这个python文件当作一个服务，__name__代表当前这个python文件
class API():
    def setupAPI():
        CORS(api, resources=r'/*')
        # 'index'是接口路径，methods不写，默认get请求     
        @api.route('/editToCNAccount') 
        # get方式访问
        def editToCNAccount():
            db_instance = DatabaseHandler()
            
            if not flask.request.args.get('tag') or not flask.request.args.get('token') or not flask.request.args.get('cntag'):
                ren = {'msg':'参数缺失！','msg_code':400}
                return json.dumps(ren,ensure_ascii=False)
            if cf_verify(flask.request.args.get('cftstoken'),request.remote_addr) == False:
                ren = {'msg':'Captcha未通过！','msg_code':401}
                return json.dumps(ren,ensure_ascii=False)
            Long = Helpers.convert_player_tag_to_long(tag=flask.request.args.get('tag'))
            playerData = db_instance.getPlayer(Long)
            if isLoginEffective(flask.request.args.get('tag'),flask.request.args.get('token'),playerData) == False:
                ren = {'msg':'修改失败，Token错误！','msg_code':400}
                return json.dumps(ren,ensure_ascii=False)
            CNTag = flask.request.args.get('cntag')
            Response = requests.get(f"https://127.0.0.1:13000/v1/getprofilebytag?tag={CNTag}",verify=False)
            if Response.status_code!=200:
                ren = {'msg':f'请求错误！({Response.status_code})，如果你确定你的标签没有错误，请重试！','msg_code':400}
                return json.dumps(ren,ensure_ascii=False)
            CNData = Response.json()
            OwnedBrawlersInCN = []

            stats = map_stats(CNData["stats"])
            playerData["stats_3v3"] = stats["3v3"]
            playerData["stats_showdown"] = stats["sd_wins"]
            playerData["stats_duoshowdown"] = stats["dsd_wins"]
            playerData["stats_robo_rumble"] = stats["RoboRumble"]
            playerData["stats_robo"] = stats["RaidBoss"]
            playerData["stats_city_rampage"] = stats["SuperCity"]
            playerData["stats_challenge"] = stats["championship"]
            playerData["stats_3v3rank"] = stats["TeamRanked"]
            playerData["stats_solorank"] = stats["SoloRanked"]
            playerData["stats_clubwars"] = stats["ClubLeague"]
            playerData["stats_Fame"] = stats["Fame"]
            playerData["Experience"] = stats["exp"]
            playerData["Trophies"] = stats["trophies"]
            playerData["HighestTrophies"] = stats["highesttrophies"]

            playerData["Name"] = CNData["name"]
            playerData["FakeID"] = [CNData["high"],CNData["low"]]
            playerData["Namecolor"] = CNData["namecolor"] if CNData["namecolor"] <= 11 else 0
            if CNData["thumbnail"] < 28000322:
                playerData["Thumbnail"] = CNData["thumbnail"] - 28000000
            if CNData["battleCardThumbnail1"][1] <= 322:
                playerData["BattleCardThumb1"] = CNData["battleCardThumbnail1"][1]
            if CNData["battleCardThumbnail2"][1] <= 322:
                playerData["BattleCardThumb2"] = CNData["battleCardThumbnail2"][1]
            if CNData["battleCardEmote"][1] <= 1308:
                playerData["BattleCardEmote"] = CNData["battleCardEmote"][1]
            if CNData["battleCardTitle"][1] <= 71:
                playerData["BattleCardTitle"] = CNData["battleCardTitle"][1]
            
            for brawler in CNData["heroes"]:
                HeroID = brawler["chara"][1]
                OwnedBrawlersInCN.append(brawler["chara"][1])
                if HeroID > 73:
                    continue
                playerData["OwnedBrawlers"][str(HeroID)]["Trophies"] = brawler["trophy"]
                playerData["OwnedBrawlers"][str(HeroID)]["HighestTrophies"] = brawler["highesttrophy"]
                playerData["OwnedBrawlers"][str(HeroID)]["PowerLevel"] = brawler["level"]
            playerConnection = ClientsManager.GetPlayerByLowID(Long[1])
            if  playerConnection != False:
                fields = {
                    "Socket": playerConnection["Socket"],
                    "Message":"玩家数据已更新！"
                }
                Crypto = playerConnection["Crypto"]
                Messaging.sendMessage(20103, fields, Crypto)
            db_instance.updatePlayerDataByLowID(playerData,Long[1])
            
            db_instance.cursor.close()

            ren = {'msg':'修改成功！请上线EMBrawl查看','msg_code':200}
            #json.dumps 序列化时对中文默认使用的ascii编码.想输出中文需要指定ensure_ascii=False
            return json.dumps(ren,ensure_ascii=False)
        '''
        #post入参访问方式一：url格式参数
        @api.route('/article',methods=['post']) 
        def article():
        #url格式参数?id=12589&name='lishi'
            id = flask.request.args.get('id')
            
            if id:
                if id == '12589':
                    ren = {'msg':'成功访问文章','msg_code':200}
                else:
                    ren = {'msg':'找不到文章','msg_code':400}
            else:
                ren = {'msg':'请输入文章id参数','msg_code':-1}
            return json.dumps(ren,ensure_ascii=False)
            
        #post入参访问方式二：from-data（k-v）格式参数
        @api.route('/login',methods=['post'])
        def login():
            #from-data格式参数
            usrname = flask.request.values.get('usrname')
            pwd = flask.request.values.get('pwd')
            
            if usrname and pwd:
                if usrname =='test' and pwd =='123456':
                    ren = {'msg':'登录成功','msg_code':200}
                else:
                    ren = {'msg':'用户名或密码错误','msg_code':-1}
            else:
                ren = {'msg':'用户名或密码为空','msg_code':1001}
            return json.dumps(ren,ensure_ascii=False)
            
        #post入参访问方式二：josn格式参数  
        @api.route('/loginjosn',methods=['post'])
        def loginjosn():
            #from-data格式参数
            usrname = flask.request.json.get('usrname')
            pwd = flask.request.json.get('pwd')
            
            if usrname and pwd:
                if usrname =='test' and pwd =='123456':
                    ren = {'msg':'登录成功','msg_code':200}
                else:
                    ren = {'msg':'用户名或密码错误','msg_code':-1}
            else:
                ren = {'msg':'用户名或密码为空','msg_code':1001}
            return json.dumps(ren,ensure_ascii=False)
        print(f"API服务启动成功！端口:{apiPort}")
        '''
        while True:
            api.run(port = apiPort,debug=False,host='0.0.0.0',ssl_context=('APIHandle/certificate.crt', 'APIHandle/private.key')) # 启动服务
        
        # debug=True,改了代码后，不用重启，它会自动重启
        # 'host='127.0.0.1'别IP访问地址
        