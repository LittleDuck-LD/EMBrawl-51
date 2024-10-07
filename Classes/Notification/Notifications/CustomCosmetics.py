
import time

from Classes.Notification.NotificationBase import NotificationBase

class CustomCosmetics():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)
        ByteStream.writeVInt(fields["NotificationData"]["CosmeticsType"])#28,52,68

    def getNotificationType(self):
        return 72