from Classes.Logic.LogicLong import LogicLong
from Classes.Wrappers.PlayerDisplayData import PlayerDisplayData

class PlayerProfile:
    def encode(calling_instance, fields, playerData):
        calling_instance.encodeLogicLong(LogicLong(fields["PlayerID"][0], fields["PlayerID"][1]))
        calling_instance.writeDataReference(16, playerData["FavouriteBrawler"])

        sortedBrawlers = sorted(playerData["OwnedBrawlers"], key=lambda x: (playerData["OwnedBrawlers"][x]['Trophies']), reverse=True)

        calling_instance.writeVInt(len(sortedBrawlers))
        for brawlerID in sortedBrawlers:
            brawlerData = playerData["OwnedBrawlers"][brawlerID]
            calling_instance.writeDataReference(16, brawlerID)
            if brawlerData["Skins"] != []:
                calling_instance.writeDataReference(29, brawlerData["Skins"][0]) # TODO: Sync with current skin
            else:
                calling_instance.writeDataReference(0)
            calling_instance.writeVInt(brawlerData["Trophies"])
            calling_instance.writeVInt(brawlerData["HighestTrophies"])
            calling_instance.writeVInt(brawlerData["PowerLevel"])
        calling_instance.writeVInt(19)

        calling_instance.writeVInt(1) 
        calling_instance.writeVInt(playerData["stats_3v3"]) # 3v3 victories

        calling_instance.writeVInt(2)
        calling_instance.writeVInt(playerData["Experience"]) # total exp

        calling_instance.writeVInt(3)
        calling_instance.writeVInt(playerData["Trophies"]) # current trophies

        calling_instance.writeVInt(4)
        calling_instance.writeVInt(playerData["HighestTrophies"]) # highest trophies

        calling_instance.writeVInt(5) 
        calling_instance.writeVInt(len(sortedBrawlers)) # unlocked brawler?

        calling_instance.writeVInt(8)
        calling_instance.writeVInt(playerData["stats_showdown"]) # solo victories

        calling_instance.writeVInt(11) 
        calling_instance.writeVInt(playerData["stats_duoshowdown"]) # duo victories

        calling_instance.writeVInt(9) 
        calling_instance.writeVInt(playerData["stats_robo_rumble"]) # highest level robo rumble

        calling_instance.writeVInt(12) 
        calling_instance.writeVInt(playerData["stats_robo"]) # highest level boss fight

        calling_instance.writeVInt(13)
        calling_instance.writeVInt(1) # highest power league points

        calling_instance.writeVInt(14)
        calling_instance.writeVInt(1) # some power league stuff最高排名

        calling_instance.writeVInt(15)
        calling_instance.writeVInt(playerData["stats_challenge"]) # most challenge win

        calling_instance.writeVInt(16) #highest level city rampage
        calling_instance.writeVInt(playerData["stats_city_rampage"])

        calling_instance.writeVInt(18) #highest solo power league rank
        calling_instance.writeVInt(playerData["stats_solorank"])

        calling_instance.writeVInt(17) #highest team power league rank
        calling_instance.writeVInt(playerData["stats_3v3rank"])

        calling_instance.writeVInt(19) # highest Club league rank
        calling_instance.writeVInt(playerData["stats_clubwars"])
        if "stats_Fame" not in playerData:
            playerData["stats_Fame"] = 0
        calling_instance.writeVInt(20) # number fame
        calling_instance.writeVInt(playerData["stats_Fame"])

        calling_instance.writeVInt(21)
        calling_instance.writeVInt(playerData["Experience"]) #v50

        calling_instance.writeVInt(22)
        calling_instance.writeVInt(playerData["Theme"]) #v50

        PlayerDisplayData.encode(calling_instance, playerData)

    def decode(calling_instance, fields):
        pass