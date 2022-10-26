# class MyClass:
#     def __getattr__(self, attr):
#         print(attr)
#         return attr

# mc = MyClass()
# print(mc.imnothere)

###

# class InnerClass:
#     def __get__(self, instance, owner = None):
#         print('get')
#         return 'Yolo'

#     def __set__(self, instance, value):
#         print('set')

# class OuterClass:
#     ic = InnerClass()

# oc = OuterClass()
# oc.ic = 'Hello'
# print(oc.ic)

###

class HamiltonianDescriptor:
    def __get__(self, instance, owner = None):
        print('get')
        return instance._hamiltonian

    def __set__(self, instance, value):
        print('set')
        instance._hamiltonian = value

class Ising:
    hamiltonian = HamiltonianDescriptor()

    def __init__(self, hamiltonian = None):
        self.hamiltonian = hamiltonian

ising = Ising()
ising.hamiltonian = 5
print(ising.hamiltonian)
