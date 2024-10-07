from Classes.Packets.PiranhaMessage import PiranhaMessage


class AddFriendFailedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        if "ErrorID" not in fields:
            fields["ErrorID"] = 0
        self.writeInt(fields["ErrorID"])

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20112

    def getMessageVersion(self):
        return self.messageVersion