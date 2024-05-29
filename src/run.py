import logging
import json

from parser import Parser
from parser import Tokenizer 

if __name__ == "__main__": 

    program = Parser('139dmasdjf')

    print(program.parse())
