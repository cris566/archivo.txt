def contar_letras_y_espacios(contador.txt):
    contador_letras = 0
    contador_espacios = 0
        
    for caracter in contador.txt:
        if caracter.isalpha():  # Verifica si es una letra
            contador_letras += 1
        elif caracter.isspace():  # Verifica si es un espacio
            contador_espacios += 1
    return contador_letras, contador_espacios

def resumen_contador(contador_letras, contador_espacios):
    resumen = f"Resumen del conteo:\nLetras: {contador_letras}\nEspacios: {contador_espacios}"
    return resumen


nombre_archivo_entrada = 'contador.txt'
nombre_archivo_salida = 'resumen.txt'

    # Lectura del archivo de entrada
with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
    # with open(nombre_archivo_entrada, 'r', encoding='utf-8') as archivo:
    contenido = archivo.read()
    
    # Contar letras y espacios en el contenido del archivo 
    letras, espacios = contar_letras_y_espacios(contenido)

    # Crear el resumen
    resumen = resumen_contador(letras, espacios)

    # Escribir el resumen en el archivo de salida
with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
    archivo.write(resumen)
    print(f"El resumen ha sido guardado en '{nombre_archivo_salida}'.")

   

    

