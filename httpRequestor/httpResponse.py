'''
Created on Feb 21, 2019

@author: code
'''

import json

import requests


class httpResponseClass(object):
    '''
    classdocs
    '''
    
    def getResponse(self):
        # sending get request and saving the response as response object 
        if self.PARAMS is not None:
            self.responseReturn = requests.get(url=self.URL, params=self.PARAMS).content
            self.isJSONFlag = self.JSONCheck()
            return self.responseReturn 
        else:
            self.responseReturn = requests.get(url=self.URL).content
            self.isJSONFlag = self.JSONCheck()
            return self.responseReturn 
        # extracting data in json format 
    
    def isJSON(self):
        self.responseReturn = self.getResponse()
        return self.isJSONFlag
    
    def getJSONResponse(self):
        if (self.isJSON()):
            return self.JSONResponse
        else:
            return self.JSONResponse
        
    def JSONCheck(self):
        if(isinstance(self.responseReturn, str)):
            try:
                self.JSONResponse = json.loads(self.responseReturn)
                return True
            except:
                return False
        else:
            # print("Response Type: " + str(type(self.responseReturn)))
            return False    
   
    def getResponseCode(self):
        return requests.get(self.URL, self.PARAMS).status_code
    
    def isRedirect(self):
        return requests.get(self.URL, self.PARAMS)
  
#     def getJSONResponse(self):
#         # sending get request and saving the response as response object 
#         r = requests.get(url = self.URL, params = self.PARAMS) 
#         # extracting data in json format 
#         return r.json() 

    def paramParser(self):
        print(type(self.PARAMS))

    def __init__(self, URL, PARAMS=None):
        '''
        Constructor
        '''
        self.URL = URL
        self.PARAMS = PARAMS
        self.responseReturn = None
        self.isJSONFlag = False
        self.JSONResponse = json.loads('{"status": "Invalid Request: Return value is not JSON format"}')
