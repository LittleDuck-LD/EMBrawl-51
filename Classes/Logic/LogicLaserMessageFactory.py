from Classes.Packets.Client.Alliance.AlliancePremadeChatMessage import AlliancePremadeChatMessage
from Classes.Packets.Client.Alliance.KickAllianceMemberMessage import KickAllianceMemberMessage
from Classes.Packets.Client.Alliance.ReportAllianceStreamMessage import ReportAllianceStreamMessage
from Classes.Packets.Client.Alliance.SendAllianceMailMessage import SendAllianceMailMessage
from Classes.Packets.Client.Authentification.ClientHelloMessage import ClientHelloMessage
from Classes.Packets.Client.Authentification.LoginMessage import LoginMessage
from Classes.Packets.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage
from Classes.Packets.Client.Battle.CancelMatchmakingMessage import CancelMatchmakingMessage
from Classes.Packets.Client.Battle.StartSpectateMessage import StartSpectateMessage
from Classes.Packets.Client.Billing.AppleBillingRequestMessage import AppleBillingRequestMessage
from Classes.Packets.Client.Friend.AcceptFriendMessage import AcceptFriendMessage
from Classes.Packets.Client.Friend.AddFriendMessage import AddFriendMessage
from Classes.Packets.Client.Friend.AskForFriendListMessage import AskForFriendListMessage
from Classes.Packets.Client.Friend.RemoveFriendMessage import RemoveFriendMessage
from Classes.Packets.Client.Home.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Classes.Packets.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage
from Classes.Packets.Client.Home.ClientCapabilitiesMessage import ClientCapabilitiesMessage
from Classes.Packets.Client.Home.ClientCryptoErrorMessage import ClientCryptoErrorMessage
from Classes.Packets.Client.Home.EndClientTurnMessage import EndClientTurnMessage
from Classes.Packets.Client.Home.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Classes.Packets.Client.Home.GoHomeMessage import GoHomeMessage
from Classes.Packets.Client.MapEditor.CreatePlayerMapMessage import CreatePlayerMapMessage
from Classes.Packets.Client.Socket.KeepAliveMessage import KeepAliveMessage
from Classes.Packets.Client.Home.GetPlayerProfileMessage import GetPlayerProfileMessage
from Classes.Packets.Client.Alliance.CreateAllianceMessage import CreateAllianceMessage
from Classes.Packets.Client.Alliance.AskForAllianceDataMessage import AskForAllianceDataMessage
from Classes.Packets.Client.Alliance.AskForJoinableAlliancesListMessage import AskForJoinableAlliancesListMessage
from Classes.Packets.Client.Alliance.ChangeAllianceSettingsMessage import ChangeAllianceSettingsMessage
from Classes.Packets.Client.Home.AskForFriendSuggestionsMessage import AskForFriendSuggestionsMessage
from Classes.Packets.Client.Home.SetSupportedCreatorMessage import SetSupportedCreatorMessage
from Classes.Packets.Client.Home.SetCountryMessage import SetCountryMessage
from Classes.Packets.Client.Alliance.LeaveAllianceMessage import LeaveAllianceMessage
from Classes.Packets.Client.Alliance.ChatToAllianceStreamMessage import ChatToAllianceStreamMessage
from Classes.Packets.Client.Alliance.JoinAllianceMessage import JoinAllianceMessage
from Classes.Packets.Client.Alliance.ChangeAllianceMemberRoleMessage import ChangeAllianceMemberRoleMessage


