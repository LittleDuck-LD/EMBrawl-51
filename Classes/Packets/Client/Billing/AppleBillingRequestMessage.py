import time
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class AppleBillingRequestMessage(PiranhaMessage):
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
        #Messaging.sendMessage(20105, fields, cryptoInit, calling_instance.player)
        Messaging.sendMessage(20121, fields, cryptoInit)

    def getMessageType(self):
        return 10150

    def getMessageVersion(self):
        return self.messageVersion