import json
import random
import string

from Database.DatabaseHandler import DatabaseHandler
Thumbnails=[]
for i in range(322):
    Thumbnails.append(i)
Emotes = []
for i in range(1308):
    Emotes.append(i)

class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    Token = ""
    Name = "爱萝莉"
    Registered = False
    Thumbnail = 0
    Namecolor = 0
    Region = "CN"
    ContentCreator = "EmberHeart"
    Theme = 41000075

    Coins = 999999
    Gems = 999999
    StarPoints = 999999
    Trophies = 999999
    Blings = 0

    stats_3v3 = 0
    stats_showdown = 0
    stats_duoshowdown = 0
    stats_solorank = 0
    stats_3v3rank = 0
    stats_city_rampage = 0
    stats_robo = 0
    stats_robo_rumble = 0
    stats_challenge = 0
    stats_clubwars = 0
    

    HighestTrophies = 999999
    TrophyRoadTier = 135
    Experience = 999999
    Level = 500
    Tokens = 200
    TokensDoubler = 1000

    Notification = []
    Banned = False
    IsOperator = False
    BattleCardThumb1 = 0
    BattleCardThumb2 = 0
    BattleCardEmote = 0
    BattleCardTitle = 0
    FavouriteBrawler = 0
    IP = ""
    Maps = []
    Friends = []
    CurrentTeamID = 0
    LastOnlineTime = 0
    IMEI = ""
    AppleIFV = ""
    AndroidID = ""
    isAndroid = False
    Device = ""

    SelectedSkins = {}
    SelectedBrawlers = [73, 72, 71]
    RandomizerSelectedSkins = []
    OwnedPins = Emotes
    OwnedThumbnails = Thumbnails
    OwnedBrawlers = {
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
        18: {'CardID': 72, 'Skins': [70, 158, 250, 251, 264, 351, 511], 'Trophies': 1250, 'HighestTrophies': 1250, 'PowerLevel': 11, 'PowerPoints': 0, 'State': 2},
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

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            #self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            #self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.ID[0] = 100
            self.ID[1] = DatabaseHandler().getLastPlayer()["ID"][1]+1
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'Registered': self.Registered,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,

            'Theme': self.Theme,
            'Notification' : self.Notification,
            'Banned' : self.Banned,
            'IsOperator' : self.IsOperator,
            'BattleCardThumb1' : self.BattleCardThumb1,
            'BattleCardThumb2' : self.BattleCardThumb2,
            'BattleCardEmote' : self.BattleCardEmote,
            'BattleCardTitle' : self.BattleCardTitle,
            'FavouriteBrawler' : self.FavouriteBrawler,
            'IP' : self.IP,
            'Maps' : self.Maps,
            'LastOnlineTime' : self.LastOnlineTime,
            'IMEI' : self.IMEI,
            'AppleIFV' : self.AppleIFV,
            'AndroidID' : self.AndroidID,
            'isAndroid' : self.isAndroid,
            'Device' : self.Device,
            'Friends' : self.Friends,
            'CurrentTeamID' : self.CurrentTeamID,

            'stats_3v3' : self.stats_3v3,
            'stats_showdown' : self.stats_showdown,
            'stats_duoshowdown' : self.stats_duoshowdown,
            'stats_solorank' : self.stats_solorank,
            'stats_3v3rank' : self.stats_3v3rank,
            'stats_city_rampage' : self.stats_city_rampage,
            'stats_robo' : self.stats_robo,
            'stats_robo_rumble' : self.stats_robo_rumble,
            'stats_challenge' : self.stats_challenge,
            'stats_clubwars' : self.stats_clubwars,

            'Coins': self.Coins,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensDoubler': self.TokensDoubler,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
