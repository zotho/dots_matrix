import math

import numpy

import constants
import dot
import space


class TestEarthCase:     
    def test_simple_earth_gravity(self):
        """Test gravitational acceleration at Earth surface near 9.8 m/s^2."""
        earth = dot.Dot()
        earth.mass = constants.EARTH.MASS

        simple_dot = dot.Dot()
        simple_dot.pos[0] = constants.EARTH.RADIUS

        test_space = space.Space(dots=[earth, simple_dot])

        test_space.step_acceleration()
        assert math.isclose(simple_dot.acc[0], -9.8, abs_tol=0.01)

    def test_earth_moon_loop(self):
        """Test that moon loops over Earth."""
        moon = dot.Dot()
        moon.mass = constants.MOON.MASS
        moon.pos[0] = constants.MOON.PERIGEE_ORBIT_RADIUS
        init_moon_pos = numpy.array(moon.pos)
        moon.vel[1] = constants.MOON.MAX_ORBITAL_VELOCITY

        earth = dot.Dot()
        earth.mass = constants.EARTH.MASS
        # Set system inertion to 0
        earth.vel[1] = -constants.MOON.MAX_ORBITAL_VELOCITY * moon.mass / earth.mass

        test_space = space.Space(dots=[earth, moon])

        # Distance between moon initial position and position after loop
        min_distance = numpy.inf

        n_loops = 4.
        n_iterations = 10000
        t = 0
        dt = n_loops * constants.MOON.SIDEREAL_ROTATION_PERIOD / n_iterations
        for iteration in range(n_iterations):
            test_space.step(time=dt)
            t += dt
            if t > constants.MOON.SIDEREAL_ROTATION_PERIOD / 2:
                min_distance = min(
                    min_distance,
                    space.Space.distance(init_moon_pos, moon.pos),
                )

        assert min_distance < constants.MOON.RADIUS / 100, "Moon not reached init position."
