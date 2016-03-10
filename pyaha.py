def run_aha(t0, dt, nt, spp_cfg, n_organisms):
    import datetime
    import numpy
    import random

    import environment
    import movement
    import organism
    import prey

    # Gen environment grid
    grid = environment.make_environment()
    ydim = grid.shape[0]
    xdim = grid.shape[1]

    # Init organisms
    organisms = list()
    for i in range(n_organisms):
        mean_weight = 15.0
        biomass = numpy.random.normal(mean_weight, 1.0)
        mature = False
        x = random.randint(0, xdim-1)
        y = random.randint(0, ydim-1)
        z = 0
        mature = False

        organisms.append(organism.Organism(i, 0, biomass, mature, x, y, z))

    # Create output data array
    sim_data = dict()
    for var in vars(organisms[0]):
        sim_data[var] = list()

    # Time-step model
    sim_time = t0
    prey_grid = prey.random(xdim, ydim, 200)

    for t in range(nt):
        sim_time = t0 + datetime.timedelta(days=t)

        # Loop through organisms
        for o in organisms:
            # Get and set new position to organism
            o.x, o.y = movement.random_walk(o.x, o.y, xdim, ydim)
            #TODO appraise: aroused, hungry, fear
              # feed (stomach)
            if prey_grid[o.y, o.x]!=0:
                prey_grid[o.y, o.x] -= 1
                o.stomach += 1
              # run
              # mate
              # rest

            #TODO update age
            #TODO update biomass
              # metabolism/death (energy store + intake - energy consumed)

            # Save position to simulation output data
            sim_data = archive(sim_data, o, sim_time.strftime('%Y-%m-%s %H%M%S'))

    return sim_data


def archive(sim_data, organism_obj, t):
    '''Save organism attributes and timestep'''

    organism_vars = vars(organism_obj)

    for var in organism_vars.keys():
        sim_data[var].append(organism_vars[var])

    sim_data['t'] = t

    return sim_data


if __name__ == '__main__':
    import datetime
    import numpy

    from pinniped import SEAL_CFG
    import plot

    # Start date and timestep increment
    t0 = datetime.datetime(2015, 1, 1, 0, 0, 0)
    dt = datetime.timedelta(seconds=5)
    nt = 100

    sim_data = run_aha(t0, dt, nt, SEAL_CFG, 10)

    # Extract data from simulationd data
    t = numpy.asarray(sim_data['t'])
    myid = numpy.asarray(sim_data['id'])
    x = numpy.asarray(sim_data['x'])
    y = numpy.asarray(sim_data['y'])

    # Plat track for organism 1
    idx = (myid==1)
    xs = x[idx]
    ys = y[idx]
    plot.movement(xs, ys)
