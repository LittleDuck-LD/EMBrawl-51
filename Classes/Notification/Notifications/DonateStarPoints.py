
import time
from Classes.Notification.NotificationBase import NotificationBase

class DonateStarPoints():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)
        ByteStream.writeVInt(fields["NotificationData"]["Count"])#0=Support;1=System

    def getNotificationType(self):
        return 81