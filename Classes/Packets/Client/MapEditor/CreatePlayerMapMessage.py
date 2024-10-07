from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class CreatePlayerMapMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields['Name']=self.readString()
        fields['GMV']=self.readVInt()
        fields['Envirionment']=self.readVInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        
        Messaging.sendMessage(22100, fields, cryptoInit)
        #Messaging.sendMessage(20103, fields, cryptoInit)

    def getMessageType(self):
        return 12100

    def getMessageVersion(self):
        return self.messageVersion