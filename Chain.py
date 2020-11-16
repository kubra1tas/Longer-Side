from enum import Enum


class Side(Enum):
    none = 0
    left = 1
    right = 2


class ChainLink:

    def __init__(self):
        self._left = None
        self._right = None

    def append(self, link):
        if self._right is not None: raise Exception("Link already connected!")
        self._right = link
        link._left = self

    def longer_side(self):
        if self._left == None:
            return Side.right
        elif self._right == None:
            return Side.left
        else:
            return Side.none
        return ChainLink.longer_side()


left = ChainLink()
middle = ChainLink()
right = ChainLink()
left.append(middle)
middle.append(right)
print(left.longer_side() == Side.right)