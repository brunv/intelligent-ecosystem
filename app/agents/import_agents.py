import numpy as np
from custom.functions import *

RANGE = 100
DEAD = 0
ALIVE = 1

id_list = np.zeros(10*RANGE)
water_list = [(9,24), (8,24), (8,23), (7,23), (7,22), (7,21), (6,21), (6,20), (6,19), (5, 19),
    (5, 18), (5, 17), (4, 17), (4, 16), (4, 15), (3, 14), (4, 14), (3, 13), (3, 12), (3, 11), (4, 11),
    (3, 10), (4, 10), (4, 7), (4, 8), (4, 9), (4, 8), (5, 8), (5, 7), (5, 6), (5, 5), (6, 5), (6, 4),
    (6, 3), (7, 3),(7, 2), (8, 2), (8, 1), (9, 1), (9, 0),
    (17,17), (17,18), (18,17), (19,16), (18,16), (17,16), (19,15),(18,15),(20,15),(19,14),(20,14)]
    
from agents.antelope_agent import *
from agents.bush_agent import *
from agents.bird_agent import *
from agents.crocodile_agent import *
from agents.jungle_agent import *
from agents.lion_agent import *
from agents.snake_agent import *
from agents.water_agent import *
from agents.desert_agent import *