from Classes.Commands.LogicServerCommand import LogicServerCommand

import random

from Classes.DeliveryItems.DeliveryItemFactory import DeliveryItemFactory

class LogicGiveDeliveryItemsCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        if "BoxType" not in fields:
            fields["BoxType"] = 11
        if "ShowType" not in fields:
            fields["ShowType"] = 0
        self.writeVInt(0)#没有用

        self.writeVInt(1)#物品数量
        for i in range(1):
            if fields["BoxType"] == 100:
                BoxData = fields["BoxData"]
            else:
                BoxData = DeliveryItemFactory.createDeliveryItem(fields["BoxType"])().getBoxData()
            #print(BoxData)
            

            self.writeVInt(fields["BoxType"])#物品类型
            
            self.writeVInt(len(BoxData["Rewards"]))#奖励数量
            '''
            for i in range(1):

                self.writeVInt(1)#count
                self.writeDataReference(29,100)#data
                self.writeVInt(19)#type
                self.writeDataReference(0)
                self.writeDataReference(0)#emote
                self.writeDataReference(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
            
            for i in range(10):

                self.writeVInt(1)#count
                self.writeDataReference(16, i)#data
                self.writeVInt(1)#type
                self.writeDataReference(0)
                self.writeDataReference(0)#emote
                self.writeDataReference(0)
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
                '''
            for RewardData in BoxData["Rewards"]:

                self.writeVInt(RewardData["Count"])#count
                self.writeDataReference(RewardData["HeroID"][0],RewardData["HeroID"][1])#data(英雄)type=1
                self.writeVInt(RewardData["RewardType"])#type
                self.writeDataReference(RewardData["SkinID"][0],RewardData["SkinID"][1])#皮肤type=9
                self.writeDataReference(RewardData["EmoteID"][0],RewardData["EmoteID"][1])#表情ID
                self.writeDataReference(RewardData["CardID"][0],RewardData["CardID"][1])#?cardsID
                self.writeVInt(0)
                self.writeVInt(0)
                self.writeVInt(0)
            '''
            self.writeVInt(1)#count
            self.writeDataReference(16,0)#data
            self.writeVInt(7)#type
            self.writeDataReference(0)
            self.writeDataReference(0)#emote
            self.writeDataReference(23, 606)#cardsID
            self.writeVInt(3)
            self.writeVInt(4)
            self.writeVInt(5)
            '''

            

        
        
        
        '''
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(29)
        self.writeVInt(218)
        self.writeVInt(5)
        self.writeHexa('00 00 00', 3)
        
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        '''

        self.writeBoolean(True)#array
        #if True:
        #    self.writeVInt(0)
        #    self.writeVInt(0)
        #    self.writeVInt(0)
        #    for i in range(0):
        #        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)#1=不显示
        self.writeVInt(114513)#第x+2季奖励
        self.writeVInt(fields["ShowType"])#0=宝箱 1=赛季末奖励 2=4 3=养成新方式 4=直接送 5=宝箱
        self.writeBoolean(False)
        self.writeBoolean(False)
        self.writeDataReference(0)
        self.writeVInt(1)
        self.writeVInt(1)

        self.writeVInt(1)

        self.writeVInt(1)
        self.writeVInt(1)

        self.writeVLong(0,0)
        LogicServerCommand.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 203