from mesa import Agent
from agents.import_agents import *

class LionAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.specie = specie
        self.health = 70
    
    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts() 
            self.damage()

    def percepts(self):
        cellmates = self.model.grid.get_cell_list_contents([self.pos])
        other = self.random.choice(cellmates)
        agent_target = self.target(cellmates) 
        if (len(cellmates) > 1):
            if(agent_target!=None):
                self.fight(agent_target)
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
            #if(other.specie == "leao" and self.unique_id != other.unique_id):
            #    self.born()

            self.move(new_position)
    
    def fight(self, other):          
        if(self.health<150):
            self.health = self.health+50
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)

    def born(self):
            born_chance = random.randint(1,10)
            if (born_chance > 5 and self.health>30):
                for i in range(RANGE):
                    if (id_list[i] == DEAD):
                        id_list[i]=ALIVE
                        lion = LionAgent(i, self.model, "leao", "animal")
                        self.model.schedule.add(lion)
                        self.model.grid.place_agent(lion, self.pos)
                        break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        if(self.health<100):
            self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 7:
            self.health = self.health - 4
            if (self.health <= 0):
                id_list[self.unique_id]=0
                self.model.grid._remove_agent(self.pos, self)
                # print(self.specie,"[",self.unique_id,"] -> ", self.health)
    def target(self, agents_list):
        for item in agents_list:
            if (item.specie == "passsaro" or item.specie == "antilope" or item.specie == "crocodilo" or item.specie == "cobra"):
                print("ACHEI UMA PRESA!")
                return item
        return None
