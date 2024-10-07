from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import ClubDatabaseHandler
from Classes.Stream.StreamEntryFactory import StreamEntryFactory
import json

class AllianceStreamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        if 'SendData' not in fields:
            clubdb_instance = ClubDatabaseHandler()
            SendData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])
        else:
            SendData = fields['SendData']
        if "SendDataCount" not in fields:
            fields['SendDataCount'] = len(SendData["ChatData"])

    
        self.writeVInt(fields['SendDataCount'])
        for i in SendData['ChatData']:
            self.writeVInt(i['StreamType'])
            StreamEntryFactory.encode(self, fields, i)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24311

    def getMessageVersion(self):
        return self.messageVersion