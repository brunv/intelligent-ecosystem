import random
from mesa import Model

def get_neighborhood(self):
        neighborhood = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=True)
        return neighborhood

def get_object(self, choice):
    # Recebe por parametro a posicao (ou lista de posicoes) que será retornado o objeto
    if choice == "neighborhood":
        content = get_neighborhood(self)
    elif choice == "self":
        content = [self.pos]
    else:
        content = choice
    return self.model.grid.get_cell_list_contents(content)

def generate_random_gender(self):
    gender = random.randint(1,2)
    if (gender == 1):
        return "male"
    if (gender == 2):
        return "female"
