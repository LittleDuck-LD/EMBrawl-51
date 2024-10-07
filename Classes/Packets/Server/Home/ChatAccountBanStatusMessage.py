
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class ChatAccountBanStatusMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(fields["MuteSecs"])#禁言秒数:x+5

    def decode(self):
        return

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20118

    def getMessageVersion(self):
        return self.messageVersion