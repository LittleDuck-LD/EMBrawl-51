from Classes.Commands.Client.LogicBuyFameCommand import LogicBuyFameCommand
from Classes.Commands.Client.LogicEditBattleCardCommand import LogicEditBattleCardCommand
from Classes.Commands.Client.LogicSelecGearCommand import LogicSelectGearCommand
from Classes.Commands.Client.LogicSelectFavouriteBrawlerCommand import LogicSelectFavouriteBrawlerCommand
from Classes.Commands.Client.LogicSelectStarPowerCommand import LogicSelectStarPowerCommand
from Classes.Commands.Client.LogicViewInboxNotificationCommand import LogicViewInboxNotificationCommand
from Classes.Commands.Client.LogicPurchaseOfferCommand import LogicPurchaseOfferCommand
from Classes.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Classes.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Classes.Commands.Client.LogicGatchaCommand import LogicGatchaCommand
from Classes.Commands.Server.LogicDiamondsAddedCommand import LogicDiamondsAddedCommand
from Classes.Commands.Server.LogicSetSupportedCreatorCommand import LogicSetSupportedCreatorCommand
from Classes.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Classes.Commands.Server.LogicGiveDeliveryItemsCommand import LogicGiveDeliveryItemsCommand
from Classes.Commands.Server.LogicAddNotificationCommand import LogicAddNotificationCommand


class LogicCommandManager:
    commandsList = {
        201: LogicChangeAvatarNameCommand,
        202: LogicDiamondsAddedCommand,
        203: LogicGiveDeliveryItemsCommand,
        204: 'LogicDayChangedCommand',
        205: 'LogicDecreaseHeroScoreCommand',
        206: LogicAddNotificationCommand,
        207: 'LogicChangeResourcesCommand',
        208: 'LogicTransactionsRevokedCommand',
        209: 'LogicKeyPoolChangedCommand',
        210: 'LogicIAPChangedCommand',
        211: 'LogicOffersChangedCommand',
        212: 'LogicPlayerDataChangedCommand',
        213: 'LogicInviteBlockingChangedCommand',
        214: 'LogicGemNameChangeStateChangedCommand',
        215: LogicSetSupportedCreatorCommand,
        216: 'LogicCooldownExpiredCommand',
        217: 'LogicProLeagueSeasonChangedCommand',
        218: 'LogicBrawlPassSeasonChangedCommand',
        219: 'LogicBrawlPassUnlockedCommand',
        220: 'LogicHerowinQuestsChangedCommand',
        221: 'LogicTeamChatMuteStateChangedCommand',
        222: 'LogicRankedSeasonChangedCommand',
        223: 'LogicCooldownAddedCommand',
        224: 'LogicSetESportsHubNotificationCommand',
        500: LogicGatchaCommand,
        503: 'LogicClaimDailyRewardCommand',
        504: 'LogicSendAllianceMailCommand',
        505: LogicSetPlayerThumbnailCommand,
        506: 'LogicSelectSkinCommand',
        507: 'LogicUnlockSkinCommand',
        508: 'LogicChangeControlModeCommand',
        509: 'LogicPurchaseDoubleCoinsCommand',
        511: 'LogicHelpOpenedCommand',
        512: 'LogicToggleInGameHintsCommand',
        514: 'LogicDeleteNotificationCommand',
        515: 'LogicClearShopTickersCommand',
        517: 'LogicClaimRankUpRewardCommand',
        518: 'LogicPurchaseTicketsCommand',
        519: LogicPurchaseOfferCommand,
        520: 'LogicLevelUpCommand',
        521: 'LogicPurchaseHeroLvlUpMaterialCommand',
        522: 'LogicHeroSeenCommand',
        523: 'LogicClaimAdRewardCommand',
        524: 'LogicVideoStartedCommand',
        525: 'LogicSelectCharacterCommand',
        526: 'LogicUnlockFreeSkinsCommand',
        527: LogicSetPlayerNameColorCommand,
        528: LogicViewInboxNotificationCommand,
        529: LogicSelectStarPowerCommand,
        530: 'LogicSetPlayerAgeCommand',
        531: 'LogicCancelPurchaseOfferCommand',
        532: 'LogicItemSeenCommand',
        533: 'LogicQuestSeenCommand',
        534: 'LogicPurchaseBrawlPassCommand',
        535: 'LogicClaimTailRewardCommand',
        536: 'LogicPurchaseBrawlpassProgressCommand',
        537: 'LogicVanityItemSeenCommand',
        538: 'LogicSelectEmoteCommand',
        539: 'LogicBrawlPassAutoCollectWarningSeenCommand',
        540: 'LogicPurchaseChallengeLivesCommand',
        541: 'LogicClearESportsHubNotificationCommand',
        542: 'LogicSelectGroupSkinCommand',
        543: LogicSelectGearCommand,
        566: LogicBuyFameCommand,
        568: LogicEditBattleCardCommand,
        570: LogicSelectFavouriteBrawlerCommand
    }

    def getCommandsName(commandType):
        try:
            command = LogicCommandManager.commandsList[commandType]
        except KeyError:
            command = str(commandType)
        if type(command) == str:
            return command
        else:
            return command.__name__

    def commandExist(commandType):
        return (commandType in LogicCommandManager.commandsList.keys())

    def createCommand(commandType, commandPayload=b''):
        commandList = LogicCommandManager.commandsList
        if LogicCommandManager.commandExist(commandType):
            if type(commandList[commandType]) == str:
                print(commandType, ":", LogicCommandManager.getCommandsName(commandType), "skipped")
            else:
                print(commandType, ":", LogicCommandManager.getCommandsName(commandType), "created")
                return commandList[commandType](commandPayload)
        else:
            print(commandType, "skipped")
            return None

    def isServerToClient(commandType):
        if 200 <= commandType < 500:
            return True
        elif 500 <= commandType:
            return False