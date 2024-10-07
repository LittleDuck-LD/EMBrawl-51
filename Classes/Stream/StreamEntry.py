from Classes.ByteStream import ByteStream

import time

class StreamEntry:
    def encode(self: ByteStream, info): 
        self.writeVLong(info['StreamID'][0],info['StreamID'][1]) # StreamEntryID
        self.writeVLong(info['PlayerID'][0],info['PlayerID'][1]) # TargetID
        self.writeString(info['PlayerName'])
        self.writeVInt(info['PlayerRole'])
        self.writeVInt(int(time.time())-info['Time'])
        self.writeVInt(0)

