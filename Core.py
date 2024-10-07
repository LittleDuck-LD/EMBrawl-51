import os
from APIHandle.Handler import API
import Configuration
from Classes.ServerConnection import ServerConnection
from Static.StaticData import StaticData
#import threading

if not os.path.exists(f"HexDumpV{Configuration.settings['DumpMajor']}"):
    os.mkdir(f"HexDumpV{Configuration.settings['DumpMajor']}")

StaticData.Preload()
#APIServer = threading.Thread(target=API.setupAPI)
#APIServer.start()
ServerConnection(("0.0.0.0", 9559))