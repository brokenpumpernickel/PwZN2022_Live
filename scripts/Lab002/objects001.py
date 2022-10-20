### Classes 101

# class Student:
#     pass

# class Student:
#     def __init__(self):
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()

# class Student:
#     classes = []

#     def __init__(self):
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()

# s1.classes.append('PwZN')
# s2.classes.append('WdPRiR')

# print(s1.classes, s2.classes, Student.classes)
# print(Student.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         print("I'm a student!")

# s1 = Student()
# s2 = Student()

# s1.classes.append('PwZN')
# s2.classes.append('WdPRiR')

# s1.lol = 'lol'

# print(s1.classes, s2.classes, s1.lol)
# print(s1.__dict__, s2.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         print("I'm a student!")

#     def print_classes(self, od_czapy):
#         print(self.classes, od_czapy)

# s1 = Student()
# s2 = Student()

# s1.classes.append('PwZN')
# s2.classes.append('WdPRiR')

# s1.print_classes('xD')
# #Student.print_classes(s1, 'xD')

# print(s1.classes, s2.classes)
# print(s1.__dict__, s2.__dict__)

# class Student:
#     def __init__(self):
#         self.classes = []
#         self._private_attr = 3213
#         print("I'm a student!")

#     def __getitem__(self, pp):
#         print(pp)
#         return 9001

#     def print_classes(self, od_czapy):
#         print(self.classes, od_czapy)
    
#     def __len__(self):
#         return 232131

# s1 = Student()

# print(s1['xD'])
# print(len(s1))
# print(s1._private_attr)

### Basic inheritance

# class Parent:
#     def __init__(self):
#         self.parent_atr = 3
#         print('Hello from Parent!')

# class Child(Parent):
#     pass

# c = Child()
# print(c.parent_atr)


# class Parent:
#     def __init__(self):
#         self.parent_atr = 3
#         print('Hello from Parent!')

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Hello from Child!')

# c = Child()
# print(c.parent_atr)


# class Parent:
#     def __init__(self):
#         self.parent_atr = 3
#         print('Hello from Parent!')

#     def parent_function(self):
#         print('Function from Parent!')

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Hello from Child!')

#     def parent_function(self):
#         print('Function from Child!')

# c = Child()
# c.parent_function()


# class Parent:
#     def __init__(self):
#         self.parent_atr = 3
#         print('Hello from Parent!')

#     def parent_function(self):
#         print('Function from Parent!')

#     def other_function(self):
#         self.parent_function()

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print('Hello from Child!')

#     def parent_function(self):
#         print('Function from Child!')

# c = Child()
# c.other_function()


class Parent:
    def __init__(self):
        self.parent_atr = 3
        print('Hello from Parent!')

    def parent_function(self):
        print('Function from Parent!')

    __parent_function = parent_function

    def other_function(self):
        self.__parent_function()

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Hello from Child!')

    def parent_function(self):
        print('Function from Child!')

    __parent_function = parent_function

print(Parent.__dict__)
print(Child.__dict__)

c = Child()
c.other_function()