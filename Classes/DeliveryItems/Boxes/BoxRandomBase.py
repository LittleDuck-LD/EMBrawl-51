import random


from Classes.DeliveryItems.DeliveryItemsID import DeliveryItemsID
from Classes.Files.Classes.Random_Chest import Random_Chest
from Classes.Files.Classes.Random_Chest_Rewards import Random_Chest_Rewards
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Cards import Cards


class BoxRandomBase:

    def getBoxData(BoxName:str = "OldHeroBoxLarge", Droptime:int = 10, DeliveryItemType:int =11, PlayerID:list = [100,0]):
        BoxData = Random_Chest.getBoxDataByName(BoxName)
        BoxRate = {}
        for Reward in BoxData:
            BoxRate[Reward["RewardName"]]=int(Reward["Rate"])
        TotalRate = 0
        for name in BoxRate:
            TotalRate += BoxRate[name]
        BoxReward = []
        for i in range(Droptime):
            BoxKey = random.randint(0,TotalRate)
            TempKey = 0
            GotReward = False
            for name in BoxRate:
                TempKey += BoxRate[name]
                
                if GotReward == True:
                    pass
                elif TempKey >= BoxKey:
                    BoxReward.append(name)
                    GotReward = True
                    #print(BoxKey,TempKey,TotalRate,BoxRate,name)
                    
        
        FinalRewards=[]
        ResourceRewards={
            "Coins":0,
            "PowerPoints": 0
        }
        for RewardName in BoxReward:
            Reward = {
                    "Count":1,
                    "HeroID":[0,0],
                    "RewardType":7,
                    "SkinID":[0,0],
                    "EmoteID":[0,0],
                    "CardID":[0,0]
                }
            #RewardName = "Brawler Rare"
            RewardData = Random_Chest_Rewards().getRewardDataByName(RewardName)
            ID = DeliveryItemsID().getIDByName(RewardData["TypeName"])
            if "Brawler" in RewardName:
                Rarity = RewardName.split(" ")[1]
                match(Rarity):
                    case "Rare":
                        CardRarity = "rare"
                    case "Super":
                        CardRarity = "super_rare"
                    case "Epic":
                        CardRarity = "epic"
                    case "Mythic":
                        CardRarity = "mega_epic"
                    case "Legendary":
                        CardRarity = "legendary"
                    case _:
                        print(Rarity)
                BrawlerList = Characters().getBrawlerFromSepcificRarity(CardRarity)
                Reward["HeroID"] = [16,random.choice(BrawlerList)]
                isAlreadyGot = False
                for Items in FinalRewards:
                    if Items["HeroID"] == Reward["HeroID"]:
                        ResourceRewards["Coins"] += 1000
                        isAlreadyGot = True
                if isAlreadyGot == True:
                    continue
                Reward["Count"] = 1
                Reward["RewardType"] = 1  
            elif "Gadget" == RewardName:
                CardList = Cards().getCardsListFromMetaType(5)
                Reward["CardID"] = [23,random.choice(CardList)]
                Reward["Count"] = 1
                Reward["RewardType"] = 4
            elif "Star Power" == RewardName:
                CardList = Cards().getCardsListFromMetaType(4)
                Reward["CardID"] = [23,random.choice(CardList)]
                Reward["Count"] = 1
                Reward["RewardType"] = 4
            elif "Overcharge" == RewardName:
                CardList = Cards().getCardsListFromMetaType(6)
                Reward["CardID"] = [23,random.choice(CardList)]
                Reward["Count"] = 1
                Reward["RewardType"] = 4
            elif "Coins" in RewardName:
                ResourceRewards["Coins"] += random.randint(int(RewardData["AmountMin"]),int(RewardData["AmountMax"]))
                continue
            elif "Power Points" in RewardName:
                ResourceRewards["PowerPoints"] += random.randint(int(RewardData["AmountMin"]),int(RewardData["AmountMax"]))
                continue
            else:
                Reward["Count"] = random.randint(int(RewardData["AmountMin"]),int(RewardData["AmountMax"]))
                Reward["RewardType"] = int(ID)
            FinalRewards.append(Reward)
        for name in ResourceRewards:
            ID = DeliveryItemsID().getIDByName(name)
            if ResourceRewards[name] != 0:
                FinalRewards.append({
                    "Count":ResourceRewards[name],
                    "HeroID":[0,0],
                    "RewardType":ID,
                    "SkinID":[0,0],
                    "EmoteID":[0,0],
                    "CardID":[0,0]
                })
        FinalRewards.reverse()
        Template = {
            "Type":DeliveryItemType,
            "Rewards": FinalRewards
        }

        return Template