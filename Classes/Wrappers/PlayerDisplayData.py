class PlayerDisplayData:
    def encode(calling_instance, playerData):
        calling_instance.writeString(playerData["Name"])
        calling_instance.writeVInt(100)
        calling_instance.writeVInt(28000000 + playerData["Thumbnail"])
        calling_instance.writeVInt(43000000 + playerData["Namecolor"])

        calling_instance.writeVInt(14)

        calling_instance.writeBoolean(True)
        calling_instance.writeVInt(300)

        calling_instance.writeString("hello world")
        calling_instance.writeVInt(100)
        calling_instance.writeVInt(200)
        calling_instance.writeDataReference(29, 558)
        if playerData["BattleCardThumb1"] != 0:
            calling_instance.writeDataReference(28, playerData["BattleCardThumb1"])
        else:
            calling_instance.writeDataReference(0)
        if playerData["BattleCardThumb2"] != 0:
            calling_instance.writeDataReference(28, playerData["BattleCardThumb2"])
        else:
            calling_instance.writeDataReference(0)
        if playerData["BattleCardEmote"] != 0:
            calling_instance.writeDataReference(52, playerData["BattleCardEmote"])
        else:
            calling_instance.writeDataReference(0)
        if playerData["BattleCardTitle"] != 0:
            calling_instance.writeDataReference(76, playerData["BattleCardTitle"])
        else:
            calling_instance.writeDataReference(0)

        

    def decode(calling_instance, fields):
        fields["PlayerDisplayData"] = {}
        fields["PlayerDisplayData"]["Name"] = calling_instance.readString()
        fields["PlayerDisplayData"]["Unknown"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Thumbnail"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Namecolor"] = calling_instance.readVInt()
        fields["PlayerDisplayData"]["Unknown"] = calling_instance.readVInt()