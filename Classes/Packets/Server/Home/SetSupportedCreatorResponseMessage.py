from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class SetSupportedCreatorResponseMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        print(fields)
        self.writeVInt(fields['Unk1'])
        self.writeStringReference(fields['Code'])

    def decode(self):
        fields = {}
        fields["Unk1"] = self.readVInt()
        fields["Code"] = self.readStringReference()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 28686

    def getMessageVersion(self):
        return self.messageVersion