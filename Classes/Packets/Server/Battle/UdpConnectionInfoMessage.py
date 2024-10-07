from Classes.Packets.PiranhaMessage import PiranhaMessage


class UdpConnectionInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(9569)
        self.writeString("127.0.0.1")
        self.writeInt(0)
        self.writeLong(0,1)
        self.writeShort(0)
        self.writeInt(0)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24112

    def getMessageVersion(self):
        return self.messageVersion