
import time

from Classes.Notification.NotificationBase import NotificationBase


class ClubMail():
    def encode(self, ByteStream, fields):
        #ByteStream.writeVInt(self.getNotificationType())
        NotificationBase.encode(ByteStream, fields)
        ByteStream.writeString("Test1")
        ByteStream.writeVInt(1)
        ByteStream.writeVInt(1)
        ByteStream.writeVInt(1)
        ByteStream.writeVInt(1)

    def getNotificationType(self):
        return 82