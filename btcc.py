import sys
import os
import time
import thread
import quickfix as fix
import quickfix44 as fix44
from datetime import datetime
import Application

if __name__ == '__main__':
    config = 'client.cfg'
    accesskey = ''
    secretkey = ''

    settings = fix.SessionSettings (config)
    storeFactory = fix.FileStoreFactory (settings)
    logFactory = fix.FileLogFactory (settings)
    application = Application.Application()
    initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

    initiator.start ()
    application.run (accesskey, secretkey)
    initiator.stop ()
