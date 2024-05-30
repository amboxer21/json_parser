import logging
import json

from _main_.parser import Parser
from _main_.tokenizer import Tokenizer

if __name__ == "__main__": 
    
    tok        = Tokenizer('139dmasdjf')
    tok_parser = Parser('139dmasdjf')

    tok_parser.parse()

    print(tok_parser.Program())
