'''
Created on Feb 17, 2019

@author: code
'''
import mysql.connector


class dbConnect(object):
    '''
    classdocs
    '''
    
    def dbCusror(self):
        """

        Returns:

        """
        self.cursor = self.connect.cursor()
        return self.cursor

    def executeQuery(self, query):
        """

        Args:
            query:

        Returns:

        """
        if self.isOpen():
            self.cursor.execute(query)
            self.connect.commit()
            return "Query Executed"
        else:
            return "Connection Closed"

    def dbDisconnect(self):
        """

        """
        self.connect.close()
        if self.connect.is_connected():
            self.connect.disconnect()

    def isOpen(self):
"""

Returns:

"""
#         print("Connection is Open" if self.connect.is_connected() else "Connection is Closed")
        return self.connect.is_connected()


    def __init__(self, host=None, username=None,password=None):
        '''
        Constructor
        '''
        if host is not None:
            self.host = host
        else:
            self.host = "localhost"
        
        if username is not None:
            self.username = username
        else:
            self.username = "user"
        
        if password is not None:
            self.password = password
        else:
            self.password = "1234"
        
        self.connect = mysql.connector.connect(
            host=self.host, 
            user=self.username,
            password=self.password
            )
        
        self.cursor = self.connect.cursor()