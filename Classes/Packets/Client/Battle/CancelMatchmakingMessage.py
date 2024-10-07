from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utils.Helpers import Helpers


class CancelMatchmakingMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        Messaging.sendMessage(20406, fields, cryptoInit)
        Helpers.MatchMakingCount -= 1

    def getMessageType(self):
        return 14106

    def getMessageVersion(self):
        return self.messageVersion
