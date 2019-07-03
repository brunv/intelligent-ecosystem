from mesa import Agent
from agents.import_agents import *

class AntelopeAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.gender = generate_random_gender(self)
        self.specie = specie
        self.health = 100

    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts()
            #self.damage()

    def percepts(self):
        cellmates = get_object(self, "self")
        
        agent_target = self.target(cellmates) 
        
        if(agent_target!=None):
            self.fight(agent_target)
        
        self.breeding(cellmates)
        self.set_move()

    def fight(self, other):          
        if(self.health<150):
            self.health = self.health+50
        other.health = DEAD
        id_list[other.unique_id] = DEAD
        self.model.grid._remove_agent(other.pos, other)

    def breeding(self, cellmates):
        cellmates = get_object(self, "self")
        for other in cellmates:
            if(other.specie == "antilope" and self.unique_id != other.unique_id):
                if(self.gender == "female" and other.gender == "male"):
                    self.born()

    def born(self):
        born_chance = random.randint(1,10)
        if (born_chance > 8 and self.health>60):
            for i in range(RANGE, RANGE*2):
                if (id_list[i] == DEAD):
                    possible_positions = get_neighborhood(self)
                    position_choose = self.random.choice(possible_positions)
                    born_position = self.avoid("antilope", position_choose, possible_positions, 0)
                    if (born_position):
                        id_list[i]=ALIVE
                        antelope = AntelopeAgent(i, self.model, "antilope", "animal")
                        self.model.schedule.add(antelope)
                        self.model.grid.place_agent(antelope, born_position)
                    break

    def set_move(self):
        agent_list = get_object(self, "neighborhood")
        possible_steps = get_neighborhood(self)
        possible_position = self.random.choice(possible_steps)
        for item in agent_list:
            if (item.type == "arbusto"):
                possible_position=item.pos
            if(item.specie == "agua"):
                self.drink()
                break

        new_position = self.avoid("leao", possible_position, possible_steps, 0)
        if (new_position):
            print("NEW antilope: ", new_position)
            self.move(new_position)

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def avoid(self, avoid, possible_position, possible_steps, times):
        have_avoid = False
        agents_list = get_object(self, possible_position)
        for item in agents_list:
            if (item.specie == avoid):
                have_avoid = True
        if (have_avoid == True):
            if (times < 18):
                new_random_position = self.random.choice(possible_steps)
                times = times+1
                return self.avoid(avoid, new_random_position, possible_steps, times)
            else:
                return None
        else:
            return item.pos

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

    def target(self, agents_list):
        for item in agents_list:
            if (item.specie == "arbusto"):
                return item
        return None