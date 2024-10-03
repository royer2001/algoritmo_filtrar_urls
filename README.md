# Proyecto: Filtrado de URLs

Este proyecto consiste en dos partes principales:

1. **Generación de URLs aleatorias** para crear un archivo de texto que contiene al menos 100 URLs.
2. **Filtrado y procesamiento de URLs** para encontrar aquellas que pertenecen a dominios que contienen la palabra "shop" y que terminan con la extensión `.html`, eliminando duplicados y contando el número de URLs válidas.

## Requisitos

- Python 3.x

## Estructura del Proyecto

```
├── generate_urls.py      # Script para generar URLs aleatorias
├── main.py               # Script para filtrar URLs según criterios
├── urls.txt              # Archivo generado con URLs aleatorias (se genera al ejecutar generate_urls.py)
├── README.md             # Documentación del proyecto
```

## Instrucciones

### 1. Generar URLs Aleatorias

El archivo `generate_urls.py` genera un archivo `urls.txt` con al menos 100 URLs aleatorias, de las cuales algunas cumplirán con los criterios del problema (dominios que contienen "shop" y terminan en `.html`).

#### Ejecución:

```bash
python generate_urls.py
```

Este comando generará el archivo `urls.txt` con 100 URLs aleatorias.

### 2. Filtrar URLs

El archivo `main.py` toma el archivo `urls.txt` como entrada y filtra las URLs que cumplen con los siguientes criterios:

- El dominio contiene la palabra "shop".
- La URL termina con la extensión `.html`.
- Se eliminan las URLs duplicadas.

Además, el script cuenta y muestra el número total de URLs únicas que cumplen con estos criterios.

#### Ejecución:

```bash
python main.py
```

Este comando mostrará las URLs que cumplen con los criterios y el número total de URLs únicas que cumplen con los requisitos.

### 3. Estructura de las URLs Generadas

Las URLs generadas son aleatorias y pueden tener la siguiente estructura:

- Válidas: 
  - `http://www.shoponline.com/index.html`
  - `http://www.myshop.net/products.html`
- No válidas:
  - `http://www.example.com/index.php`
  - `http://www.bestbuy.io/about`

Las URLs válidas son aquellas que contienen "shop" en el dominio y terminan en `.html`.

## Ejemplo de Salida

Si ejecutas `main.py`, obtendrás una salida como la siguiente:

```bash
URLs que cumplen con los criterios:
http://www.shoponline.com/products.html
http://www.techshop.net/about.html
...
[Más datos]

Número total de URLs únicas: 10
```