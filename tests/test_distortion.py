import unittest

import plotly.graph_objects as go

import mathematics.sde.linear.distortion as dist


class MyTestCase(unittest.TestCase):
    def test_zero(self):
        # create traces
        dt = 0.01
        fig1 = go.Figure()

        d = dist.Zero()

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

        d = dist.Const(3)

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

        d = dist.Polynomial([1, 2, 3])

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

        d = dist.Harmonic([1, 2, 3])

        vec_x = [i * dt for i in range(0, 500)]
        vec_y = [d.t(i) for i in vec_x]

        fig1.add_trace(go.Scatter(x=vec_x, y=vec_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
