from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.AllianceHeaderEntry import AllianceHeaderEntry
from Database.DatabaseHandler import ClubDatabaseHandler
import json

class MyAllianceMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        if "HasClub" not in fields or fields["HasClub"] == True:
            clubdb_instance = ClubDatabaseHandler()
            clubData = json.loads(clubdb_instance.getClubWithLowID(player.AllianceID[1])[0][1])
            localMemberData = clubData["Members"][str(player.ID[1])]
            OnlinePlayers = ClientsManager.GetAll()
            OnlinePlayersInClub = 0
            for member in clubData['Members']:
                if int(member) in OnlinePlayers.keys():
                    OnlinePlayersInClub+=1
            self.writeVInt(OnlinePlayersInClub) # Onlines Members TODO: members state
            self.writeBoolean(True)
            self.writeDataReference(25, localMemberData["Role"])
        
            AllianceHeaderEntry.encode(self, clubdb_instance, clubData)

            self.writeBoolean(False)
        else:
            self.writeVInt(0) # Online people in alliance
            self.writeBoolean(False) # isInAlliance
            
            


    def decode(self):
        fields = {}
        fields["ResponseID"] = self.readVInt()
        fields["Unk1"] = self.readVInt()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24399

    def getMessageVersion(self):
        return self.messageVersion