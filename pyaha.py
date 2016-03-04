def run_aha(t0, dt, nt, spp_cfg, n_organisms):
    import numpy
    import datetime
    import random

    from organism import Organism, random_walk
    import environment

    # Gen environment grid
    grid = environment.make_environment()
    ymax = grid.shape[0]
    xmax = grid.shape[1]

    # Init organisms
    organisms = list()
    for i in range(n_organisms):
        mean_weight = 15.0
        biomass = numpy.random.normal(mean_weight, 1.0)
        x = random.randint(0, xmax)
        y = random.randint(0, ymax)
        z = 0
        mature = False

        organisms.append(Organism(i, 0, biomass, mature, x, y, z))

    data = dict()
    data['t']  = list()
    data['id'] = list()
    data['x']  = list()
    data['y']  = list()


    # Time-step model
    sim_time = t0
    #for t in range(nt):
    for t in range(nt):
        sim_time = t0 + datetime.timedelta(days=t)

        for i in range(len(organisms)):
            y, x = random_walk(organisms[i].x, organisms[i].y, xmax, ymax)
            organisms[i].y, organisms[i].x = y, x
            data = organisms[i].archive(sim_time.strftime('%Y-%m-%s %H%M%S'), data)

    return (numpy.asarray(data['t']), numpy.asarray(data['id']),
            numpy.asarray(data['x']), numpy.asarray(data['y']))


if __name__ == '__main__':
    import datetime

    from pinniped import SEAL_CFG
    import plot

    # Start date and timestep increment
    t0 = datetime.datetime(2015, 1, 1, 0, 0, 0)
    dt = datetime.timedelta(seconds=5)
    nt = 100

    t, myid, x, y = run_aha(t0, dt, nt, SEAL_CFG, 10)

    idx = myid==1
    xs = x[idx]
    ys = y[idx]
    plot.movement(xs, ys)
