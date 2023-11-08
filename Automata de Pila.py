def validate(value):
	flag = 0
	for x in value:
		if x != "0" and x != "1":
			flag = 1
	if flag == 1:
		print ("Esta palabra no es valida")
	else:
		pos = value.find("1")
		unos = value[pos: ]
		ceros = value[:pos]
		for y in unos:
			if y == "0":
				print ("Esta palabra no es valida")
				break
		if len(unos) != len(ceros):
			print ("Esta palabra no es valida")
		

def check_automata(value):
    pila = ["$"]
    alfabeto_pila = "ε"
    print("Palabra del alfabeto: ", value)
    print("Estado inicial de la pila: ", pila)
    
    for i in value:
        if i == "0":
            pila.append(alfabeto_pila)
            print("Se lee un", i, "en la pila y se INSERTA ε")
            print("pila:", pila)
        elif i == "1":
            if pila[-1] == "ε":
                pila.pop()
                print("Se lee un", i, "en la pila y se EXTRAE ε")
                print("pila:", pila)
            else:
                print("Error: No se puede extraer ε de una pila no vacía.")
                return

    if pila == ["$"] and "0" in value and "1" in value:
        print("La palabra es válida según el autómata de pila.")
    else:
        print("La palabra no es válida según el autómata de pila.")

								
print ("Automata de pila de la forma: P ={Q, Σ, Γ, q0, Z0, δ, F}, con Q = {q0, q1, q2}, Σ = {0, 1}, Γ = {X, Z0}, F = {q2}")
print ("Alfabeto de la pila = {$,ε}")
print ('''Funcion de transicion:
	δ(q0, 0, Z0) = (q0, XXZ0),
        δ(q0, 0, X) = (q0, XX),
        δ(q0, 1, X) = (q1, ε),
        δ(q1, 1, X) = (q1, ε),
        δ(q1, ε, Z0) = (q2, Z0).''')
print('Escriba exit para finalizar')

while True:
	valores = input("Escriba los valores:")
	if valores == "exit":
		break
	else:
		validate(valores)
		check_automata(valores)