#!/usr/bin/python3
import sys
import json
import logging
import requests
import msal
import datetime
import sqlite3
from socket import socket, AF_UNIX, SOCK_DGRAM

tenantId = "***************************"
clientId = "***************************"
clientSecret = "***************************"
authority = "https://login.microsoftonline.com/"
scope = ["https://graph.microsoft.com/.default"]

#Define Start time when the log is fetched
minutes = 15
currentTime = datetime.datetime.now(datetime.timezone.utc)
sinceTime = currentTime - datetime.timedelta(minutes=minutes)
startTime = sinceTime.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
endpoint = f"https://graph.microsoft.com/beta/auditLogs/signIns?$filter=createdDateTime ge {startTime}"

#endpoint = "https://graph.microsoft.com/v1.0/auditLogs/signIns"
sname = sys.argv[0]
socketAddr = '/var/ossec/queue/sockets/queue'

# Send event to Wazuh manager
def send_event(msg):
     logging.debug('Sending {} to {} socket.'.format(msg, socketAddr))
     string = '1:azure_signin:{}'.format(msg)
     sock = socket(AF_UNIX, SOCK_DGRAM)
     sock.connect(socketAddr)
     sock.send(string.encode())
     sock.close()

#def IdCheck(azid):
#    db = '/var/ossec/etc/uwe/modules/azure.db'
#    con = sqlite3.connect(db)
#    cur = con.cursor()
#    cur.execute('CREATE TABLE IF NOT EXISTS signin (ID text);')
#    cur.execute(f'SELECT ID FROM signin WHERE ID LIKE "{azid}";')
#    ids = cur.fetchone()
#    if ids == None:
#        ids = []
#    if azid in ids:
#        return False
#    cur.execute(f'INSERT INTO signin VALUES ("{azid}");')
#    cur.execute('DELETE FROM signin WHERE ID NOT IN (SELECT ID FROM signin ORDER BY ID DESC LIMIT 10000);')
#    con.commit()
#    con.close()
#    if azid not in ids:
#        return True


if __name__ == "__main__":
    # Optional logging
    # logging.basicConfig(level=logging.DEBUG)

    # config = json.load(open(sys.argv[1]))

    # Create a preferably long-lived app instance which maintains a token cache.
    app = msal.ConfidentialClientApplication(
        clientId, authority=authority,
        client_credential=clientSecret
    )

# The pattern to acquire a token looks like this.
# result = None

# Firstly, looks up a token from cache
# Since we are looking for token for the current app, NOT for an end user,
# notice we give account parameter as None.



result = app.acquire_token_silent(scope, account=None)

if not result:
    logging.info(f"Script Failed: {sname} - Failed to aquire token")
    result = app.acquire_token_for_client(scopes=scope)
print(result)
if "access_token" in result:
    # Calling graph using the access token
    print(result['access_token'])
    data = requests.get(  # Use token to call downstream service
        endpoint,
        headers={'Authorization': 'Bearer ' + result['access_token']}, )
    graph_data=data.json()
    print(graph_data)
    response_code= data.status_code
    if not response_code==200:
        logging.error(f"script failed {sname} with response_code {response_code}")
    print("Graph API call result: ")
    #print(json.dumps(graph_data['value'], indent=2))
    #print(len(graph_data['value']))

    for value in graph_data['value']:
 #      if IdCheck(value['id']):
            azure_signin_event = {}
            azure_signin_event['azure_signin'] = value
            #send_event(json.dumps(azure_signin_event))
            print(json.dumps(azure_signin_event))
else:
    print(result.get(f"Script Failed: {sname} - error"))
    print(result.get("error_description"))
    print(result.get("correlation_id"))
