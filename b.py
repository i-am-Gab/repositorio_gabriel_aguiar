class B:
    def __init__(self):
        self._B1 = 0
        self._B2 = 0.0

    def get_B1(self):
        return self._B1

    def set_B1(self, value):
        self._B1 = value

    def get_B2(self):
        return self._B2

    def set_B2(self, value):
        self._B2 = value

    def MB1(self):
        print("Método MB1 executado.")

    def MB2(self):
        print("Método MB2 executado.")
