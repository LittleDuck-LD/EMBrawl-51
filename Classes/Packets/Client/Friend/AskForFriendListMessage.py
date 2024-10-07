from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class AskForFriendListMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        pass

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client

        Messaging.sendMessage(20105, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 10504

    def getMessageVersion(self):
        return self.messageVersion