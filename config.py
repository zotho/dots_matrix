import functools

import numpy


n_dim = 3
"""Number space dimensions."""

n_float = numpy.float128
"""Float precision."""

n_data = functools.partial(numpy.zeros, shape=(3, n_dim), dtype=n_float)
"""Data for every dot."""
