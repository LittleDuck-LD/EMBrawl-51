
from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage


class TeamMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        self.writeVInt(fields["room_type"])
        self.writeBoolean(False)
        self.writeVInt(3)#小队人数上限
        self.writeLong(50,fields["room_id"])
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, 121)
        self.writeVInt(0)

        self.writeVInt(1)
        for x in range(1):

            self.writeBoolean(True)#是否队长

            self.writeLong(100,0)#玩家ID

            self.writeDataReference(16, 0)
            self.writeDataReference(29, 0)

            self.writeVInt(1000)
            self.writeVInt(99999)
            self.writeVInt(99999)

            self.writeVInt(11)
            self.writeVInt(0)

            self.writeBoolean(False)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeString("测试中")
            self.writeVInt(100)
            self.writeVInt(28000000 + 0)
            self.writeVInt(43000000 + 0)
            self.writeVInt(-1)

            #self.writeDataReference(23, fields["starpower"]) if False else self.writeVInt(0)
            #self.writeDataReference(23, fields["gadget"])    if False else self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeVInt(0)
        for x in range(0):
            pass

        self.writeVInt(0)
        if False:
            self.writeVInt(6)
        else:
            self.writeVInt(0)

        self.writeBoolean(False)
        self.writeBoolean(True)
        self.writeBoolean(True)

        self.writeVInt(0)

    def decode(self):
        return

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24124

    def getMessageVersion(self):
        return self.messageVersion