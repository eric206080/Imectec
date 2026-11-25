"""Piezas compartidas del sitio IMECTEC (head, navbar, footer, íconos, schema).

Genera HTML estático. Ejecuta `python3 tools/build.py` y luego `npm run build:css`.
"""
import json

SITE = "https://imectec.com"
WA_NUMBER = "51980038307"
WA_DISPLAY = "+51 980 038 307"
EMAIL = "comercial@imectec.com"
ADS_TAG = "AW-17952331494"  # Etiqueta de Google Ads ya existente: NO quitar
import hashlib as _h, os as _os
_ROOT = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))


def _asset_hash():
    """Versión = huella de css/main.css + js/main.js: cambia sola para que nadie vea estilos viejos en caché."""
    m = _h.sha1()
    for f in ("css/main.css", "js/main.js"):
        try:
            m.update(open(_os.path.join(_ROOT, f), "rb").read())
        except FileNotFoundError:
            pass
    return m.hexdigest()[:10]


ASSET_VERSION = _asset_hash()


def wa(text="Hola IMECTEC, deseo cotizar un servicio"):
    from urllib.parse import quote
    return f"https://wa.me/{WA_NUMBER}?text={quote(text)}"


# ---------------------------------------------------------------- íconos (Heroicons, MIT)
ICONS = {
    "check": "M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
    "bolt": "M13 10V3L4 14h7v7l9-11h-7z",
    "users": "M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z",
    "flask": "M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z",
    "columns": "M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2",
    "chart": "M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z",
    "calc": "M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z",
    "layout": "M4 5a1 1 0 011-1h14a1 1 0 011 1v2a1 1 0 01-1 1H5a1 1 0 01-1-1V5zM4 13a1 1 0 011-1h6a1 1 0 011 1v6a1 1 0 01-1 1H5a1 1 0 01-1-1v-6zM16 13a1 1 0 011-1h2a1 1 0 011 1v6a1 1 0 01-1 1h-2a1 1 0 01-1-1v-6z",
    "bulb": "M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
    "cube": "M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4",
    "fire": "M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z",
    "globe": "M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
    "building": "M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4",
    "shield": "M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z",
    "badge": "M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z",
    "pin": "M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z M15 11a3 3 0 11-6 0 3 3 0 016 0z",
    "mail": "M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z",
    "arrow": "M17 8l4 4m0 0l-4 4m4-4H3",
    "down": "M19 14l-7 7m0 0l-7-7m7 7V3",
    "up": "M5 10l7-7m0 0l7 7m-7-7v18",
    "ext": "M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14",
    "menu": "M4 6h16M4 12h16M4 18h16",
    "x": "M6 18L18 6M6 6l12 12",
    "clipboard": "M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2m-6 9l2 2 4-4",
    "search": "M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z",
    "doc": "M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z",
    "photo": "M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z",
    "chat": "M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z",
    "clock": "M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z",
    "plus": "M12 4v16m8-8H4",
}

WA_PATH = "M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"
LI_PATH = "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"
FB_PATH = "M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"


def icon(name, cls="w-6 h-6", sw="2"):
    return (f'<svg class="{cls}" fill="none" stroke="currentColor" stroke-width="{sw}" viewBox="0 0 24 24" aria-hidden="true">'
            f'<path stroke-linecap="round" stroke-linejoin="round" d="{ICONS[name]}"/></svg>')


def solid(path, cls="w-5 h-5"):
    return f'<svg class="{cls}" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="{path}"/></svg>'


# ---------------------------------------------------------------- servicios (para menús y schema)
SERVICE_PAGES = [
    ("tableros-electricos", "Tableros Eléctricos BT/MT", "layout"),
    ("mantenimiento-electrico", "Mantenimiento Eléctrico Industrial", "shield"),
    ("subestaciones", "Mantenimiento de Subestaciones", "bolt"),
    ("automatizacion-plc-scada", "Automatización PLC, HMI y SCADA", "chart"),
    ("variadores-de-frecuencia", "Variadores de Frecuencia", "calc"),
]

ORG_ID = SITE + "/#organizacion"


