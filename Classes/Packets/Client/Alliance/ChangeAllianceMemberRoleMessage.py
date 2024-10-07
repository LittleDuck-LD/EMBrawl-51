import time
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class ChangeAllianceMemberRoleMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["MemberID"] = self.readLong()
        fields["RoleID"] = self.readVInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()

        db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        target_data = json.loads(db_instance.getPlayerEntry(fields["MemberID"])[2])
        club_data = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
        #if club_data["Members"][str(calling_instance.player.ID[1])]["Role"]
        if club_data["Members"][str(calling_instance.player.ID[1])]["Role"] <= club_data["Members"][str(fields["MemberID"][1])]["Role"] and club_data["Members"][str(calling_instance.player.ID[1])]["Role"] != 2:
            fields["ResponseID"] = 95
            Messaging.sendMessage(24333, fields, cryptoInit)  
            return
        if club_data["Members"][str(fields["MemberID"][1])]["Role"] >= fields["RoleID"]:
            IsUp = False
        else:
            IsUp = True
        club_data["Members"][str(fields["MemberID"][1])]["Role"] = fields["RoleID"]
        if fields["RoleID"] == 2:
            club_data["Members"][str(calling_instance.player.ID[1])]["Role"] = 4
            fields["ResponseID"] = 102
            Messaging.sendMessage(24333, fields, cryptoInit)
        #创建消息
        if len(club_data['ChatData']) > 200:
            club_data['ChatData'].pop(0)
        message_tick = club_data['ChatData'][-1]['StreamID'][1] if club_data['ChatData'] else 0
        message_tick += 1
        message = { 'StreamType': 4 ,
                    'EventType': 5 if IsUp else 6,
                    'Target': {
                        "ID": fields["MemberID"],
                        "Name": target_data["Name"]
                    },
                    'PlayerID': calling_instance.player.ID,
                    'PlayerName':calling_instance.player.Name,
                    'PlayerRole': 2,
                    'StreamID': [0,message_tick],
                    "Time" : int(time.time())   }
        
        club_data['ChatData'].append(message)

        
        #统一写入数据库
        db_instance.updatePlayerData(player_data, calling_instance)
        clubdb_instance.updateClubData(club_data,calling_instance.player.AllianceID[1])

        fields["ResponseID"] = 81 if IsUp else 82
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

        #fields["ResponseID"] = 81
        #Messaging.sendMessage(24333, fields, cryptoInit)
        db_instance.cursor.close()

    def getMessageType(self):
        return 14306

    def getMessageVersion(self):
        return self.messageVersion