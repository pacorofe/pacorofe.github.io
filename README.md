# Atlas

Atlas interactivos sobre mis aficiones, publicados con GitHub Pages.

| Atlas | Ruta |
|---|---|
| Atlas Geopolítico 2026 | `/geopolitica/` |
| Atlas de la fotografía | `/fotografia/` |
| Atlas de la libre improvisación | `/improvisacion/` |

## Ver en local

```bash
python3 -m http.server 8000
# abre http://localhost:8000/
```

## Publicar

1. Crea en GitHub un repositorio **público** llamado `<tu-usuario>.github.io`.
2. Sube este contenido a la rama `main`.
3. Ve a **Settings → Pages**, elige *Deploy from a branch*, rama `main` y carpeta `/ (root)`.
4. En uno o dos minutos estará en `https://<tu-usuario>.github.io/`.

## Páginas privadas

GitHub Pages gratis es siempre público. Para los atlas que no quieras publicar:

- guárdalos en una carpeta `privado/` incluida en `.gitignore` (solo viven en tu Mac), o
- mantenlos en un repositorio privado aparte, sin Pages.