def org_schema():
    return {
        "@type": "ProfessionalService",
        "@id": ORG_ID,
        "name": "IMECTEC Ingeniería & Proyectos",
        "legalName": "IMECTEC Ingeniería & Proyectos S.A.C.",
        "url": SITE + "/",
        "logo": SITE + "/images/logo-256.png",
        "image": SITE + "/images/og-image.jpg",
        "description": "Empresa peruana de ingeniería eléctrica y electromecánica: tableros eléctricos BT/MT, mantenimiento eléctrico industrial, subestaciones, variadores de frecuencia, automatización PLC/SCADA, puesta a tierra e ingeniería de detalle.",
        "telephone": "+51980038307",
        "email": EMAIL,
        "priceRange": "$$",
        "address": {"@type": "PostalAddress", "addressLocality": "Lima", "addressRegion": "Lima", "addressCountry": "PE"},
        "areaServed": {"@type": "Country", "name": "Perú"},
        "contactPoint": {"@type": "ContactPoint", "telephone": "+51980038307", "email": EMAIL, "contactType": "sales", "areaServed": "PE", "availableLanguage": ["es"]},
        "knowsAbout": ["Ingeniería eléctrica", "Tableros eléctricos", "Media tensión", "Subestaciones eléctricas", "Variadores de frecuencia", "Automatización industrial", "PLC", "SCADA", "Puesta a tierra", "Mantenimiento eléctrico"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog", "name": "Servicios de ingeniería eléctrica y electromecánica",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": name, "url": f"{SITE}/{slug}/"}}
                for slug, name, _ in SERVICE_PAGES
            ] + [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": n}} for n in
                 ["Protecciones y sincronismo", "Puesta a tierra y pararrayos", "Canalización y cableado", "Ingeniería de detalle"]],
        },
    }


def faq_schema(faqs):
    return {"@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


def jsonld(graph):
    return ('<script type="application/ld+json">'
            + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":"))
            + "</script>")


# ---------------------------------------------------------------- head
def head(*, title, description, path, root, jsonld_html="", og_title=None, preload_poster=False):
    url = SITE + path
    og_title = og_title or title
    poster = f'\n    <link rel="preload" as="image" href="{root}images/hero-poster.jpg" fetchpriority="high">' if preload_poster else ""
    return f"""<!DOCTYPE html>
<html lang="es-PE">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <meta name="robots" content="index, follow, max-image-preview:large">
    <meta name="author" content="IMECTEC Ingeniería & Proyectos">
    <meta name="theme-color" content="#252b66">
    <meta name="geo.region" content="PE-LIM">
    <meta name="geo.placename" content="Lima">
    <link rel="canonical" href="{url}">
    <!-- Google Search Console / Bing Webmaster Tools: pega aquí sus metas de verificación si usas ese método -->
    <link rel="alternate" type="text/plain" title="Resumen para asistentes de IA" href="{SITE}/llms.txt">

    <meta property="og:type" content="website">
    <meta property="og:site_name" content="IMECTEC">
    <meta property="og:url" content="{url}">
    <meta property="og:title" content="{og_title}">
    <meta property="og:description" content="{description}">
    <meta property="og:image" content="{SITE}/images/og-image.jpg">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="es_PE">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{og_title}">
    <meta name="twitter:description" content="{description}">
    <meta name="twitter:image" content="{SITE}/images/og-image.jpg">

    <link rel="icon" type="image/png" sizes="32x32" href="{root}images/favicon-32.png">
    <link rel="icon" href="{root}favicon.ico" sizes="any">
    <link rel="apple-touch-icon" href="{root}images/apple-touch-icon.png">{poster}

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,700&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{root}css/main.css?v={ASSET_VERSION}">
    <!-- Etiqueta de Google (Google Ads) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={ADS_TAG}"></script>
    <script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','{ADS_TAG}');</script>
    <script src="{root}js/main.js?v={ASSET_VERSION}" defer></script>
    {jsonld_html}
</head>
<body class="font-body text-slate-700 bg-slate-50">
    <a href="#contenido" class="sr-only focus:not-sr-only focus:fixed focus:top-3 focus:left-3 focus:z-[60] focus:rounded-lg focus:bg-white focus:px-4 focus:py-2 focus:text-primary-700 focus:shadow-lg">Saltar al contenido</a>
"""


# ---------------------------------------------------------------- navbar
def logo_block(root, home, dark=False):
    name_cls = "text-white" if dark else "text-navy"
    sub_cls = "text-slate-400" if dark else "text-slate-500"
    return f"""<a href="{home}" class="flex items-center gap-3" aria-label="IMECTEC - Inicio">
                    <img src="{root}images/logo-128.png" alt="" width="46" height="46" class="h-[46px] w-[46px]">
                    <span class="leading-none">
                        <span class="block font-brand text-[1.5rem] font-extrabold tracking-wide {name_cls}">IMECTEC</span>
                        <span class="mt-1 block text-[11px] font-medium tracking-wide {sub_cls}">Ingeniería &amp; Proyectos</span>
                    </span>
                </a>"""


