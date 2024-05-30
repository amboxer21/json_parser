from numbers import Number
from _main_.tokenizer import Tokenizer

class Parser(Tokenizer):

    __number = str()
    __string = str()
          
    def __init__(self, string):
        super().__init__(string)
        a = []
        self.lookahead = self.getNextToken() 
        self.string = string
    
    def parse(self):
        return({'type' : 'Program', 'body': self.Literal()})
    
    def Literal(self): 
        match (self.token_type): 
            case 'STRING':
                return self.NumericLiteral() 
            case 'NUMBER':
                return self.StringLiteral() 
        raise ValueError('Literal: unexpected literal production')
    
    def StringLiteral(self):
        token = self.eat('STRING')
        return({'type': 'StringLiteral'}, {'value': token[1:-1]}) 

    def NumericLiteral(self):
        token = self.eat('NUMBER') 
        return ({'type': 'NumericLiteral'}, {'value' : token})  
    
    def eat(self, tokenType): 
        token = self.lookahead
        if token is None:
            raise ValueError('Unexpected End of Input, expected "${tokenType}"') 
        
        if token.token_type is not tokenType: 
            raise ValueError('Unexpected token type, expected "${tokenType}"')
        
        self.lookahead = self.getNextToken()
        return token
        
    def Program(self): 
        return( {'type' : 'Program' , 'body' : self.NumericLiteral()})
