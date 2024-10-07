from Classes.Packets.PiranhaMessage import PiranhaMessage


class AllianceOnlineStatusUpdatedMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(100)
        self.writeVInt(1)#Count
        print(fields["AccountID"])
        self.writeLong(fields["AccountID"][0],fields["AccountID"][1])
        self.writeVInt(fields["Status"])

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["Count"] = self.readVInt()
        fields["AccountID"] = self.readLong()
        fields["Status"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20207

    def getMessageVersion(self):
        return self.messageVersion