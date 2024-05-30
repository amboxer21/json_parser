import re

class Tokenizer(object): 

    def __init__ (self, string):
        self.cursor = 1
        self.token  = {}
        self.string = string
        self.getNextToken()

    def isEOF(self, string): 
        return self.cursor is len(self.string)

    def hasMoreTokens(self): 
        return self.cursor < len(self.string) 

    def getNextToken(self): 

        if(self.hasMoreTokens()):
            #return None
            pass
        
        number = str()
        string = str()

        #Numbers: 
        for n in self.string:
            if re.search('[0-9]',n):
                number += n
        self.token = {'type' : 'NUMBER', 'value': number } 
        return self.token
        
        #String: 
        for s in self.string:
            if re.search('[0-9]',s):
                string += s
        self.token = {'type' :'STRING', 'value': string}
        return self.token

            
