from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class SendAllianceMailMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Status"]=self.readInt()
        fields["MailContent"]=self.readString()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        if fields["Status"] == 1:
            fields["ResponseID"] = 114
            Messaging.sendMessage(24333, fields, cryptoInit)
        elif fields["Status"] == 0:
            print(fields["MailContent"])

    def getMessageType(self):
        return 14330

    def getMessageVersion(self):
        return self.messageVersion