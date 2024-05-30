import re
#tokenizer.py
from numbers import Number

class Tokenizer(object): 

    def __init__ (self, string):
        self.cursor     = 1
        self.token_type = ''
        self.string     = string

    def isEOF(self, string): 
        return self.cursor is len(self.string)

    def hasMoreTokens(self): 
        return self.cursor < len(self.string) 

    def getNextToken(self): 

        if(self.hasMoreTokens()):
            #return None
            pass
        
        string = self.string[:self.cursor] 

        #Numbers: 
        if re.search('[0-9]',string):
            number = '' 
            while not re.search('[a-zA-Z]',string): 
                self.cursor += 1
                number += string[self.cursor]
            return {'type' : 'NUMBER', 'value': number } 
        
        #String: 
        if (string[0] == '"'):
            s = '' 
            while(string[self.cursor] is not '"' and not self.isEOF()): 
                self.cursor += 1
                s += string[self.cursor] 
            s += self.cursor + 1 
            return {'type' :'STRING', 'value': s} 

            
