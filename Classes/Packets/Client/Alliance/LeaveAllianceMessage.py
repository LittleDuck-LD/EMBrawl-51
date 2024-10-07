import time
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class LeaveAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        pass

    def execute(message, calling_instance, fields, cryptoInit):
        fields={}
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        fields["Socket"] = calling_instance.client

        db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)

        fields["ClubID"] = calling_instance.player.AllianceID

        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data["AllianceID"] = None
        player_data["HasClub"] = False
        db_instance.updatePlayerData(player_data, calling_instance)

        fields["ResponseID"] = 80
        Messaging.sendMessage(24333, fields, cryptoInit)
        #Messaging.sendMessage(24311, fields, cryptoInit, calling_instance.player)
        fields["HasClub"] = False
        Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)
        club_data = json.loads(clubdb_instance.getClubWithLowID(fields["ClubID"][1])[0][1])

        if len(club_data['Members']) == 1:
            clubdb_instance.deleteClub(fields["ClubID"][1])
            return
        
        

        #创建消息
        if len(club_data['ChatData']) > 200:
            club_data['ChatData'].pop(0)
        message_tick = club_data['ChatData'][-1]['StreamID'][1] if club_data['ChatData'] else 0
        message_tick += 1
        message = { 'StreamType': 4 ,
                    'EventType': 4,
                    'Target': {
                        "ID": calling_instance.player.ID,
                        "Name": calling_instance.player.Name
                    },
                    'PlayerID': calling_instance.player.ID,
                    'PlayerName': calling_instance.player.Name,
                    'PlayerRole': club_data['Members'][str(calling_instance.player.ID[1])]["Role"],
                    'StreamID': [0,message_tick],
                    "Time" : int(time.time())   }
        
        club_data['ChatData'].append(message)

        del club_data['Members'][str(calling_instance.player.ID[1])]
        
        #统一写入数据库
        db_instance.updatePlayerData(player_data, calling_instance)
        clubdb_instance.updateClubData(club_data,fields["ClubID"][1])

        fields["SendData"]=club_data
        OnlinePlayers = ClientsManager.GetAll()
        for member in club_data['Members']:
            if int(member) in OnlinePlayers.keys():
                fields["Socket"] = OnlinePlayers[int(member)]["Socket"]
                Crypto = OnlinePlayers[int(member)]["Crypto"]
                Messaging.sendMessage(24311, fields, Crypto, calling_instance.player)
        db_instance.cursor.close()

    def getMessageType(self):
        return 14308

    def getMessageVersion(self):
        return self.messageVersion