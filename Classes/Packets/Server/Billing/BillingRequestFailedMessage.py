
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class BillingRequestFailedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(0)
        self.writeString("1")
        self.writeInt(0)

    def decode(self):
        return

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20121

    def getMessageVersion(self):
        return self.messageVersion