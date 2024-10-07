import time
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class KickAllianceMemberMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields={}
        fields['TargetID'] = self.readLong()
        fields['Reason'] = self.readString()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        fields["Socket"] = calling_instance.client
        fields["ClubID"] = calling_instance.player.AllianceID
        club_data = json.loads(clubdb_instance.getClubWithLowID(fields["ClubID"][1])[0][1])
        if club_data['Members'][str(calling_instance.player.ID[1])]["Role"] != 2:
            fields["ResponseID"] = 95
            Messaging.sendMessage(24333, fields, cryptoInit)
            return

        db_instance.loadAccount(calling_instance.player, fields['TargetID'])
        
        Kick_Player = json.loads(db_instance.getPlayerEntry(fields['TargetID'])[2])
        Kick_Player["AllianceID"] = None
        Kick_Player["HasClub"] = False
        db_instance.updatePlayerDataByLowID(Kick_Player, fields['TargetID'][1])

        fields["ResponseID"] = 70
        Messaging.sendMessage(24333, fields, cryptoInit)
        #Messaging.sendMessage(24311, fields, cryptoInit, calling_instance.player)
        fields["HasClub"] = True
        Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)
        

        if len(club_data['Members']) == 1:
            clubdb_instance.deleteClub(fields["ClubID"][1])
            return

        OnlinePlayers = ClientsManager.GetAll()
        for Player in OnlinePlayers:
            if int(Player) == fields['TargetID'][1]:
                fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                Crypto = OnlinePlayers[int(Player)]["Crypto"]
                fields["ResponseID"] = 100
                Messaging.sendMessage(24333, fields, Crypto)
                fields["HasClub"] = False
                Messaging.sendMessage(24399, fields, Crypto, calling_instance.player)
        
        

        #创建消息
        if len(club_data['ChatData']) > 200:
            club_data['ChatData'].pop(0)
        message_tick = club_data['ChatData'][-1]['StreamID'][1] if club_data['ChatData'] else 0
        message_tick += 1
        message = { 'StreamType': 4 ,
                    'EventType': 1,
                    'Target': {
                        "ID": fields['TargetID'],
                        "Name": Kick_Player['Name']
                    },
                    'PlayerID': calling_instance.player.ID,
                    'PlayerName': calling_instance.player.Name,
                    'PlayerRole': club_data['Members'][str(calling_instance.player.ID[1])]["Role"],
                    'StreamID': [0,message_tick],
                    "Time" : int(time.time())   }
        
        club_data['ChatData'].append(message)

        del club_data['Members'][str(fields['TargetID'][1])]
        
        #统一写入数据库
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