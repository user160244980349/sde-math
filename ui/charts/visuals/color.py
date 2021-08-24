from random import choice


class Color:
    reserved_colors = [
        "#ff834a",
        "#ffe100",
        "#c700c7",
        "#24e280",
        "#1100ff",
        "#ff1e22",
    ]
    available_colors = [
        "#ff834a",
        "#ffe100",
        "#c700c7",
        "#24e280",
        "#1100ff",
        "#ff1e22",
    ]

    def __new__(cls, *args, **kwargs):

        try:
            return cls.available_colors.pop()

        except IndexError:
            return f"#{''.join([choice('0123456789ABCDEF') for j in range(6)])}"

    @classmethod
    def free(cls, code: str):

        if code in cls.reserved_colors:
            cls.available_colors.append(code)
