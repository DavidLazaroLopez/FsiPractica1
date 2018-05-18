# -*- coding: utf-8 -*-

# Search methods
import search

sl = search.GPSProblem('S', 'L', search.romania)

## De Oradea a Giurgiu ##
# Ramificacion y acotacion con subestimacion: 26 (9 expansiones)
# FIFO: 148 (54 expansiones)
# STACK: 31 (tras quitar la lista cerrada hace un bucle infinito)
og = search.GPSProblem('O', 'G', search.romania)

## De Arad a Bucharest ##
# Ramificacion y acotacion con subestimacion: 15 (5 expansiones)
# FIFO: 59 (21 expansiones)
# STACK: 23 (tras quitar la lista cerrada hace un bucle infinito)
ab = search.GPSProblem('A', 'B', search.romania)

## De Craiova a Fagaras ##
# Ramificacion y acotacion con subestimacion: 21 (7 expansiones)
# FIFO: 61 (21 expansiones)
# STACK: 22 (tras quitar la lista cerrada hace un bucle infinito)
cf = search.GPSProblem('C', 'F', search.romania)



result = [0] * 20

result[0] = search.busqueda_ramificacion_subestimacion(ab)
result[1] = search.busqueda_ramificacion_subestimacion(cf)
result[2] = search.busqueda_ramificacion_subestimacion(sl)
result[3] = search.busqueda_ramificacion_subestimacion(og)

result[4] = search.busqueda_ramificacion_costes(ab)
result[5] = search.busqueda_ramificacion_costes(cf)
result[6] = search.busqueda_ramificacion_costes(sl)
result[7] = search.busqueda_ramificacion_costes(og)

result[8] = search.breadth_first_graph_search(ab)
result[9] = search.breadth_first_graph_search(cf)
result[10] = search.breadth_first_graph_search(sl)
result[11] = search.breadth_first_graph_search(og)

result[12] = search.busqueda_stack(ab)
result[13] = search.busqueda_stack(cf)
result[14] = search.busqueda_stack(sl)
result[15] = search.busqueda_stack(og)

print ""
print " --------------------------------------------- "
print " ------------------> TABLA <------------------ "
print " --------------------------------------------- "
print ""

print "                                                     | Arad to Bucharest |    | Craiova to Fagaras |      | Sibiu to Lugoj |      | Oradea to Giurgiu |"
print ""
print "Ramificacion y acotacion:"+ "                                   " +str(result[0]) + "                           " +str(result[1]) + "                       " +str(result[2]) + "                         " +str(result[3])
print ""
print "Ramificacion y acotacion con subestimacion:" + "                  " +str(result[4]) + "                            " +str(result[5]) + "                       " +str(result[6]) + "                           " +str(result[7])
print ""
print "Primero en anchura (FIFO):" + "                                  " +str(result[8]) + "                           " +str(result[9]) + "                       " +str(result[10]) + "                          " +str(result[11])
print ""
print "Primero en profundidad (STACK):"+ "                             " +str(result[12]) + "                            " +str(result[13]) + "                       " +str(result[14]) + "                          " +str(result[15])



# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


