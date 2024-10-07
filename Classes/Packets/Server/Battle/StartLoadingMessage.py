from io import BytesIO

from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData
from Database.DatabaseHandler import DatabaseHandler


class StartLoadingMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeInt(1)
        self.writeInt(1)
        self.writeInt(0)

        self.writeInt(1)
        for Player in range(1):
        
            self.writeLong(100,0)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeInt(0)
            self.writeVInt(1)
            for i in range(1):
            
                self.writeDataReference(16,0)
                self.writeBoolean(True)
                if True:
                
                    #//logic Hero Upgrades
                    self.writeVInt(11)
                    self.writeDataReference(0)
                    self.writeDataReference(0)
                    self.writeDataReference(0)
                    self.writeDataReference(0)
                    self.writeDataReference(0)
                    #ByteStreamHelper.WriteDataReference(stream, StarPowerDatas[i])
                    #ByteStreamHelper.WriteDataReference(stream, AccessoryCardDatas[i])
                    #//ByteStreamHelper.WriteDataReference(stream, null)

                    #ByteStreamHelper.WriteDataReference(stream, Gear1)
                    #ByteStreamHelper.WriteDataReference(stream, Gear2)
                    #//self.writeVInt(3)
                    #//self.writeVInt(3)
                    #ByteStreamHelper.WriteDataReference(stream, null) //OverCharge

                
                self.writeBoolean(False)
                if False:
                
                    self.writeVInt(5)
                    self.writeDataReference(52, 175)
                    self.writeDataReference(52, 176)
                    self.writeDataReference(52, 177)
                    self.writeDataReference(52, 178)
                    self.writeDataReference(52, 179)
                    #ByteStreamHelper.WriteDataReference(stream, GetDefaultEmoteForCharacter(DataTables.Get(DataType.Character).GetDataByGlobalId<CharacterData>(CharacterIds[i]).Name, "HAPPY"))
                    #ByteStreamHelper.WriteDataReference(stream, GetDefaultEmoteForCharacter(DataTables.Get(DataType.Character).GetDataByGlobalId<CharacterData>(CharacterIds[i]).Name, "SAD"))
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(52, 175))
                    #ByteStreamHelper.WriteDataReference(stream, GetDefaultEmoteForCharacter(DataTables.Get(DataType.Character).GetDataByGlobalId<CharacterData>(CharacterIds[i]).Name, "THANKS"))
                    #ByteStreamHelper.WriteDataReference(stream, GetDefaultEmoteForCharacter(DataTables.Get(DataType.Character).GetDataByGlobalId<CharacterData>(CharacterIds[i]).Name, "GG"))
                    #//ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(52, 175))
                    self.writeVInt(5)


                
                self.writeBoolean(False)
                if False:
                    self.writeVInt(5)
                    self.writeDataReference(68, 0)
                    self.writeDataReference(68, 1)
                    self.writeDataReference(68, 2)
                    self.writeDataReference(68, 3)
                    self.writeDataReference(68, 4)
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(68, 0))
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(68, 1))
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(68, 2))
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(68, 3))
                    #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(68, 4))

                
                #string tmp = DataTables.Get(DataType.Character).GetDataByGlobalId<CharacterData>(CharacterIds[i]).Name
                #if (tmp == "MechaDude" || tmp == "CannonGirl") ByteStreamHelper.WriteDataReference(stream, null)
                #else ByteStreamHelper.WriteDataReference(stream, SkinIds[i])
                self.writeDataReference(0)
                self.writeDataReference(0)
                self.writeVInt(0)
            
            #db_instance = DatabaseHandler()
            #playerData = db_instance.getPlayer(player.ID)
            #PlayerDisplayData.encode(self,playerData)
            self.writeString("1")
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeVInt(-1)
            self.writeBoolean(False)
            self.writeBoolean(False)
            #if (self.writeBoolean(false))
            #{
            #    self.writeVLong(AccountId)
            #    self.writeString("SB")
            #    ByteStreamHelper.WriteDataReference(stream, null)//8
            #}
            #//new
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            #ByteStreamHelper.WriteDataReference(stream, T1)
            #ByteStreamHelper.WriteDataReference(stream, T2)
            #ByteStreamHelper.WriteDataReference(stream, E)
            #ByteStreamHelper.WriteDataReference(stream, GlobalId.CreateGlobalId(76, RandomNumberGenerator.GetInt32(0, 66)))//76
            self.writeVInt(0)
        

        self.writeInt(0) #// array 2*80LL

        self.writeInt(0)
        #foreach (int modifier in t) self.writeInt(modifier)

        self.writeInt(0)

        self.writeVInt(39)
        self.writeVInt(0)
        self.writeVInt(0)#//gamemode varidatino
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(15, 121)
        self.writeBoolean(False)
        #self.writeBattlePlayerMap(Stream,map)

        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(True)

    def decode(self):
        fields = {}
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 20559

    def getMessageVersion(self):
        return self.messageVersion