
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return self.x.__hash__() ^ self.y.__hash__()

# Tạo đối tượng Point
p = Point(3, 8)

# Tính giá trị băm
hash_value = hash(p)
print(hash_value)