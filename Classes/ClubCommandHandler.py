from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging
from Classes.Logic.LogicLongTag import LogicLongTag

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json
import time
import random



class ClubCmdHandler():
    def __init__(self):
        pass

    def MakeDefaultMessage(self,message):
        #message_tick = self.club_data['ChatData'][-1]['StreamID'][1] if self.club_data['ChatData'] else 0
        #message_tick += 1
        message_tick = random.randint(200,1000000)
        return {"ChatData":[{'StreamType': 2 ,'Message': message, 'PlayerID': [100,0], 'PlayerName': "---服务器---", 'PlayerRole':2, 'StreamID': [0,message_tick], "Time" : int(time.time())}]}
    
    def SendDefaultMessage(self,message,fields):
        fields['SendData'] = self.MakeDefaultMessage(message)
        Messaging.sendMessage(24311, fields, self.Crypto, self.calling_instance.player)

    def Handle(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()

        Cmds = fields["Command"].split(" ")
        MainCmd = Cmds[0]
        MainCmd = MainCmd[1:]

        db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)
        club_ID = calling_instance.player.AllianceID[1]
        club_data = json.loads(clubdb_instance.getClubWithLowID(club_ID)[0][1])
        self.club_data = club_data
        self.calling_instance = calling_instance
        self.Crypto = cryptoInit
        Issued_player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        Issued_Player_Name = Issued_player_data["Name"]
        Issued_Player_ID = Issued_player_data["ID"]
        print(f"命令执行：{MainCmd}|{Issued_Player_Name}|{Issued_Player_ID}")
        fields['SendDataCount'] = 1
        MainCmd = MainCmd.lower()
        match MainCmd:
            case "mailall":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                if Cmds[1]:
                    Message = Cmds[1]
                    self.SendDefaultMessage("已为在线玩家发送邮件！",fields)
                else:
                    self.SendDefaultMessage("邮件内容缺失！",fields)
                    return
                
                OnlinePlayers = ClientsManager.GetAll()
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : Message,
                    "Sender" : 0
                }
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                for Player in OnlinePlayers:
                    fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                    Crypto = OnlinePlayers[int(Player)]["Crypto"]

                    Messaging.sendMessage(24111, fields, Crypto)
                
                
            case "gb":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                if Cmds[1]:
                    Message = Cmds[1]
                    self.SendDefaultMessage("已为在线的玩家发送浮动消息！",fields)
                else:
                    self.SendDefaultMessage("消息内容缺失！",fields)
                    return
                OnlinePlayers = ClientsManager.GetAll()
                NotificationData = {
                    "ID": 66,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : Message,
                    "Sender" : 0
                }
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                for Player in OnlinePlayers:
                    fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                    Crypto = OnlinePlayers[int(Player)]["Crypto"]
                    fields["Message"] = Message
                    Messaging.sendMessage(24111, fields, Crypto)
                
            case "shutdown":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                self.SendDefaultMessage("已为在线的玩家发送维护消息！",fields)
                
                OnlinePlayers = ClientsManager.GetAll()
                for Player in OnlinePlayers:
                    fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                    Crypto = OnlinePlayers[int(Player)]["Crypto"]
                    Messaging.sendMessage(20161, fields, Crypto)
                return

            case "ban":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Target_Long = LogicLongTag.convert_player_tag_to_long(Cmds[1])
                    
                except IndexError as e:
                    self.SendDefaultMessage("标签缺失！",fields)
                    return
                target_player_data = json.loads(db_instance.getPlayerEntry(Target_Long)[2])
                if target_player_data['Banned'] == True:
                    self.SendDefaultMessage("该玩家早已被封禁！",fields)
                    return
                TargetPlayerIP = target_player_data["IP"]
                TargetPlayerName = target_player_data["Name"]
                target_player_data["Banned"] = True
                db_instance.updatePlayerDataByLowID(target_player_data, Target_Long[1])
                OnlinePlayers = ClientsManager.GetAll()
                if Target_Long[1] in OnlinePlayers:
                    fields["Socket"] = OnlinePlayers[Target_Long[1]]["Socket"]
                    Crypto = OnlinePlayers[Target_Long[1]]["Crypto"]
                    fields['ErrorID'] = 5
                    fields['FingerprintData'] = None
                    fields['ContentURL'] = None
                    fields["Message"] = "违规游戏行为，您被迫下线。"
                    Messaging.sendMessage(20103, fields, Crypto)
                fields["Socket"] = calling_instance.client
                self.SendDefaultMessage(f"已封禁玩家 {Target_Long}({TargetPlayerName}) ！该玩家IP：{TargetPlayerIP}",fields)
                
            case "pardon":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Target_Long = LogicLongTag.convert_player_tag_to_long(Cmds[1])
                    
                except IndexError as e:
                    self.SendDefaultMessage("标签缺失！",fields)
                    return
                target_player_data = json.loads(db_instance.getPlayerEntry(Target_Long)[2])
                if target_player_data['Banned'] == False:
                    self.SendDefaultMessage("该玩家本来就没有被封禁！",fields)
                    return
                TargetPlayerIP = target_player_data["IP"]
                TargetPlayerName = target_player_data["Name"]
                target_player_data["Banned"] = False
                db_instance.updatePlayerDataByLowID(target_player_data, Target_Long[1])
                self.SendDefaultMessage(f"已解封玩家 {Target_Long}({TargetPlayerName}) ！该玩家IP：{TargetPlayerIP}",fields)
                
            case "op":
                if Issued_player_data['IsOperator']==False or Issued_player_data['ID'] != [100,0]:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Target_Long = LogicLongTag.convert_player_tag_to_long(Cmds[1])
                    
                except IndexError as e:
                    self.SendDefaultMessage("标签缺失！",fields)
                    return
                target_player_data = json.loads(db_instance.getPlayerEntry(Target_Long)[2])
                if target_player_data['IsOperator'] == True:
                    self.SendDefaultMessage("该玩家早已是OP！",fields)
                    return
                TargetPlayerIP = target_player_data["IP"]
                TargetPlayerName = target_player_data["Name"]
                target_player_data["IsOperator"] = True
                db_instance.updatePlayerDataByLowID(target_player_data, Target_Long[1])
                self.SendDefaultMessage(f"已给予玩家 {Target_Long}({TargetPlayerName}) OP权限！该玩家IP：{TargetPlayerIP}",fields)
                
            case "deop":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Target_Long = LogicLongTag.convert_player_tag_to_long(Cmds[1])
                except IndexError as e:
                    self.SendDefaultMessage("标签缺失！",fields)
                    return
                target_player_data = json.loads(db_instance.getPlayerEntry(Target_Long)[2])
                if target_player_data['IsOperator'] == False:
                    self.SendDefaultMessage("该玩家本来就不是OP！",fields)
                    return
                TargetPlayerIP = target_player_data["IP"]
                TargetPlayerName = target_player_data["Name"]
                target_player_data["IsOperator"] = False
                db_instance.updatePlayerDataByLowID(target_player_data, Target_Long[1])
                self.SendDefaultMessage(f"已撤销玩家 {Target_Long}({TargetPlayerName}) OP权限！该玩家IP：{TargetPlayerIP}",fields)
                
            case "check":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Target_Long = LogicLongTag.convert_player_tag_to_long(Cmds[1])
                except IndexError as e:
                    self.SendDefaultMessage("标签缺失！",fields)
                    return
                target_player_data = json.loads(db_instance.getPlayerEntry(Target_Long)[2])
                TargetPlayerIP = target_player_data["IP"]
                TargetPlayerIMEI = target_player_data["IMEI"]
                TargetPlayerAppleIFV = target_player_data["AppleIFV"]
                TargetPlayerAndroidID = target_player_data["AndroidID"]
                TargetPlayerisAndroid = target_player_data["isAndroid"]
                TargetPlayerDevice = target_player_data["Device"]
                TargetPlayerName = target_player_data["Name"]
                self.SendDefaultMessage(f"该玩家({TargetPlayerName})信息:\n"
                                        f"IP：{TargetPlayerIP}\n"
                                        f"IMEI：{TargetPlayerIMEI}\n"
                                        f"AppleIFV：{TargetPlayerAppleIFV}\n"
                                        f"AndroidID：{TargetPlayerAndroidID}\n"
                                        f"isAndroid：{TargetPlayerisAndroid}\n"
                                        f"Device：{TargetPlayerDevice}\n"
                                        ,fields)
                
            case "kickall":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                try:
                    Message = Cmds[1]
                except IndexError as e:
                    self.SendDefaultMessage("内容缺失！",fields)
                    return
                self.SendDefaultMessage("已为在线的玩家发送登录失败消息！",fields)
                fields['ErrorID'] = 5
                fields['FingerprintData'] = None
                fields['ContentURL'] = None
                fields['Message'] = Message
                OnlinePlayers = ClientsManager.GetAll()
                for Player in OnlinePlayers:
                    fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                    Crypto = OnlinePlayers[int(Player)]["Crypto"]
                    Messaging.sendMessage(20103, fields, Crypto)
                
            case "starpoints":
                try:
                    Count = Cmds[1]
                except IndexError as e:
                    self.SendDefaultMessage("数量缺失！默认发送10个星光点数！",fields)
                    Count = 10
                #self.SendDefaultMessage(f"功能测试中，您暂无权限。",fields)
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                NotificationData = {
                    "ID": 80,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : f"\n——EmberHeart活动",
                    "Count" : int(Count)
                }
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
                NotificationData["Reviewed"] = True #不知道为什么不领重进会有bug
                playerData["Notification"].append(NotificationData)
                db_instance.updatePlayerData(playerData, calling_instance)
                
                self.SendDefaultMessage("已为自己发送星光点数！",fields)
                
            case "mail":
                try:
                    Message = Cmds[1]
                except IndexError as e:
                    self.SendDefaultMessage("内容缺失！",fields)
                    return
                #self.SendDefaultMessage(f"功能测试中，您暂无权限。",fields)
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : Message+f"\n——EmberHeart活动",
                    "Sender" : 0
                }
                playerData["Notification"].append(NotificationData)
                db_instance.updatePlayerData(playerData, calling_instance)
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
                self.SendDefaultMessage("已为自己发送邮件！",fields)
            
            case "token":
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                Token = random.randint(10000000,99999999)
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : f"您的API令牌已更新为: {Token}，如有旧令牌将即时作废！\n——EMBrawl",
                    "Sender" : 1
                }
                playerData["Notification"].append(NotificationData)
                db_instance.updatePlayerData(playerData, calling_instance)
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
                playerData["APIToken"] = Token
                db_instance.updatePlayerData(playerData, calling_instance)
                self.SendDefaultMessage("已更新API令牌，请前往邮箱查看！",fields)

            case "cleartoken":
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : f"您的API令牌已清除！\n——EMBrawl",
                    "Sender" : 1
                }
                playerData["Notification"].append(NotificationData)
                db_instance.updatePlayerData(playerData, calling_instance)
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
                del playerData["APIToken"]
                db_instance.updatePlayerData(playerData, calling_instance)
                self.SendDefaultMessage("API令牌已移除！\n现有API令牌已无法使用。",fields)
                
            case "gems":
                try:
                    Count = Cmds[1]
                except IndexError as e:
                    self.SendDefaultMessage("数量缺失！默认发送10个宝石！",fields)
                    Count = 10
                #self.SendDefaultMessage(f"功能测试中，您暂无权限。",fields)
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                NotificationData = {
                    "ID": 89,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : f"\n——EmberHeart活动",
                    "Sender" : 0,
                    "GemsCount" : int(Count)
                }
                playerData["Notification"].append(NotificationData)
                db_instance.updatePlayerData(playerData, calling_instance)
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
                self.SendDefaultMessage("已为自己发送宝石！",fields)
                
            case "clearmail":
                playerData = db_instance.getPlayer(calling_instance.player.ID)
                playerData["Notification"] = []
                db_instance.updatePlayerData(playerData, calling_instance)
                self.SendDefaultMessage("已清空邮箱！",fields)
                fields['ErrorID'] = 5
                fields['FingerprintData'] = None
                fields['ContentURL'] = None
                fields['Message'] = "已清空邮箱！需要重新登录。"
                Messaging.sendMessage(20103, fields, cryptoInit)
                
            case "clearmailall":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                MaxID=db_instance.getLastPlayer()["ID"][1]
                for i in range(MaxID):
                    playerData = db_instance.getPlayer([100,i])
                    playerData["Notification"] = []
                    db_instance.updatePlayerDataByLowID(playerData, i)
                self.SendDefaultMessage("已清空所有人的邮箱！",fields)
                fields['ErrorID'] = 5
                fields['FingerprintData'] = None
                fields['ContentURL'] = None
                fields['Message'] = "已清空邮箱！需要重新登录。"
                Messaging.sendMessage(20103, fields, cryptoInit)

            case "clearfriendall":
                if Issued_player_data['IsOperator']==False:
                    self.SendDefaultMessage("你没有权限使用该指令！",fields)
                    return
                MaxID=db_instance.getLastPlayer()["ID"][1]
                for i in range(MaxID):
                    playerData = db_instance.getPlayer([100,i])
                    playerData["Friends"] = []
                    db_instance.updatePlayerDataByLowID(playerData, i)
                self.SendDefaultMessage("已清空所有人的好友！",fields)
                Messaging.sendMessage(20105, fields, cryptoInit,calling_instance.player)
                
            case "suicide":
                if Cmds[1]:
                    Secs = int(Cmds[1])
                else:
                    Secs=3
                if Secs>120:
                    Secs=120
                    self.SendDefaultMessage("时间过长，已自动缩短至120秒",fields)
                
                self.SendDefaultMessage("正在suicide！",fields)
                time.sleep(1)
                for i in range(Secs,0,-1):
                    self.SendDefaultMessage(str(i),fields)
                    fields["Command"] = {}
                    fields["Command"]["ID"] = 206
                    fields["NotificationID"] = 66
                    fields["Message"] = str(i)
                    Messaging.sendMessage(24111, fields, cryptoInit)
                    time.sleep(1)
                fields['ErrorID'] = 5
                fields['FingerprintData'] = None
                fields['ContentURL'] = None
                fields['Message'] = "你suicide了。"
                Messaging.sendMessage(20103, fields, cryptoInit)
                
            case "status":
                LastLowID = db_instance.getLastPlayer()["ID"][1]
                self.SendDefaultMessage(f"服务器状态：\n"
                                        f"当前在线玩家数量：{ClientsManager.GetCount()}\n"
                                        f"您是本服务器第{calling_instance.player.ID[1]+1}位(全服共{LastLowID+1}位)玩家\n",fields)
                
            case "help":
                self.SendDefaultMessage(f"服务器指令列表：\n"
                                        f"/status--查看服务器状态\n"
                                        f"/suicide [时间]--字面意思\n"
                                        f"/token--获取API令牌\n"
                                        f"/cleartoken--清除API令牌\n"
                                        f"/mail [内容]--为自己发送一封邮件\n"
                                        f"/gems [数量]--为自己送一点宝石(虽然不能拿。)\n"
                                        f"/starpoints [数量]--为自己送一点星光点数(可领取)\n"
                                        f"/clearmail--清空邮箱(需要重启游戏)\n",fields)
                
            case _: 
                self.SendDefaultMessage("未知指令！输入/help以查看指令列表！",fields)
                return
            
        db_instance.cursor.close()