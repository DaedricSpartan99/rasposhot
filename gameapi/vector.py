import math

# vector 2D
class Vector:
    def __init__(self, x, y, z = 1.0):
        self.x = x
        self.y = y
        self.z = z

    # returns the mod squared
    def mod_squared(self):
        return self.x**2 + self.y**2

    def mod(self):
        return math.sqrt(self.mod_squared())

    # tranform it into a null vector
    def null(self):
        self.x = 0
        self.y = 0

    # transform it into a unit vector
    def unit(self):
        mod = self.mod()
        self.x /= mod
        self.y /= mod

    # (x, y)
    def tuple(self):
        return (self.x, self.y)

    # for value in v:
    def __iter__(self):
        return self.tuple()

    # v[key]
    def __getitem__(self, key):
        if (key == 0):
            return self.x
        elif (key == 1):
            return self.y
        else:
            return 0
        
    # v1 * v2
    def __mul__(self, num):
        return Vector((self.x * num, self.y * num))

    # v1 / v2
    def __truediv__(self, num):
        return Vector((self.x / num, self.y / num))

    # v1 // v2
    def __floordiv__(self, num):
        return Vector((self.x // num, self.y // num))

    # v * num
    def __rmul__(self, num):
        return Vector((self.x * num, self.y * num))

    # v / num
    def __rtruediv__(self, num):
        return Vector((self.x / num, self.y / num))

    # v // num
    def __rfloordiv__(self, num):
        return Vector((self.x // num, self.y // num))

    # v *= num
    def __imul__(self, num):
        self.x *= num
        self.y *= num
        return self

    # v1 += v2
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    # v1 -= v2
    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    # v /= num
    def __itruediv__(self, num):
        self.x /= num
        self.y /= num
        return self

    # v //= num
    def __ifloordiv__(self, num):
        self.x //= num
        self.y //= num
        return self

    # det
    def det(self, other):
        return self.x * other.y - self.y * other.x

    # v1 + v2
    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    # v1 - v2
    def __sub__(self, other):
        return Vector((self.x - other.x, self.y - other.y))

    # v1 == v2
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # v1 != v2
    def __ne__(self, other):
        return self.x != other.x or self.y != other.y
