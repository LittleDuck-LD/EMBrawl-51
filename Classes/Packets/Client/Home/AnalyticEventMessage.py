import json
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.BattleLogPlayerEntry import BattleLogPlayerEntry


class AnalyticEventMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["analyticTitle"] = self.readString()
        fields["analyticData"] = self.readString()
        #super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        analyticData = json.loads(fields["analyticData"])
        match(fields["analyticTitle"]):
            case "laser_fps":
                calling_instance.player.fps = analyticData["fps"]
                calling_instance.player.mode = analyticData["mode"]

    def getMessageType(self):
        return 10110

    def getMessageVersion(self):
        return self.messageVersion