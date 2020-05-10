import rdflib

graph = rdflib.Graph()
graph.parse('rdf_djinni.xml')

print(f"Total number of triplets: {len(graph)}")

for stmt in graph:
    print(stmt)

for s, p, o in graph.triples((None, rdflib.namespace.DC.language, rdflib.term.Literal('en'))): # в скобках задаем фильтр
    print(s, p, o)

# Проверка на валидность. Если документ не валидный, то выдаст ошибку:
try:
    unvalid_graph = rdflib.Graph()
    graph.parse('djinni.xml')
except TypeError as e:
    print(f"Если бы документ не был валидным, то выдало бы подобную ошибку: {e}")
