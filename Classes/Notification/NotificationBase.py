
import time

class NotificationBase():
    def encode(ByteStream, fields):
        ByteStream.writeVInt(fields["NotificationData"]["ID"])
        ByteStream.writeInt(0)
        ByteStream.writeBoolean(fields["NotificationData"]["Reviewed"])
        ByteStream.writeInt(int(time.time()) - fields["NotificationData"]["Time"])
        ByteStream.writeString(fields["NotificationData"]["Message"])
        ByteStream.writeVInt(0)