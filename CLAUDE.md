# Atlas de aficiones: instrucciones para Claude

Este repositorio es un sitio estático de GitHub Pages con varios **atlas interactivos**
sobre las aficiones de Paco. Cada atlas es una página HTML autocontenida (HTML + CSS + JS
en un único `index.html`, sin build; solo Google Fonts y, en geopolítica, d3/topojson
guardados en `geopolitica/vendor/`).

Se publica en `https://<usuario>.github.io/` desde la rama `main`, carpeta `/`.

## Estructura

```
index.html               Portada: una tarjeta por atlas
geopolitica/index.html   Atlas Geopolítico 2026: mapa mundial SVG + panel de fichas
fotografia/index.html    Atlas de la fotografía: corrientes como tira de contactos
improvisacion/index.html Atlas de la libre improvisación: corrientes como partitura gráfica
.nojekyll                Desactiva Jekyll: se sirve el HTML tal cual
geopolitica/vendor/      d3 7.9.0 y topojson-client 3.1.0 en local (sin depender de CDNs)
scripts/sync_artifact.py Copia un atlas desde su artifact de Claude al repo
```

## Reglas de trabajo

- **Idioma**: todo el contenido en español de España.
- **Autocontenido**: cada atlas es un único `index.html`. Nada de frameworks, bundlers ni
  peticiones a APIs: los datos viven en constantes JS dentro de la página.
- **Dónde están los datos**: cada atlas tiene un bloque de datos marcado con comentarios
  (`/* ===== DATOS ... */`, `const CORRIENTES = [...]`, `FICHAS`, etc.). Para añadir
  autores, discos, libros, países o corrientes, edita esos bloques respetando el formato
  que documentan los propios comentarios; no toques el código de renderizado si no hace falta.
- **Edición**: archivos grandes (el de geopolítica pasa de 600 KB). Edita con reemplazos
  precisos, nunca reescribiendo el archivo entero.
- **Familia visual**: fotografía e improvisación comparten tipografías (Syne, Source Serif 4,
  IBM Plex Mono) y estructura (filtros, línea de tiempo, ficha, índice, panel lateral).
  Un atlas nuevo debería seguir esa misma familia. Todos soportan modo claro y oscuro.
- **Notas personales**: los atlas guardan notas en `localStorage`; eso es por navegador y
  no se sube al repo.
- **Atlas nuevo**: crea `<nombre>/index.html` y añade su tarjeta a la portada `index.html`
  (número, título, descripción de una o dos frases, color propio y un pequeño SVG).
- **Verificación**: tras cada cambio, abre la página (por ejemplo con
  `python3 -m http.server 8000` y `http://localhost:8000/`) y comprueba que no hay errores
  en consola.
- **Git**: mensajes de commit cortos en español, del tipo `fotografia: añade Saul Leiter`.

## Atlas Geopolítico: actualización semanal

Una tarea programada revisa la actualidad cada viernes a las 17:00 (Madrid), republica el
artifact del atlas en Claude y después copia el resultado aquí con
`scripts/sync_artifact.py` y hace push a `main`. El artifact es la fuente original;
`geopolitica/index.html` es una copia, así que no lo edites a mano: tus cambios se
perderían en la siguiente actualización. Pide los cambios sobre el artifact.

## Visibilidad

En el plan gratuito de GitHub, Pages publica todo lo que hay en el repo y el repo debe ser
público. No pongas aquí nada privado. Las páginas privadas van en otro sitio (ver README).
