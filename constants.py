import functools

import numpy

from config import n_float

n_exp = functools.partial(numpy.power, n_float(10.))


GRAVITATIONAL_CONST = n_float(6.67430) * n_exp(-11.)
"""Gravitational constant, m^3 * kg^-1 * s^-2."""


class SUN:

    RADIUS = n_float(695_510) * n_exp(3.)
    """Equatorial radius, m."""

    MASS = n_float(1.989) * n_exp(30.)
    """Mass, kg."""


class EARTH:

    RADIUS = n_float(6378.1) * n_exp(3.)
    """Equatorial radius, m."""

    MASS = n_float(5.97237) * n_exp(24.)
    """Mass, kg."""

    ORBIT_RADIUS = n_float(149.6) * n_exp(9.)
    """Orbit radius, m."""

    ORBITAL_VELOCITY = n_float(29.8) * n_exp(3.)
    """Orbital velocity, m/s."""

    ROTATION_PERIOD = n_float(365.2) * 24. * 60. * 60.
    """Sidereal rotation period, s."""


class MOON:
    """Source: `https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html`."""

    RADIUS = n_float(1738.1) * n_exp(3.)
    """Equatorial radius, m."""

    MASS = n_float(0.07346) * n_exp(24.)
    """Mass, kg."""

    PERIGEE_ORBIT_RADIUS = n_float(0.3633) * n_exp(9.)
    """Perigee orbit radius, m."""

    MAX_ORBITAL_VELOCITY = n_float(1.082) * n_exp(3.)
    """Max. orbital velocity, m/s."""

    SYNODIC_PERIOD = n_float(29.53) * 24. * 60. * 60.
    """Synodic period, s."""

    SIDEREAL_ROTATION_PERIOD = n_float(655.728) * 60. * 60.
    """Sidereal rotation period, s.

    Rotation around Earth
    """
