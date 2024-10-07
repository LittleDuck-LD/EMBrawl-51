
import time

from Classes.Notification.NotificationBase import NotificationBase

class DonateGems():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)
        ByteStream.writeVInt(2)
        ByteStream.writeVInt(fields["NotificationData"]["GemsCount"])

    def getNotificationType(self):
        return 89