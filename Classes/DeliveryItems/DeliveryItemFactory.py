


from Classes.DeliveryItems.Boxes.BigBox import BigBox
from Classes.DeliveryItems.Boxes.BrawlBox import BrawlBox
from Classes.DeliveryItems.Boxes.MegaBox import MegaBox
from Classes.DeliveryItems.Boxes.OmegaBox import OmegaBox


class DeliveryItemFactory:
    DeliveryItemsList = {
        10 : BrawlBox,
        11 : MegaBox,
        12 : BigBox,
        13 : OmegaBox
    }

    def getDeliveryItemsName(DeliveryItemType):
        try:
            DeliveryItem = DeliveryItemFactory.DeliveryItemsList[DeliveryItemType]
        except KeyError:
            DeliveryItem = str(DeliveryItemType)
        if type(DeliveryItem) == str:
            return DeliveryItem
        else:
            return DeliveryItem.__name__

    def DeliveryItemExist(DeliveryItemType):
        return (DeliveryItemType in DeliveryItemFactory.DeliveryItemsList.keys())

    def createDeliveryItem(DeliveryItemType):
        DeliveryItemList = DeliveryItemFactory.DeliveryItemsList
        if DeliveryItemFactory.DeliveryItemExist(DeliveryItemType):
            if type(DeliveryItemList[DeliveryItemType]) == str:
                print(DeliveryItemType, ":", DeliveryItemFactory.getDeliveryItemsName(DeliveryItemType), "skipped")
            else:
                print(DeliveryItemType, ":", DeliveryItemFactory.getDeliveryItemsName(DeliveryItemType), "created")
                return DeliveryItemList[DeliveryItemType]
        else:
            print(DeliveryItemType, "skipped")
            return None
