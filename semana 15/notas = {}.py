notas = {}

notas["Carla"] = 4.5
notas["Isaias"] = 3.8
notas["Lilia"] = 5.0

print("Lista de estudiantes y notas:")
for nombre, nota in notas.items():
    print(f"{nombre}: {nota}")

buscar = input("\nEscribe el nombre del estudiante a buscar: ")
if buscar in notas:
    print(f"{buscar} tiene nota {notas[buscar]}")
else:
    print(f"{buscar} no esta registrado")