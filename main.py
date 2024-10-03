def filter_urls(input_file):
    unique_urls = set()

    
    with open(input_file, 'r') as file:
        for line in file:
            url = line.strip()  # Eliminar espacios en blanco alrededor
            # Comprobar si la URL cumple con los criterios
            if "shop" in url and url.endswith(".html"):
                unique_urls.add(url)  # Agregar la URL al conjunto set


    print("URLs que cumplen con los criterios:")
    for url in unique_urls:
        print(url)

    print(f"Número total de URLs únicas: {len(unique_urls)}")

# Llamar a la función con el nombre de tu archivo
filter_urls('urls.txt')
