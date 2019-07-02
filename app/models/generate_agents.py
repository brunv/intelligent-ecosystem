from agents.import_agents import *
from mesa import Model
import random

def generate_water(self):   
    i = 1000
    water_list = [(9,24), (8,24), (8,23), (7,23), (7,22), (7,21), (6,21), (6,20), (6,19), (5, 19),
    (5, 18), (5, 17), (4, 17), (4, 16), (4, 15), (3, 14), (4, 14), (3, 13), (3, 12), (3, 11), (4, 11),
    (3, 10), (4, 10), (4, 7), (4, 8), (4, 9), (4, 8), (5, 8), (5, 7), (5, 6), (5, 5), (6, 5), (6, 4),
    (6, 3), (7, 3),(7, 2), (8, 2), (8, 1), (9, 1), (9, 0),
    (17,17), (17,18), (18,17), (19,16), (18,16), (17,16), (19,15),(18,15),(20,15),(19,14),(20,14)]
    for pos in water_list:
        water = WaterAgent(i,self, "agua", "terreno")
        self.schedule.add(water)
        self.grid.place_agent(water,pos)
        i=i+1

def generate_jungle(self, width, height):
    k = 2000
    for i in range(height):        
        for j in range(width):
            is_ground = True
            x=i
            y=j
            pos=(x,y)
            agents_list = self.grid.iter_cell_list_contents(pos)
            print("Posicao:\t", pos,"\tagents_list:\t",agents_list, "\n\tdir:\t", dir(agents_list))
            for item in agents_list:
                is_ground = False
                if (item.type != "terreno"):
                    is_ground = True
            if (is_ground == True):
                jungle = JungleAgent(k,self, "floresta", "terreno")
                self.schedule.add(jungle)
                self.grid.place_agent(jungle, (x, y))
                k=k+1

def generate_desert(self):
    desert = DesertAgent(999999,self, "deserto", "terreno")
    self.schedule.add(desert)
    self.grid.place_agent(desert, (12, 19))
    self.grid.place_agent(desert, (13, 19))
    self.grid.place_agent(desert, (14, 19))
    self.grid.place_agent(desert, (15, 19))
    self.grid.place_agent(desert, (16, 19))
    self.grid.place_agent(desert, (17, 19))
    self.grid.place_agent(desert, (18, 19))
    self.grid.place_agent(desert, (19, 19))
    self.grid.place_agent(desert, (13, 18))
    self.grid.place_agent(desert, (14, 18))
    self.grid.place_agent(desert, (15, 18))
    self.grid.place_agent(desert, (16, 18))
    self.grid.place_agent(desert, (17, 18))
    self.grid.place_agent(desert, (18, 18))
    self.grid.place_agent(desert, (19, 18))
    self.grid.place_agent(desert, (13, 17))
    self.grid.place_agent(desert, (14, 17))
    self.grid.place_agent(desert, (15, 17))
    self.grid.place_agent(desert, (16, 17))
    self.grid.place_agent(desert, (17, 17))
    self.grid.place_agent(desert, (18, 17))
    self.grid.place_agent(desert, (19, 17))
    self.grid.place_agent(desert, (14, 16))
    self.grid.place_agent(desert, (15, 16))
    self.grid.place_agent(desert, (16, 16))
    self.grid.place_agent(desert, (17, 16))
    self.grid.place_agent(desert, (18, 16))
    self.grid.place_agent(desert, (19, 16))
    self.grid.place_agent(desert, (15, 15))
    self.grid.place_agent(desert, (16, 15))
    self.grid.place_agent(desert, (17, 15))
    self.grid.place_agent(desert, (18, 15))
    self.grid.place_agent(desert, (19, 15))
    self.grid.place_agent(desert, (15, 14))
    self.grid.place_agent(desert, (16, 14))
    self.grid.place_agent(desert, (17, 14))
    self.grid.place_agent(desert, (18, 14))
    self.grid.place_agent(desert, (19, 14))
    self.grid.place_agent(desert, (16, 13))
    self.grid.place_agent(desert, (17, 13))
    self.grid.place_agent(desert, (18, 13))
    self.grid.place_agent(desert, (19, 13))
    self.grid.place_agent(desert, (18, 12))
    self.grid.place_agent(desert, (19, 12))
    
    
def generate_lion(self, lion_num):
    i=0
    while(i!=lion_num):
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        pos=(x,y)
        # Verifica se o leao será renderizado na agua
        if (self.grid.is_cell_empty((x,y))):
            id_list[i]=ALIVE 
            lion = LionAgent(i,self, "leao", "animal")
            self.schedule.add(lion)
            self.grid.place_agent(lion, (x, y))
            i=i+1
            print("ID: \t", lion.unique_id, "\tPosicao: ", lion.pos,"\tEspecie: ", lion.specie)

def generate_antelope(self, antelope_num):
    for i in range(RANGE, RANGE+antelope_num):
        antelope = AntelopeAgent(i, self, "antilope", "animal")
        id_list[i]=ALIVE 
        self.schedule.add(antelope)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(antelope, (x, y))
        print("ID: \t", antelope.unique_id, "\tPosicao: ", antelope.pos,"\tEspecie: ", antelope.specie)

def generate_bird(self, bird_num):
    for i in range(RANGE*2, RANGE*2+bird_num):
        bird = BirdAgent(i, self, "passaro", "animal")
        id_list[i]=ALIVE 
        self.schedule.add(bird)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(bird, (x, y))
        print("ID: \t", bird.unique_id, "\tPosicao: ", bird.pos,"\tEspecie: ", bird.specie)

def generate_snake(self, snake_num):
    for i in range(RANGE*3, RANGE*3+snake_num):
        snake = SnakeAgent(i, self, "cobra", "animal")
        id_list[i]=ALIVE 
        self.schedule.add(snake)
        x = self.random.randrange(self.grid.width)
        y = self.random.randrange(self.grid.height)
        self.grid.place_agent(snake, (x, y))
        print("ID: \t", snake.unique_id, "\tPosicao: ", snake.pos,"\tEspecie: ", snake.specie)


def generate_crocodile(self, crocodile_num):
    for i in range(RANGE*4, RANGE*4+crocodile_num):
        crocodile = CrocodileAgent(i, self, "crocodilo", "animal")
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
            bush = BushAgent(i,self, "arbusto", "planta")
            self.schedule.add(bush)
            self.grid.place_agent(bush, (x, y))
            i=i+1
