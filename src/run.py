import logging
import json

from _main_.parser import Parser
from _main_.parser import Tokenizer 

if __name__ == "__main__": 

    program = Parser('139dmasdjf')

    print(program.parse())
