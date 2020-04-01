import random


class RandomColor:
    def __init__(self, color_count):
        random.seed(10)
        self._colors = []
        for i in range(0, color_count):
            self._colors.append(self._generate_new_color(self._colors, pastel_factor=0.9))

    @staticmethod
    def _get_random_color(pastel_factor=0.5):
        return [(x+pastel_factor)/(1.0+pastel_factor) for x in [random.uniform(0, 1.0) for i in [1, 2, 3]]]

    @staticmethod
    def _color_distance(c_1, c_2):
        return sum([abs(x[0]-x[1]) for x in zip(c_1, c_2)])

    @staticmethod
    def _generate_new_color(existing_colors, pastel_factor=0.5):
        max_distance = None
        best_color = None
        for i in range(0, 100):
            color = RandomColor._get_random_color(pastel_factor=pastel_factor)
            if not existing_colors:
                return color
            best_distance = min([RandomColor._color_distance(color, c) for c in existing_colors])
            if not max_distance or best_distance > max_distance:
                max_distance = best_distance
                best_color = color
        return best_color

    def get_color(self, i):
        assert i < len(self._colors)
        color = self._colors[i]
        return "#%02X%02X%02X" % (int(color[0] * 256), int(color[1] * 256), int(color[2] * 256))
