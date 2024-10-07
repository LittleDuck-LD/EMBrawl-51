from Classes.Commands.LogicServerCommand import LogicServerCommand
from Classes.Notification.NotificationFactory import NotificationFactory


class LogicAddNotificationCommand(LogicServerCommand):
    def __init__(self, commandData):
        super().__init__(commandData)

    def encode(self, fields):
        self.writeVInt(1) # Notification factory
        Notification = NotificationFactory.createNotification(fields["NotificationData"]["ID"])
        Notification.encode(self, fields)
        return self.messagePayload

    def decode(self, calling_instance):
        fields = {}
        return LogicServerCommand.decode(calling_instance, fields)

    def getCommandType(self):
        return 206