from Classes.Packets.Client.Team.TeamCreateMessage import TeamCreateMessage
from Classes.Packets.Client.Team.TeamLeaveMessage import TeamLeaveMessage
from Classes.Packets.Client.Team.TeamSetMemberReadyMessage import TeamSetMemberReadyMessage
from Classes.Packets.Server.Alliance.AllianceOnlineStatusUpdatedMessage import AllianceOnlineStatusUpdatedMessage
from Classes.Packets.Server.Authentification.LoginFailedMessage import LoginFailedMessage
from Classes.Packets.Server.Authentification.LoginOkMessage import LoginOkMessage
from Classes.Packets.Server.Authentification.OutOfSyncMessage import OutOfSyncMessage
from Classes.Packets.Server.Authentification.ServerHelloMessage import ServerHelloMessage
from Classes.Packets.Server.Battle.BattleEndMessage import BattleEndMessage
from Classes.Packets.Server.Battle.MatchMakingCancelledMessage import MatchMakingCancelledMessage
from Classes.Packets.Server.Battle.MatchMakingStatusMessage import MatchMakingStatusMessage
from Classes.Packets.Server.Battle.SpectacleFailedMessage import SpectacleFailedMessage
from Classes.Packets.Server.Battle.StartLoadingMessage import StartLoadingMessage
from Classes.Packets.Server.Battle.UdpConnectionInfoMessage import UdpConnectionInfoMessage
from Classes.Packets.Server.Billing.BillingRequestFailedMessage import BillingRequestFailedMessage
from Classes.Packets.Server.Friend.AddFriendFailedMessage import AddFriendFailedMessage
from Classes.Packets.Server.Friend.FriendListMessage import FriendListMessage
from Classes.Packets.Server.Friend.FriendListUpdateMessage import FriendListUpdateMessage
from Classes.Packets.Server.Home.AvailableServerCommandMessage import AvailableServerCommandMessage
from Classes.Packets.Server.Home.ChatAccountBanStatusMessage import ChatAccountBanStatusMessage
from Classes.Packets.Server.Home.DisconnectedMessage import DisconnectedMessage
from Classes.Packets.Server.Home.LobbyInfoMessage import LobbyInfoMessage
from Classes.Packets.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage
from Classes.Packets.Server.Home.ReportUserStatusMessage import ReportUserStatusMessage
from Classes.Packets.Server.Home.ServerErrorMessage import ServerErrorMessage
from Classes.Packets.Server.Home.SpellFactoryClaimFailedMessage import SpellFactoryClaimFailedMessage
from Classes.Packets.Server.MapEditor.CreatePlayerMapResponseMessage import CreatePlayerMapResponseMessage
from Classes.Packets.Server.Socket.KeepAliveServerMessage import KeepAliveServerMessage
from Classes.Packets.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Classes.Packets.Server.Home.AvatarNameCheckResponseMessage import AvatarNameCheckResponseMessage
from Classes.Packets.Server.Home.SetSupportedCreatorResponseMessage import SetSupportedCreatorResponseMessage
from Classes.Packets.Server.Alliance.AllianceResponseMessage import AllianceResponseMessage
from Classes.Packets.Server.Alliance.AllianceStreamMessage import AllianceStreamMessage
from Classes.Packets.Server.Alliance.AllianceDataMessage import AllianceDataMessage
from Classes.Packets.Server.Alliance.MyAllianceMessage import MyAllianceMessage
from Classes.Packets.Server.Alliance.JoinableAllianceListMessage import JoinableAllianceListMessage
from Classes.Packets.Server.Alliance.ChangeAllianceSettingsOkMessage import ChangeAllianceSettingsOkMessage
from Classes.Packets.Server.Home.ShutdownStartedMessage import ShutdownStartedMessage
from Classes.Packets.Server.Team.TeamGameStartingMessage import TeamGameStartingMessage
from Classes.Packets.Server.Team.TeamLeftMessage import TeamLeftMessage
from Classes.Packets.Server.Team.TeamMessage import TeamMessage


