def random_walk(x0, y0, xdim, ydim):
    '''Move to surrounding cell randomly'''
    import random

    valid = False
    while not valid:
        x1 = x0 + random.choice([-1,0,1])
        y1 = y0 + random.choice([-1,0,1])

        valid = position_check(x1, y1, xdim, ydim)

    return x1, y1


def position_check(x, y, xdim, ydim):
    # Check if cell within grid
    if (x >= 0) & (x <= xdim-1) & \
       (y >= 0) & (y <= ydim-1):
        return True
    else:
        return False
