from numbers import Number
from _main_.tokenizer import Tokenizer

class Parser(Tokenizer):
        
    def __init__(self, string):
        super().__init__()
        self.lookahead = self.parse_token(string) 
    
    def parse(self):
        return self.token
