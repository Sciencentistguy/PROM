screen = [[0 for i in range(24)] for j in range(80)]
print(len(screen))
print(len(screen[0]))


class Ball():

    direction = 0
    speed = 0
    pos = [0, 0]

    def __init__(self):
        pass

    def __str__(self):
        s = "<Ball; pos: "
        s += ",".join([str(x) for x in self.pos])
        s += "; speed: " + str(self.speed)
        s += "; direction: "
        s += str(self.direction)
        s += ">"
        return str(s)

    __rel__ = __str__


class Paddle():
    length = 4
    height = 0

    def __init__(self, length=4):
        self.length = length

    def __str__(self):
        s = "<Paddle; length: "
        s += str(self.length)
        s += "; height: "
        s += str(self.height)
        s += ">"
        return s

    __rel__ = __str__


b = Ball()
p = Paddle()
print(b)
print(p)