def navbar(root, home_prefix):
    """home_prefix: '' en el inicio, '../' en subpáginas (para enlaces a secciones)."""
    h = home_prefix  # anclas
    home = "#inicio" if not h else h
    items = [("Inicio", f"{h}#inicio"), ("Servicios", f"{h}#servicios"), ("Sectores", f"{h}#sectores"),
             ("Proyectos", f"{h}#proyectos"), ("Nosotros", f"{h}#nosotros"), ("Preguntas", f"{h}#preguntas"), ("Contacto", f"{h}#contacto")]
    desk = "\n".join(f'                    <a href="{u}" class="rounded-lg px-3 py-2 text-sm font-medium text-slate-600 transition-colors hover:bg-primary-50 hover:text-primary-700">{t}</a>' for t, u in items)
    mob = "\n".join(f'            <a href="{u}" class="block rounded-xl px-4 py-3 font-medium text-slate-700 hover:bg-primary-50 hover:text-primary-700">{t}</a>' for t, u in items)
    mob_services = "\n".join(f'                <a href="{root}{s}/" class="block rounded-lg px-4 py-2 text-sm text-slate-600 hover:bg-primary-50 hover:text-primary-700">{n}</a>' for s, n, _ in SERVICE_PAGES)
    return f"""
    <!-- NAVBAR -->
    <header id="navbar" class="fixed inset-x-0 top-0 z-50 border-b border-slate-200/70 bg-white/90 backdrop-blur-md transition-all duration-300">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="flex h-20 items-center justify-between">
                {logo_block(root, home)}
                <nav class="hidden items-center gap-0.5 lg:flex" aria-label="Principal">
{desk}
                </nav>
                <div class="hidden lg:block">
                    <a href="{wa()}" target="_blank" rel="noopener" data-track="navbar" class="btn-whatsapp !px-5 !py-2.5 text-sm">{solid(WA_PATH,'w-4 h-4')} Cotizar</a>
                </div>
                <button id="mobile-menu-btn" type="button" class="rounded-xl p-2 hover:bg-slate-100 lg:hidden" aria-label="Abrir menú" aria-controls="mobile-menu" aria-expanded="false">{icon('menu','w-7 h-7 text-navy')}</button>
            </div>
        </div>
    </header>

    <!-- MENÚ MÓVIL -->
    <div id="mobile-menu-overlay" class="invisible fixed inset-0 z-50 bg-navy-dark/60 opacity-0 backdrop-blur-sm transition-all duration-300 lg:hidden"></div>
    <div id="mobile-menu" class="fixed right-0 top-0 z-50 flex h-full w-[85%] max-w-sm translate-x-full flex-col bg-white shadow-2xl transition-transform duration-300 lg:hidden" aria-hidden="true">
        <div class="flex items-center justify-between border-b border-slate-100 p-5">
            <span class="font-brand text-xl font-extrabold text-navy">IMECTEC</span>
            <button id="mobile-menu-close" type="button" class="rounded-xl p-2 hover:bg-slate-100" aria-label="Cerrar menú">{icon('x','w-6 h-6 text-slate-500')}</button>
        </div>
        <nav class="flex-1 space-y-1 overflow-y-auto p-5" aria-label="Menú móvil">
{mob}
            <div class="mt-3 border-t border-slate-100 pt-3">
                <p class="px-4 pb-1 text-xs font-semibold uppercase tracking-wider text-slate-400">Servicios</p>
{mob_services}
            </div>
        </nav>
        <div class="border-t border-slate-100 p-5">
            <a href="{wa()}" target="_blank" rel="noopener" data-track="menu_movil" class="btn-whatsapp w-full">{solid(WA_PATH)} Cotizar por WhatsApp</a>
        </div>
    </div>
"""


