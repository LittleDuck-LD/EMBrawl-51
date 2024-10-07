import datetime
import socket
import time

import Configuration
from Classes.ClientsManager import ClientsManager
from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
import json


class LoginMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        fields["AccountID"] = self.readLong()
        fields["PassToken"] = self.readString()
        fields["ClientMajor"] = self.readInt()
        fields["ClientMinor"] = self.readInt()
        fields["ClientBuild"] = self.readInt()
        fields["ResourceSha"] = self.readString()
        fields["Device"] = self.readString()
        fields["PreferredLanguage"] = self.readDataReference()
        fields["PreferredDeviceLanguage"] = self.readString()
        fields["OSVersion"] = self.readString()
        fields["isAndroid"] = self.readBoolean()
        fields["IMEI"] = self.readString()
        fields["AndroidID"] = self.readString()
        fields["isAdvertisingEnabled"] = self.readBoolean()
        fields["AppleIFV"] = self.readString()
        fields["RndKey"] = self.readInt()
        fields["AppStore"] = self.readVInt()
        fields["ClientVersion"] = self.readString()
        fields["TencentOpenId"] = self.readString()
        fields["TencentToken"] = self.readString()
        fields["TencentPlatform"] = self.readVInt()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["AppLicensingSignature"] = self.readString()
        fields["DeviceVerifierResponse"] = self.readString()
        fields["SupercellIdToken"] = self.readCompressedString()
        fields["UpdateMaintenanceMode"] = self.readBoolean()
        fields["YoozooOsdkTicket"] = self.readString()
        fields["YoozooDeviceId"] = self.readString()
        fields["unk1"] = self.readString()
        fields["unk2"] = self.readString()
        fields["unk3"] = self.readString()
        fields["unk4"] = self.readString()
        fields["Country"] = self.readString()
        fields["unk6"] = self.readString()
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        fields["Socket"] = calling_instance.client
        if fields["ClientMajor"] != 51:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 8, 'Message': "请更新！", 'FingerprintData': None, 'ContentURL': None}, cryptoInit,needEncrypt=False)
            return
        

        
        calling_instance.player.ClientVersion = f'{str(fields["ClientMajor"])}.{str(fields["ClientBuild"])}.{str(fields["ClientMinor"])}'
        
        
        db_instance = DatabaseHandler()

        if db_instance.playerExist(fields["PassToken"], fields["AccountID"]):
            player_data = json.loads(db_instance.getPlayerEntry(fields["AccountID"])[2])
            try:
                player_data["AllianceID"] = player_data["AllianceID"]
            except:
                player_data["AllianceID"] = [0, 0]
                db_instance.updatePlayerData(player_data, calling_instance)
            db_instance.loadAccount(calling_instance.player, fields["AccountID"])
        elif fields["AccountID"][0] != 0 and fields["AccountID"][1] != 0:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 11, 'Message': "为了清除您的客户端账号数据，请您重新登录", 'FingerprintData': None, 'ContentURL': None}, cryptoInit, needEncrypt=False)
            return
        else:
            db_instance.createAccount(calling_instance.player.getDataTemplate(fields["AccountID"][0], fields["AccountID"][1], fields["PassToken"]))
            player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])

        if player_data['Banned'] == True:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 5, 'Message': "你已被服务器封禁！\n原因：违规行为封停(1)\n解封时间：未知", 'FingerprintData': None, 'ContentURL': None}, cryptoInit, needEncrypt=False)
            return

        if player_data['ID'] == [100,0]:
            player_data["IsOperator"] = True
        if Configuration.settings["Maintenance"]:
            MaintanceEndDateTime = datetime.datetime.strptime(Configuration.settings["MaintenanceEndTime"], "%Y-%m-%dT%H:%M:%S")
            MaintanceTimestamp = int(time.mktime(MaintanceEndDateTime.timetuple())) - int(time.time())
            if Configuration.settings["OpenServerAfterMaintenance"] == True and MaintanceTimestamp < 0:
                pass
            elif Configuration.settings["AllowOPPlayWhileMaintenance"] == True and player_data["IsOperator"] == True:
                pass
            else:
                fields["SecondsUntilMaintenanceEnd"] = MaintanceTimestamp
                fields["ErrorID"] = 10
                Messaging.sendMessage(20103, fields, cryptoInit,needEncrypt=False)
                return
            
        player_data['IMEI'] = fields["IMEI"]
        player_data['AppleIFV'] = fields['AppleIFV']
        player_data['AndroidID'] = fields["AndroidID"]
        player_data['isAndroid'] = fields['isAndroid']
        player_data['Device'] = fields["Device"]
        player_data['LastOnlineTime'] = int(time.time())

        player_data["IP"] = calling_instance.address
        db_instance.updatePlayerData(player_data, calling_instance)

        ClientsManager.AddPlayer(calling_instance.player.ID, calling_instance.client, cryptoInit)

        contentUpdateInfo = Utility.getContentUpdaterInfo()
        #print(fields["ResourceSha"],contentUpdateInfo[1])
        if Configuration.settings["UseContentUpdater"] == True and fields["ResourceSha"] != Configuration.settings["UseContentUpdater"][""]:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 7, 'Message': None, 'FingerprintData': Utility.getFingerprintData(contentUpdateInfo[1]), 'ContentURL': f'https://gameassets.s3-us-east-1.ossfiles.com'}, cryptoInit,needEncrypt=False)
        
        elif fields["ClientMajor"] == 51:
            #Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 1, 'Message': "123", 'FingerprintData': None, 'ContentURL': None}, cryptoInit)
            Messaging.sendMessage(20104, fields, cryptoInit, calling_instance.player)
            Messaging.sendMessage(24101, fields, cryptoInit, calling_instance.player)

            try:
                clubdb_instance = ClubDatabaseHandler()
                club_data = json.loads(clubdb_instance.getClubWithLowID(calling_instance.player.AllianceID[1])[0][1])
                fields["HasClub"] = True

            except IndexError:
                player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
                player_data["AllianceID"] = [0, 0]
                db_instance.updatePlayerData(player_data, calling_instance)
                fields["HasClub"] = False
            except TypeError:
                player_data = json.loads(db_instance.getPlayerEntry(calling_instance.player.ID)[2])
                player_data["AllianceID"] = [0, 0]
                db_instance.updatePlayerData(player_data, calling_instance)
                fields["HasClub"] = False

            Messaging.sendMessage(24399, fields, cryptoInit, calling_instance.player)
            if player_data["AllianceID"] == [0,0]:
                NotificationData = {
                    "ID": 81,
                    "Reviewed": False,
                    "Time" : int(time.time()),
                    "Message" : "检测到您未加入战队！\n请尽快加入战队，否则将无法体验服务器特色功能！",
                    "Sender" : 1
                }
                fields["Command"] = {}
                fields["Command"]["ID"] = 206
                fields["NotificationID"] = 81
                fields["NotificationData"] = NotificationData
                Messaging.sendMessage(24111, fields, cryptoInit)
           
            if fields["HasClub"]:
                Messaging.sendMessage(24311, fields, cryptoInit, calling_instance.player)
                OnlinePlayers = ClientsManager.GetAll()
                fields["AccountID"] = player_data['ID']
                fields["Status"] = 2
                for member in club_data['Members']:
                    if int(member) in OnlinePlayers.keys():
                        fields["Socket"] = OnlinePlayers[int(member)]["Socket"]
                        Crypto = OnlinePlayers[int(member)]["Crypto"]
                        Messaging.sendMessage(20207, fields, Crypto)
                fields["Socket"] = calling_instance.client
            Messaging.sendMessage(20105, fields, cryptoInit, calling_instance.player)
            
        else:
            Messaging.sendMessage(20103, {'Socket': calling_instance.client, 'ErrorID': 8, 'Message': "请更新！", 'FingerprintData': None, 'ContentURL': None}, cryptoInit,needEncrypt=False)

        db_instance.cursor.close()
        
            

    def getMessageType(self):
        return 10101

    def getMessageVersion(self):
        return self.messageVersion