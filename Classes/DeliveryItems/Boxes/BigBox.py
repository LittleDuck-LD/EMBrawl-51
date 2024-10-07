
import time
import random


from Classes.DeliveryItems.Boxes.BoxRandomBase import BoxRandomBase
from Classes.DeliveryItems.DeliveryItemsID import DeliveryItemsID
from Classes.Files.Classes.Random_Chest import Random_Chest
from Classes.Files.Classes.Random_Chest_Rewards import Random_Chest_Rewards
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Cards import Cards

class BigBox:
    def getDeliveryItemType(self):
        return 12
    
    def getDropTime(self):
        return 3
    
    def getBoxData(self):
        return BoxRandomBase.getBoxData("OldHeroBoxMid",self.getDropTime(),self.getDeliveryItemType())

