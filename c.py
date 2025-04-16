class C:
    def __init__(self):
        self._C1 = ""
        self._C2 = 0

    def get_C1(self):
        return self._C1

    def set_C1(self, value):
        self._C1 = value

    def get_C2(self):
        return self._C2

    def set_C2(self, value):
        self._C2 = value

    def MC1(self):
        print("Método MC1 executado.")

    def MC2(self):
        print("Método MC2 executado.")