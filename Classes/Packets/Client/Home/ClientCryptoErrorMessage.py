from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class ClientCryptoErrorMessage(PiranhaMessage):
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
        #Messaging.sendMessage(20103, fields, cryptoInit)

    def getMessageType(self):
        return 10099

    def getMessageVersion(self):
        return self.messageVersion