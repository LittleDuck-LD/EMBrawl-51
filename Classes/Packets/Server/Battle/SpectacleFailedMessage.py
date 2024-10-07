from Classes.Packets.PiranhaMessage import PiranhaMessage


class SpectacleFailedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeInt(1)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24105

    def getMessageVersion(self):
        return self.messageVersion