def make_environment():
    '''Create a square boolean grid where true corresponds to haul-out'''
    import numpy

    # boolean mask of environment
    environment = numpy.zeros((10,10))

    environment[3:7, 3:7] = True

    return environment

if __name__ == '__main__':
    make_environment()
