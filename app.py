import random
from helpers.log import log
num = random.randint(0, 100)

if(num >= 50):
    log('Winner!')
else:
    log('Loser...')