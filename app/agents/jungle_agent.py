from mesa import Agent
from agents.import_agents import *

class JungleAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.specie=specie
        self.health = 100