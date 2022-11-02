class myproperty:
    def __init__(self, getter):
        self._getter = getter

    def __get__(self, instance, owner = None):
        return self._getter(instance)

    def __set__(self, instance, value):
        self._setter(instance, value)

    def setter(self, setter):
        self._setter = setter
        return self

class Ising:
    def __init__(self, hamiltonian = None):
        self.hamiltonian = hamiltonian

    @myproperty
    def hamiltonian(self):
        print('getter')
        return f'{self._hamiltonian = }'

    @hamiltonian.setter
    def hamiltonian(self, hamiltonian):
        print('setter')
        self._hamiltonian = hamiltonian

ising = Ising()
ising.hamiltonian = 'My Hamiltonian'
ising.hamiltonian = 'My Hamiltonian 2'

print(ising.hamiltonian)