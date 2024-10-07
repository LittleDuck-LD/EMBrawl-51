
import time

from Classes.Notification.NotificationBase import NotificationBase

class JoinClubTips():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)
        ByteStream.writeVLong(81,14353999)#idk
        ByteStream.writeDataReference(8,1)#badge

    def getNotificationType(self):
        return 58