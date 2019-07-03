from mesa import Agent
from agents.import_agents import *


class LionAgent(Agent):
    def __init__(self, unique_id, model, specie, agent_type):
        super().__init__(unique_id, model)
        self.type = agent_type
        self.gender = generate_random_gender(self)
        self.specie = specie
        self.health = 150
    
    def step(self):
        if(id_list[self.unique_id] == ALIVE):
            self.percepts() 
            #self.damage()

    def percepts(self):
        self.breeding()
        self.set_move()
    
    def fight(self, other, possible_position):          
        #if(self.health<=150):
        print("SELF:", self.specie, "\tPOS: ", self.pos)
        print("OTHER:", other.specie, "\tPOS: ", other.pos)
        aux = possible_position
        if(self.pos == other.pos):
            self.health = self.health+50
            other.health = DEAD
            id_list[other.unique_id] = DEAD
            self.model.grid._remove_agent(other.pos, other)
            print("Vou pegar a posicao RANDOM, JA QUE MATEI")

        else:
            print("Vou pegar a posicao do OTHER")
            possible_position = other.pos
        if (aux == possible_position):
            print("NADA DISSO! Vou pegar a posicao do RANDO, JA QUE ESSE FILHO DA PUTA FUGIU")

        print("DENTRO DO FIGHT: ", possible_position)
        return possible_position

    def breeding(self):
        cellmates = get_object(self, "self")
        for other in cellmates:
            if(other.specie == "leao" and self.unique_id != other.unique_id):
                if(self.gender == "female" and other.gender == "male"):
                    self.born()

    def born(self):
        born_chance = random.randint(1,10)
        #if (born_chance > 5 and self.health>30):
        for i in range(RANGE):
            if (id_list[i] == DEAD):
                possible_positions = get_neighborhood(self)
                position_choose = self.random.choice(possible_positions)
                born_position = self.avoid("leao", position_choose, possible_positions, 0)
                if (born_position):
                    id_list[i]=ALIVE
                    lion = LionAgent(i, self.model, "leao", "animal")
                    self.model.schedule.add(lion)
                    self.model.grid.place_agent(lion, born_position)
                break

    def set_move(self):
        possible_steps = get_neighborhood(self)
        possible_position = self.random.choice(possible_steps)
        agent_target = self.target() 
        
        if(agent_target!=False):
            new_possible_position = self.fight(agent_target, possible_position)
        else:
            new_possible_position = possible_position
        print("possible_position: ", new_possible_position)
        new_position = self.avoid("agua", new_possible_position, possible_steps, 0)
        if (new_position != None):
            print("NEW LIAO: ", new_position)
            self.move(new_position)

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

    def target(self):
        agents_list = get_object(self, "neighborhood")
        for item in agents_list:
            if (item.specie == "passaro" or item.specie == "antilope" or item.specie == "crocodilo" or item.specie == "cobra"):
                print("RETORNEI UM ", item.specie, "EM:", item.pos )           
                return item

        for item in agents_list:
            if (item.specie == "agua"):
                self.drink()
                break
        return False
