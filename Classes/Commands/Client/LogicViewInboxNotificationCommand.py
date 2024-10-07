import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler


class LogicViewInboxNotificationCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["unk1"] = calling_instance.readVInt()
        fields["unk2"] = calling_instance.readVInt()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        db_instance = DatabaseHandler()
        player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
        Notifications = player_data["Notification"]
        for Notification in Notifications:
            Notification["Reviewed"] = True
        player_data["Notification"] = Notifications
        db_instance.updatePlayerData(player_data, calling_instance)
        fields["Socket"] = calling_instance.client
        fields["Command"] = {}
        fields["Command"]["ID"] = 203
        fields["BoxType"] = 100
        fields["BoxData"] = { "Rewards":[{
                    "Count":99,
                    "HeroID":[0,0],
                    "RewardType":8,
                    "SkinID":[0,0],
                    "EmoteID":[0,0],
                    "CardID":[0,0]
        }
        ]}
        Messaging.sendMessage(24111, fields, cryptoInit)

    def getCommandType(self):
        return 528