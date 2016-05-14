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
    accesskey = '3346e714-2311-48aa-b4e2-082df25e55ce' #test
    secretkey = 'ccb9b3d2-6be5-41ae-b9c6-bb84c771e2b4'

    settings = fix.SessionSettings (config)
    storeFactory = fix.FileStoreFactory (settings)
    logFactory = fix.FileLogFactory (settings)
    application = Application.Application()
    initiator = fix.SocketInitiator(application, storeFactory, settings, logFactory)

    initiator.start ()
    application.run (accesskey, secretkey)
    initiator.stop ()
