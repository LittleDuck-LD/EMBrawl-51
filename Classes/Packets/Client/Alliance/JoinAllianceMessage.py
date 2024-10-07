from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json
import time


class JoinAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeLong(fields["AllianceID"][0], fields["AllianceID"][1])

    def decode(self):
        fields = {}
        fields["AllianceID"] = self.readLong()
        super().decode(fields)

        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        if not calling_instance.player.AllianceID or calling_instance.player.AllianceID == [0,0]:
            db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)
            club_ID = fields["AllianceID"]
            club_data = json.loads(clubdb_instance.getClubWithLowID(club_ID[1])[0][1])
            
            #战队成员更新
            club_data['Members'][str(calling_instance.player.ID[1])] = clubdb_instance.getDefaultMembersData(calling_instance.player,1)

            #玩家信息更新
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            player_data["AllianceID"] = club_ID
            

            #创建消息
            if len(club_data['ChatData']) > 200:
                club_data['ChatData'].pop(0)
            message_tick = club_data['ChatData'][-1]['StreamID'][1] if club_data['ChatData'] else 0
            message_tick += 1
            message = { 'StreamType': 4 ,
                        'EventType': 3,
                        'Target': {
                            "ID": calling_instance.player.ID,
                            "Name": calling_instance.player.Name
                        },
                        'PlayerID': calling_instance.player.ID,
                        'PlayerName':calling_instance.player.Name,
                        'PlayerRole': 2,
                        'StreamID': [0,message_tick],
                        "Time" : int(time.time())   }
            
            club_data['ChatData'].append(message)

            
            #统一写入数据库
            db_instance.updatePlayerData(player_data, calling_instance)
            clubdb_instance.updateClubData(club_data,club_ID[1])

            fields["ResponseID"] = 40
            Messaging.sendMessage(24333, fields, cryptoInit)
            #Messaging.sendMessage(24311, fields, cryptoInit, calling_instance.player)
            fields["HasClub"] = True
            Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)

            OnlinePlayers = ClientsManager.GetAll()
            for member in club_data['Members']:
                if int(member) in OnlinePlayers.keys():
                    fields["Socket"] = OnlinePlayers[int(member)]["Socket"]
                    Crypto = OnlinePlayers[int(member)]["Crypto"]
                    Messaging.sendMessage(24311, fields, Crypto, calling_instance.player)

        else:
            fields["ResponseID"] = 44
            Messaging.sendMessage(24333, fields, cryptoInit)
        db_instance.cursor.close()

    def getMessageType(self):
        return 14305

    def getMessageVersion(self):
        return self.messageVersion