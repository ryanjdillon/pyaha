def random_walk(x0, y0, xmax, ymax):
    '''Move to surrounding cell randomly'''
    import random

    valid = False
    while not valid:
        x1 = x0 + random.choice([-1,0,1])
        y1 = y0 + random.choice([-1,0,1])

        valid = position_check(x1, y1, xmax, ymax)

    return x1, y1


def position_check(x, y, xmax, ymax):
    # Check if cell within grid
    if (x >= 0) & (x <= xmax) & \
       (y >= 0) & (y <= ymax):
        return True
    else:
        return False
