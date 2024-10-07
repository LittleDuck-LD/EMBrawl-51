from Classes.Commands.LogicServerCommand import LogicServerCommand


class LogicDiamondsAddedCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeBoolean(False)
        self.writeInt(100)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeString("GPA.0000-0000-0000-00000")
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        fields["Unk1"] = calling_instance.readVInt()
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 202