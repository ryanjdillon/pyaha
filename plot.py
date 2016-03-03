def movement(x, y):
    #from shapely.geometry import import Point, LineString
    import matplotlib.pyplot as plt

    #line = LineString([Point(j, i) for j, i in zip(ys, xs)])

    fig, ax = plt.subplots()

    ax.plot(x, y, color='#999999', linewidth=2, solid_capstyle='round', zorder=1)

    plt.show()
