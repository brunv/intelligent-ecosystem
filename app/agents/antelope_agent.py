from mesa import Agent
from agents.import_agents import *

class AntelopeAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.specie = specie
        self.health = 100

    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts()
            self.damage()

    def percepts(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        other = self.random.choice(cellmates)

        if (len(cellmates) > 1 and other.specie == "arbusto"):
            self.fight(other)
        if(other.specie == "antilope" and self.unique_id != other.unique_id):
            self.born()

        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True)
        new_position = self.random.choice(possible_steps)
        agent_list = self.model.grid.iter_cell_list_contents(new_position)
        for item in agent_list:
            if(item.specie == "agua"):
                self.drink()
                break

        self.move(new_position)

    def fight(self, other):          
        if(self.health<150):
            self.health = self.health+50
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)

    def born(self):
            born_chance = random.randint(1,10)
            if (born_chance > 8 and self.health>60):
                for i in range(RANGE, RANGE*2):
                    if (id_list[i] == DEAD):
                        id_list[i]=ALIVE
                        antelope = AntelopeAgent(i, self.model, "antilope", "animal")
                        self.model.schedule.add(antelope)
                        self.model.grid.place_agent(antelope, self.pos)
                        break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        if(self.health<150):
            self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 5
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)
