from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class RemoveFriendMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        
        db_instance = DatabaseHandler()
        LastLowID = db_instance.getLastPlayer()["ID"][1]

        ownPlayerData = db_instance.getPlayer(calling_instance.player.ID)
        friendPlayerData = db_instance.getPlayer(fields["AccountID"])

        #好友添加失败处理

         
        
        
        for i,Friend in enumerate(ownPlayerData["Friends"]):
            if Friend["ID"] == fields["AccountID"]:
                del ownPlayerData["Friends"][i]
                break
        
        db_instance.updatePlayerDataByLowID(ownPlayerData,calling_instance.player.ID[1])
        fields["Socket"] = calling_instance.client
        ownFriendData = {
            "ID":fields["AccountID"],
            "State":1,
            "Reason":0,
            "ReasonData":999
        }
        fields["FriendData"] = ownFriendData
        Messaging.sendMessage(20106, fields, cryptoInit)

        for i,Friend in enumerate(friendPlayerData["Friends"]):
            if Friend["ID"] == calling_instance.player.ID:
                del friendPlayerData["Friends"][i]
                break
        

        db_instance.updatePlayerDataByLowID(friendPlayerData,fields["AccountID"][1])
        
        db_instance.cursor.close()
        onlinePlayers = ClientsManager.GetAll()
        if fields["AccountID"][1] in onlinePlayers:
            otherFriendData = {
                "ID":calling_instance.player.ID,
                "State":1,
                "Reason":0,
                "ReasonData":999
            }
            fields["FriendData"] = otherFriendData
            fields["Socket"] = onlinePlayers[fields["AccountID"][1]]["Socket"]
            Crypto = onlinePlayers[fields["AccountID"][1]]["Crypto"]
            Messaging.sendMessage(20106, fields, Crypto)
        

    def getMessageType(self):
        return 10506

    def getMessageVersion(self):
        return self.messageVersion
