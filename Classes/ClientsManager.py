import json,time

from Database.DatabaseHandler import DatabaseHandler

class ClientsManager:

    PlayersList = {}

    def AddPlayer(playerID, socket, cryptoInit):
        if ClientsManager.PlayersList.keys().__contains__(playerID[1]):
            ClientsManager.RemovePlayer(playerID)
        ClientsManager.PlayersList[playerID[1]] = {"Socket": socket, "Crypto": cryptoInit}

    def RemovePlayer(PlayerID):
        try:
            ClientsManager.PlayersList.pop(PlayerID[1])
            db_instance = DatabaseHandler()
            player_data = json.loads(db_instance.getPlayerEntryByLowID(int(PlayerID[1]))[2])
            player_data["LastOnlineTime"] = int(time.time())
            db_instance.updatePlayerDataByLowID(player_data, int(PlayerID[1]))
        except KeyError:
            print(f"Cannot remove socket with id: {PlayerID} Reason: {PlayerID} is not in the list.")

    def GetPlayerByLowID(LowID):
        if int(LowID) not in ClientsManager.PlayersList:
            return False
        return ClientsManager.PlayersList[int(LowID)]

    def GetAll():
        return ClientsManager.PlayersList

    def GetCount():
        return len(ClientsManager.PlayersList)