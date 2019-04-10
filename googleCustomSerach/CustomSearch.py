import pprint
from googleapiclient.discovery import build
from json.decoder import JSONObject


def main():
    # Build a service object for interacting with the API. Visit
    # the Google APIs Console <http://code.google.com/apis/console>
    # to get an API key for your own application.
    service = build("customsearch", "v1",
              developerKey="AIzaSyAve5FCxnf78jPRs8yIaaTxsLPpU2S9UbE")
    
    
    
 
#     res = service.cse().list(
#         q='lectures',
#         cx='017576662512468239146:omuauf_lfve',
#       ).execute()
#     pprint.pprint(res)

    resp = service.cse().list(
        q='MicroSoft',
        cx='013826543168171249541:ggx2dveg6sa'
        ).execute()
    
    print(resp)
    
    JObj = JSONObject(resp)
    print(JObj)
    
#     pprint.pprint(resp)
    

if __name__ == '__main__':
    main()

