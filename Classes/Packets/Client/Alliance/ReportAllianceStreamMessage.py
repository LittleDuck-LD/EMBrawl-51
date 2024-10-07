import time
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class ReportAllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["StreamID"]=self.readLong()
        fields["MessageSender"]=self.readLong()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        if calling_instance.player.IsOperator == True:
            StreamID = fields["StreamID"]
            NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : f"你的发言违规，警告一次\n\nStreamID:{StreamID}"+f"\n——EMBrawl",
                    "Sender" : 1
                }
            playerData = db_instance.getPlayer(fields["MessageSender"])
            playerData["Notification"].append(NotificationData)
            db_instance.updatePlayerDataByLowID(playerData, fields["MessageSender"][1])
            fields["Command"] = {}
            fields["Command"]["ID"] = 206
            fields["NotificationData"] = NotificationData
            OnlinePlayers = ClientsManager.GetAll()
            for Player in OnlinePlayers:
                if int(Player) == fields["MessageSender"][1]:
                    fields["Socket"] = OnlinePlayers[int(Player)]["Socket"]
                    Crypto = OnlinePlayers[int(Player)]["Crypto"]
                    Messaging.sendMessage(24111, fields, Crypto)
            fields["Socket"] = calling_instance.client
            fields["StatusID"] = 1
            Messaging.sendMessage(20117, fields, cryptoInit)
        else:
            fields["StatusID"] = 2
            Messaging.sendMessage(20117, fields, cryptoInit)
        db_instance.cursor.close()

    def getMessageType(self):
        return 10119

    def getMessageVersion(self):
        return self.messageVersion