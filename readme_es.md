# Tubify

## Versiones en Idiomas
[![Inglés](https://img.shields.io/badge/Inglés-English-blue)](readme.md)
[![Alemán](https://img.shields.io/badge/Alemán-German-blue)](readme_de.md)
[![Español](https://img.shields.io/badge/Español-Spanish-blue)](readme_es.md)

## Resumen

Tubify es una utilidad basada en Python que permite a los usuarios trabajar tanto con Spotify como con YouTube, lo que facilita la obtención y descarga de listas de canciones de las listas de reproducción de Spotify y la descarga de audio de las listas de reproducción o videos de YouTube. Es una herramienta versátil para los entusiastas de la música que desean crear colecciones offline de sus canciones favoritas.

## Implementaciones Prácticas

En un mundo donde la música es una parte esencial de nuestras vidas, nuestra utilidad ofrece una alternativa económica para disfrutar de tus canciones favoritas sin la necesidad de suscripciones premium. Aquí tienes algunas implementaciones prácticas:

- **Escucha sin conexión**: Puedes guardar tus canciones preferidas directamente en tu dispositivo, eliminando la necesidad de una conexión a Internet constante y reduciendo el uso de datos.

- **Colecciones personales**: Crea tu propia colección personalizada de canciones de diversas plataformas para disfrutar sin conexión. No más dependencia de servicios de streaming con disponibilidad limitada.

- **Copia de seguridad y redundancia**: Mantén una copia de seguridad de tu música querida en caso de que se elimine o no esté disponible en las plataformas de streaming. Tu música, bajo tu control.

- **Experiencia sin anuncios**: Di adiós a las interrupciones de los anuncios durante tus sesiones de música. La música descargada significa una experiencia de escucha ininterrumpida.

- **Mixtapes personalizados**: Crea tus propias mixtapes o listas de reproducción personalizadas eligiendo tus canciones favoritas y organizándolas a tu gusto.

Nuestra utilidad te permite tomar el control de tu experiencia musical, ofreciendo una forma más flexible y personalizada de disfrutar de la música a tu manera.

## Cómo Utilizar

1. **Requisitos previos**:
   - Python instalado en tu sistema.
   - Instala las bibliotecas requeridas: `spotipy`, `youtubesearchpython`, `pytube` y `moviepy`.

2. **Obtención de Credenciales de API**:
   - Si planeas utilizar la funcionalidad de Spotify, necesitas obtener credenciales de la API de Spotify.
   - Si trabajas con YouTube, no necesitas una clave de API.

3. **Configuración de Credenciales de API**:
   - Para utilizar la funcionalidad de Spotify, debes obtener credenciales de la API de Spotify, que incluyen un **ID de Cliente** y un **Secreto de Cliente**. Sigue estos pasos para obtenerlos:

     1. **Crea una cuenta de desarrollador de Spotify**:
        - Visita el sitio web de [Spotify for Developers](https://developer.spotify.com/dashboard/).
        - Inicia sesión o crea una cuenta de Spotify si aún no la tienes.

     2. **Crea una nueva aplicación de Spotify**:
        - Una vez iniciada la sesión, ve al Panel de Desarrolladores de Spotify.
        - Haz clic en el botón "Crear una aplicación" o "Crear un ID de Cliente".
        - Completa la información requerida para tu aplicación, como su nombre y descripción.
        - Es posible que se te solicite que aceptes los términos y condiciones para desarrolladores.

     3. **Obtén tus credenciales**:
        - Después de crear la aplicación, se te proporcionará un **ID de Cliente** y un **Secreto de Cliente**.
        - Reemplaza `YOUR_SPOTIFY_CLIENT_ID` y `YOUR_SPOTIFY_CLIENT_SECRET` en el código con las credenciales que recibiste.

   - Si utilizas la utilidad únicamente para tareas relacionadas con YouTube, puedes omitir este paso, ya que la funcionalidad de YouTube no requiere credenciales de API.

4. **Ejecución de la Herramienta**:
   - Ejecuta el script de Python.
   - Se te pedirá que ingreses una URL de lista de reproducción de Spotify o YouTube.
   - La utilidad identificará el tipo de URL y realizará la acción correspondiente:
     - Para listas de reproducción de Spotify, obtendrá los nombres de las canciones y las descargará desde YouTube.
     - Para listas de reproducción de YouTube, descargará el audio de cada video.
     - Para videos de YouTube, descargará directamente el audio.

5. **Salida**:
   - Las canciones o archivos de audio se guardarán en el directorio especificado (`save_directory`).

6. **¡Disfruta!**:
   - Ahora puedes disfrutar de tu música descargada sin conexión o para cualquier otro propósito.

## Nota

- Ten en cuenta los términos de uso y las restricciones de derechos de autor al descargar contenido de plataformas en línea como Spotify y YouTube. Respeta los derechos de los creadores de contenido y cumple con todas las regulaciones legales.

## Licencia

Este proyecto está bajo la [Licencia Pública General de GNU, versión 3.0](LICENSE). Puedes encontrar el texto completo de la licencia [aquí](https://www.gnu.org/licenses/gpl-3.0.html).
