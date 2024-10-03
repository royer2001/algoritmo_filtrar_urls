import random

# Función para generar una URL aleatoria
def generate_url():
    # Lista de dominios y subdominios de ejemplo
    domains = ['shoponline', 'myshop', 'bestbuy', 'example', 'supermarket', 'techshop', 'ecommerce', 'mywebsite', 'webshop']
    extensions = ['.com', '.net', '.org', '.io']
    paths = ['/index.html', '/products.html', '/about.html', '/contact.html', '/home.html', '/profile.html', '/services.html']
    invalid_paths = ['/index.php', '/products', '/about', '/contact.jsp', '/home', '/profile', '/services']
    
    # Seleccionar aleatoriamente un dominio, una extensión y un path
    domain = random.choice(domains)
    extension = random.choice(extensions)
    
    # Decidir si generamos una URL válida o no
    if random.random() > 0.5:
        path = random.choice(paths)  # URL válida
    else:
        path = random.choice(invalid_paths)  # URL no válida
    
    return f"http://www.{domain}{extension}{path}"

# Generar URLs y guardarlas en un archivo de texto
def generate_urls_file(filename, num_urls=100):
    with open(filename, 'w') as file:
        for _ in range(num_urls):
            url = generate_url()
            file.write(url + "\n")

# Llamada para generar el archivo con 100 URLs
generate_urls_file('urls.txt', num_urls=100)
