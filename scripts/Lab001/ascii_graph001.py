from turtle import color
from ascii_graph import Pyasciigraph
from ascii_graph import colors

data = [('Cokolwiek', 30, colors.Gre), ('Wpisalem', 20, colors.Pur), ('Hakuna', 45, colors.Blu), ('Matata', 5)]

graph = Pyasciigraph()

for line in graph.graph('My Histogram', data):
    print(line)