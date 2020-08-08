import sympy as sp


class CustomFunction(sp.Function):
    """
    Custom function class that able to store context variables

    Note: nargs variable supposed to be set with tuple of 2, the first is count of
    necessary arguments, the second is count of optional arguments, but if the
    context of calculation is set earlier
    """

    @property
    def validated_args(self):
        """
        Gives arguments that are set and replaces unset arguments with arguments
        from calculation context
        TODO: determine arguments that can have defaults

        Returns
        -------
            Tuple of all arguments even if they are not set (they are set to None)
        """
        args = list(self.args)
        args_max = max(self.nargs)
        args_len = len(args)
        args.extend([None for i in range(args_len, args_max)])
        defaults = self._get_defaults()
        return tuple([CustomFunction._parse_argument(defaults[i], args[i]) for i in range(args_max)])

    @staticmethod
    def _parse_argument(default, actual):
        """
        If argument is not set it is replaced with argument by default
        depending on calculation context

        Parameters
        ----------
            default - default argument
            actual - explicit value

        Returns
        -------
            Explicitly set argument or argument by default
        """
        if actual is not None:
            return actual
        return CustomFunction._parse_default(default)

    @staticmethod
    def _parse_default(default):
        """
        Checks if default value vor argument is set

        Parameters
        ----------
            default - default argument

        Returns
        -------
            Default value of argument
        """
        if default is None:
            raise Exception('Context is not set completely')
        else:
            return default

    @classmethod
    def _get_defaults(cls):
        """
        Gives default values for arguments

        Returns
        -------
            Tuple of arguments by default
        """
        raise NotImplemented('_get_defaults')
