Graph = {
	'BL':{'J':446},
	'J':{'BL':629, 'B':421, 'C':246},
	'B':{'J':446, 'Ba':320},
	'C':{'Ba':320, 'S':108, 'Ci':156, 'P':132},
	'Ba':{'B':320, 'C':246, 'T':248},
	'T':{'Ba':320, 'Ci':156},
	'Ci':{'T':248, 'C':246, 'P':132},
	'P':{'Ci':156, 'C':246, 'Y':0},
	'S':{'C':246, 'Y':0},
	'Y':{ 'S':108, 'Ci':156, 'P':132},
}

start = 'BL'
target = 'Y'

for i in Graph:
	for j in Graph[i]:
		value = Graph[i]
		print(value[j])




def gbfs(Graph, start, target):
	state = Graph.get(start)
	



gbfs(Graph, start, target)