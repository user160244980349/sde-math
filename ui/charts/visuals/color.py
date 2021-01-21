class Color:
    available_colors = [

        # contrast group 1
        "#FF0000",

        # contrast group 2
        "#00008B",

        # contrast group 3
        "#00FF00",

        # contrast group 4
        "#40E0D0",

        # contrast group 5
        "#800080",

        # contrast group 6
        "#FF1493",

        # contrast group 7
        "#8B4513",

        # red
        "#CD5C5C",
        "#F08080",
        "#FA8072",
        "#E9967A",
        "#FFA07A",
        "#DC143C",
        "#B22222",
        "#8B0000",

        #  pink
        "#FFC0CB",
        "#FFB6C1",
        "#FF69B4",
        "#C71585",
        "#DB7093",

        # orange
        "#FFA07A",
        "#FF7F50",
        "#FF6347",
        "#FF8C00",
        "#FFA500",

        # yellow
        "#FFD700",
        "#FFFACD",
        "#FAFAD2",
        "#FFEFD5",
        "#FFE4B5",
        "#FFDAB9",
        "#EEE8AA",
        "#F0E68C",
        "#BDB76B",

        # purple
        "#E6E6FA",
        "#D8BFD8",
        "#DDA0DD",
        "#EE82EE",
        "#DA70D6",
        "#FF00FF",
        "#BA55D3",
        "#9370DB",
        "#8A2BE2",
        "#9400D3",
        "#9932CC",
        "#8B008B",
        "#4B0082",
        "#6A5ACD",
        "#483D8B",

        # brown
        "#FFF8DC",
        "#FFEBCD",
        "#FFE4C4",
        "#FFDEAD",
        "#F5DEB3",
        "#DEB887",
        "#D2B48C",
        "#BC8F8F",
        "#F4A460",
        "#DAA520",
        "#B8860B",
        "#CD853F",
        "#D2691E",
        "#A0522D",
        "#A52A2A",
        "#800000",

        # green
        "#ADFF2F",
        "#7FFF00",
        "#32CD32",
        "#98FB98",
        "#90EE90",
        "#00FA9A",
        "#00FF7F",
        "#3CB371",
        "#2E8B57",
        "#228B22",
        "#008000",
        "#006400",
        "#9ACD32",
        "#6B8E23",
        "#808000",
        "#556B2F",
        "#66CDAA",
        "#20B2AA",
        "#8FBC8F",
        "#20B2AA",
        "#008B8B",

        # blue
        "#00FFFF",
        "#AFEEEE",
        "#7FFFD4",
        "#00CED1",
        "#5F9EA0",
        "#4682B4",
        "#B0C4DE",
        "#B0E0E6",
        "#ADD8E6",
        "#87CEEB",
        "#00BFFF",
        "#1E90FF",
        "#6495ED",
        "#7B68EE",
        "#4169E1",
        "#0000FF",
        "#0000CD",
        "#191970",
    ]

    uid = 0

    def __new__(cls, *args, **kwargs):
        if cls.uid > len(cls.available_colors):
            cls.uid = 1
        cls.uid += 1
        return cls.available_colors[cls.uid - 1]