# ---------------------------------------------------------------- footer
def footer(root, home_prefix):
    h = home_prefix
    services = "\n".join(f'                        <li><a href="{root}{s}/" class="hover:text-white">{n}</a></li>' for s, n, _ in SERVICE_PAGES)
    return f"""
    <!-- FOOTER -->
    <footer class="bg-navy-dark pt-16 pb-8 text-slate-400">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid gap-10 border-b border-white/10 pb-12 sm:grid-cols-2 lg:grid-cols-4">
                <div>
                    <div class="mb-4">{logo_block(root, h or '#inicio', dark=True)}</div>
                    <p class="mb-6 text-sm leading-relaxed">Ingeniería eléctrica y electromecánica para proyectos exigentes. Más de 10 años impulsando la industria peruana.</p>
                    <div class="flex gap-3">
                        <a href="{wa()}" target="_blank" rel="noopener" data-track="footer" aria-label="IMECTEC en WhatsApp" class="flex h-10 w-10 items-center justify-center rounded-xl bg-white/10 text-white transition-colors hover:bg-[#1fae53]">{solid(WA_PATH)}</a>
                    </div>
                </div>
                <div>
                    <h2 class="mb-4 font-heading text-base font-bold text-white">Servicios</h2>
                    <ul class="space-y-3 text-sm">
{services}
                    </ul>
                </div>
                <div>
                    <h2 class="mb-4 font-heading text-base font-bold text-white">Empresa</h2>
                    <ul class="space-y-3 text-sm">
                        <li><a href="{h}#sectores" class="hover:text-white">Sectores</a></li>
                        <li><a href="{h}#proyectos" class="hover:text-white">Proyectos</a></li>
                        <li><a href="{h}#nosotros" class="hover:text-white">Nosotros</a></li>
                        <li><a href="{h}#preguntas" class="hover:text-white">Preguntas frecuentes</a></li>
                        <li><a href="{root}politica-de-privacidad/" class="hover:text-white">Política de privacidad</a></li>
                    </ul>
                </div>
                <div>
                    <h2 class="mb-4 font-heading text-base font-bold text-white">Contacto</h2>
                    <ul class="space-y-3 text-sm">
                        <li class="flex items-center gap-2">{icon('pin','w-4 h-4 text-accent-400')} Lima, Perú</li>
                        <li><a href="mailto:{EMAIL}" data-track="footer" class="flex items-center gap-2 hover:text-white">{icon('mail','w-4 h-4 text-accent-400')} {EMAIL}</a></li>
                        <li><a href="{wa()}" target="_blank" rel="noopener" data-track="footer" class="flex items-center gap-2 hover:text-white">{solid(WA_PATH,'w-4 h-4 text-green-400')} {WA_DISPLAY}</a></li>
                    </ul>
                </div>
            </div>
            <div class="flex flex-col items-center justify-between gap-4 pt-8 text-sm md:flex-row">
                <p>&copy; <span data-year>2026</span> IMECTEC Ingeniería &amp; Proyectos S.A.C. – Perú. Todos los derechos reservados.</p>
                <a href="{root}politica-de-privacidad/" class="hover:text-white">Política de privacidad</a>
            </div>
        </div>
    </footer>

    <!-- WHATSAPP FLOTANTE -->
    <a href="{wa()}" target="_blank" rel="noopener" data-track="boton_flotante" class="group fixed bottom-5 right-5 z-40" aria-label="Escríbenos por WhatsApp">
        <span class="absolute inset-0 animate-ping rounded-full bg-green-500 opacity-25"></span>
        <span class="relative flex h-14 w-14 items-center justify-center rounded-full bg-[#1fae53] text-white shadow-lg shadow-green-600/30 transition-transform group-hover:scale-110">{solid(WA_PATH,'w-7 h-7')}</span>
        <span class="pointer-events-none absolute right-full top-1/2 mr-3 hidden -translate-y-1/2 whitespace-nowrap rounded-xl bg-white px-4 py-2 text-sm font-medium text-slate-700 opacity-0 shadow-lg transition-opacity group-hover:opacity-100 sm:block">¡Escríbenos ahora!</span>
    </a>

    <button id="back-to-top" type="button" aria-label="Volver arriba" class="invisible fixed bottom-5 left-5 z-40 flex h-12 w-12 items-center justify-center rounded-full bg-white text-primary-700 opacity-0 shadow-lg transition-all hover:bg-primary-700 hover:text-white">{icon('up','w-5 h-5')}</button>
</body>
</html>
"""


def section_head(eyebrow, title_html, text="", dark=False, ic="flask"):
    eb = "bg-white/10 text-accent-300" if dark else "bg-primary-50 text-primary-700 ring-1 ring-primary-100"
    h2 = "text-white" if dark else "text-navy"
    p = "text-slate-300" if dark else "text-slate-600"
    ptag = f'<p class="text-lg {p}">{text}</p>' if text else ""
    return f"""<div class="reveal mx-auto mb-14 max-w-3xl text-center">
                <span class="eyebrow mb-4 {eb}">{icon(ic,'w-4 h-4')} {eyebrow}</span>
                <h2 class="mb-5 font-heading text-3xl font-extrabold tracking-tight {h2} sm:text-4xl lg:text-5xl">{title_html}</h2>
                {ptag}
            </div>"""


def faq_list(faqs, dark=False):
    out = []
    for q, a in faqs:
        out.append(f"""<details class="faq card group p-0">
                    <summary class="flex items-center justify-between gap-4 p-6 font-heading text-lg font-bold text-navy">
                        <span>{q}</span>
                        <span class="faq-icon flex h-8 w-8 flex-shrink-0 items-center justify-center rounded-full bg-primary-50 text-primary-700 transition-transform">{icon('plus','w-4 h-4')}</span>
                    </summary>
                    <p class="px-6 pb-6 leading-relaxed text-slate-600">{a}</p>
                </details>""")
    return "\n                ".join(out)
