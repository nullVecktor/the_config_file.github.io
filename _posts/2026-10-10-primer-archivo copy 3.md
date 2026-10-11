---
layout: post
title: "Primer archivo: cómo funciona este blog"
date: 2026-10-10 12:00:00 +0000
category: "WEB / SETUP"
description: "Una guía rápida para entender la estructura de THE_CONFIG_FILE y publicar nuevos artículos."
---

Bienvenido a **THE_CONFIG_FILE**. Este blog se genera a partir de archivos Markdown y se publica mediante GitHub Pages.

## Publicar una entrada

1. Crea un archivo dentro de la carpeta `_posts`.
2. Usa el formato de nombre `AAAA-MM-DD-titulo.md`.
3. Añade un bloque de metadatos al principio, entre dos líneas de tres guiones.
4. Escribe el contenido en Markdown y guarda los cambios.

Ejemplo:

```markdown
---
layout: post
title: "Mi nueva entrada"
date: 2026-10-10 13:00:00 +0000
category: "REDES"
description: "Qué aprenderás en esta guía."
---

## Introducción

Escribe aquí tu artículo.
```

Al subir los cambios a la rama `main`, GitHub Actions construirá y publicará la web automáticamente.

> Consejo: no guardes contraseñas, tokens, claves API ni datos privados en un repositorio público.
