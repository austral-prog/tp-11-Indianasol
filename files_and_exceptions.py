def read_file_to_dict(filename):
    ventas = dict()
    with open(filename, 'r') as archivo:
        linea = archivo.read().strip()
        if not linea:
            return ventas

        pares = linea.split(';')
        for par in pares:
            if par:
                producto, valor = par.split(':')
                valor = float(valor)
                if producto in ventas:
                    ventas[producto].append(valor)
                else:
                    ventas[producto] = [valor]
    return ventas





def process_dict(data):
    for producto in data:
        ventas = data[producto]
        total = sum(ventas)
        promedio = total / len(ventas)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")

