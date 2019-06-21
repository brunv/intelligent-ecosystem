
from agents.agents import *
from mesa.time import RandomActivation
from mesa.space import MultiGrid

def generate_water(self):   
    water = WaterAgent(999997,self, "agua")
    self.schedule.add(water)
    self.grid.place_agent(water, (5, 19))
    self.grid.place_agent(water, (5, 18))
    self.grid.place_agent(water, (5, 17))
    self.grid.place_agent(water, (4, 17))
    self.grid.place_agent(water, (4, 16))
    self.grid.place_agent(water, (4, 15))
    self.grid.place_agent(water, (3, 14))
    self.grid.place_agent(water, (4, 14))  
    self.grid.place_agent(water, (3, 13))
    self.grid.place_agent(water, (3, 12))
    self.grid.place_agent(water, (3, 11))
    self.grid.place_agent(water, (4, 11))
    self.grid.place_agent(water, (3, 10))
    self.grid.place_agent(water, (4, 10))
    self.grid.place_agent(water, (4, 7))
    self.grid.place_agent(water, (4, 8))
    self.grid.place_agent(water, (4, 9))
    self.grid.place_agent(water, (4, 8))
    self.grid.place_agent(water, (5, 8))
    self.grid.place_agent(water, (5, 7))
    self.grid.place_agent(water, (5, 6))
    self.grid.place_agent(water, (5, 5))
    self.grid.place_agent(water, (6, 5))
    self.grid.place_agent(water, (6, 4))
    self.grid.place_agent(water, (6, 3))
    self.grid.place_agent(water, (7, 3))
    self.grid.place_agent(water, (7, 2))
    self.grid.place_agent(water, (8, 2))
    self.grid.place_agent(water, (8, 1))
    self.grid.place_agent(water, (9, 1))
    self.grid.place_agent(water, (9, 0))

def generate_jungle(self):
    jungle = JungleAgent(999998,self, "floresta")
    self.schedule.add(jungle)
    for i in range(20):        
        for j in range(20):
            x=i
            y=j
            self.grid.place_agent(jungle, (x, y))


def generate_lion(self, lion_num):
    i=0
    while(i!=lion_num):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        # Verifica se o leao será renderizado na agua
        if (self.grid.is_cell_empty((x,y))):
            id_list[i]=ALIVE 
            lion = LionAgent(i,self, "leao")
            self.schedule.add(lion)
            self.grid.place_agent(lion, (x, y))
            i=i+1
            print("ID: \t", lion.unique_id, "\tPosicao: ", lion.pos,"\tEspecie: ", lion.specie)

def generate_antelope(self, antelope_num):
    for i in range(RANGE, RANGE+antelope_num):
        antelope = AntelopeAgent(i, self, "antilope")
        id_list[i]=ALIVE 
        self.schedule.add(antelope)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(antelope, (x, y))
        print("ID: \t", antelope.unique_id, "\tPosicao: ", antelope.pos,"\tEspecie: ", antelope.specie)

def generate_bird(self, bird_num):
    for i in range(RANGE*2, RANGE*2+bird_num):
        bird = BirdAgent(i, self, "passaro")
        id_list[i]=ALIVE 
        self.schedule.add(bird)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(bird, (x, y))
        print("ID: \t", bird.unique_id, "\tPosicao: ", bird.pos,"\tEspecie: ", bird.specie)

def generate_snake(self, snake_num):
    for i in range(RANGE*3, RANGE*3+snake_num):
        snake = SnakeAgent(i, self, "cobra")
        id_list[i]=ALIVE 
        self.schedule.add(snake)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(snake, (x, y))
        print("ID: \t", snake.unique_id, "\tPosicao: ", snake.pos,"\tEspecie: ", snake.specie)


def generate_crocodile(self, crocodile_num):
    for i in range(RANGE*4, RANGE*4+crocodile_num):
        crocodile = CrocodileAgent(i, self, "crocodilo")
        id_list[i]=ALIVE 
        self.schedule.add(crocodile)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(crocodile, (x, y))
        print("ID: \t", crocodile.unique_id, "\tPosicao: ", crocodile.pos,"\tEspecie: ", crocodile.specie)

def generate_bush(self, bush_num):
    i=RANGE*5
    while (i!=RANGE*5+bush_num):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        # Verifica se o arbusto será renderizado na agua
        if (self.grid.is_cell_empty((x,y))):
            id_list[i]=ALIVE 
            bush = BushAgent(i,self, "arbusto")
            self.schedule.add(bush)
            self.grid.place_agent(bush, (x, y))
            i=i+1

class WildModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height, lion_num, antelope_num, bird_num, snake_num, crocodile_num, bush_num):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)
        self.running = True
        
        # ORDEM DOS AGENTES IMPORTA
        generate_water(self)
        generate_bush(self, bush_num)
        generate_lion(self,lion_num)
        generate_antelope(self, antelope_num)
        generate_bird(self, bird_num)
        generate_snake(self, snake_num)
        generate_crocodile(self, crocodile_num)
        generate_jungle(self)

    def step(self):
        self.schedule.step()
        # print(id_list) 

