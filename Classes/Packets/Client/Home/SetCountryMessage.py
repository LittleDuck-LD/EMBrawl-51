from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class SetCountryMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['Unk1']=self.readVInt()
        fields['Code']=self.readVInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(calling_instance.player.ID)
        playerData["Theme"] = int(fields["Code"])-7+41000000
        db_instance.updatePlayerData(playerData, calling_instance)
        fields['ErrorID'] = 12
        fields['FingerprintData'] = None
        fields['ContentURL'] = None
        if fields['Code'] == "":
            fields['Message'] = f"已清除支持!"
        else:
            fields['Message'] = f"已修改为:{fields['Code']-7}!"
        Messaging.sendMessage(20103, fields, cryptoInit)

        db_instance.cursor.close()

    def getMessageType(self):
        return 14101

    def getMessageVersion(self):
        return self.messageVersion