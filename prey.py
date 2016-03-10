def random(xdim, ydim, n_prey):
    '''Generate random prey over grid with size (ydim, xdim)'''
    import numpy
    import random

    #TODO use prey class, save prey id in list in prey_grid

    prey_grid = numpy.zeros((ydim, xdim), dtype=int)

    for i in range(n_prey):
        rx = random.randint(0, xdim-1)
        ry = random.randint(0, ydim-1)
        prey_grid[ry, rx] += 1

    return prey_grid

#class Prey(object):
#
#    def __init__(self, prey_id, biomass, size, energy, x, y, z):
#        import random
#
#        self.id = prey_id
#        self.biomass = biomass
#        self.size = size
#        self.energy = energy
#        self.x = x
#        self.y = y
#        self.z = z
