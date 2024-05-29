import re
#tokenizer.py
from numbers import Number

class Tokenizer(object): 

    def __init__ (self):
        self.token  = {}

    def parse_token(self,t_string): 
    
        number = str()
        string = str()

        #Numbers: 
        for s in t_string:
            if re.search('[0-9]',s): number += s 
            elif re.search('[a-zA-Z]',s): string += s
            self.token['NUMBER'] = number
            self.token['STRING'] = string
        return self.token
