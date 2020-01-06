import matplotlib
matplotlib.rcParams['text.usetex'] = True
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy

import constants
import dot
import space


if __name__ == '__main__':
    earth = dot.Dot()
    earth.mass = constants.EARTH.MASS

    moon = dot.Dot()
    moon.mass = constants.MOON.MASS
    moon.pos[0] = constants.MOON.PERIGEE_ORBIT_RADIUS
    moon.vel[1] = constants.MOON.MAX_ORBITAL_VELOCITY
    moon.vel[2] = 20

    earth.vel[1] = -constants.MOON.MAX_ORBITAL_VELOCITY * moon.mass / earth.mass

    test_space = space.Space(dots=[earth, moon])

    print()
    print(test_space)

    n_loops = 3
    n_iterations = 1000
    results = numpy.zeros(shape=(n_iterations, 12))
    dt = n_loops * constants.MOON.SIDEREAL_ROTATION_PERIOD / n_iterations
    for iteration in range(n_iterations):
        test_space.step(time=dt)
        results[iteration, 0:3] = moon.acc
        results[iteration, 3:6] = moon.vel
        results[iteration, 6:9] = moon.pos
        results[iteration, 9:12] = earth.pos

    fig = plt.figure(figsize=(16., 16.))

    ax = fig.add_subplot(2, 2, 1)
    ax.plot(results[:, 0:3])
    ax.set_ylabel(r"$\displaystyle Acceleration, m/s^2$")

    ax = fig.add_subplot(2, 2, 3)
    ax.plot(results[:, 3:6])
    ax.set_ylabel(r"$\displaystyle Velocity, m/s$")

    ax = fig.add_subplot(2, 2, 2)
    ax.plot(results[:, 6:9])
    ax.set_ylabel(r"$\displaystyle Position, m$")

    ax = fig.add_subplot(2, 2, 4, projection='3d')
    ax.plot(results[:, 6], results[:, 7], results[:, 8])
    ax.plot(results[:, 9], results[:, 10], results[:, 11])

    plt.show()
