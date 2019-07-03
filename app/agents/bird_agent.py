from mesa import Agent
from agents.import_agents import *

class BirdAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.gender = generate_random_gender(self)
        self.specie=specie
        self.health = 100
        self.seed=False
        self.seed_time=0

    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts()
            self.damage()

    def percepts(self):
        self.breeding()
        self.set_move()
    
    def breeding(self):
        cellmates = get_object(self, "self")
        for other in cellmates:
            if(other.specie == "bird" and self.unique_id != other.unique_id):
                if(self.gender == "female" and other.gender == "male"):
                    self.born()

    def born(self):
        born_chance = random.randint(1,10)
        #if (born_chance > 5 and self.health>30):
        for i in range(RANGE):
            if (id_list[i] == DEAD):
                possible_positions = get_neighborhood(self)
                position_choose = self.random.choice(possible_positions)
                born_position = self.avoid("bird", position_choose, possible_positions, 0)
                if (born_position):
                    id_list[i]=ALIVE
                    bird = BirdAgent(i, self.model, "bird", "animal")
                    self.model.schedule.add(bird)
                    self.model.grid.place_agent(bird, self.pos)
                break

    def set_move(self):
        possible_steps = get_neighborhood(self)
        possible_position = self.random.choice(possible_steps)
        agent_target = self.target() 
        
        if(agent_target!=False):
            self.fight(agent_target)
        
        new_position = self.avoid("cobra", possible_position, possible_steps, 0)
        
        if (new_position != None):
            self.move(new_position)
            if (self.seed == True and self.seed_time >= 10):
                bush_position = self.avoid(["water", "bush"], new_position, possible_steps, 0)
                if (bush_position != None):
                    self.born_bush(bush_position)
                    self.seed_time=0
                    self.seed=False

        self.seed_time = self.seed_time + 1

    def target(self):
        agents_list = get_object(self, "neighborhood")
        for item in agents_list:
            if (item.specie == "bush"):
                return item

        for item in agents_list:
            if (item.specie == "water"):
                self.drink()
                break
        return False

    def fight(self, other):          
        if(self.health<=150):
            if(self.pos == other.pos):
                self.health = self.health+50
                self.seed=True
                if(self.seed_time >= 20):
                    self.seed_time=0

    def drink(self):
        if(self.health<100):
            self.health = self.health+10
                     

    def avoid(self, avoid, possible_position, possible_steps, times):
        have_avoid = False
        agents_list = get_object(self, possible_position)
        for item in agents_list:
            if (item.specie in avoid):
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

    def born_bush(self, bush_position):
        #born_chance = random.randint(1,10)
        #if (born_chance > 3):
        for i in range(RANGE*5, RANGE*7):
            if (id_list[i] == DEAD):
                id_list[i]=ALIVE
                bush = BushAgent(i, self.model, "bush", "plant")
                self.model.schedule.add(bush)
                self.model.grid.place_agent(bush, bush_position)
                break

    def move(self, new_position):
        self.model.grid.move_agent(self, new_position)

    def damage(self):
        damage_chance = random.randint(1,10)
        if damage_chance > 5:
            self.health = self.health - 2
            if (self.health <= 0):
                id_list[self.unique_id]= DEAD
                self.model.grid._remove_agent(self.pos, self)