class LogicLaserMessageFactory:
    messagesList = {
        10055: 'AskPlayerJWTokenMessage',
        10099: ClientCryptoErrorMessage,
        10100: ClientHelloMessage,
        10101: LoginMessage,
        10102: 'LoginUsingSessionMessage',
        10103: 'CreateAccountMessage',
        10107: ClientCapabilitiesMessage,
        10108: KeepAliveMessage,
        10109: 'UdpCheckConnectionMessage',
        10110: 'AnalyticEventMessage',
        10111: 'AccountIdentifiersMessage',
        10112: 'AuthenticationCheckMessage',
        10113: 'SetDeviceTokenMessage',
        10116: 'ResetAccountMessage',
        10117: 'ReportUserMessage',
        10118: 'AccountSwitchedMessage',
        10119: ReportAllianceStreamMessage,
        10121: 'UnlockAccountMessage',
        10150: AppleBillingRequestMessage,
        10151: 'GoogleBillingRequestMessage',
        10152: 'TencentBillingRequestMessage',
        10153: 'CafeBazaarBillingRequestMessage',
        10159: 'KunlunBillingRequestMessage',
        10160: 'BillingCancelledByClientMessage',
        10177: 'ClientInfoMessage',
        10212: ChangeAvatarNameMessage,
        10309: 'GetAllianceInviteTokenMessage',
        10321: 'AttributionEventMessage',
        10401: 'CreateGameMessage',
        10501: AcceptFriendMessage,
        10502: AddFriendMessage,
        10503: 'AskForAddableFriendsMessage',
        10504: AskForFriendListMessage,
        10506: RemoveFriendMessage,
        10507: 'AddFriendByEmailMessage',
        10509: 'AddFriendByAvatarNameAndCodeMessage',
        10512: 'AskForPlayingGamecenterFriendsMessage',
        10513: 'AskForPlayingFacebookFriendsMessage',
        10514: 'AskForPlayingKakaoFriendsMessage',
        10515: 'AskForPlayingTencentFriendsMessage',
        10516: 'AskForPlayingLineFriendsMessage',
        10517: 'AskForPlayingSupercellFriendsMessage',
        10523: 'YoozooBillingRequestMessage',
        10555: 'ClientInputMessage',
        10576: 'SetBlockFriendRequestsMessage',
        10599: AskForFriendSuggestionsMessage,
        10636: 'SCIDBindAccountMessage',
        11736: 'SCIDLogoutAllDevicesMessage',
        12100: CreatePlayerMapMessage,
        12101: 'DeletePlayerMapMessage',
        12102: 'GetPlayerMapsMessage',
        12103: 'UpdatePlayerMapMessage',
        12104: 'SubmitPlayerMapMessage',
        12105: 'PublishPlayerMapMessage',
        12106: 'ChangePlayerMapNameMessage',
        12107: 'EnterMapEditorMessage',
        12108: 'GoHomeFromMapEditorMessage',
        12110: 'TeamSetPlayerMapMessage',
        12111: 'SignoffPlayerMapMessage',
        12125: 'ReportPlayerMapMessage',
        12152: 'RankedMatchBanHeroMessage',
        12155: 'RankedMatchPickHeroMessage',
        12157: 'RankedMatchUpdateHeroDataMessage',
        12541: TeamCreateMessage,
        12905: 'GetCurrentBattleReplayDataMessage',
        12998: SetCountryMessage,
        13922: 'AcceptTokenFriendMessage',
        14101: GoHomeMessage,
        14102: EndClientTurnMessage,
        14103: 'StartGameMessage',
        14104: StartSpectateMessage,
        14105: 'HomeLogicStoppedMessage',
        14106: CancelMatchmakingMessage,
        14107: 'StopSpectateMessage',
        14108: 'GoHomeFromSpectateMessage',
        #14109: GoHomeFromOfflinePractiseMessage,
        14110: AskForBattleEndMessage,
        #14113: GetPlayerProfileMessage,
        14114: 'GetBattleLogMessage',
        14115: 'BattleLogViewReplayMessage',
        14116: 'ViewReplayByStringMessage',
        14117: 'RequestMatchCancelMessage',
        14118: 'SinglePlayerMatchRequestMessage',
        14166: 'ChronosEventSeenMessage',
        14167: 'ChronosEventSeenMessage',
        14177: 'PlayAgainMessage',
        14178: 'DebugCommandMessage',
        14199: 'LookForGameRoomRequestMessage',
        14211: 'UnbindFacebookAccountMessage',
        14201: 'BindFacebookAccountMessage',
        14202: 'BindKakaoAccountMessage',
        14203: 'BingLineAccountMessage',
        14212: 'BindGamecenterAccountMessage',
        14213: 'UnbindKakaoAccountMessage',
        14214: 'UnbindLineAccountMessage',
        14262: 'BindGoogleServiceAccountMessage',
        14266: 'BindTencentAccountMessage',
        14268: 'TencentCheckCanPayMessage',
        14276: 'TencentAntiAddictionInstructionExecutedMessage',
        14277: 'GetSeasonRewardsMessage',
        14299: 'SetAllianceCountryMessage',
        14301: CreateAllianceMessage,
        14302: AskForAllianceDataMessage,
        14303: AskForJoinableAlliancesListMessage,
        14304: 'AskForAllianceStreamMessage',
        14305: JoinAllianceMessage,
        14306: ChangeAllianceMemberRoleMessage,
        14307: KickAllianceMemberMessage,
        14308: LeaveAllianceMessage,
        14315: ChatToAllianceStreamMessage,
        14316: ChangeAllianceSettingsMessage,
        14317: 'RequestJoinAllianceMessage',
        14321: 'RespondToAllianceJoinRequestMessage',
        14322: 'SendAllianceInvitationMessage',
        14323: 'JoinAllianceUsingInvitationMessage',
        14324: 'SearchAlliancesMessage',
        14326: 'SendAllianceInvitationToFriendMessage',
        14330: SendAllianceMailMessage,
        14350: TeamCreateMessage,
        14351: 'TeamJoinMessage',
        14352: 'TeamKickMessage',
        14353: TeamLeaveMessage,
        14354: 'TeamChangeMemberSettingsMessage',
        14355: TeamSetMemberReadyMessage,
        14356: 'TeamTogglePractiseMessage',
        14357: 'TeamToggleMemberSideMessage',
        14358: 'TeamSpectateMessage',
        14359: 'TeamChatMessage',
        14360: 'TeamPostAdMessage',
        14361: 'TeamMemberStatusMessage',
        14362: 'TeamSetEventMessage',
        14363: 'TeamSetLocationMessage',
        14364: 'TeamReportChatMessage',
        14365: 'TeamInviteMessage',
        14366: 'PlayerStatusMessage',
        14367: 'TeamClearInviteMessage',
        14368: 'TeamInviteResponseMessage',
        14369: 'TeamPremadeChatMessage',
        14370: 'TeamAllianceMemberInviteMessage',
        14371: 'TeamJoinOrCreateGameRoomMessage',
        14372: 'TeamToggleSettingsMessage',
        14373: 'TeamBotSlotDisableMessage',
        14403: 'GetLeaderboardMessage',
        14405: 'AskForAvatarStreamMessage',
        14406: 'AskForBattleReplayStreamMessage',
        14418: 'RemoveAvatarStreamEntryMessage',
        14469: AlliancePremadeChatMessage,
        14479: 'TeamInvitationResponseMessage',
        14600: AvatarNameCheckRequestMessage,
        14700: 'ListBrawlTvChannelsMessage',
        14701: 'TuneBrawlTvChannelMessage',
        14715: 'SendGlobalChatLineMessage',
        14777: 'SetInvitesBlockedMessage',
        14778: 'SetTeamChatMutedMessage',
        14867: 'SetRegionMessage',
        14880: 'TeamRequestJoinCancelMessage',
        14881: 'TeamRequestJoinMessage',
        14882: 'TeamRequestJoinApproveMessage',
        15081: GetPlayerProfileMessage, #v50
        15793: 'GetTokenFriendMessage',
        16000: 'LogicDeviceLinkCodeRequestMessage',
        16001: 'LogicDeviceLinkMenuClosedMessage',
        16002: 'LogicDeviceLinkEnterCodeMessage',
        16003: 'LogicDeviceLinkConfirmYesMessage',
        16939: 'AskApiTokenMessage',
        17000: 'LogicAccountTransferCodeRequestMessage',
        17190: 'JoinAllianceUsingTokenMessage',
        17337: 'UnbotifyReportMessage',
        17338: 'AdjustPackageMessage',
        17750: GoHomeFromOfflinePractiseMessage, #v50
        18686: SetSupportedCreatorMessage,
        19001: 'LatencyTestResultMessage',
        19002: 'UdpLatencyTestRequestMessage',
        19003: 'TriggerStartLatencyTestMessage',
        19004: 'RequestLatencyTestStatusMessage',
        20000: 'SetEncryptionMessage',
        20100: ServerHelloMessage,
        20101: 'CreateAccountOkMessage',
        20103: LoginFailedMessage,
        20104: LoginOkMessage,
        20105: FriendListMessage,
        20106: FriendListUpdateMessage,
        20107: 'AddableFriendsMessage',
        20108: KeepAliveServerMessage,
        20109: 'FriendOnlineStatusMessage',
        20110: 'FriendLoggedInMessage',
        20111: 'FriendLoggedOutMessage',
        20112: AddFriendFailedMessage,
        20117: ReportUserStatusMessage,
        20118: ChatAccountBanStatusMessage,
        20121: BillingRequestFailedMessage,
        20132: 'UnlockAccountOkMessage',
        20133: 'UnlockAccountFailedMessage',
        20151: 'AppleBillingProcessedByServerMessage',
        20152: 'GoogleBillingProcessedByServerMessage',
        20153: 'TencentBillingProcessedByServerMessage',
        20154: 'CafeBazaarBillingProcessedByServerMessage',
        20156: 'KunlunBillingProcessedByServerMessage',
        20161: ShutdownStartedMessage,
        20171: 'PersonalBreakStartedMessage',
        20173: 'YoozooBillingProcessedByServerMessage',
        20199: 'FriendSuggestionsMessage',
        20205: 'AvatarNameChangeFailedMessage',
        20206: 'AvatarOnlineStatusUpdated',
        20207: AllianceOnlineStatusUpdatedMessage,
        20300: AvatarNameCheckResponseMessage,
        20402: 'CreateGameFailedMessage',
        20405: MatchMakingStatusMessage,
        20406: MatchMakingCancelledMessage,
        20501: 'AcceptFriendFailedMessage',
        20523: 'YoozooOrderAvailableMessage',
        20545: 'YoozooOrderDeliveryFailedMessage',
        20559: StartLoadingMessage,
        20801: 'NotificationMessage',
        20802: 'OpponentRejoinsMatchNotificationMessage',
        20931: 'AntiAddictionDataUpdatedMessage',
        22089: 'GetTokenFriendResultMessage',
        22100: CreatePlayerMapResponseMessage,
        22101: 'DeletePlayerMapResponseMessage',
        22102: 'PlayerMapsMessage',
        22103: 'UpdatePlayerMapResponseMessage',
        22104: 'SubmitPlayerMapResponseMessage',
        22105: 'PublishPlayerMapResponseMessage',
        22106: 'ChangePlayerMapNameMResponseMessage',
        22107: 'PlayerMapInfoUpdatedMessage',
        22109: 'DebugPlayerMapReviewResultOverrideSetMessage',
        22111: 'PlayerMapGreenlightedMessage',
        22125: 'ReportPlayerMapResponseMessage',
        22150: 'RankedMatchStartMessage',
        22151: 'RankedMatchBanStartedMessage',
        22152: 'RankedMatchBanHeroResponseMessage',
        22153: 'RankedMatchBanEndedMessage',
        22154: 'RankedMatchPickStartedMessage',
        22155: 'RankedMatchPickHeroFailedMessage',
        22156: 'RankedMatchHeroPickedMessage',
        22157: 'RankedMatchHeroDataUpdatedMessage',
        22158: 'RankedMatchFinalPreparationStartedMessage',
        22159: 'RankedMatchTerminatedMessage',
        22160: 'AllianceLeagueRankingListMessage',
        22202: 'MapPreviewMessage',
        22377: 'GoogleServiceAccountBoundMessage',
        22687: 'GamecenterAccountAlreadyBoundMessage',
        22957: 'PvpMatchmakeNotificationMessage',
        23067: 'SCIDLogoutAllDevicesResultMessage',
        23302: 'GetAllianceInviteTokenResultMessage',
        23456: BattleEndMessage,
        23457: LobbyInfoMessage,
        23458: 'BattleLogMessage',
        23459: 'BattleLogReplayAvailableMessage',
        23494: 'GoogleServiceAccountAlreadyBoundMessage',
        23774: 'PlayerJWTokenMessage',
        24101: OwnHomeDataMessage,
        24104: OutOfSyncMessage,
        24105: SpectacleFailedMessage,
        24106: 'StopHomeLogicMessage',
        24108: 'MatchmakeFailedMessage',
        24109: 'VisionUpdateMessage',
        24111: AvailableServerCommandMessage,
        24112: UdpConnectionInfoMessage,
        24113: PlayerProfileMessage,
        24114: 'HomeBattleReplayDataMessage',
        24115: ServerErrorMessage,
        24116: 'HomeBattleReplayFailedMessage',
        24117: 'HomeBattleReplayViewedMessage',
        24123: 'SeasonRewardsMessage',
        24124: TeamMessage,
        24125: TeamLeftMessage,
        24129: 'TeamErrorMessage',
        24130: TeamGameStartingMessage,
        24131: 'TeamStreamMessage',
        24177: 'SetRegionResponseMessage',
        24178: 'SetCountryResponseMessage',
        24199: 'LookForGameRoomRequestMessage',
        24201: 'FacebookAccountBoundMessage',
        24202: 'FacebookAccountAlreadyBoundMessage',
        24203: 'KakaoAccountBoundMessage',
        24204: 'KakaoAccountAlreadyBoundMessage',
        24205: 'LineAccountAlreadyBoundMessage',
        24206: 'LineAccountBoundMessage',
        24214: 'FacebookAccountUnboundMessage',
        24215: 'KakaoAccountUnboundMessage',
        24216: 'LineAccountUnboundMessage',
        24220: 'TencentAccountBoundMessage',
        24221: 'TencentAccountAlreadyBoundMessage',
        24223: 'tencentCheckCanPayResponseMessage',
        24301: AllianceDataMessage,
        24304: JoinableAllianceListMessage,
        24308: 'AllianceMemberMessage',
        24309: 'AllianceMemberRemovedMessage',
        24310: 'AllianceListMessage',
        24311: AllianceStreamMessage,
        24312: 'AllianceStreamEntryMessage',
        24313: ChangeAllianceSettingsOkMessage,
        24318: 'AllianceStreamEntryRemovedMessage',
        24319: 'TeamStreamEntryRemovedMessage',
        24321: 'AllianceInvitationSendFailedMessage',
        24333: AllianceResponseMessage,
        24364: 'AllianceTeamsMessage',
        24365: 'AllianceTeamRemovedMessage',
        24399: MyAllianceMessage,
        24403: 'LeaderboardMessage',
        24411: 'AvatarStreamMessage',
        24412: 'AvatarStreamEntryMessage',
        24413: 'BattleReportStreamMessage',
        24418: 'AvatarStreamEntryRemovedMessage',
        24555: 'FriendOnlineStatusEntryMessage',
        24582: 'TeamInviteStatusMessage',
        24589: 'TeamInvitationMessage',
        24700: 'BrawlTvChannelListMessage',
        24701: 'BrawlTvChannelNextUpMessage',
        24715: 'GlobalChatLineMessage',
        24758: 'ApiTokenMessage',
        24776: 'AllianceWarMessage',
        24777: 'PlayAgainStatusMessage',
        25165: 'SCIDAccountBoundMessage',
        25892: DisconnectedMessage,
        26002: 'LogicDeviceLinkCodeResponseMessage',
        26003: 'LogicDeviceLinkNewDeviceLinkedMessage',
        26004: 'LogicDeviceLinkCodeDeactivatedMessage',
        26005: 'LogicDeviceLinkResponseMessage',
        26007: 'LogicDeviceLinkDoneMessage',
        26008: 'LogicDeviceLinkErrorMessage',
        26085: 'GamecenterAccountBoundMessage',
        27002: 'LogicAccountTransferCodeResponseMessage',
        28275: SpellFactoryClaimFailedMessage,
        28363: 'BuyBundleBillingPackResponseMessage',
        28686: SetSupportedCreatorResponseMessage,
        28689: 'SCIDAccountAlreadyBoundMessage',
        29001: 'StartLatencyTestRequestMessage',
        29002: 'UdpLatencyTestResponseMessage',
        29003: 'LatencyTestStatusMessage',
        29900: 'SupercellIdNotificationMessage',
        29997: 'CryptoErrorMessage',
        30000: 'AttributionMessage',
        40000: 'AdUpdateConversionValueMessage'
    }

    def getMessageName(messageType):
        try:
            message = LogicLaserMessageFactory.messagesList[messageType]
        except KeyError:
            message = str(messageType)
        if type(message) == str:
            return message
        else:
            return message.__name__

    def messageExist(messageType):
        return (messageType in LogicLaserMessageFactory.messagesList.keys())

    def createMessageByType(messageType, messagePayload):
        messagesList = LogicLaserMessageFactory.messagesList
        if LogicLaserMessageFactory.messageExist(messageType):
            if type(messagesList[messageType]) == str:
                print(messageType, ":", LogicLaserMessageFactory.getMessageName(messageType), "skipped", messagePayload)
            else:
                print(messageType, ":", LogicLaserMessageFactory.getMessageName(messageType), "created")
                return messagesList[messageType](messagePayload)
        else:
            print(messageType, "skipped")
            return None