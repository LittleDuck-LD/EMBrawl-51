import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicSelectFavouriteBrawlerCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["FavouriteBrawler"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        if fields["FavouriteBrawler"][0]!=16:
            return
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        player_data["FavouriteBrawler"] = fields["FavouriteBrawler"][1]
        db_instance.updatePlayerData(player_data, calling_instance)
        db_instance.cursor.close()

    def getCommandType(self):
        return 570