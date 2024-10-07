import traceback

import Configuration
from Classes.Logic.LogicLaserMessageFactory import LogicLaserMessageFactory
from Classes.Messaging import Messaging


class MessageManager:
    def receiveMessage(self, messageType, messagePayload, cryptoInit):
        message = LogicLaserMessageFactory.createMessageByType(messageType, messagePayload)
        if message is not None:
            try:
                if Configuration.settings["Proxy"] == False and message.isServerToClient():
                    message.encode()
                else:
                    message.fields = message.decode()
                    if Configuration.settings["Proxy"] == False:
                        message.execute(self, message.fields, cryptoInit)

            except Exception:
                print(traceback.format_exc())
        
        if Configuration.settings["Proxy"] == False and messageType > 10100 and messageType != 10099 and messageType != 10110:
            Messaging.sendMessage(23457, {"Socket": self.client}, cryptoInit, self.player)