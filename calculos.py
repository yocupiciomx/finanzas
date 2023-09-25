# -*- coding: utf-8 -*-

#Software de Finanzas Generales
#Desarrollado por Angel Yocupicio
#Versión 3.x.x de Python
#Sitio Web www.yocupicio.com
#Inicio 26 de Octubre de 2019
#Monto del pago mensual mediante Saldos Insolutos
#Contribución Joshyba
#Sitio Web www.JoshybaDevelopments.blogspot.com
#Fin ...

print("Software de Finanzas Generales")

tipo = str(input("""Elige la letra de la operación deseada: 
	Monto Acumulado.........(F)
	Valor Presente..........(P)
	Anualidad...............(A)
	Número de Anualidades...(n)
	Tasa de Interés.........(i)
	Pago mensual S.I........(S)
	"""))
if tipo == "F" or "P" or "A" or "n" or "i" or "S":

	if tipo == "F":
		A = float(input("Valor de la anualidad, A = $"))
		ii = float(input("Tasa de interés, i = "))
		t = float(input("Cuantos años ahorrarás, t = "))
		m = int(input("""Elige el número segun el tipo de capitalización:
			mensual.........(12)
			bimestral.......(6)
			trimestral......(4)
			cuatrimestral...(3)
			semestral.......(2)
			anual...........(1)
			"""))
		k = 12/m
		n = 12*t/k
		i = ii/(100*m)
		F = A*((1+i)**(n+1)-(1+i))/i
		print("F = ${:,}\nA = ${:,}\ni = {}%\nn = {}".format(round(F,2),round(A,2),ii,n))
	elif tipo == "P":
		A = float(input("Valor de la anualidad, A = $"))
		ii = float(input("Tasa de interés, i = "))
		t = float(input("Cuantos años ahorrarás, t = "))
		m = int(input("""Elige el número segun el tipo de capitalización:
			mensual.........(12)
			bimestral.......(6)
			trimestral......(4)
			cuatrimestral...(3)
			semestral.......(2)
			anual...........(1)
			"""))
		k = 12/m
		n = 12*t/k
		i = ii/(100*m)
		P = A*((1+i)-(1+i)**(1-n))/i
		print("P = ${:,}\nA = ${:,}\ni = {}%\nn = {}".format(round(P,2),round(A,2),ii,n))
	elif tipo == "A":
		opcion = str(input("¿Conoces F o P? "))
		if opcion == "F":
			F = float(input("Valor del Monto Acumulado, F = $"))
			ii = float(input("Tasa de interés, i = "))
			t = float(input("Cuantos años ahorrarás, t = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			k = 12/m
			n = 12*t/k
			i = ii/(100*m)
			A = F*i/((1+i)**(n+1)-(1+i))
			print("A = ${:,}\nF = ${:,}\ni = {}%\nn = {}".format(round(A,2),round(F,2),ii,n))
		elif opcion == "P":
			P = float(input("Valor Presente, P = $"))
			ii = float(input("Tasa de interés, i = "))
			t = float(input("Cuantos años ahorrarás, t = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			k = 12/m
			n = 12*t/k
			i = ii/(100*m)
			A = P*i/((1+i)-(1+i)**(1-n))
			print("A = ${:,}\nP = ${:,}\ni = {}%\nn = {}".format(round(A,2),round(P,2),ii,n))
	elif tipo == "n":
		import math
		opcion = str(input("¿Conoces F o P? "))
		if opcion == "F":
			F = float(input("Valor del Monto Acumulado, F = $"))
			A = float(input("Valor de la anualidad, A = $"))
			ii = float(input("Tasa de interés, i = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			i = ii/(100*m)
			n = math.log10(F*i/(A*(1+i))+1)/math.log10(1+i)
			n1 = n - int(n)
			A2 = n1*A
			print("Pagarás {} anualidades de A = ${:,} y la última de ${:,}".format(int(n),A,round(A2,2)))
			print("n = {}\nF = ${:,}\ni = {}%\nA = ${:,}".format(round(n,4),round(F,2),ii,round(A,2)))
		elif opcion == "P":
			P = float(input("Valor Presente, P = $"))
			A = float(input("Valor de la anualidad, A = $"))
			ii = float(input("Tasa de interés, i = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			i = ii/(100*m)
			n = -math.log10(1-P*i/(A*(1+i)))/math.log10(1+i)
			n1 = n - int(n)
			A2 = n1*A
			print("Pagarás {} anualidades de A = ${:,} y la última de ${:,}".format(int(n),A,round(A2,2)))
			print("n = {}\nP = ${:,}\ni = {}%\nA = ${:,}".format(round(n,4),round(P,2),ii,round(A,2)))
	elif tipo == "i":
		opcion = str(input("¿Conoces F o P? "))
		if opcion == "F":
			F = float(input("Valor del Monto Acumulado, F = $"))
			A = float(input("Valor de la anualidad, A = $"))
			t = float(input("Cuantos años ahorrarás, t = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			k = 12/m
			n = 12*t/k
			f = 1
			i = 0
			while f <= F:
				i = i + 0.000001
				f = A*((1+i)**(n+1)-(1+i))/i
			ii = i*1200
			print("i% = {}%\nF = ${:,}\nf = ${:,}\nn = {}\ni = {}\nA = ${:,}".format(round(ii,2),round(F,2),round(f,2),n,i,A))
		elif opcion == "P":
			P = float(input("Valor Presente, P = $"))
			A = float(input("Valor de la anualidad, A = $"))
			t = float(input("Cuantos años ahorrarás, t = "))
			m = int(input("""Elige el número segun el tipo de capitalización:
				mensual.........(12)
				bimestral.......(6)
				trimestral......(4)
				cuatrimestral...(3)
				semestral.......(2)
				anual...........(1)
				"""))
			k = 12/m
			n = 12*t/k
			p = 1
			i = 0
			while p <= P:
				i = i + 0.000001
				p = A*((1+i)-(1+i)**(1-n))/i
			ii = i*1200
			print("i% = {}%\nP = ${:,}\np = ${:,}\nn = {}\ni = {}\nA = ${:,}".format(round(ii,2),round(P,2),round(p,2),n,i,A))

	elif tipo == "S":
		Monto = float(input("Monto del prestamo = $"))
		NumCuotas = float(input("Número de cuotas = "))
		TM = float(input("Tasa de interés mensual sin Iva = "))
		TM=TM/100
		I2=TM*(1+0.16)
		I3=I2+1
		I4=I3**-NumCuotas
		I2xMonto=I2*Monto
		UnoMenossI4=1-I4
		MMensual =I2xMonto/UnoMenossI4
		print("Monto mensual a pagar $",MMensual)
