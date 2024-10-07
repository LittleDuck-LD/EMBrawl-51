import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicSelectGearCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["unk1"] = calling_instance.readDataReference()
        fields["unk2"] = calling_instance.readDataReference()
        print("选择配件：",fields)
        fields["unk3_1"] = calling_instance.readVInt()
        fields["unk3_2"] = calling_instance.readBoolean()
        print("选择配件2：",fields)
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        pass

    def getCommandType(self):
        return 543