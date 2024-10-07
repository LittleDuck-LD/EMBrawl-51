from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class AcceptFriendMessage(PiranhaMessage):
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
        if fields["AccountID"] == calling_instance.player.ID:
            fields["ErrorID"] = 4
            Messaging.sendMessage(20112, fields, cryptoInit)
            return
        
        if fields["AccountID"][0] != 100 or fields["AccountID"][1] > LastLowID:
            fields["ErrorID"] = 5
            Messaging.sendMessage(20112, fields, cryptoInit)
            return
         
        
        
        ownFriendData = None
        for i,Friend in enumerate(ownPlayerData["Friends"]):
            if Friend["ID"] == fields["AccountID"]:
                ownPlayerData["Friends"][i]["State"] = 4
                ownFriendData = ownPlayerData["Friends"][i]
                break
        if ownFriendData == None:
            fields["ErrorID"] = 5#找不到
            Messaging.sendMessage(20112, fields, cryptoInit)
            return
        db_instance.updatePlayerDataByLowID(ownPlayerData,calling_instance.player.ID[1])
        fields["FriendData"] = ownFriendData
        Messaging.sendMessage(20106, fields, cryptoInit)

        otherFriendData = None
        for i,Friend in enumerate(friendPlayerData["Friends"]):
            if Friend["ID"] == calling_instance.player.ID:
                friendPlayerData["Friends"][i]["State"] = 4
                otherFriendData = friendPlayerData["Friends"][i]
                break
        if otherFriendData == None:
            otherFriendData = {
                "ID":calling_instance.player.ID,
                "State":3,
                "Reason":fields["Reason"],
                "ReasonData":999
            }
            friendPlayerData["Friends"].append(otherFriendData)
        db_instance.updatePlayerDataByLowID(friendPlayerData,fields["AccountID"][1])
        
        onlinePlayers = ClientsManager.GetAll()
        if fields["AccountID"][1] in onlinePlayers:
            fields["FriendData"] = otherFriendData
            fields["Socket"] = onlinePlayers[fields["AccountID"][1]]["Socket"]
            Crypto = onlinePlayers[fields["AccountID"][1]]["Crypto"]
            Messaging.sendMessage(20106, fields, Crypto)
        db_instance.cursor.close()

    def getMessageType(self):
        return 10501

    def getMessageVersion(self):
        return self.messageVersion
