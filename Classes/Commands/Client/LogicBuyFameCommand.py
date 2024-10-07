import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicBuyFameCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["UsingResourceType"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        if fields["UsingResourceType"][0]!=5:
            return
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        if "stats_Fame" not in player_data:
            player_data["stats_Fame"] = 0
        if player_data["stats_Fame"] > 89100:
            return
        player_data["stats_Fame"] += 200
        db_instance.updatePlayerData(player_data, calling_instance)
        db_instance.cursor.close()

    def getCommandType(self):
        return 570