import time
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utils.Gameroom import Gameroom
from Classes.Utils.Helpers import Helpers


class TeamCreateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["unk1"] = self.readLong()
        fields["room_type"] = self.readVInt()
        fields["map_slot"] = self.readVInt()
        fields["unk"] = self.readVInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        fields["map_id"] = 121
        fields["room_id"] = 1+len(Helpers.rooms)
        fields["player"]={}
        fields["player"]["low_id"] = calling_instance.player.ID[1]
        Messaging.sendMessage(24124, fields, cryptoInit)
        Gameroom.create({}, fields)

    def getMessageType(self):
        return 12541

    def getMessageVersion(self):
        return self.messageVersion