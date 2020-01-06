import dataclasses
from typing import List, Optional

import numpy

from config import n_float
import constants
import dot


@dataclasses.dataclass
class Space:
    """3D space with array of dots and gravitation logic."""
    dots: List[dot.Dot] = dataclasses.field(default_factory=list)
    _gravitation_const: n_float = constants.GRAVITATIONAL_CONST
    _default_step: n_float = n_float(1)

    def step_newton(self):
        """Update dots acceleration by `Newton's law of universal gravitation`."""
        G = self.gravitation_const
        for dot_1_index, dot_1 in enumerate(self.dots):
            for dot_2_index, dot_2 in enumerate(self.dots[dot_1_index + 1:], start=dot_1_index + 1):
                x_1 = dot_1.pos
                m_1 = dot_1.mass
                x_2 = dot_2.pos
                m_2 = dot_2.mass
                dx = x_2 - x_1
                distance = numpy.linalg.norm(dx)
                a = G / numpy.power(distance, 3) * dx
                print(f"Acc {dot_1_index} {dot_2_index} {a}")
                a_1 = a * m_2
                a_2 = -a * m_1
                dot_1.acc = a_1
                dot_2.acc = a_2

    step_acceleration = step_newton

    def step_velocity_and_position(self, time=_default_step):
        """Update dots velotity and position."""
        for dot in self.dots:
            dot.step(time=time)

    def step(self, time=_default_step):
        """Do all steps."""
        self.step_acceleration()
        self.step_velocity_and_position(time=time)

    @staticmethod
    def distance(vec_a, vec_b):
        return numpy.linalg.norm(vec_a - vec_b)

    def __str__(self):
        return "\n".join([
            f"{number} {dot}"
            for number, dot in enumerate(self.dots)
        ])

    @property
    def gravitation_const(self):
        return self._gravitation_const

    @gravitation_const.setter
    def gravitation_const(self, value):
        self._gravitation_const = n_float(value)

    @property
    def default_step(self):
        return self._default_step

    @default_step.setter
    def default_step(self, value):
        self._default_step = n_float(value)
