import unittest

import plotly.graph_objects as go

from mathematics.sde.linear.distortion import Harmonic, Zero, Const, Polynomial


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        # create traces
        dt = 0.01
        fig1 = go.Figure()

        d = Zero()

        vec_x = [i * dt for i in range(0, 500)]
        vec_y = [d.t(i) for i in vec_x]

        fig1.add_trace(go.Scatter(x=vec_x, y=vec_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_const(self):
        # create traces
        dt = 0.01
        fig1 = go.Figure()

        d = Const(3)

        vec_x = [i * dt for i in range(0, 500)]
        vec_y = [d.t(i) for i in vec_x]

        fig1.add_trace(go.Scatter(x=vec_x, y=vec_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_polynomial(self):
        # create traces
        dt = 0.01
        fig1 = go.Figure()

        d = Polynomial([1, 2, 3])

        vec_x = [i * dt for i in range(0, 500)]
        vec_y = [d.t(i) for i in vec_x]

        fig1.add_trace(go.Scatter(x=vec_x, y=vec_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_harmonic(self):
        # create traces
        dt = 0.01
        fig1 = go.Figure()

        d = Harmonic([1, 2, 3])

        vec_x = [i * dt for i in range(0, 500)]
        vec_y = [d.t(i) for i in vec_x]

        fig1.add_trace(go.Scatter(x=vec_x, y=vec_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
