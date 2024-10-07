import string
import random

class Helpers:
    game1 = [{"LogicGameObjects": 2},{"id": 1, "hp": 3000,"immun": True,"UltiPress": False,"UltiCharge": 0,"battleX": 3150,"battleY": 6725,"angle": 270},{"id": 228, "hp": 3000, "immun": True, "UltiPress": False, "UltiCharge": 0,"battleX": 3150,"battleY": 3725,"angle": 180}]
    rooms = []
    MatchMakingCount = 0
    online = 0
    freepass = 0
    buyepass = 0
    udp_port = 0

    def convert_long_to_player_tag(high_id, low_id):
        conversion_chars = "0289PYLQGRJCUV"
        full_id = (int(low_id) << 8) | int(high_id)
        tag = ""
        while full_id > 0:
            conversion_char_index = full_id % len(conversion_chars)
            tag += conversion_chars[conversion_char_index]
            full_id -= conversion_char_index
            full_id //= len(conversion_chars)
        return "#" + tag[::-1]

    def convert_player_tag_to_long(tag):
        conversion_chars = "0289PYLQGRJCUV"
        tag_array = list(tag.upper())
        id_value = 0
        if tag_array[0] == "#":
            tag_array.pop(0)
        for character in tag_array:
            char_index = conversion_chars.index(character)
            id_value *= len(conversion_chars)
            id_value += char_index
        return [id_value % 256, ((id_value - 256) >> 8) + 1]
    def randomStringDigits(self):
        """Generate a random string of letters and digits """
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))
    def randomID(self):
        length = 9
        return int(''.join([str(random.randint(0, 10)) for _ in range(length)]))
    def randomClubID(self):
        length = 9
        return int(''.join([str(random.randint(0, 9)) for _ in range(length)]))
    
    def getDefaultMegaBoxData(self):
        return {
            "Boxes":[
                {
                    "Type":11,
                    "Rewards":[
                        {
                            "Count":0,
                            "HeroID":[16,0],
                            "RewardType":0,
                            "SkinID":[29,0],
                            "EmoteID":[52,0]
                        }
                    ]
                }
            ],
            "Season": 35,
            "GiveType": 0
        }