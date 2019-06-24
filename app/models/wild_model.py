from models.generate_agents import *
from mesa.time import RandomActivation
from mesa.space import MultiGrid


class WildModel(Model):
    def __init__(self, N, width, height, lion_num, antelope_num, bird_num, snake_num, crocodile_num, bush_num):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        
        # ORDEM DOS AGENTES IMPORTA
        generate_water(self)
        generate_bush(self, bush_num)
        generate_lion(self,lion_num)
        generate_antelope(self, antelope_num)
        generate_bird(self, bird_num)
        generate_snake(self, snake_num)
        generate_crocodile(self, crocodile_num)
        generate_jungle(self)

    def step(self):
        self.schedule.step()
        # print(id_list) 

