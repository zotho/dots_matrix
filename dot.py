import dataclasses

import numpy

from config import n_float, n_data


@dataclasses.dataclass
class Dot:
    """3D dot with position, velocity and acceleration."""
    data: numpy.array = dataclasses.field(default_factory=n_data)
    _mass: n_float = n_float(1)
    _default_step: n_float = n_float(1)

    def step(self, time=_default_step):
        """Update velocity and position by acceleration and time."""
        self.vel += self.acc * time
        self.pos += self.vel * time
        # self.data[2] = numpy.zeros(shape=(3,))  # ?

    def __str__(self):
        header = f"{self.__class__.__name__} m={self.mass}"
        data = "\n".join([
            "{key}: {value}".format(
                key=key,
                value=", ".join([
                    f"{number:.2f}"
                    for number in value
                ])
            )
            for key, value in zip("xva", self.data)
        ])
        return "\n".join([header, data])

    @property
    def pos(self):
        return self.data[0]

    @pos.setter
    def pos(self, value):
        self.data[0] = value

    @property
    def vel(self):
        return self.data[1]

    @vel.setter
    def vel(self, value):
        self.data[1] = value

    @property
    def acc(self):
        return self.data[2]

    @acc.setter
    def acc(self, value):
        self.data[2] = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        self._mass = n_float(value)

    @property
    def default_step(self):
        return self._default_step

    @default_step.setter
    def default_step(self, value):
        self._default_step = n_float(value)
