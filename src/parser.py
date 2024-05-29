from numbers import Number
from tokenizer import Tokenizer

class Parser(Tokenizer):
        
    def __init__(self, string):
        super().__init__()
        self.lookahead = self.parse_token(string) 
    
    def parse(self):
        return self.token
