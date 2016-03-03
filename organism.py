class Organism(object):

    def __init__(self, organism_id, age, biomass, mature, x, y, z):
        import random

        self.id = organism_id
        self.alive = True
        self.age = age
        self.sex = round(random.random()) # 0: female; 1: male
        self.biomass = biomass
        self.mature = sample_maturity(self.age, self.sex, self.biomass)
        self.stomach = 0
        self.x = x
        self.y = y
        self.z = z

    def archive(self, t, sim_data):
        #with open(filename, 'w+') as f:
        #    for att in self.keys():
        #        f.write(att

        sim_data['t'].append(t)

        sim_data['id'].append(self.id)
        sim_data['x'].append(self.x)
        sim_data['y'].append(self.y)

        return sim_data


def sample_maturity(age, sex, biomass):
    '''Sample maturity state using logistic function of age, sex, biomass'''
    import random
    from scipy.special import expit

    #TODO generate curve of sex maturity for species
    ## Male maturity stage
    #if sex == 1:
    #    mature = expit()
    ## Femail maturity stage
    #elif sex == 0:
    #    mature = expit()
    #else:
    #    raise ValueError, 'Sex value {} incorrect'.format(sex)

    return False


def sample_biomass(age, sex):
    '''Sample biomass at age'''
    #TODO generage curve of biomass for species at age

    return 10


def random_walk(x0, y0, xmax, ymax):
    '''Move to surrounding cell randomly'''
    import random

    valid = False
    while not valid:
        x1 = x0 + random.choice([-1,0,1])
        y1 = y0 + random.choice([-1,0,1])

        # Check if cell within grid
        if (x1 >= 0) & (x1 <= xmax) & \
           (y1 >= 0) & (y1 <= ymax):
            valid = True

    return y1, x1
