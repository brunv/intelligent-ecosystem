from mesa import Agent
from agents.import_agents import *

class SnakeAgent(Agent):
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
        agent_target = self.target(cellmates) 
        if (len(cellmates) > 1):
            if(agent_target!=None):
                self.fight(agent_target)
            if(other.specie == "cobra" and self.unique_id != other.unique_id):
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
            self.health = self.health+20
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)

    def born(self):
        born_chance = random.randint(1,10)
        if (born_chance > 7 and self.health>50):
            for i in range(RANGE*3, RANGE*4):
                if (id_list[i] == DEAD):
                    id_list[i]=ALIVE
                    snake = SnakeAgent(i, self.model, "cobra")
                    self.model.schedule.add(snake)
                    self.model.grid.place_agent(snake, self.pos)
                    break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def drink(self):
        if(self.health<150):
            self.health = self.health+10

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 3
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)

    def target(self, agents_list):
        for item in agents_list:
            if (item.specie == "passaro"):
                return item
        return None