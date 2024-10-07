import time
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class SetSupportedCreatorMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['Code']=self.readString()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        playerData["ContentCreator"] = fields["Code"]
        db_instance.updatePlayerData(playerData, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["ServerCommandID"] = 215
        fields["Command"] = {}
        fields["Command"]["ID"] = 215
        fields["Creator"] = fields["Code"]
        Messaging.sendMessage(24111, fields, cryptoInit)
        #'''
        NotificationData = {
                    "ID": int(fields['Code']),
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : "Test",
                    "Sender" : 0
                }
        fields["NotificationData"] = NotificationData
        fields["Command"] = {}
        fields["Command"]["ID"] = 206
        fields["ErrorID"] = int(fields['Code'])
        Messaging.sendMessage(25892, fields, cryptoInit)
        #'''
        #Messaging.sendMessage(20103, fields, cryptoInit)
        db_instance.cursor.close()

    def getMessageType(self):
        return 18686

    def getMessageVersion(self):
        return self.messageVersion