class A:
    def __init__(self):
        self._A1 = 0
        self._A2 = 0.0

    def get_A1(self):
        return self._A1

    def set_A1(self, value):
        self._A1 = value

    def get_A2(self):
        return self._A2

    def set_A2(self, value):
        self._A2 = value

    def MA1(self):
        print("Método MA1 executado.")

    def MA2(self):
        print("Método MA2 executado.")

    def MA3(self):
        print("Alteração a classe A a partir do clone.")
