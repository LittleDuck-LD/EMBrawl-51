import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicEditBattleCardCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Brawler"] = calling_instance.readDataReference()
        fields["ItemID"] = calling_instance.readDataReference()
        fields["IsHide"] = calling_instance.readBoolean()
        fields["SoltID"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        if fields["Brawler"] != None:
            return
        if fields["SoltID"] == 0:
            if fields["IsHide"] == True:
                player_data["BattleCardThumb1"] = 0
            if fields["ItemID"] != None:
                if fields["ItemID"][0] != 28:
                    return
                else:
                    player_data["BattleCardThumb1"] = fields["ItemID"][1]
        elif fields["SoltID"] == 1:
            if fields["IsHide"] == True:
                player_data["BattleCardThumb2"] = 0
            if fields["ItemID"] != None:
                if fields["ItemID"][0] != 28:
                    return
                else:
                    player_data["BattleCardThumb2"] = fields["ItemID"][1]
        elif fields["SoltID"] == 5:
            if fields["IsHide"] == True:
                player_data["BattleCardEmote"] = 0
            if fields["ItemID"] != None:
                if fields["ItemID"][0] != 52:
                    return
                else:
                    player_data["BattleCardEmote"] = fields["ItemID"][1]
        elif fields["SoltID"] == 10:
            if fields["IsHide"] == True:
                player_data["BattleCardTitle"] = 0
            if fields["ItemID"] != None:
                if fields["ItemID"][0] != 76:
                    return
                else:
                    player_data["BattleCardTitle"] = fields["ItemID"][1]

        db_instance.updatePlayerData(player_data, calling_instance)
        db_instance.cursor.close()

    def getCommandType(self):
        return 568