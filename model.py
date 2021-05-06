class Location:
    def __init__(self,r,c):
        self.r_index = r
        self.c_index = c

    @property
    def r_index(self):
        return self.__r_index

    @r_index.setter
    def r_index(self,value):
        self.__r_index = value

    @property
    def c_index(self):
        return self.__c_index

    @c_index.setter
    def c_index(self, value):
        self.__c_index = value


class Direction:
    """
        方向类
    """
    up = 1
    down = 2
    left = 3
    right = 4