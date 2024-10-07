from Classes.Instances.Classes.Alliance import Alliance
from Classes.Messaging import Messaging
from Classes.ClientsManager import ClientsManager

from Classes.Packets.PiranhaMessage import PiranhaMessage
from Classes.Utility import Utility
from Database.DatabaseHandler import DatabaseHandler, ClubDatabaseHandler
from Classes.ClubCommandHandler import ClubCmdHandler
import json
import time


class AlliancePremadeChatMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields={}
        fields['MessageDataID']=self.readDataReference()#[40,46]???
        fields['PremadeID']=self.readVInt()
        return fields

    def execute(message, calling_instance, fields, cryptoInit):
        
        fields["Socket"] = calling_instance.client
        db_instance = DatabaseHandler()
        clubdb_instance = ClubDatabaseHandler()
        
        
        db_instance.loadAccount(calling_instance.player, calling_instance.player.ID)
        club_ID = calling_instance.player.AllianceID[1]
        club_data = json.loads(clubdb_instance.getClubWithLowID(club_ID)[0][1])
        if len(club_data['ChatData']) > 200:
            club_data['ChatData'].pop(0)
        message_tick = club_data['ChatData'][-1]['StreamID'][1] if club_data['ChatData'] else 0
        message_tick += 1

        message = {'StreamType': 8 ,'Message': None, 'PlayerID': calling_instance.player.ID, 'PlayerName':calling_instance.player.Name, 'PlayerRole':club_data["Members"][str(calling_instance.player.ID[1])]["Role"], 'StreamID': [0,message_tick], "Time" : int(time.time()), "MessageDataID" : fields['MessageDataID'][1], "PremadeID": fields['PremadeID']}
        club_data['ChatData'].append(message)
        clubdb_instance.updateClubData(club_data, club_ID)
        fields['SendDataCount'] = 1
        fields['SendData'] = {"ChatData":[message]}

        #Messaging.sendMessage(24311, fields, cryptoInit, calling_instance.player)#在下面统一发给自己
        OnlinePlayers = ClientsManager.GetAll()
        for member in club_data['Members']:
            if int(member) in OnlinePlayers.keys():
                fields["Socket"] = OnlinePlayers[int(member)]["Socket"]
                Crypto = OnlinePlayers[int(member)]["Crypto"]
                Messaging.sendMessage(24311, fields, Crypto, calling_instance.player)
        #for member in club_data['Members']:
        #    member_id = member['ID']
        #    AllianceStreamMessage(self.client, self.player, [message]).sendByID(member_id)
        #TODO: 发给别人
        db_instance.cursor.close()
        


    def getMessageType(self):
        return 14469

    def getMessageVersion(self):
        return self.messageVersion