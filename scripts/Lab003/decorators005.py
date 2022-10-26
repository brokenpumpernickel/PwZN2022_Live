# class Ising:
#     def __init__(self, hamiltonian = None):
#         self._hamiltonian = hamiltonian

#     def get_hamiltonian(self):
#         print('Calculate cache')
#         return self._hamiltonian

#     def set_hamiltonian(self, hamiltonian):
#         self._hamiltonian = hamiltonian

###

# class Ising:
#     def __init__(self, hamiltonian = None):
#         self.hamiltonian = hamiltonian

# ising = Ising()
# ising.hamiltonian = 'My Hamiltonian'

# print(ising.hamiltonian)

###

class Ising:
    def __init__(self, hamiltonian = None):
        self.hamiltonian = hamiltonian

    @property
    def hamiltonian(self):
        print('getter')
        return self._hamiltonian

    @hamiltonian.setter
    def hamiltonian(self, hamiltonian):
        print('setter')
        self._hamiltonian = hamiltonian

ising = Ising()
ising.hamiltonian = 'My Hamiltonian'

print(ising.hamiltonian)