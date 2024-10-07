
import time

from Classes.Notification.NotificationBase import NotificationBase

class FloaterText():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)

    def getNotificationType(self):
        return 66