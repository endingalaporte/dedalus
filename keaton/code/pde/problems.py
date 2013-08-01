

import numpy as np


class Problem(object):
    """Class defining PDE through matrices and non-linear constructor"""

    def __init__(self, field_names, order=1):

        # Inputs
        self.field_names = field_names
        self.order = order

        # Parameters
        self.size = len(field_names)

        # Build matrix lists
        size = self.size
        self.M0 = [np.zeros((size, size)) for i in xrange(order)]
        self.M1 = [np.zeros((size, size)) for i in xrange(order)]
        self.L0 = [np.zeros((size, size)) for i in xrange(order)]
        self.L1 = [np.zeros((size, size)) for i in xrange(order)]
        self.ML = np.zeros((size, size))
        self.MR = np.zeros((size, size))
        self.LL = np.zeros((size, size))
        self.LR = np.zeros((size, size))
        self.b = np.zeros(size)


# Wave equation:  y_tt = c2 y_xx
#
# y_t - v = 0
# y_x - dy = 0
# v_t - c2 dy_x = 0
#
wave_equation_1d = Problem(['y', 'dy', 'v'], 3)
wave_equation_1d.M0[0] = np.array([[1., 0., 0.],
                                   [0., 0., 0.],
                                   [0., 0., 1.]])
wave_equation_1d.L0[0] = np.array([[0., 0., -1.],
                                   [0., -1., 0.],
                                   [0., 0., 0.]])
wave_equation_1d.L1[0] = np.array([[0., 0., 0.],
                                   [1., 0., 0.],
                                   [0., -9./8., 0.]])
wave_equation_1d.L1[1] = np.array([[0., 0., 0.],
                                   [0., 0., 0.],
                                   [0., -1., 0.]])
wave_equation_1d.L1[2] = np.array([[0., 0., 0.],
                                   [0., 0., 0.],
                                   [0., -1./8., 0.]])
wave_equation_1d.LL = np.array([[0., 0., 0.],
                                [1., 0., 0.],
                                [0., 0., 0.]])
wave_equation_1d.LR = np.array([[0., 0., 0.],
                                [0., 0., 0.],
                                [1., 0., 0.]])


# Heat equation: y_t = y_xx
#
# y_x - dy = 0
# y_t - dy_x = 0
#
heat_equation_1d = Problem(['y', 'dy'], 1)
heat_equation_1d.M0[0] = np.array([[0., 0.],
                                   [1., 0.]])
heat_equation_1d.L0[0] = np.array([[0., -1.],
                                   [0., 0.]])
heat_equation_1d.L1[0] = np.array([[1., 0.],
                                   [0., -1.]])
heat_equation_1d.LL = np.array([[1., 0.],
                                [0., 0.]])
heat_equation_1d.LR = np.array([[0., 0.],
                                [1., 0.]])
heat_equation_1d.b = np.array([1., 1.])

