from numbers import Number
from _main_.tokenizer import Tokenizer

class Parser(Tokenizer):

    __token = {'number': '', 'string': ''}
          
    def __init__(self, string):
        super().__init__(string)
        #self.getNextToken()
    
    def parse(self):
        return({'type' : 'Program', 'body': self.Literal()})
    
    def Literal(self): 
        match (self.token['type']): 
            case 'STRING':
                return self.StringLiteral() 
            case 'NUMBER':
                return self.NumericLiteral() 
        raise ValueError('Literal: unexpected literal production')
    
    def StringLiteral(self):
        return({'type': 'StringLiteral'}, {'value': self.eat('STRING')[1:-1]}) 

    def NumericLiteral(self):
        return ({'type': 'NumericLiteral'}, {'value' : self.eat('NUMBER')})  
    
    def eat(self, tokenType): 
        token = self.getNextToken()
        if token is None:
            raise ValueError('Unexpected End of Input, expected "${tokenType}"') 
        
        if self.token['type'] is not tokenType: 
            raise ValueError('Unexpected token type, expected "${tokenType}"')
        
        self.getNextToken()
        return token
        
    def Program(self): 
        return( {'type' : 'Program' , 'body' : self.NumericLiteral()})
