class LogicLongTag:
    @staticmethod
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

    @staticmethod
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
    