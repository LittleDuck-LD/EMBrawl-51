import cProfile, pstats, sys
import time
import threading
import traceback

import Configuration
from Classes.ClientsManager import ClientsManager
from Classes.Instances.Classes.Player import Player
from Classes.MessageManager import MessageManager
from Classes.Messaging import Messaging
from Classes.Utility import Utility
from Classes.Crypto import Crypto


class Connection(threading.Thread):
    def __init__(self, socket, address):
        super().__init__()
        self.client = socket
        self.address = address
        self.player = Player()
        self.timeout = time.time()

    def recv(self, n):
        data = bytearray()
        while len(data) < n:
            packet = self.client.recv(n - len(data))
            if not packet:
                return b''
            data.extend(packet)
        return data

    def run(self):
        cryptoInit = Crypto()
        try:
            while True:
                time.sleep(0.001)
                messageHeader = self.client.recv(7)
                
                if len(messageHeader) >= 7:
                    headerData = Messaging.readHeader(messageHeader)
                    self.timeout = time.time()
                    packetPayload = Connection.recv(self, headerData[1])
                    packetID = headerData[0]
                    packetPayload = cryptoInit.decryptClient(packetID, bytes(packetPayload))
                    # print("Received", headerData[0], LogicLaserMessageFactory.getMessageName(headerData[0]), "length", headerData[1], "data", packetPayload, '\n')
                    if Configuration.settings["DumpPacket"] == True:
                        Utility.dumpPacket(packetPayload, headerData[0])
                    if packetID == 10099:
                        print(f"与客户端断开连接: {self.address} (Crypto错误)")
                        self.disconnectClient()
                        break
                    MessageManager.receiveMessage(self, headerData[0], packetPayload, cryptoInit)
            
                if time.time() - self.timeout > 7:
                    print(f"Client with ip: {self.address} disconnected!")
                    allSockets = ClientsManager.GetAll()
                    if self.player.ID[1] in allSockets.keys() and allSockets[self.player.ID[1]]["Socket"] == self.client:
                        ClientsManager.RemovePlayer(self.player.ID)
                    self.client.close()
                    break

        except ConnectionError:
            print(f"Client with ip: {self.address} disconnected!")
            allSockets = ClientsManager.GetAll()
            if self.player.ID[1] in allSockets.keys() and allSockets[self.player.ID[1]]["Socket"] == self.client:
                ClientsManager.RemovePlayer(self.player.ID)
            self.client.close()

        except Exception:
            print(traceback.format_exc())

    def disconnectClient(self):
        try:
            print(f"Manually disconnecting client with ip: {self.address}")
            allSockets = ClientsManager.GetAll()
            if self.player.ID[1] in allSockets.keys() and allSockets[self.player.ID[1]]["Socket"] == self.client:
                ClientsManager.RemovePlayer(self.player.ID)
            self.client.close()
        except Exception:
            print("Error while disconnecting client:")
            print(traceback.format_exc())