import time

from Classes.ByteStreamHelper import ByteStreamHelper
from Classes.Packets.PiranhaMessage import PiranhaMessage
from Database.DatabaseHandler import DatabaseHandler
from Static.StaticData import StaticData
from Classes.Logic.LogicStarrDropData import starrDropOpening
from Classes.Notification.NotificationFactory import NotificationFactory


class OwnHomeDataMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        db_instance = DatabaseHandler()
        
        ownedBrawlersCount = len(player.OwnedBrawlers)
        ownedPinsCount = len(player.OwnedPins)
        ownedThumbnailCount = len(player.OwnedThumbnails)
        ownedSkins = []
        playerData = db_instance.getPlayer(player.ID)
        AdditionalNotification = []

        for brawlerInfo in player.OwnedBrawlers.values():
            try:
                ownedSkins.extend(brawlerInfo["Skins"])
            except KeyError:
                continue
        self.writeVInt(int(time.time())) #timestamp
        self.writeVInt(1191532375)#timestamp
        self.writeVInt(2023189)#timestamp LogicDailyDataBegin
        self.writeVInt(73530) #timestamp
        self.writeVInt(player.Trophies) # current trophies
        self.writeVInt(player.HighestTrophies) # hightest trophies
        self.writeVInt(player.HighestTrophies) #highest trophies today
        
        self.writeVInt(player.TrophyRoadTier) # collected trophy road rewards
        self.writeVInt(player.Experience) # exp points
         # profile icon
        self.writeDataReference(28, player.Thumbnail)
        # name color
        self.writeDataReference(43, player.Namecolor)

        self.writeVInt(26) # played Game Mode
        for x in range(26):
            self.writeVInt(x)

        self.writeVInt(0) # selected skin count
        for x in range(0):
            self.writeDataReference(29, x)

        self.writeVInt(0) # available ramdon skins
        for x in range(0):
            self.writeDataReference(29, x)

        self.writeVInt(0) # random skins
        for x in range(0):
            self.writeDataReference(29, x)

        SkinBlackList = [351]
        SkinList = list(range(725))
        for Skin in SkinBlackList:
            del SkinList[Skin]
        self.writeVInt(len(SkinList))
        
        for x in range(len(SkinList)):
            self.writeDataReference(29, x) # unlocked skin array

        self.writeVInt(0) # skin purchase option
        for x in range(0):
            self.writeDataReference(29, x)

        self.writeVInt(0) # unk skin array5
        for x in range(0):
            self.writeDataReference(29, x)

        self.writeVInt(0) # leaderboard region
        self.writeVInt(player.HighestTrophies) # highest trophies
        self.writeVInt(0) # tokens used in battle
        self.writeVInt(2) # control mode
        self.writeBoolean(True) # battle hints
        self.writeVInt(player.TokensDoubler) # token doubler left
        self.writeVInt(115) # maybe starr drop timer ? #v50
        self.writeVInt(335442) # trophy league timer
        self.writeVInt(1001442) # power play timer
        self.writeVInt(5778642) # Brawl pass season timer
        #self.writeVInt(0) # maybe starr drop timer ? #v50

        self.writeVInt(120) # 
        self.writeVInt(200) # 
        self.writeVInt(0) # drop chance of characters in boxes
        # self.writeVInt(93)
        # self.writeVInt(206)
        # self.writeVInt(456)
        # self.writeVInt(1001)
        # self.writeVInt(2264)

        self.writeBoolean(True) # false, false, true
        self.writeVInt(2) # token doubler  new tag state
        self.writeVInt(2) # event tickets new tag state
        self.writeVInt(2) # coins pack new tag state
        self.writeVInt(0) # name change cost
        self.writeVInt(0) # timer for next name change
        '''
        0: FREE BOX
        1: COINS
        2: RANDOM BRAWLER RARITY
        3: BRAWLER
        4: SKIN
        5: ?
        6: BRAWL BOX
        7: TICKETS
        8: POWER POINTS
        9: TOKEN DOUBLER
        10: MEGA BOX
        11: ?
        12: POWER POINTS
        13: NEW EVENT SLOT
        14: BIG BOX
        15: BRAWL BOX
        16: GEMS
        17: STAR POINTS
        18: QUEST???
        19: PIN
        20: SET OF PINS
        21: PIN PACK
        22: PIN PACK FOR
        23: PIN OF RARITY
        24: ?
        25: ?
        26: ?
        27: PIN PACK OF RARITY
        28: ?
        29: ?
        30: NEW BRAWLER UPGRADED TO LEVEL
        31: RANDOM BRAWLER OF RARITY UPGRADED TO LEVEL
        32: GEAR TOKENS
        33: SCRAP
        38: 英雄券
        42: 金券s15更新的最后的内容
        43: ?
        44: ?
        45: BLING
        46: ?
        47: 极限充能
        49: STARR DROP
        '''
        ShopData = StaticData.ShopData
        self.writeVInt(2 + len(ShopData["Offers"]) + 0) # type: ignore # Offers count

        self.writeVInt(1)  # RewardCount
        for i in range(1):
            self.writeVInt(49) # ItemType
            self.writeVInt(10)
            self.writeDataReference(0) # CsvID
            self.writeVInt(5)

        self.writeVInt(0)#ID
        self.writeVInt(-1)#需要货币的数量
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(8881)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        #self.writeInt(0)
        self.writeString("全英雄 表情 头像 皮肤")
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeString("offer_wf")
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(1)#加倍=1，加量=2，优惠=3，无=0/>=4
        self.writeVInt(114514)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(-1)
        self.writeVInt(0)
        #v51
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)



        self.writeVInt(2)  # RewardCount
        for i in range(1):
            self.writeVInt(16) # ItemType
            self.writeVInt(140)
            self.writeDataReference(0) # CsvID
            self.writeVInt(0)

            self.writeVInt(1) # ItemType
            self.writeVInt(100)
            self.writeDataReference(0) # CsvID
            self.writeVInt(0)

        self.writeVInt(1)
        self.writeVInt(-1)
        self.writeVInt(950400)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeBoolean(False)
        self.writeVInt(8881)
        self.writeVInt(0)
        self.writeBoolean(False)
        self.writeVInt(49)
        self.writeString("清空账号")
        self.writeVInt(0)
        self.writeBoolean(True)
        self.writeString("offer_wf")
        self.writeVInt(-1)
        self.writeBoolean(False)
        self.writeVInt(1)
        self.writeVInt(10)
        self.writeString()
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeDataReference(0)
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(-1)
        self.writeVInt(0)
        #v51
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)

        for i in ShopData["Offers"]: # type: ignore
            self.writeVInt(i["RewardsCount"])  # RewardCount
            for reward in i["Rewards"]:
                self.writeVInt(reward["ItemType"]) # ItemType
                self.writeVInt(reward["Amount"])
                if reward["CsvID1"] != 0:
                    self.writeDataReference(reward["CsvID1"], reward["CsvID2"]) # CsvID
                else:
                    self.writeDataReference(0)
                self.writeVInt(reward["SkinID"])

            self.writeVInt(i["Currency"])
            self.writeVInt(i["Cost"])
            self.writeVInt(i["Time"])
            self.writeVInt(2) # ?
            self.writeVInt(0)
            self.writeBoolean(i["Claim"])
            self.writeVInt(8881) # ?
            self.writeVInt(0)
            self.writeBoolean(i["DailyOffer"])
            self.writeVInt(i["OldPrice"])
            #self.writeInt(0)
            if i["Text"] == "None":
                self.writeString()
            else:
                self.writeString(i["Text"])
            self.writeVInt(0)
            self.writeBoolean(False)
            if i["Background"] == "None":
                self.writeString()
            else:
                self.writeString(i["Background"])
            self.writeVInt(-1)
            self.writeBoolean(i["Processed"])
            self.writeVInt(i["TypeBenefit"])
            self.writeVInt(i["Benefit"])
            self.writeString()
            self.writeBoolean(i["OneTimeOffer"])
            self.writeBoolean(i["Claimed"])
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(-1)
            self.writeVInt(0)
            #v51
            self.writeBoolean(False)
            self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)


        

        self.writeVInt(player.Tokens) # tokens for battle
        self.writeVInt(-1) # timer until new token

        self.writeVInt(0) #count
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1) #unk
        self.writeVInt(30) #unk

        self.writeByte(len(player.SelectedBrawlers)) # count brawlers selected
        for i in player.SelectedBrawlers:
            self.writeDataReference(16, i)

        self.writeString(str(player.Theme-41000000)) # location
        self.writeString(player.ContentCreator) # supported creator

        self.writeVInt(8) # count

        self.writeVLong(1,18)
        self.writeVLong(0,19)

        self.writeVInt(1) # resources id
        self.writeVInt(9) # resources gained

        self.writeVInt(1) # resources id
        self.writeVInt(22) # resources gained

        self.writeVInt(3) # resources id
        self.writeVInt(25) # resources gained

        self.writeVInt(1) # resources id
        self.writeVInt(24) # resources gained

        self.writeVInt(0) # resources id
        self.writeVInt(15) # resources gained

        self.writeVInt(32447) # resources id
        self.writeVInt(28) # resources gained


        self.writeVInt(0) # count 0
        for x in range(0):
            self.writeVInt(x)
            self.writeVInt(x)
            self.writeDataReference(29, x)

        self.writeVInt(20) # count brawl pass seasons
        for season in range(20):
            self.writeVInt(season) # season
            self.writeVInt(56999) # season token collected
            self.writeBoolean(True) # 0x1
            self.writeVInt(56)
            self.writeBoolean(False)
            self.writeBoolean(True) # 0x1
            self.writeInt(-4)
            self.writeInt(16383)
            self.writeInt(0)
            self.writeInt(0)
            self.writeBoolean(True) # 0x1
            self.writeInt(-4)
            self.writeInt(2147483647)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVLong(0)


        self.writeBoolean(True) # 0x1
        self.writeVInt(1)

        self.writeVInt(6293)
        self.writeVInt(19)
        self.writeVInt(1)
        self.writeVInt(99)
        self.writeVInt(100)
        
        self.writeVInt(3)

        self.writeDataReference(16,0)
        self.writeDataReference(16,1)
        self.writeDataReference(16,2)

        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(27)
        self.writeVInt(114514)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(30)
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)
        #self.writeVInt(16)
        #self.writeVInt(-64)
        #self.writeVInt(-425592849)
        #self.writeVInt(0)
        
        
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(0) # club league quest count

        self.writeBoolean(True) # Vanity items
        self.writeVInt(ownedPinsCount + ownedThumbnailCount + 71)  # Vanity Count
        for i in player.OwnedPins:
            self.writeDataReference(52, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)

        for i in player.OwnedThumbnails:
            self.writeDataReference(28, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)
        
        for i in range(71):
            self.writeDataReference(76, i)
            self.writeVInt(1)
            for i in range(1):
                self.writeVInt(1)
                self.writeVInt(1)
        
        #for i in range(213):
        #    self.writeDataReference(68, i)
        #    self.writeVInt(1)
        #    for i in range(1):
        #        self.writeVInt(1)
        #        self.writeVInt(1)
        



        self.writeBoolean(False) # Power league season data
        if False:
            for x in range(12):
                self.writeVInt(0)
        self.writeInt(0)
        self.writeVInt(0)
        self.writeDataReference(16, player.FavouriteBrawler)
        self.writeBoolean(False) # Logic Daily Data end

        self.writeVInt(2023189) # Logic Conf Data begin

        self.writeVInt(34) # event slot id
        self.writeVInt(1)
        self.writeVInt(2)
        self.writeVInt(3)
        self.writeVInt(4)
        self.writeVInt(5)
        self.writeVInt(6)
        self.writeVInt(7)
        self.writeVInt(8)
        self.writeVInt(9)
        self.writeVInt(10)
        self.writeVInt(11)
        self.writeVInt(12) # map maker candidate
        self.writeVInt(13) # map maker winner
        self.writeVInt(14)
        self.writeVInt(15)
        self.writeVInt(16)
        self.writeVInt(17)
        self.writeVInt(18) # mystery
        self.writeVInt(19)
        self.writeVInt(20)# championship challenge
        self.writeVInt(21) 
        self.writeVInt(22)
        self.writeVInt(23)
        self.writeVInt(24)
        self.writeVInt(25)
        self.writeVInt(26)
        self.writeVInt(27)
        self.writeVInt(28)
        self.writeVInt(29)
        self.writeVInt(30)
        self.writeVInt(31)
        self.writeVInt(32)
        self.writeVInt(33)
        self.writeVInt(34) # hypercharge 

        self.writeVInt(3 + 1) # Events

        eventIndex = 1
        for i in [5, 567, 121]:
            self.writeVInt(-1)
            self.writeVInt(eventIndex)  # EventType
            self.writeVInt(0)  # EventsBeginCountdown
            self.writeVInt(0)  # Timer
            self.writeVInt(0)  # tokens reward for new event
            self.writeDataReference(15, i)  # MapID
            self.writeVInt(-1)  # GameModeVariation
            self.writeVInt(2)  # State
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)  # Modifiers
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # Map Maker Map Structure Array
            if False:
                self.writeVLong(0,0)
                self.writeString()
                self.writeVInt(0)
                self.writeDataReference(0)
                #112LL?
                self.writeVLong(0,0)
                self.writeString()
                self.writeVInt(0)#if=0多读一个VInt就return
                self.writeVInt(0)
                for x in range(0):
                    self.writeVLong(0,0)
            self.writeVInt(0)
            self.writeBoolean(False)  # Power League Data Array
            
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeBoolean(False)  # ChronosTextEntry
            if False:
                self.writeString()
                self.writeVInt(0)
            self.writeBoolean(False)
            if False:
                self.writeString()
                self.writeVInt(0)
            self.writeBoolean(False)
            if False:
                self.writeString()
                self.writeVInt(0)
            self.writeVInt(-1)#Reward??
            self.writeBoolean(False)#2*32LL
            self.writeBoolean(False)#(6+1)*VInt

            self.writeVInt(-1) # 
            self.writeVInt(0) # new count v51 DataReference
            self.writeVInt(0) # new count v51 VInt
            self.writeVInt(0) # new count v51
            eventIndex += 1

        self.writeVInt(-1)
        self.writeVInt(12)  # EventType
        self.writeVInt(0)  # EventsBeginCountdown
        self.writeVInt(0)  # Timer
        self.writeVInt(0)  # tokens reward for new event
        self.writeDataReference(15, 0)  # MapID
        self.writeVInt(-1)  # GameModeVariation
        self.writeVInt(2)  # State
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)  # Modifiers
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Map Maker Map Structure Array
        if False:
            self.writeVLong(0,0)
            self.writeString()
            self.writeVInt(0)
            self.writeDataReference(0)
            self.writeVInt(0)#112LL?
            self.writeVLong(0,0)
            self.writeString()
            self.writeVInt(0)#if=0多读一个VInt就return
            self.writeVInt(0)
            for x in range(0):
                self.writeVLong(0,0)
        self.writeVInt(0)
        self.writeBoolean(False)  # Power League Data Array
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)  # ChronosTextEntry
        if False:
            self.writeString()
            self.writeVInt(0)
        self.writeBoolean(False)
        if False:
            self.writeString()
            self.writeVInt(0)
        self.writeBoolean(False)
        if False:
            self.writeString()
            self.writeVInt(0)
        self.writeVInt(-1)#Reward??
        self.writeBoolean(False)#2*32LL
        self.writeBoolean(False)#(6+1)*VInt

        self.writeVInt(-1) # 
        self.writeVInt(0) # new count v51 DataReference
        self.writeVInt(0) # new count v51 VInt
        self.writeVInt(0) # new count v51


        self.writeVInt(0) # upcoming event count
       
        ByteStreamHelper.encodeIntList(self, [20, 35, 75, 140, 290, 480, 800, 1250, 1875, 2800]) # Brawler Upgrade Cost
        ByteStreamHelper.encodeIntList(self, [20, 50, 140, 280]) # Shop Coins Price
        ByteStreamHelper.encodeIntList(self, [150, 400, 1200, 2600]) # Shop Coins Amount

        self.writeVInt(0) #locked for chronos
        for x in range(0):
            self.writeDataReference(16, 61)
            self.writeInt(0)
            self.writeInt(0)

        self.writeVInt(4)
        
        DisabledThemeList = [[90,105],[115,120]]
        IsThemeIDDisabled = False
        for List in DisabledThemeList:
            TempList = list(range(List[0],List[1]))
            if int(player.Theme-41000000) in TempList:
                IsThemeIDDisabled = True
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : "检测到您的背景无法正常加载，请尽快更换！\n\n--EMBrawl",
                    "Sender" : 1
                }
                AdditionalNotification.append(NotificationData)
                break
        
        if IsThemeIDDisabled == True:
            self.writeVLong(41000000 , 1) # theme
        else:
            self.writeVLong(player.Theme , 1) # theme
        self.writeVLong(36270,61)
        self.writeVLong(0,50)
        self.writeVLong(0,14)
        


        self.writeVInt(0) # Timed int entry count 4*VInt
        #self.writeVLong(36270,61)
        # self.writeVInt(31)
        # self.writeVInt(1)
        # self.writeVInt(499427)
        # self.writeVInt(758627)
        # self.writeVInt(29)
        # self.writeVInt(24)
        # self.writeVInt(0)
        # self.writeVInt(413027)
        self.writeVInt(0) # custom event
        for x in range(0):
            self.writeVInt(2)
            self.writeVInt(1)
            self.writeString()
            self.writeVInt(1)
            self.writeString()
            self.writeVInt(1)
            self.writeString()
            self.writeVInt(1)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(2)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(-1)

        self.writeVInt(2)
        self.writeVInt(1)
        self.writeVInt(4)

        ByteStreamHelper.encodeIntList(self, [0, 29, 79, 169, 349, 699]) # brawler cost gems ?
        ByteStreamHelper.encodeIntList(self, [0, 160, 450, 114514, 1250, 2500]) # what is that ? looks like chroma price of chromatic brawlers but it doesn't go under 500
        #logic conf data end
        self.writeLong(0, 1) # Player ID
        


        self.writeVInt(len(AdditionalNotification)+len(player.Notification)) # Notification factory
        

        
        player.Notification.reverse()
        for Noti in player.Notification:
            fields["NotificationData"] = Noti
            Notification = NotificationFactory.createNotification(fields["NotificationData"]["ID"])
            Notification.encode(self, fields)
        for Noti in AdditionalNotification:
            fields["NotificationData"] = Noti
            Notification = NotificationFactory.createNotification(fields["NotificationData"]["ID"])
            Notification.encode(self, fields)


        
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(1) # gatcha drop
        
        for x in range(1):
            self.writeVInt(1) 
            self.writeDataReference(0)
            self.writeVInt(8) 
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeDataReference(0)
            self.writeVInt(0) 
            self.writeVInt(0) 
            self.writeVInt(0) 

        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeBoolean(False)#login calendar
        # new function v46
        countBrawler = 74
        self.writeVInt(0) # new function v46 Gears
        
        self.writeBoolean(True) # 星妙之路 不是login calendar
        if True:
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(16,1)#流彩
            
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(16,2)
            
            self.writeDataReference(0)
            self.writeVInt(2)
            for i in range(2):#星妙之路本体
                self.writeDataReference(16,i)

                self.writeVInt(10)#需要英雄券数量
                self.writeVInt(1)#解锁需要的宝石数
                #for
                self.writeVInt(2)
                for x in range(2):
                    self.writeVInt(1)
                    self.writeBoolean(False)
                self.writeVInt(3)#当前已积累英雄券数量
                self.writeVInt(0)

                self.writeVInt(0)
                
                #for datareference
            self.writeVInt(1)
            for i in range(1):
                self.writeDataReference(16,0)

                self.writeVInt(10)#需要英雄券数量
                self.writeVInt(1)#解锁需要的宝石数
                #for
                self.writeVInt(2)
                for x in range(2):
                    self.writeVInt(1)
                    self.writeBoolean(False)
                self.writeVInt(3)#当前已积累英雄券数量
                self.writeVInt(0)

                self.writeVInt(0)
                
                #for datareference
            self.writeVInt(1)
            for i in range(1):
                self.writeVLong(0,0)
            self.writeVInt(0)
            

        self.writeVInt(23) # 专精
        for i in range(23):
            self.writeVInt(24800)#专精点数
            self.writeVInt(9)#已领取奖励数量
            self.writeDataReference(16,i)#英雄ID
        

        self.writeDataReference(0) # v48

        #self.writeDataReference(0) # v48
        #self.writeDataReference(0) # v48
        #self.writeDataReference(0) # v48
        #self.writeDataReference(0) # v48
        if player.BattleCardThumb1 != 0:
            self.writeDataReference(28, player.BattleCardThumb1)
        else:
            self.writeDataReference(0)
        if player.BattleCardThumb2 != 0:
            self.writeDataReference(28, player.BattleCardThumb2)
        else:
            self.writeDataReference(0)
        if player.BattleCardEmote != 0:
            self.writeDataReference(52, player.BattleCardEmote)
        else:
            self.writeDataReference(0)
        if player.BattleCardTitle != 0:
            self.writeDataReference(76, player.BattleCardTitle)
        else:
            self.writeDataReference(0)
        self.writeBoolean(player.BattleCardThumb1 == 0)  # v48
        self.writeBoolean(player.BattleCardThumb2 == 0)  # v48
        self.writeBoolean(player.BattleCardEmote == 0)  # v48
        self.writeBoolean(player.BattleCardTitle == 0)  # v48

        self.writeVInt(0)

        # v50 this is starr drop thing
        starrDropOpening.encode(self)
        #self.writeVInt(0) # end LogicClientHome
        #if "FakeID" in playerData:
        #    self.writeVLong(playerData["FakeID"][0], playerData["FakeID"][1])
        #else:
        #    self.writeVLong(player.ID[0], player.ID[1]) # player id
        self.writeVLong(player.ID[0], player.ID[1]) # player id
        self.writeVLong(0, 0)
        self.writeVLong(0, 0)
        self.writeStringReference(player.Name)
        self.writeBoolean(player.Registered) # name set
        self.writeInt(-1)

        self.writeVInt(16)

        self.writeVInt(7 + ownedBrawlersCount)#Resources

        for brawlerInfo in player.OwnedBrawlers.values():
            self.writeDataReference(23, brawlerInfo["CardID"])
            self.writeVInt(-1)
            self.writeVInt(1)

        self.writeDataReference(5, 8)
        self.writeVInt(-1)
        self.writeVInt(1000)#金币

        self.writeDataReference(5, 10)
        self.writeVInt(-1)
        self.writeVInt(1234)# 星光点数

        self.writeDataReference(5, 13)
        self.writeVInt(-1)
        self.writeVInt(99999) # Club coins

        self.writeDataReference(5, 18)
        self.writeVInt(-1)
        self.writeVInt(5) # spray

        self.writeDataReference(5, 23)
        self.writeVInt(-1)
        self.writeVInt(114514) # blings

        self.writeDataReference(5, 20)
        self.writeVInt(-1)
        self.writeVInt(100000) # 流彩券
        if "stats_Fame" not in playerData:
            playerData["stats_Fame"] = 0
        self.writeDataReference(5, 21)
        self.writeVInt(-1)
        self.writeVInt(playerData["stats_Fame"]) # fames

        
        self.writeVInt(ownedBrawlersCount)

        for brawlerID,brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["Trophies"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["HighestTrophies"])

        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerPoints"])

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["PowerLevel"] - 1)


        self.writeVInt(0)

        self.writeVInt(ownedBrawlersCount)

        for brawlerID, brawlerInfo in player.OwnedBrawlers.items():
            self.writeDataReference(16, brawlerID)
            self.writeVInt(-1)
            self.writeVInt(brawlerInfo["State"])

        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # 指定战力能量
        self.writeVInt(0) # Array

        self.writeVInt(2147483647) # Diamonds
        self.writeVInt(2147483647) # Free Diamonds
        self.writeVInt(10) # Player Level
        self.writeVInt(100)
        self.writeVInt(0) # CumulativePurchasedDiamonds or Avatar User Level Tier | 10000 < Level Tier = 3 | 1000 < Level Tier = 2 | 0 < Level Tier = 1
        self.writeVInt(100) # Battle Count
        self.writeVInt(10) # WinCount
        self.writeVInt(80) # LoseCount
        self.writeVInt(50) # WinLooseStreak
        self.writeVInt(20) # NpcWinCount
        self.writeVInt(0) # NpcLoseCount
        self.writeVInt(2) # TutorialState | shouldGoToFirstTutorialBattle = State == 0
        self.writeVInt(12)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        

    def decode(self):
        fields = {}
        # fields["AccountID"] = self.readLong()
        # fields["HomeID"] = self.readLong()
        # fields["PassToken"] = self.readString()
        # fields["FacebookID"] = self.readString()
        # fields["GamecenterID"] = self.readString()
        # fields["ServerMajorVersion"] = self.readInt()
        # fields["ContentVersion"] = self.readInt()
        # fields["ServerBuild"] = self.readInt()
        # fields["ServerEnvironment"] = self.readString()
        # fields["SessionCount"] = self.readInt()
        # fields["PlayTimeSeconds"] = self.readInt()
        # fields["DaysSinceStartedPlaying"] = self.readInt()
        # fields["FacebookAppID"] = self.readString()
        # fields["ServerTime"] = self.readString()
        # fields["AccountCreatedDate"] = self.readString()
        # fields["StartupCooldownSeconds"] = self.readInt()
        # fields["GoogleServiceID"] = self.readString()
        # fields["LoginCountry"] = self.readString()
        # fields["KunlunID"] = self.readString()
        # fields["Tier"] = self.readInt()
        # fields["TencentID"] = self.readString()
        #
        # ContentUrlCount = self.readInt()
        # fields["GameAssetsUrls"] = []
        # for i in range(ContentUrlCount):
        #     fields["GameAssetsUrls"].append(self.readString())
        #
        # EventUrlCount = self.readInt()
        # fields["EventAssetsUrls"] = []
        # for i in range(EventUrlCount):
        #     fields["EventAssetsUrls"].append(self.readString())
        #
        # fields["SecondsUntilAccountDeletion"] = self.readVInt()
        # fields["SupercellIDToken"] = self.readCompressedString()
        # fields["IsSupercellIDLogoutAllDevicesAllowed"] = self.readBoolean()
        # fields["isSupercellIDEligible"] = self.readBoolean()
        # fields["LineID"] = self.readString()
        # fields["SessionID"] = self.readString()
        # fields["KakaoID"] = self.readString()
        # fields["UpdateURL"] = self.readString()
        # fields["YoozooPayNotifyUrl"] = self.readString()
        # fields["UnbotifyEnabled"] = self.readBoolean()
        # super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24101

    def getMessageVersion(self):
        return self.messageVersion