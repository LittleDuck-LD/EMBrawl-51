from Classes.Packets.PiranhaMessage import PiranhaMessage


class CreatePlayerMapResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(8)
        self.writeBoolean(False)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 22100

    def getMessageVersion(self):
        return self.messageVersion