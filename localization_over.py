#Programa que estima la posición de un robot en un mundo de cinco estados.

mundo = ["cerrado", "abierto", "abierto", "cerrado", "cerrado"]
p = [0.2, 0.2, 0.2, 0.2, 0.2]

p_sensor_acierta = 0.6
p_sensor_falla = 0.4

p_no_llega = 0.1
p_se_pasa = 0.1
p_exacto = 0.8

#Estima la creencia de estar en un estado dada una lectura
def sensar(p, z):
	q = []
	for i in range(len(p)):
		if mundo[i]==z:
			q.append(p_sensor_acierta * p[i])
		else:
			q.append(p_sensor_falla * p[i])
	s = sum(q)
	for i in range(len(q)):
		q[i] = q[i]/s
	return q

#Estima la creencia de estar en un estado dado un movimiento (control)
def mover(p, u):
	q = []
	n = len(p)
	for i in range(len(p)):
		# no llega
		s1 = p[(i-(u-1))%n] * p_no_llega
		s2 = p[(i-u)%n] * p_exacto
		s3 = p[(i-(u+1))%n] * p_se_pasa
		q.append(s1+s2+s3)
	return q


p = sensar(p, "abierto")
p = mover(p, 1)
p = sensar(p, "abierto")
p = mover(p,1)
print p
