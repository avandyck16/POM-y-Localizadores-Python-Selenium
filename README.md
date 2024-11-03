# Page Object Methods - Selenium
## Axel Van Dyck

Este proyecto contiene prácticas de automatización en Python utilizando Selenium y el modelo Page Object Model (POM) para manejar una página tipo red social. 
Los archivos y clases están estructurados para manejar acciones clave en la página, como registro de usuario, inicio de sesión, subida y eliminación de publicaciones, y otras interacciones web.

## Estructura del Proyecto

El proyecto se compone de aproximadamente 5 archivos, cada uno diseñado para representar diferentes secciones y funcionalidades de la página. A continuación, se describen las principales clases y métodos incluidos.

### Clases y Métodos Principales

1. **Clases de atributos de objeto
   - Representa la página.
   - **Inicializadores**
   - **Atributos (Localizadores)**
   - **Métodos**
   
2. **Clases de pruebas con @classmethod**
   - Clase de pruebas que utiliza Selenium WebDriver
   - **Métodos**:
     - `setup_class()`: Método de configuración que abre el navegador y navega a la URL de registro (`https://around-v1.nm.tripleten-services.com/signup`), y crea una instancia de `RegistrationPageAround`.
     - `test_methods()`: Métodos de pruebas automatizadas.
     - `teardown_class()`: Método de limpieza que cierra el navegador al finalizar la prueba.

## Funcionalidades Implementadas

Este proyecto incluye varias prácticas y funcionalidades para interactuar con elementos web en la página de red social, como:

- Registro de nuevos usuarios.
- Interacción con elementos Web.
- Inicio de sesión y autenticación.
- Localización de elementos web en las herramientas de desarrollo.
- Subida de fotos.
- Eliminación de publicaciones.

## Estructura del Código

- **Page Object Model (POM)**: Cada página de la aplicación está representada por una clase, y cada clase contiene los métodos específicos para interactuar con los elementos de esa página.
- **Uso de Localizadores y Esperas**: Se utilizan localizadores para acceder a los elementos, y se aplican esperas explícitas (`WebDriverWait`) para asegurar que los elementos estén presentes antes de interactuar con ellos.
- **Modularidad**: Cada funcionalidad está implementada en su propia clase y archivo, lo que permite un código más limpio y organizado.

### Este proyecto busca mejorar mis habilidades de automatización con Selenium, Python, y Selenium IDE, y trabajar con localizadores y también solicitudes en caso de ser necesario, para hacer pruebas.
