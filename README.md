# Analizador de Texto con Estadísticas

Este proyecto es una **aplicación de consola en Python** que permite analizar textos ingresados manualmente o desde un archivo.  
Genera estadísticas detalladas como **número de palabras, caracteres y palabras más frecuentes**.

---

## Características principales

- Ingreso de texto por consola o desde archivo.  
- Conteo de caracteres con y sin espacios.  
- Detección de la palabra más larga.  
- Frecuencia de palabras (las 10 más comunes).  
- Limpieza automática de signos de puntuación.  
- Interfaz sencilla y totalmente en consola.

---

## Tecnologías utilizadas

- **Python 3**: Lenguaje principal.  
- **string**: Limpieza de puntuación.  
- **collections.Counter**: Cálculo de frecuencias de palabras.

---

## Cómo ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/alanaquino72/analizador-texto-estadistica-python.git
   ```

2. Ejecuta el script:
   ```bash
   python analizador_texto_estadistica.py
   ```
   
---

## Estructura del proyecto

```bash
analizador-texto-estadistica-python
├── analizador_texto_estadistica.py   # Lógica principal del analizador.
└── README.md                         # Documentación del proyecto.
```

---

## Ejemplo de salida

```bash
ANALIZADOR DE TEXTOS CON ESTADÍSTICAS

Opciones de entrada:
1. Ingresar texto por consola.
2. Cargar texto desde archivo.
3. Salir.

ESTADÍSTICAS
Caracteres totales (con espacios): 124
Caracteres totales (sin espacios): 98
Total de palabras: 20
Palabra más larga: estadística (12 caracteres)

Palabras más frecuentes:
de: 3 ocurrencias
texto: 2 ocurrencias
análisis: 2 ocurrencias
```

---

## Autor

**Alan Aquino.**
Estudiante de Ingeniería en Informática.


---

## Licencia

Este proyecto se distribuye bajo la Licencia MIT.
Puedes usarlo, modificarlo y compartirlo dando el crédito correspondiente.
