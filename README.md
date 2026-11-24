# IMECTEC – Sitio web

Sitio estático publicado con GitHub Pages en **https://imectec.com**.

## Estructura

| Ruta | Contenido |
|---|---|
| `index.html` | Página principal |
| `tableros-electricos/`, `mantenimiento-electrico/`, `subestaciones/`, `automatizacion-plc-scada/`, `variadores-de-frecuencia/` | Páginas por servicio (para Google y Google Ads) |
| `politica-de-privacidad/` | Política de privacidad (Ley N.° 29733) |
| `404.html` | Página de error |
| `css/main.css` | Estilos compilados (Tailwind, minificado) |
| `js/main.js` | Menú, videos, formulario → WhatsApp y medición (GA4 / Ads) |
| `images/`, `videos/` | Imágenes y videos originales. `images/web/` y `videos/video2-web.mp4` son copias livianas de las mismas fotos/video que usa la web |
| `sitemap.xml`, `robots.txt` | Archivos para buscadores |
| `tools/`, `src/`, `tailwind.config.js` | Código fuente para regenerar las páginas |

## Cómo editar

Los textos de todas las páginas están en `tools/build.py` (contenido) y `tools/sitekit.py` (menú, pie de página, datos de contacto). Después de editar:

```bash
npm install          # solo la primera vez
npm run build        # regenera los HTML y el CSS
```

Cambios pequeños (un texto, un número) también se pueden hacer directamente en el `.html`, pero se perderán la próxima vez que se ejecute `npm run build`.

**Colores de marca** (tomados del logo) en `tailwind.config.js`: azul engranaje `navy #252b66` / `primary-700 #2e407a`, amarillo rayo `accent-300 #ffe030` / `accent-500 #ffb101`.

## Google Ads / Google Analytics

La etiqueta de Google Ads **AW-17952331494** está en el `<head>` de todas las páginas (se genera desde `tools/sitekit.py`, variable `ADS_TAG`). **No la quites.**

En `js/main.js` puedes completar `GA4_ID` (si creas Google Analytics) y `ADS_LEAD_LABEL` (etiqueta de la conversión de Ads). Eventos registrados: `whatsapp_click`, `email_click`, `generate_lead` (formulario).

## Pendientes recomendados

1. **Google Search Console**: verificar `imectec.com` y enviar `https://imectec.com/sitemap.xml`.
2. **Google Business Profile**: crear/actualizar la ficha con el mismo teléfono, horario y web.
3. **Videos del inicio**: muestran marcas de agua (iStock / clideo.com). Reemplazarlos por videos con licencia o propios (mismos nombres).
