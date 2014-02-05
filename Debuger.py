'''
Created on Feb 4, 2014
@version: 0.3
@author: Furqan Wasi
'''
# Fixity Scheduler
# Version 0.3, 2013-10-28
# Copyright (c) 2013 AudioVisual Preservation Solutions
# All rights reserved.
# Released under the Apache license, v. 2.0

import logging
import datetime
from os import getcwd 

''' Class to manage all the the errors and warning loging'''
class Debuger():
    
    
    # Constuctor
    def __init__(self):
        self.loger = logging
        self.loger.basicConfig(filename=getcwd() + '\\debug\\debug.log',level=logging.DEBUG)
        self.loger.info('Logging for Date '+ str(datetime.datetime.now()).rpartition('.')[0] +"\n")
        self.isdebugerOn = False
        
    # Function to Log Errors
    # @param msg Message to log
    def logError(self,msg,moreInformation = None):
        if(self.isdebugerOn):
            self.loger.debug(msg)
            if(moreInformation):
                for key in moreInformation:
                    self.loger.debug(key + '::' + moreInformation[key]+"\n")
             
    
    
    # Function to Log Information
    # @param msg Message to log
    def logInfo(self,msg,moreInformation = None):
        if(self.isdebugerOn):
            self.loger.info(msg)
            if(moreInformation):
                for key in moreInformation:
                    self.loger.info(key + '::' + moreInformation[key]+"\n")
    
    # Function to Log Warning
    # @param msg Message to log         
    def logWarning(self,msg,moreInformation = None):
        if(self.isdebugerOn):
            self.loger.warning(msg)
            if(moreInformation):
                for key in moreInformation:
                    self.loger.warning(key + '::' + moreInformation[key]+"\n")
         
        
    # Function to turn debugging On  
    def tureDebugerOn(self):
        self.isdebugerOn = True
        
    # Function to turn debugging of 
    def tureDebugerOff(self):
        self.isdebugerOn = False
        
    # Function to Get Current Time   
    def getCurrentTime(self):
        if(self.isdebugerOn):
            return str(datetime.datetime.now()).rpartition('.')[0]





            