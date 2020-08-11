import unittest
import warnings

import plotly.graph_objects as go

import mathematics.sde.linear.distortion as dist


class MyTestCase(unittest.TestCase):
    def setUp(self):
        warnings.filterwarnings(action="ignore", message="unclosed",
                                category=ResourceWarning)

    def test_zero(self):
        dt = 0.01
        fig1 = go.Figure()

        d = dist.Zero()

        v_x = [i * dt for i in range(0, 500)]
        v_y = [d.t(i) for i in v_x]

        fig1.add_trace(go.Scatter(x=v_x, y=v_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_const(self):
        dt = 0.01
        fig1 = go.Figure()

        d = dist.Const(3)

        v_x = [i * dt for i in range(0, 500)]
        v_y = [d.t(i) for i in v_x]

        fig1.add_trace(go.Scatter(x=v_x, y=v_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_polynomial(self):
        dt = 0.01
        fig1 = go.Figure()

        d = dist.Polynomial([1, 2, 3])

        v_x = [i * dt for i in range(0, 500)]
        v_y = [d.t(i) for i in v_x]

        fig1.add_trace(go.Scatter(x=v_x, y=v_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)

    def test_harmonic(self):
        dt = 0.01
        fig1 = go.Figure()

        d = dist.Harmonic([1, 2, 3])

        v_x = [i * dt for i in range(0, 500)]
        v_y = [d.t(i) for i in v_x]

        fig1.add_trace(go.Scatter(x=v_x, y=v_y,
                                  mode='lines',
                                  name="component"))
        fig1.show()

        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
