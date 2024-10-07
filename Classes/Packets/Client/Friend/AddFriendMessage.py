from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class AddFriendMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["Reason"] = self.readInt()
        fields["unk1"] = self.readInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        #if calling_instance.player.ID not in [[100,0],[100,46]]:
        #    fields["ErrorID"] = 0
        #    Messaging.sendMessage(20112, fields, cryptoInit)
        #    return
        print(fields)
        
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
        if len(ownPlayerData["Friends"]) >= 100:
            fields["ErrorID"] = 7
            Messaging.sendMessage(20112, fields, cryptoInit)
            return
        if len(friendPlayerData["Friends"]) >= 100:
            fields["ErrorID"] = 8
            Messaging.sendMessage(20112, fields, cryptoInit)
            return

        for i,Friend in enumerate(ownPlayerData["Friends"]):
            if Friend["ID"] == fields["AccountID"]:
                fields["ErrorID"] = 0
                Messaging.sendMessage(20112, fields, cryptoInit)
                return
        
        for i,Friend in enumerate(friendPlayerData["Friends"]):
            if Friend["ID"] == fields["AccountID"]:
                friendPlayerData["Friends"][i]["State"] = 4
                db_instance.updatePlayerDataByLowID(friendPlayerData,calling_instance.player.ID[1])
                return
        
        
        ownFriendData = {
            "ID":fields["AccountID"],
            "State":2,
            "Reason":fields["Reason"],
            "ReasonData":999
        }
        ownPlayerData["Friends"].append(ownFriendData)
        db_instance.updatePlayerDataByLowID(ownPlayerData,calling_instance.player.ID[1])
        fields["FriendData"] = ownFriendData
        Messaging.sendMessage(20106, fields, cryptoInit)

        
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
        return 14104

    def getMessageVersion(self):
        return self.messageVersion
