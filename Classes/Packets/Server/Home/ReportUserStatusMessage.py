
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class ReportUserStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(fields["StatusID"])
        self.writeInt(0)

    def decode(self):
        return

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20117

    def getMessageVersion(self):
        return self.messageVersion