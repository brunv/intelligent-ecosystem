from models. generate_agents import *
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.batchrunner import BatchRunner

def get_amount_agent_lion(model):
    return agent_counter_dict["{specie}".format(specie = "lion")]

def get_amount_agent_snake(model):
    return agent_counter_dict["{specie}".format(specie = "snake")]

def get_amount_agent_antelope(model):
    return agent_counter_dict["{specie}".format(specie = "antelope")]

def get_amount_agent_bird(model):
    return agent_counter_dict["{specie}".format(specie = "bird")]

def get_amount_agent_crocodile(model):
    return agent_counter_dict["{specie}".format(specie = "crocodile")]

class WildModel(Model):
    def __init__(self, width, height, lion_num, antelope_num, bird_num, snake_num, crocodile_num, bush_num):
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        
        generate_water(self)
        generate_bush(self, bush_num)
        generate_lion(self,lion_num)
        generate_antelope(self, antelope_num)
        generate_bird(self, bird_num)
        generate_snake(self, snake_num)
        generate_crocodile(self, crocodile_num)
        generate_jungle(self, width, height)

        self.datacollector = DataCollector(
            model_reporters={"Lion": get_amount_agent_lion,
                "Snake": get_amount_agent_snake,
                "Antelope": get_amount_agent_antelope,
                "Bird": get_amount_agent_bird,
                "Crocodile": get_amount_agent_crocodile
            }
        )
    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()