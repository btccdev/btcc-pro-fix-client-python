import sys
import os
import time
import thread
import quickfix as fix
import quickfix44 as fix44
from datetime import datetime
import Application

if __name__ == '__main__':
    config = 'settings.cfg'
    accesskey = 'add your accesskey here' # add your API keys created in BTCC exchange
    secretkey = 'add your secretkey here'

    settings = fix.SessionSettings (config)
    storeFactory = fix.FileStoreFactory (settings)
    logFactory = fix.FileLogFactory (settings)
    application = Application.Application()
    initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

    initiator.start ()
    application.run (accesskey, secretkey)
    initiator.stop ()
