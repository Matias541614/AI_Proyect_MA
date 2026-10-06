# Portafolio de Evidencias: Sistema de Recomendación con IA

Este repositorio documenta el paso a paso del desarrollo de un sistema de recomendación en Python, desde la creación del entorno de trabajo hasta la codificación asistida por Inteligencia Artificial y el control de versiones en la nube.

## Fase 1: Creación del Repositorio en GitHub
El proyecto inició en la plataforma web de GitHub con la creación de un nuevo repositorio vacío destinado a alojar el código fuente.

Se ingresó al panel principal y se inició el proceso de creación.
![Paso 1](captura1.jpeg)

Se definió la configuración inicial del repositorio en la plataforma.
![Paso 2](captura2.jpeg)

Se asignó el nombre `AI_Proyect_MA` y se estableció la visibilidad del proyecto.
![Paso 3](captura3.jpeg)

Se confirmaron los detalles estructurales antes de finalizar la creación.
![Paso 4](captura4.jpeg)

El repositorio remoto quedó creado exitosamente, listo para ser conectado al entorno local.
![Paso 5](captura5.jpeg)

---

## Fase 2: Autenticación en Visual Studio Code
Para trabajar localmente, se abrió Visual Studio Code y se procedió a vincular la cuenta de GitHub con el editor de código.

Se inició el proceso de clonación desde la interfaz de bienvenida del editor.
![Paso 6](captura6.jpeg)

El sistema detectó la necesidad de iniciar sesión en GitHub para obtener los permisos de acceso.
![Paso 7](captura7.jpeg)

Se seleccionó el método de autenticación a través del navegador.
![Paso 8](captura8.jpeg)

Visual Studio Code generó un código de autenticación de dispositivo (Device Authentication) para garantizar una conexión segura.
![Paso 9](captura9.jpeg)

Se ingresó el código `0240-B8F2` en el portal de autorización de GitHub.
![Paso 10](captura10.jpeg)

La plataforma web confirmó que el dispositivo quedó autorizado y conectado correctamente al entorno local.
![Paso 11](captura11.jpeg)

---

## Fase 3: Clonación del Repositorio Local
Con la cuenta autenticada, se utilizó la terminal de Visual Studio Code para descargar el repositorio.

Se ejecutó el comando `git clone https://github.com/Matias541614/AI_Proyect_MA.git`. El sistema comenzó a enumerar y recibir los objetos del repositorio remoto.
![Paso 12](captura12.jpeg)

Una vez completada la descarga sin errores, se navegó hacia el interior de la carpeta del proyecto utilizando el comando `cd AI_Proyect_MA`.
![Paso 13](captura13.jpeg)

---

## Fase 4: Estructuración del Proyecto
Dentro de la carpeta vinculada, se preparó el entorno para comenzar a escribir la lógica de programación.

Se abrió el explorador de archivos de Visual Studio Code para visualizar el contenido de la carpeta.
![Paso 14](captura14.jpeg)

Se creó un nuevo archivo en blanco denominado `recommendation_system.py`, el cual alojaría el código de la actividad.
![Paso 15](captura15.jpeg)

---

## Fase 5: Desarrollo Asistido por GitHub Copilot
El desarrollo del script se realizó mediante "prompts" estructurados como comentarios en Python, permitiendo que la Inteligencia Artificial generara la lógica del sistema.

Se redactaron las instrucciones iniciales, se importó la librería `math` y se declaró la clase principal `SistemaRecomendacion`.
![Paso 16](captura16.jpeg)

Copilot generó el método constructor `__init__`, incluyendo un diccionario complejo de pruebas con 5 usuarios y sus respectivas calificaciones del 1 al 5 en diversas películas.
![Paso 17](captura17.jpeg)

Se generó automáticamente el método `calcular_similitud`, el cual extrae las calificaciones e implementa la fórmula matemática de similitud del coseno para encontrar afinidades entre dos perfiles.
![Paso 18](captura18.jpeg)

La IA sugirió el método `recomendar_peliculas`. Este bloque itera sobre el resto de los usuarios, evalúa las similitudes y filtra las películas que el usuario original aún no ha visto, ordenándolas por puntaje para devolver las 2 mejores opciones.
![Paso 19](captura19.jpeg)

Finalmente, se instanció la clase y se creó el bloque de prueba final para imprimir por pantalla las recomendaciones para el `usuario1`, cerrando la codificación del archivo.
![Paso 20](captura20.jpeg)

---

## Fase 6: Control de Versiones y Subida (Git Push)
Con el código finalizado y verificado, se procedió a empaquetar los cambios y subirlos a la nube mediante comandos de terminal.

En el panel izquierdo, el archivo apareció marcado con la letra "U" (Untracked), indicando que Git aún no realizaba seguimiento de los cambios.
![Paso 21](captura21.jpeg)

Se ejecutó el comando `git add .` para agregar los archivos modificados al área de preparación (staging).
![Paso 22](captura22.jpeg)

Se preparó el comando de confirmación para empaquetar el trabajo con un mensaje descriptivo.
![Paso 23](captura23.jpeg)

Se ejecutó exitosamente el comando `git commit -m "Sistema de recomendacion completado"`, registrando 1 archivo cambiado y 54 inserciones de código.
![Paso 24](captura24.jpeg)

Para concluir el proceso, se ejecutó `git push`. La terminal confirmó la escritura y transferencia de datos hacia la rama `main` del repositorio remoto `https://github.com/Matias541614/AI_Proyect_MA.git`, sincronizando de forma exitosa el entorno local con la nube.
![Paso 25](captura25.jpeg)