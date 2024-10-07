

class DeliveryItemsID:
    IDList = {
        1:"Brawler",
        2:"TokenDoubler",
        6:"PowerPointsForSingleBrawler",
        7:"Coins",
        8:"Gems",
        9:"Skin",
        11:"Emote",
        12:"StarPoints",
        19:"PowerPointsChoiceBrawler",
        22:"Credits",
        23:"ChromaticToken",
        24:"PowerPoints",
        25:"Bling",
        26:"BrawlPass",
        27:"HyperCharge",
    }
    def getIDByName(self,Name="Coins"):
        for ID in self.IDList:
            if self.IDList[ID] == Name:
                return ID