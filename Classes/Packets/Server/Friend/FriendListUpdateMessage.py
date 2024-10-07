import time
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler


class FriendListUpdateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        friendData = fields["FriendData"]
        self.writeBoolean(True)
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(friendData["ID"])
        isOnline = True
        if ClientsManager.GetPlayerByLowID(playerData["ID"][1]) == False:
            isOnline = False
        self.writeLong(playerData["ID"][0],playerData["ID"][1])  # ID

        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeString()

        self.writeInt(playerData["Trophies"])  # Trophies
        self.writeInt(friendData["State"])#好友状态 3=等审核 4=为好友
        self.writeInt(friendData["Reason"])#加好友原因
        self.writeInt(friendData["ReasonData"])#原因详情数据
        self.writeInt(0)

        self.writeBoolean(False)#战队
        if False:
            self.writelong(101,0)
            self.writeInt(100)
            self.writeString("爱萝莉战队")
            self.writeInt(0)
            self.writeInt(0)

        self.writeString()
        self.writeInt(int(time.time()) - playerData["LastOnlineTime"] if not isOnline else -1)
        self.writeInt(playerData["stats_solorank"])#段位

        self.writeBoolean(True)  # ?? is a player?

        self.writeString(playerData["Name"])
        self.writeVInt(100)
        self.writeVInt(28000000 + playerData["Thumbnail"])
        self.writeVInt(43000000 + playerData["Namecolor"])
        if True:
            self.writeVInt(43000000 + playerData["Namecolor"])
        else:
            self.writeVInt(-1)
        self.writeInt(0)
        self.writeInt(0)
        

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20106

    def getMessageVersion(self):
        return self.messageVersion