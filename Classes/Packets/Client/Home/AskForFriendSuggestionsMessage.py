import time
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class AskForFriendSuggestionsMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        #self.readBoolean()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        fields["Command"] = {}
        fields["Command"]["ID"] = 203
        fields["BoxType"] = 13
        fields["ShowType"] = 1
        Messaging.sendMessage(24111, fields, cryptoInit)
        #Messaging.sendMessage(20105, fields, cryptoInit, calling_instance.player)
        #Messaging.sendMessage(20117, fields, cryptoInit)
        '''
        fields["ServerCommandID"] = 206
        fields["Command"] = {}
        fields["Command"]["ID"] = 206
        NotificationData = {
            "ID": 89,
            "Reviewed": False,
            "Time" : int(time.time()),
            "Message" : "EMBrawl\n注：如领取则需要删后台重进游戏",
            "GemsCount" : 114514
        }
        fields["NotificationData"] = NotificationData
        Messaging.sendMessage(24111, fields, cryptoInit)
        fields['ErrorID'] = 19
        fields['FingerprintData'] = None
        fields['ContentURL'] = None
        fields['Message'] = None
        '''
        Messaging.sendMessage(28275, fields, cryptoInit)

    def getMessageType(self):
        return 10599

    def getMessageVersion(self):
        return self.messageVersion