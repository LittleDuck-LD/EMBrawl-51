import random

from Classes.Utils.Helpers import Helpers
class Gameroom:
    def create(self, fields, roomType=1, map_id=14):
        count = len(Helpers.rooms)
        new_room = {'index': count, 'roomID': fields["room_id"], 'roomType': fields["room_type"], 'map_id': fields["map_id"],'Tick': 0,'plrs': [{'id': fields["player"]["low_id"], 'isOwner': 1, 'state': 2}],'invites':[],'Premade':[], 'msg': []}
        Helpers.rooms.append(new_room)