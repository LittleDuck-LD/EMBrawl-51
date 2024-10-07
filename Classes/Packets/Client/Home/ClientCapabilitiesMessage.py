from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.BattleLogPlayerEntry import BattleLogPlayerEntry


class ClientCapabilitiesMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["Latency"] = self.readVInt()
        #super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        calling_instance.player.Latency = fields["Latency"]

    def getMessageType(self):
        return 15081

    def getMessageVersion(self):
        return self.messageVersion