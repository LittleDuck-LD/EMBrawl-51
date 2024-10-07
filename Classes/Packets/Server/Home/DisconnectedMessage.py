
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class DisconnectedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        if "ErrorID" not in fields:
            fields["ErrorID"] = 1
        self.writeInt(fields["ErrorID"])

    def decode(self):
        return

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 25892

    def getMessageVersion(self):
        return self.messageVersion