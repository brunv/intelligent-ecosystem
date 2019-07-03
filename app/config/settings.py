import numpy as np
RANGE = 100
DEAD = 0
ALIVE = 1

id_list = np.zeros(10*RANGE)

lion_num= 5
antelope_num= 20
bird_num= 15
snake_num= 5
crocodile_num=8
bush_num=90

agent_counter_dict={
	"lion" : lion_num,
	"antelope" : antelope_num,
	"bird" : bird_num,
	"crocodile" : crocodile_num,
	"snake" : snake_num,
	"bush" : bush_num
	}

water_list = [(9,24), (8,24), (8,23), (7,23), (7,22), (7,21), (6,21), (6,20), (6,19), (5, 19),
    (5, 18), (5, 17), (4, 17), (4, 16), (4, 15), (3, 14), (4, 14), (3, 13), (3, 12), (3, 11), (4, 11),
    (3, 10), (4, 10), (4, 7), (4, 8), (4, 9), (5, 8), (5, 7), (5, 6), (5, 5), (6, 5), (6, 4),
    (6, 3), (7, 3),(7, 2), (8, 2), (8, 1), (9, 1), (9, 0),
    (17,17), (17,18), (18,17), (19,16), (18,16), (17,16), (19,15),(18,15),(20,15),(19,14),(20,14)]
  
