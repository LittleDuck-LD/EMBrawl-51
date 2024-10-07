


from Classes.Notification.Notifications.ClubMail import ClubMail
from Classes.Notification.Notifications.CustomCosmetics import CustomCosmetics
from Classes.Notification.Notifications.DonateGems import DonateGems
from Classes.Notification.Notifications.DonateStarPoints import DonateStarPoints
from Classes.Notification.Notifications.FloaterText import FloaterText
from Classes.Notification.Notifications.JoinClubTips import JoinClubTips
from Classes.Notification.Notifications.SupportMail import SupportMail


class NotificationFactory:
    NotificationsList = {
        58: JoinClubTips,
        66: FloaterText,
        72: CustomCosmetics,
        80: DonateStarPoints,
        81: SupportMail,
        82: ClubMail,
        89: DonateGems,
        10000: SupportMail,
    }

    def getNotificationsName(NotificationType):
        try:
            Notification = NotificationFactory.NotificationsList[NotificationType]
        except KeyError:
            Notification = str(NotificationType)
        if type(Notification) == str:
            return Notification
        else:
            return Notification.__name__

    def NotificationExist(NotificationType):
        return (NotificationType in NotificationFactory.NotificationsList.keys())

    def createNotification(NotificationType):
        NotificationList = NotificationFactory.NotificationsList
        if NotificationFactory.NotificationExist(NotificationType):
            if type(NotificationList[NotificationType]) == str:
                print(NotificationType, ":", NotificationFactory.getNotificationsName(NotificationType), "skipped")
            else:
                print(NotificationType, ":", NotificationFactory.getNotificationsName(NotificationType), "created")
                return NotificationList[NotificationType]()
        else:
            print(NotificationType, "skipped")
            #return NotificationList[81]()
            return None
