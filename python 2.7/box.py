'''OOP Practice '''

class Box(object):

    # variables

    # constructor
    def __init__(self):
        pass

    # setters
    def set_width(self, value):
        self.width = value

    def set_length(self, value):
        self.length = value

    # getters
    def get_width(self):
        return self.width

    def get_length(self):
        return self.length


def compute_area(width, length):
    area = width * length
    return area


box = Box()

box.set_width(3)
box.set_length(5)

x = box.get_width()
y = box.get_length()
a = compute_area(x, y)

print(x)
print(y)
print(a)
