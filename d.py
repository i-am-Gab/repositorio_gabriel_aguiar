class D:
    def __init__(self, d1: str, d2: int):
        self._d1 = d1
        self._d2 = d2

    def get_d1(self):
        return self._d1

    def set_d1(self, value):
        self._d1 = value

    def get_d2(self):
        return self._d2

    def set_d2(self, value):
        self._d2 = value

    def MD1(self):
        print("MD1")

    def MD2(self):
        print("MD2")
        
    def MD4(self):
        print("MD4")