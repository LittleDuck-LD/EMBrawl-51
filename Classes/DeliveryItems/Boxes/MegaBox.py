
import time
import random


from Classes.DeliveryItems.Boxes.BoxRandomBase import BoxRandomBase
from Classes.DeliveryItems.DeliveryItemsID import DeliveryItemsID
from Classes.Files.Classes.Random_Chest import Random_Chest
from Classes.Files.Classes.Random_Chest_Rewards import Random_Chest_Rewards
from Classes.Files.Classes.Characters import Characters
from Classes.Files.Classes.Cards import Cards

class MegaBox:
    def getDropTime(self):
        return 10
    
    def getDeliveryItemType(self):
        return 11
    
    def getBoxData(self):
        return BoxRandomBase.getBoxData("OldHeroBoxLarge",self.getDropTime(),self.getDeliveryItemType())


    