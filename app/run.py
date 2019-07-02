from models.wild_model import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(agent):
    if (agent.health <= 0):
    	health_points = 0
    else:	 
    	health_points = agent.health/100.0

    #print(agent.specie,"[",agent.unique_id,"] -> ", health_points)
    
    portrayal = {"Shape": "img/lion.png",
                "scale": health_points,
                "Heath": agent.health,
                "specie": agent.specie,
                "Layer": 1}
    if (agent.specie == "leao"):
        portrayal["Layer"] = 1 
    elif (agent.specie == "antilope"):
        portrayal["Shape"]= "img/antelope.png"
        portrayal["Layer"] = 1 
    elif (agent.specie == "passaro"):
        portrayal["Shape"]= "img/bird.png"
        portrayal["Layer"] = 1
    elif (agent.specie == "crocodilo"):
        portrayal["Shape"]= "img/crocodile.png"
        portrayal["Layer"] = 1
    elif (agent.specie == "cobra"):
        portrayal["Shape"]= "img/snake.png"
        portrayal["Layer"] = 1
    elif (agent.specie == "arbusto"):
        portrayal["Shape"]= "img/bush.png"
        portrayal["Layer"] = 1 
    elif(agent.specie == "floresta"):
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Color"] = "green"
        portrayal["Layer"] = 0
        portrayal["w"] = 1
        portrayal["h"] = 1
    elif(agent.specie == "agua"):
        portrayal["Shape"] = "rect"
        portrayal["Filled"] = "true"
        portrayal["Color"] = "blue"
        portrayal["Layer"] = 0.1
        portrayal["w"] = 1
        portrayal["h"] = 1
    elif(agent.specie == "deserto"):
        portrayal["Shape"]= "img/sand.jpeg"
        portrayal["Layer"] = 0.1
        portrayal["w"] = 1
        portrayal["h"] = 1
    return portrayal

grid = CanvasGrid(agent_portrayal, 25, 25, 1000, 1000)
model_params = dict(N=5,
                    width=25, 
                    height=25,
                    lion_num= 5,
                    antelope_num= 20,
                    bird_num= 15,
                    snake_num= 10,
                    crocodile_num=5,
                    bush_num=15)
server = ModularServer(WildModel,
                       [grid],
                       "Wild Model",
                       model_params)
server.port = 8521 # The default
server.launch()

