import time
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utils.Helpers import Helpers


class TeamSetMemberReadyMessage(PiranhaMessage):
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
        NotificationData = {
            "ID": 66,
            "Reviewed": False,
            "Time" : int(time.time()),
            "Message" : "小队未完工，请退出小队后使用离线对战！\n现在开始匹配演示",
            "Sender" : 0
        }
        fields["Command"] = {}
        fields["Command"]["ID"] = 206
        fields["NotificationData"] = NotificationData
        Helpers.MatchMakingCount += 1
        Messaging.sendMessage(24111, fields, cryptoInit)
        Messaging.sendMessage(24130, fields, cryptoInit)
        Messaging.sendMessage(20405, fields, cryptoInit)
        time.sleep(5)
        Messaging.sendMessage(24112, fields, cryptoInit)
        time.sleep(1)
        
        Messaging.sendMessage(20559, fields, cryptoInit, calling_instance.player)

    def getMessageType(self):
        return 14355

    def getMessageVersion(self):
        return self.messageVersion