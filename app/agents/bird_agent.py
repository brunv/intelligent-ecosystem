from mesa import Agent
from agents.import_agents import *

class BirdAgent(Agent):
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
        water_exists = 0
        for item in agent_list:
            if(item.specie == "agua"):
                self.drink()
                water_exists = 1
                break
        
        if (water_exists == 0):
            if(self.seed_time>=10):
                if(self.agent_local() != "agua"):
                    self.born_bush()
                    self.seed_time=0
                    self.seed=False
        self.seed_time=self.seed_time+1
        self.move(new_position)
    
    def agent_local(self):
        agents_list = self.model.grid.iter_cell_list_contents(self.pos)
        what_exists = "floresta"
        for item in agents_list:
            print("agents_list: ", item.specie)
            if (item.specie == "agua"):
                what_exists = "agua"

        return what_exists

    def fight(self, other):          
        if(self.health<150):
            self.health = self.health+10
        self.seed=True
        self.seed_time=0

    def born(self):
        born_chance = random.randint(1,10)
        if (born_chance > 5 and self.health>80):
            for i in range(RANGE*2, RANGE*3):
                if (id_list[i] == DEAD):
                    id_list[i]=ALIVE
                    bird = BirdAgent(i, self.model, "passaro")
                    self.model.schedule.add(bird)
                    self.model.grid.place_agent(bird, self.pos)
                    break

    def born_bush(self):
        born_chance = random.randint(1,10)
        if (born_chance > 3):
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
        if(self.health<150):
            self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 2
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)
