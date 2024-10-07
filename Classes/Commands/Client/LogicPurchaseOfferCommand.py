import json

from Classes.Commands.LogicCommand import LogicCommand
from Classes.Messaging import Messaging
from Database.DatabaseHandler import DatabaseHandler
Thumbnails=[]
for i in range(322):
    Thumbnails.append(i)
Emotes = []
for i in range(1308):
    Emotes.append(i)

OwnedPinsLatest = Emotes
OwnedThumbnailsLatest = Thumbnails

OwnedBrawlersLatest = {
        0: {'CardID': 0, 'Skins': [29, 52, 122, 159, 195, 196, 320, 321, 322, 359], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        1: {'CardID': 4, 'Skins': [2, 103, 69, 135, 217, 303, 323, 324, 325, 326, 330, 331, 377, 544], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        2: {'CardID': 8, 'Skins': [25, 64, 102, 178, 218, 219, 262, 393, 477, 501], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        3: {'CardID': 12, 'Skins': [5, 58, 72, 91, 201, 242, 400, 401, 541], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        4: {'CardID': 16, 'Skins': [26, 68, 130, 171, 223, 224, 397, 473], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        5: {'CardID': 20, 'Skins': [11, 96, 208, 263, 301, 302, 448, 509], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        6: {'CardID': 24, 'Skins': [27, 59, 90, 92, 116, 220, 221, 357, 436], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        7: {'CardID': 28, 'Skins': [44, 47, 123, 162, 174, 253, 254, 395], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        8: {'CardID': 32, 'Skins': [15, 439, 60, 79, 148, 297, 298, 347], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        9: {'CardID': 36, 'Skins': [56, 57, 97, 160, 236, 276, 314, 315, 316, 398, 430, 431, 462], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        10: {'CardID': 40, 'Skins': [28, 30, 128, 183, 187, 213, 317, 318, 319, 354, 360, 438, 441], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        11: {'CardID': 44, 'Skins': [50, 63, 75, 173, 228, 230, 227, 229, 311], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        12: {'CardID': 48, 'Skins': [20, 49, 95, 100, 101, 248, 249, 390], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        13: {'CardID': 52, 'Skins': [71, 140, 214, 342, 406, 407], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        14: {'CardID': 56, 'Skins': [94, 98, 99, 163, 216, 245, 363, 364, 445, 478], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        15: {'CardID': 60, 'Skins': [108, 120, 147, 197, 198, 234, 382], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        16: {'CardID': 64, 'Skins': [179, 355, 411, 412], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        17: {'CardID': 68, 'Skins': [111, 145, 259, 260, 282, 516], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        #18: {'CardID': 72, 'Skins': [70, 158, 250, 251, 264, 351, 511], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        18: {'CardID': 72, 'Skins': [70, 158, 250, 251, 264,  511], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        19: {'CardID': 95, 'Skins': [61, 88, 165, 274, 453, 454], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        20: {'CardID': 100, 'Skins': [45, 125, 225, 226, 244], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        21: {'CardID': 105, 'Skins': [117, 172, 304, 305, 389], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        22: {'CardID': 110, 'Skins': [190, 243, 246, 247, 468], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        23: {'CardID': 115, 'Skins': [110, 126, 131, 199, 200, 312], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        24: {'CardID': 120, 'Skins': [215, 309, 446, 455, 456, 483], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        25: {'CardID': 125, 'Skins': [93, 104, 132, 134, 267, 308, 424, 425, 507], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        26: {'CardID': 130, 'Skins': [146, 222, 273, 345, 422, 423, 470], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        27: {'CardID': 177, 'Skins': [109, 143, 283, 402, 403, 409], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        28: {'CardID': 182, 'Skins': [471, 118, 210, 287, 371, 372], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        29: {'CardID': 188, 'Skins': [139, 188, 284, 285, 290, 365, 366], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        30: {'CardID': 194, 'Skins': [167, 185, 186, 209, 542], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        31: {'CardID': 200, 'Skins': [152, 332, 333, 415, 479, 513], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        32: {'CardID': 206, 'Skins': [137, 202, 232, 310, 404, 405], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        34: {'CardID': 218, 'Skins': [176, 189, 307, 444, 449, 450, 505], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        35: {'CardID': 224, 'Skins': [180, 241, 367, 368, 388], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        36: {'CardID': 230, 'Skins': [194, 233, 369, 370], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        37: {'CardID': 236, 'Skins': [177, 211, 379, 383, 488, 492, 493], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        38: {'CardID': 279, 'Skins': [203, 292, 419, 496, 497], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        39: {'CardID': 296, 'Skins': [212, 270, 391, 428, 429], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        40: {'CardID': 303, 'Skins': [280, 426, 427], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        41: {'CardID': 320, 'Skins': [237, 266, 306, 451, 452], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        42: {'CardID': 327, 'Skins': [358, 512], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        43: {'CardID': 334, 'Skins': [472, 281, 437, 506], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        44: {'CardID': 341, 'Skins': [268, 286, 490, 491, 539], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        45: {'CardID': 358, 'Skins': [277, 346, 420, 526, 527], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        46: {'CardID': 365, 'Skins': [294, 489, 524, 525, 547], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        47: {'CardID': 372, 'Skins': [392, 418], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        48: {'CardID': 379, 'Skins': [482, 550, 551], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        49: {'CardID': 386, 'Skins': [343, 386, 494, 495], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        50: {'CardID': 393, 'Skins': [458], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        51: {'CardID': 410, 'Skins': [381, 528, 529], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        52: {'CardID': 417, 'Skins': [475, 517, 532, 533], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        53: {'CardID': 427, 'Skins': [433, 510, 530, 531], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        54: {'CardID': 434, 'Skins': [460, 548, 558, 559], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        56: {'CardID': 448, 'Skins': [484, 552, 553], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        57: {'CardID': 466, 'Skins': [536, 554, 555], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        58: {'CardID': 474, 'Skins': [521, 556, 557], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        59: {'CardID': 491, 'Skins': [546], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        60: {'CardID': 499, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        61: {'CardID': 507, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        62: {'CardID': 515, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        63: {'CardID': 523, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        64: {'CardID': 531, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        65: {'CardID': 539, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        66: {'CardID': 547, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        67: {'CardID': 557, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        68: {'CardID': 565, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        69: {'CardID': 573, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        70: {'CardID': 581, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        71: {'CardID': 589, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
        72: {'CardID': 597, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},        
        73: {'CardID': 605, 'Skins': [], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},

    }

EmptyList = []

EmptyJson = {0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2}}


class LogicPurchaseOfferCommand(LogicCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        LogicCommand.encode(self, fields)
        self.writeVInt(0)
        self.writeDataReference(0)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        LogicCommand.decode(calling_instance, fields, False)
        fields["Unk1"] = calling_instance.readVInt()
        fields["Unk2"] = calling_instance.readDataReference()
        LogicCommand.parseFields(fields)
        return fields

    def execute(self, calling_instance, fields, cryptoInit):
        if fields["Unk1"] == 0:
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            player_data["OwnedBrawlers"] = OwnedBrawlersLatest
            #for i,v in player_data["OwnedBrawlers"].items():
            #    v["Skins"] = OwnedBrawlersLatest[int(i)]["Skins"]
            player_data["OwnedPins"] = OwnedPinsLatest
            player_data["OwnedThumbnails"] = OwnedThumbnailsLatest
            db_instance.updatePlayerData(player_data, calling_instance)
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0}, cryptoInit)
        if fields["Unk1"] == 1:
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
            player_data["OwnedBrawlers"] = EmptyJson
            player_data["OwnedPins"] = EmptyList
            player_data["OwnedThumbnails"] = EmptyList
            db_instance.updatePlayerData(player_data, calling_instance)
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0}, cryptoInit)
        elif fields["Unk1"] == 2:
            fields["Socket"] = calling_instance.client
            fields["Command"] = {}
            fields["Command"]["ID"] = 203
            fields["BoxType"] = 13
            Messaging.sendMessage(24111, fields, cryptoInit)
        elif fields["Unk1"] == 3:
            fields["Socket"] = calling_instance.client
            fields["Command"] = {}
            fields["Command"]["ID"] = 203
            fields["BoxType"] = 11
            Messaging.sendMessage(24111, fields, cryptoInit)
        elif fields["Unk1"] == 4:
            fields["Socket"] = calling_instance.client
            fields["Command"] = {}
            fields["Command"]["ID"] = 203
            fields["BoxType"] = 12
            Messaging.sendMessage(24111, fields, cryptoInit)
        else:
            Messaging.sendMessage(24104, {"Socket": calling_instance.client, "ServerChecksum": 0, "ClientChecksum": 0, "Tick": 0}, cryptoInit)

    def getCommandType(self):
        return 519