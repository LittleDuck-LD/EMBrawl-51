from Classes.ClientsManager import ClientsManager
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Wrappers.PlayerProfile import PlayerProfile
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler

import json

class PlayerProfileMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player=None):
        db_instance = DatabaseHandler()
        playerData = db_instance.getPlayer(fields["PlayerID"])
        PlayerProfile.encode(self, fields, playerData)
        HaveClub = playerData['AllianceID'] != [0,0] and playerData['AllianceID'] != None
        if HaveClub == False:
            self.writeBoolean(False) #alliance
            return
        
        clubdb_instance = ClubDatabaseHandler()
        db_instance.loadAccount(player, player.ID)
        club_ID = playerData['AllianceID'][1]
        club_data = json.loads(clubdb_instance.getClubWithLowID(club_ID)[0][1])
        member_data = clubdb_instance.getMemberWithLowID(club_data,fields["PlayerID"][1])
        self.writeBoolean(True) #alliance
        self.writeLong(club_data['HighID'],club_data['LowID']) #alliance ID
        self.writeString(club_data['Name']) #alliance name
        self.writeDataReference(8,club_data['BadgeID']) # alliance icon
        self.writeVInt(club_data['Type']) # type
        self.writeVInt(len(club_data['Members'])) # member count
        self.writeVInt(clubdb_instance.getTotalTrophies(club_data)) # total trophies
        self.writeVInt(club_data['TrophiesRequired']) # minimum trophies to enter
        self.writeDataReference(0)
        self.writeString(str(club_data['RegionID'])) #location
        self.writeVInt(4) # unknown
        self.writeBoolean(club_data['FamilyFriendly']) #is Family friendly
        self.writeVInt(0)

        self.writeDataReference(25, member_data['Role']) #alliance role
        self.writeVInt(16)

    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24113

    def getMessageVersion(self):
        return self.messageVersion