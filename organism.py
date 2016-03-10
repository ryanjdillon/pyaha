class Organism(object):

    def __init__(self, organism_id, age, biomass, mature, x, y, z):
        import random

        self.id = organism_id
        self.alive = True
        self.age = age
        self.sex = round(random.random()) # 0: female; 1: male
        self.biomass = biomass
        self.mature = mature
        self.stomach = 0
        self.x = x
        self.y = y
        self.z = z
