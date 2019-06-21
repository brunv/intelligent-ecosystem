from mesa import Agent, Model
import numpy as np
import random
RANGE = 100
DEAD = 0
ALIVE = 1

id_list = np.zeros(6*RANGE)

	
class WaterAgent(Agent):
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie=specie
        self.health = 100

class JungleAgent(Agent):
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie=specie
        self.health = 100

class BushAgent(Agent):
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie=specie
        self.health = 100

class LionAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie = specie
        self.health = 70
    
    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts() 
            self.damage()

    def percepts(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        other = self.random.choice(cellmates)
        if (len(cellmates) > 1 and other.specie != "floresta" and other.specie != "agua"):
            if(other.specie == "antilope" or other.specie == "passaro" ):
                self.fight(other)
            elif(other.specie == "leao" and self.unique_id != other.unique_id):
                self.born()

        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True)
        new_position = self.random.choice(possible_steps)
        agent_list = self.model.grid.iter_cell_list_contents(new_position)
        water_exists=0
        for item in agent_list:
            if(item.specie == "agua"):
                self.drink()
                water_exists=1
        if(water_exists==0):
            self.move(new_position)
    
    def fight(self, other):          
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)
        self.health = self.health+10

    def born(self):
            born_chance = random.randint(1,10)
            if (born_chance > 5 and self.health>10):
                for i in range(RANGE):
                    if (id_list[i] == DEAD):
                        id_list[i]=ALIVE
                        lion = LionAgent(i, self.model, "leao")
                        self.model.schedule.add(lion)
                        self.model.grid.place_agent(lion, self.pos)
                        break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 7:
            self.health = self.health - 5
            if (self.health <= 0):
                id_list[self.unique_id]=0
                self.model.grid._remove_agent(self.pos, self)
                # print(self.specie,"[",self.unique_id,"] -> ", self.health)


class AntelopeAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie=specie
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
        water_exists=0

        for item in agent_list:
            if(item.specie == "agua"):
                self.drink()
                water_exists=1
        if(water_exists==0):
            self.move(new_position)

    def fight(self, other):          
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)
        self.health = self.health+50

    def born(self):
            born_chance = random.randint(1,10)
            if (born_chance > 8 and self.health>60):
                for i in range(RANGE, RANGE*2):
                    if (id_list[i] == DEAD):
                        id_list[i]=ALIVE
                        antelope = AntelopeAgent(i, self.model, "antilope")
                        self.model.schedule.add(antelope)
                        self.model.grid.place_agent(antelope, self.pos)
                        break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 5
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)


class BirdAgent(Agent):
    """ An agent with fixed initial wealth."""
    def __init__(self, unique_id, model, specie):
        super().__init__(unique_id, model)
        self.specie=specie
        self.health = 100
        self.seed=False
        self.seed_time=0

    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts()
            self.damage()

    def percepts(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        other = self.random.choice(cellmates)

        if (len(cellmates) > 1 and other.specie == "arbusto"):
            self.fight(other)
        if(other.specie == "passaro" and self.unique_id != other.unique_id):
            self.born()

        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True)
        new_position = self.random.choice(possible_steps)
        agent_list = self.model.grid.iter_cell_list_contents(new_position)
        water_exists=0

        for item in agent_list:
            if(item.specie == "agua"):
                self.drink()
                water_exists=1
        if(water_exists==0):
            if(self.seed_time==5):
                self.born_bush()
                self.seed_time=0
                self.seed=False
            self.seed_time=self.seed_time+1
            self.move(new_position)

    def fight(self, other):          
        self.health = self.health+10
        self.seed=True
        self.seed_time=0

    def born(self):
        born_chance = random.randint(1,10)
        if (born_chance > 40 and self.health>30):
            for i in range(RANGE*2, RANGE*3):
                if (id_list[i] == DEAD):
                    id_list[i]=ALIVE
                    bird = BirdAgent(i, self.model, "passaro")
                    self.model.schedule.add(bird)
                    self.model.grid.place_agent(bird, self.pos)
                    break

    def born_bush(self):
        born_chance = random.randint(1,10)
        if (born_chance > 1):
            for i in range(RANGE*5, RANGE*6):
                if (id_list[i] == DEAD):
                    id_list[i]=ALIVE
                    bush = BushAgent(i, self.model, "arbusto")
                    self.model.schedule.add(bush)
                    self.model.grid.place_agent(bush, self.pos)
                    break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 5
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)