#Capitulo 4. Ejercicio resuelto 12

NOM = input("Ingrese su nombre: ")
NHT = int(input("Ingrese el número de horas semanales trabajadas: "))
VHN = float(input("Ingrese el valor por hora normal trabajada: "))

if NHT > 40:
    HET = NHT - 40
    if HET > 8:
        HEE8 = HET - 8
        PHE = VHN * 2 * 8 + VHN * 3 * HEE8
    else:
        PHE = VHN * 2 * HET
    SALARIO = VHN * 40 + PHE
else:
    SALARIO = NHT * VHN

print(f"EL TRABAJADOR {NOM} DEVENGÓ ${SALARIO}")
                
