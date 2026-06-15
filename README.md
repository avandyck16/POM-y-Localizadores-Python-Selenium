# Page Object Model Framework with Selenium WebDriver (Python)
### Axel Van Dyck

---

## 📌 Descripción del Proyecto

Este proyecto contiene prácticas de automatización de pruebas UI desarrolladas en **Python utilizando Selenium WebDriver**, aplicando el patrón de diseño **Page Object Model (POM)**.

Forma parte de los ejercicios realizados durante el programa de formación de TripleTen, con el objetivo de fortalecer habilidades en automatización de pruebas y diseño de frameworks básicos de testing.

El enfoque principal es la automatización de flujos funcionales en una aplicación tipo red social, simulando interacciones reales de usuario.

---

## 🏗️ Estructura del Proyecto

El proyecto está compuesto por aproximadamente 5 archivos, organizados para representar páginas, localizadores y casos de prueba.

Esta estructura busca mantener el código modular, legible y fácil de mantener.

---

## 🧱 Arquitectura del Framework

### 📄 Page Object Model (POM)

Se implementa el patrón **Page Object Model**, donde:

- Cada página de la aplicación se representa como una clase independiente
- Las clases encapsulan localizadores y métodos de interacción
- Se separa la lógica de la UI de la lógica de pruebas
- Se reduce la duplicación de código y se mejora la mantenibilidad

---

### 🧪 Estructura de Pruebas

Las pruebas están organizadas utilizando clases con `@classmethod`, manejando el ciclo de vida de ejecución:

#### 🔧 setup_class()
- Inicializa el WebDriver
- Abre el navegador
- Navega a la URL de registro:
  `https://around-v1.nm.tripleten-services.com/signup`
- Inicializa las Page Objects necesarias

#### ▶️ test_methods()
- Ejecuta los escenarios de prueba automatizados
- Valida flujos funcionales principales de la aplicación

#### 🧹 teardown_class()
- Cierra el navegador al finalizar la ejecución de las pruebas

---

## 🧪 Funcionalidades Automatizadas

- Registro de nuevos usuarios
- Inicio de sesión (login)
- Interacción con elementos de la interfaz web
- Localización de elementos en el DOM
- Subida de imágenes
- Eliminación de publicaciones
- Validación de comportamiento de la aplicación

---

## ⏳ Estrategia de Automatización

- Uso de localizadores para identificar elementos del DOM
- Implementación de esperas explícitas con `WebDriverWait`
- Manejo de elementos dinámicos para evitar fallos de sincronización
- Validación de estados antes de ejecutar acciones

---

## 🧠 Objetivo de Aprendizaje

Este proyecto tiene como objetivo reforzar habilidades en:

- Automatización de pruebas UI con Selenium WebDriver
- Implementación del patrón Page Object Model (POM)
- Organización de frameworks de testing básicos
- Manejo de localizadores en el DOM
- Construcción de flujos de prueba automatizados

---

## 📊 Conclusión

Este proyecto representa una práctica estructurada de automatización UI enfocada en el uso del patrón Page Object Model para mejorar la organización del código.

La separación entre lógica de pruebas y lógica de interacción con la interfaz permite mejorar la claridad, escalabilidad y mantenibilidad del framework.
