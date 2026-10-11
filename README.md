# THE_CONFIG_FILE

Blog estático con Jekyll, Markdown, GitHub Pages y GitHub Actions.

## Publicar en GitHub Pages

1. Crea un repositorio público llamado `TU_USUARIO.github.io` (sustituye TU_USUARIO por tu usuario exacto de GitHub).
2. Sube todos los archivos y carpetas de este proyecto a la raíz de la rama `main`.
3. Abre **Settings → Pages** en el repositorio.
4. En **Build and deployment → Source**, selecciona **GitHub Actions**.
5. Abre la pestaña **Actions** y espera a que el flujo `Deploy THE_CONFIG_FILE to GitHub Pages` termine correctamente.
6. La web quedará publicada en `https://TU_USUARIO.github.io`.

## Importante: ajustar la URL

Edita `_config.yml` y cambia `TU_USUARIO` por tu usuario real de GitHub. En un repositorio llamado `usuario.github.io`, `baseurl` debe permanecer vacío.

## Crear un artículo

Crea `_posts/AAAA-MM-DD-titulo-corto.md`. Incluye al principio:

```yaml
---
layout: post
title: "Título del artículo"
date: 2026-10-10 14:00:00 +0000
category: "REDES"
description: "Breve resumen del artículo."
---
```

Escribe el cuerpo en Markdown. Al guardar y subir el cambio a `main`, GitHub Actions lo publicará.

## Estructura

- `_layouts/`: plantillas compartidas y de artículo.
- `_posts/`: entradas Markdown.
- `assets/css/style.css`: tema y diseño responsive.
- `assets/js/main.js`: mejoras progresivas.
- `.github/workflows/pages.yml`: compilación y despliegue automático.

La ilustración de la capucha está dibujada en SVG dentro de `index.html`, así que no depende de una imagen externa.
