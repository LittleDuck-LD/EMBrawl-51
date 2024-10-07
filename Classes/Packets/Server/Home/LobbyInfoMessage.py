import time

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class LobbyInfoMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        try:
            Latency = player.Latency
        except AttributeError:
            Latency = "--"   
        LineFeeds = ""
        for i in range(30):
            LineFeeds+="\n"
        
        self.writeVInt(ClientsManager.GetCount())
        self.writeString(f"EMBrawl\n版本：{player.ClientVersion}\n延迟：{Latency}ms\n在线玩家：{ClientsManager.GetCount()}\n可前往设置更换背景！{LineFeeds}")
        self.writeVInt(1) # count event
        for i in range(1):
            self.writeVInt(0) # count event
            self.writeVInt(0) # count event
            self.writeVInt(0) # count event
            self.writeVInt(0) # count event
            self.writeVInt(0) # count event
        self.writeVInt(int(time.time())) # new timer in v51

    def decode(self):
        fields = {}
        fields["PlayerCount"] = self.readVInt()
        fields["Text"] = self.readString()
        fields["Unk1"] = self.readVInt()
        fields["Timer"] = self.readVInt()
        super().decode(fields)
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 23457

    def getMessageVersion(self):
        return self.messageVersion