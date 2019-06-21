from models.WildModel import *
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer


def agent_portrayal(agent):
    if (agent.health <= 0):
    	health_points = 0
    else:	 
    	health_points = agent.health/100.0

    #print(agent.specie,"[",agent.unique_id,"] -> ", health_points)
    
    portrayal = {"Shape": "img/leao.png",
                "scale": health_points,
                "Heath": agent.health,
                "specie": agent.specie,
                "Layer": 1}
    if (agent.specie == "leao"):
        portrayal["Layer"] = 1 
    elif (agent.specie == "antilope"):
        portrayal["Shape"]= "img/pumba.png"
        portrayal["Layer"] = 1 
    elif (agent.specie == "passaro"):
        portrayal["Shape"]= "img/passaro.png"
        portrayal["Layer"] = 1
    elif (agent.specie == "crocodilo"):
        portrayal["Shape"]= "img/crocodile.png"
        portrayal["Layer"] = 1
    elif (agent.specie == "arbusto"):
        portrayal["Shape"]= "img/arbusto.png"
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
    return portrayal

grid = CanvasGrid(agent_portrayal, 20, 20, 1000, 1000)
server = ModularServer(WildModel,
                       [grid],
                       "Wild Model",
                       {"N":5,
                        "width":20, 
                        "height":20,
                        "lion_num": 5,
                        "antelope_num": 20,
                        "bird_num": 15,
                        "crocodile_num":5,
                        "bush_num":15})
server.port = 8521 # The default
server.launch()

