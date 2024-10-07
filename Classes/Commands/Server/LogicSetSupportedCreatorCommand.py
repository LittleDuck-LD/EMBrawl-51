from Classes.Commands.LogicServerCommand import LogicServerCommand


class LogicSetSupportedCreatorCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeVInt(1)
        self.writeString(fields["Creator"])
        self.writeVInt(1)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 215