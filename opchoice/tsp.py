'''
Created on Sep 26, 2017

@author: fean9r
'''
from decider import DecisionMaker

class TSP(DecisionMaker):
    '''
    classdocs
    '''


    def __init__(self, constraint):
        '''
        Constructor
        '''
        DecisionMaker.__init__(self, constraint) 
    
    @abc.abstractmethod
    def make_decision(self):
        pass