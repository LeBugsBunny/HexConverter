import math
import os

"""

Application: HexConverter.py
Author: LeBugsBunny
Date: 03/04/2020

"""

nb = int(input('Enter a number to convert: '))

def convertHex(nb):
    nb = hex(nb)
    print('result in Hex =', nb)

convertHex(nb)

os.system("pause")
