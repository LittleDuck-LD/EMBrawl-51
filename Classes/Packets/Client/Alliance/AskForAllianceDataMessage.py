from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class AskForAllianceDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeLong(fields["AllianceID"][0], fields["AllianceID"][1])
        self.writeBoolean(fields["isInAlliance"])
        if fields["isInAlliance"] == True:
            fields["anotherIDHigh"] = self.readVInt()
            fields["anotherIDLow"] = self.readVInt()

    def decode(self):
        fields = {}
        fields["AllianceID"] = self.readLong()
        fields["isInAlliance"] = self.readBoolean()
        if fields["isInAlliance"] == True:
            fields["anotherIDHigh"] = self.readVInt()
            fields["anotherIDLow"] = self.readVInt()
        super().decode(fields)

        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client

        Messaging.sendMessage(24301, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14301

    def getMessageVersion(self):
        return self.messageVersion