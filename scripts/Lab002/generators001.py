# def yolo():
#     yield 'Hello'
#     yield 'World'
#     yield '!'

# for w in yolo():
#     print(w)

# print(type(yolo()))

def my_range(maxv):
    index = 0
    while index < maxv:
        yield index, 'Hakuna matata'
        index += 1

for i in my_range(10):
    print(i)