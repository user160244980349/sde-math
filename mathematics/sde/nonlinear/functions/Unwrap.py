import sympy as sp


class Unwrap(sp.Function):
    """
    Simple function to unwrap matrix
    """
    nargs = 1

    @classmethod
    def eval(cls, m):
        """
        Performs modeling with Milstein method with scalar substitutions in cycle
        Parameters
        ----------
            m - matrix to unwrap

        Returns
        -------
            Unwraped matrix
        """
        if m.is_Matrix and not m.is_symbol:
            return m[0, 0]
