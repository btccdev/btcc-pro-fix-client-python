first version code for BTCC pro exchange CNY market

For using this sample code, please confirm to install 'stunnel' in your local environment or your remote servers.

This version is compiled successfully in Python 2.7x.

stunnel settings for reference( mac OS ):

1. brew install stunnel
2. make a copy of stunnel.conf-sample
3. change the copied file name to stunnel.conf
4. add an extra item like(following is installed locally):
5. 
   [BTCC-PRO-EXCHANGE-SERVER] 

   client = yes 
   
   accept = 127.0.0.1:9879 #local transmit address and port 
   
   connect = pro-fix.btcc.com:9880 #real BTCC pro exchange server address and port

5. change the fix config file setting
