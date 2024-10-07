from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utils.Helpers import Helpers


class MatchMakingStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(65)#Second
        self.writeInt(Helpers.MatchMakingCount)#len(my_battle["players"]))#Found
        self.writeInt(114514)#MatchmakingLogic.MaxPlayer)#Max
        self.writeInt(0)
        self.writeInt(0)
        self.writeBoolean(True)#ShowTips

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20405

    def getMessageVersion(self):
        return self.messageVersion