"""Genera las páginas HTML del sitio IMECTEC.

Uso:  python3 tools/build.py   (luego: npm run build:css)
Edita los textos aquí y vuelve a ejecutar para actualizar todas las páginas a la vez.
"""
import os
from datetime import date
from sitekit import *  # noqa  (tools/sitekit.py)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def write(rel, html):
    p = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    print("OK", rel)


# =========================================================================== INICIO
HOME_FAQS = [
    ("¿Cuánto tiempo toma fabricar un tablero eléctrico?",
     "El tiempo depende de la complejidad del tablero. Un tablero estándar de distribución toma entre 2 y 3 semanas. Tableros de control con automatización pueden tomar de 4 a 6 semanas. Siempre confirmamos el plazo exacto al momento de cotizar."),
    ("¿Trabajan en todo el Perú?",
     "Sí, atendemos proyectos en todo el territorio nacional. Tenemos experiencia en proyectos mineros en zonas alejadas y plantas industriales en diversas regiones del país."),
    ("¿Ofrecen garantía en sus trabajos?",
     "Todos nuestros trabajos incluyen garantía. Los tableros tienen 1 año de garantía en fabricación. Las instalaciones incluyen garantía de 6 meses a 1 año dependiendo del tipo de trabajo."),
    ("¿Qué tipo de tableros fabrican?",
     "Fabricamos tableros de distribución, tableros de control, tableros de transferencia automática (ATS), tableros de arranque de motores, CCMs, tableros para variadores y tableros de medición, tanto en baja como en media tensión hasta 36 kV."),
    ("¿Realizan contratos de mantenimiento?",
     "Sí, ofrecemos contratos de mantenimiento preventivo con frecuencia mensual, trimestral o semestral según sus necesidades. Incluyen inspecciones, termografía, limpieza y ajustes."),
    ("¿Cómo solicito una cotización?",
     "Escríbanos por WhatsApp al +51 980 038 307, envíe un correo a comercial@imectec.com o complete el formulario de esta página. Para cotizaciones formales, el correo es el canal recomendado."),
]

# Mismas fotos que la web actual (versiones livianas en images/web/; los originales siguen en images/)
SERVICES = [
    # (título, descripción, imagen, alt, enlace interno o None, texto WhatsApp)
    ("Tableros Eléctricos BT/MT", "Diseño, fabricación y ensamble de tableros de distribución, control y potencia hasta 36 kV.", "servicio-tableros", "Tablero eléctrico de baja tensión en fabricación", "tableros-electricos/", "Hola IMECTEC, necesito información sobre tableros eléctricos"),
    ("Mantenimiento Eléctrico", "Mantenimiento preventivo y correctivo de sistemas eléctricos industriales y comerciales.", "servicio-mantenimiento", "Técnico de IMECTEC realizando mantenimiento en un tablero eléctrico", "mantenimiento-electrico/", "Hola IMECTEC, necesito información sobre mantenimiento eléctrico"),
    ("Variadores de Frecuencia", "Instalación, configuración y puesta en marcha de variadores para control de motores.", "galeria-02", "Tablero de control con cableado y equipos de maniobra", "variadores-de-frecuencia/", "Hola IMECTEC, necesito información sobre variadores de frecuencia"),
    ("Subestaciones", "Mantenimiento de subestaciones: mantenimiento preventivo y predictivo.", "galeria-03", "Técnico trabajando en la estructura de una subestación eléctrica", "subestaciones/", "Hola IMECTEC, necesito información sobre mantenimiento de subestaciones"),
    ("Protecciones y Sincronismo", "Sistemas de protección eléctrica y sincronización de generadores con la red.", "proyecto-01", "Transformador de potencia en una subestación eléctrica", None, "Hola IMECTEC, necesito información sobre protecciones y sincronismo"),
    ("Puesta a Tierra", "Diseño e instalación de sistemas de puesta a tierra y pararrayos certificados.", "proyecto-02", "Celdas de media tensión abiertas durante trabajos eléctricos", None, "Hola IMECTEC, necesito información sobre puesta a tierra"),
    ("Canalización y Cableado", "Tendido de cables, bandejas portacables y canalizaciones eléctricas industriales.", "galeria-01", "Tablero eléctrico con cableado, protecciones y batería de respaldo", None, "Hola IMECTEC, necesito información sobre canalización y cableado"),
    ("Automatización PLC/HMI", "Programación y configuración de PLCs, HMIs y sistemas SCADA industriales.", "proyecto-03", "Técnico realizando pruebas en celdas de una sala eléctrica", "automatizacion-plc-scada/", "Hola IMECTEC, necesito información sobre automatización PLC/HMI"),
    ("Ingeniería de Detalle", "Cálculos eléctricos, memorias descriptivas, planos unifilares y documentación técnica para proyectos.", "hero-bg", "Subestación eléctrica de alta tensión en la sierra del Perú", None, "Hola IMECTEC, necesito información sobre ingeniería de detalle"),
]

SECTORS = [("Industria", "building"), ("Minería", "cube"), ("Energía", "bolt"), ("Saneamiento", "globe"),
           ("Construcción", "layout"), ("Pesca", "chart"), ("Hidrocarburos", "fire")]

PROJECTS = [
    ("proyecto-01", "Minería", "Tablero de Distribución 1000A", "Paradas no programadas por fallas en sistema eléctrico antiguo.", "Diseño e instalación de tablero con protecciones selectivas y monitoreo.", "98% de disponibilidad operativa.", "Subestación y transformador de un proyecto minero"),
    ("proyecto-02", "Industria", "Sistema de Variadores para Fajas", "Alto consumo energético en sistema de fajas transportadoras.", "Instalación de variadores de frecuencia con control PID.", "Reducción del 35% en consumo eléctrico.", "Celdas y tableros eléctricos de una planta industrial"),
    ("proyecto-03", "Saneamiento", "Automatización PTAR", "Operación manual con alto costo de personal y errores frecuentes.", "Sistema SCADA con PLCs para control automático de procesos.", "Operación 24/7 con supervisión remota.", "Técnico en la sala eléctrica de una planta de tratamiento"),
]

DIFFS = [
    ("clock", "Respuesta Rápida", "Atención en menos de 24 horas para emergencias y cotizaciones."),
    ("shield", "Seguridad Certificada", "Personal capacitado en normas de seguridad eléctrica y trabajo en altura."),
    ("users", "Personal Calificado", "Ingenieros y técnicos con amplia experiencia en proyectos industriales."),
    ("badge", "Calidad Garantizada", "Uso de materiales certificados y procesos bajo estándares internacionales."),
    ("doc", "Documentación Completa", "Entregamos planos, protocolos de pruebas y manuales de operación."),
]


def img(name, alt, w, h, cls, lazy=True, prefix=""):
    lz = ' loading="lazy" decoding="async"' if lazy else ' fetchpriority="high"'
    return f'<img src="{prefix}images/web/{name}.jpg" alt="{alt}" width="{w}" height="{h}"{lz} class="{cls}">'


def build_home():
    root, hp = "", ""
    services_html = "\n".join(f"""                <article class="reveal card card-hover group flex flex-col overflow-hidden">
                    <div class="relative aspect-[4/3] overflow-hidden bg-slate-200">
                        {img(im, alt, 750, 1000, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105')}
                        <div class="absolute inset-0 bg-gradient-to-t from-navy-dark/60 via-transparent"></div>
                    </div>
                    <div class="flex flex-1 flex-col p-7">
                        <h3 class="mb-2 font-heading text-xl font-bold text-navy">{t}</h3>
                        <p class="mb-6 flex-1 text-slate-600">{d}</p>
                        <div class="flex flex-wrap items-center gap-x-5 gap-y-2 text-sm font-semibold">
                            <a href="{wa(w)}" target="_blank" rel="noopener" data-track="servicio" class="inline-flex items-center gap-1.5 text-[#178f43] hover:text-[#126f34]">{solid(WA_PATH,'w-4 h-4')} Cotizar<span class="sr-only"> {t}</span></a>
                            {f'<a href="{link}" class="inline-flex items-center gap-1.5 text-primary-700 transition-all hover:gap-2.5">Ver servicio {icon("arrow","w-4 h-4")}<span class="sr-only"> de {t}</span></a>' if link else ''}
                        </div>
                    </div>
                </article>""" for t, d, im, alt, link, w in SERVICES)

    sectors_html = "\n".join(f"""                <div class="reveal flex flex-col items-center gap-3 rounded-2xl border border-white/10 bg-white/[.04] px-4 py-7 text-center transition-all hover:-translate-y-1 hover:border-accent-400/60 hover:bg-white/[.08]">
                    <span class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br from-accent-300 to-accent-500 text-navy-dark shadow-lg shadow-accent-500/20">{icon(ic,'w-7 h-7')}</span>
                    <h3 class="font-heading text-lg font-bold text-white">{t}</h3>
                </div>""" for t, ic in SECTORS)

    projects_html = "\n".join(f"""                <article class="reveal card group flex flex-col overflow-hidden hover:shadow-xl hover:shadow-primary-900/10">
                    <div class="relative aspect-[4/3] overflow-hidden bg-slate-200">
                        {img(im, alt, 1000, 750, 'h-full w-full object-cover transition-transform duration-700 group-hover:scale-105')}
                        <span class="absolute left-4 top-4 rounded-full bg-accent-400 px-3 py-1 text-xs font-bold text-navy-dark shadow">{sec}</span>
                    </div>
                    <div class="flex flex-1 flex-col p-7">
                        <h3 class="mb-4 font-heading text-xl font-bold text-navy">{t}</h3>
                        <dl class="flex-1 space-y-3 text-sm">
                            <div><dt class="font-semibold text-slate-800">Problema</dt><dd class="text-slate-600">{pb}</dd></div>
                            <div><dt class="font-semibold text-slate-800">Solución</dt><dd class="text-slate-600">{so}</dd></div>
                        </dl>
                        <p class="mt-5 flex items-center gap-2 rounded-xl bg-accent-50 px-4 py-3 text-sm font-semibold text-navy ring-1 ring-accent-200">{icon('check','w-5 h-5 flex-shrink-0 text-accent-700')} {rs}</p>
                    </div>
                </article>""" for im, sec, t, pb, so, rs, alt in PROJECTS)

    diffs_html = "\n".join(f"""                <div class="reveal card p-7 text-center">
                    <div class="mx-auto mb-5 flex h-14 w-14 items-center justify-center rounded-2xl bg-primary-50 text-primary-700 ring-1 ring-primary-100">{icon(ic,'w-7 h-7')}</div>
                    <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                    <p class="text-sm leading-relaxed text-slate-600">{d}</p>
                </div>""" for ic, t, d in DIFFS)

    steps = [("search", "1. Evaluación", "Revisamos su requerimiento, planos y equipos existentes; si hace falta, visitamos la instalación."),
             ("doc", "2. Propuesta", "Le enviamos alcance, plazo y costo claros, con la solución técnica recomendada."),
             ("bolt", "3. Ejecución", "Fabricación, instalación o mantenimiento con personal calificado y estrictas normas de seguridad."),
             ("clipboard", "4. Pruebas y entrega", "Pruebas, puesta en marcha, protocolos, planos y manuales de operación.")]
    steps_html = "\n".join(f"""                <div class="reveal relative rounded-2xl bg-white p-7 shadow-sm ring-1 ring-slate-200/80">
                    <div class="mb-5 flex h-12 w-12 items-center justify-center rounded-xl bg-accent-100 text-accent-800 ring-1 ring-accent-200">{icon(ic,'w-6 h-6')}</div>
                    <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                    <p class="text-sm leading-relaxed text-slate-600">{d}</p>
                </div>""" for ic, t, d in steps)

    options = "".join(f'<option value="{t}">{t}</option>' for t, *_ in SERVICES) + '<option value="Grupos Electrógenos">Grupos Electrógenos</option><option value="Otro">Otro</option>'
    field = "w-full rounded-xl border border-slate-200 bg-slate-50 px-4 py-3 text-slate-800 placeholder-slate-400 transition-all focus:border-transparent focus:bg-white focus:outline-none focus:ring-2 focus:ring-accent-500"
    label = "mb-2 block text-sm font-semibold text-slate-700"

    ld = jsonld([
        org_schema(),
        {"@type": "WebSite", "@id": SITE + "/#web", "url": SITE + "/", "name": "IMECTEC", "inLanguage": "es-PE", "publisher": {"@id": ORG_ID}},
        {"@type": "WebPage", "@id": SITE + "/#webpage", "url": SITE + "/", "name": "IMECTEC | Ingeniería Eléctrica y Electromecánica en Perú", "isPartOf": {"@id": SITE + "/#web"}, "about": {"@id": ORG_ID}, "inLanguage": "es-PE"},
        faq_schema(HOME_FAQS),
    ])

    stat = lambda n, l, ic, g, extra='': f'<div class="stat-card w-72 animate-float rounded-2xl p-5 {extra}"><div class="flex items-center gap-4"><div class="flex h-14 w-14 items-center justify-center rounded-2xl bg-gradient-to-br {g} shadow-lg">{icon(ic,"w-7 h-7")}</div><div><div class="font-heading text-4xl font-extrabold text-navy">{n}</div><div class="text-sm font-medium text-slate-500">{l}</div></div></div></div>'

    html = head(
        title="IMECTEC | Ingeniería Eléctrica y Electromecánica en Perú · Tableros BT/MT",
        description="Ingeniería eléctrica y electromecánica en Perú: tableros BT/MT hasta 36 kV, mantenimiento eléctrico, subestaciones, variadores, automatización PLC/SCADA y puesta a tierra. ¡Cotiza por WhatsApp!",
        og_title="IMECTEC | Ingeniería Eléctrica y Electromecánica en Perú",
        path="/", root=root, jsonld_html=ld)
    html = html.replace('<link rel="preconnect" href="https://fonts.googleapis.com">', '<link rel="preload" as="image" href="images/web/hero-bg.jpg" fetchpriority="high">\n    <link rel="preconnect" href="https://fonts.googleapis.com">', 1)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido">
    <!-- HERO (mismos videos de la web actual; video2 en versión liviana) -->
    <section id="inicio" class="hero">
        <div class="hero-media" aria-hidden="true">
            <video id="hero-video" muted playsinline preload="none" poster="images/web/hero-bg.jpg" data-sources="videos/video1.mp4,videos/video2-web.mp4,videos/video3.mp4" style="opacity:0"></video>
        </div>
        <div class="hero-overlay"></div>
        <div class="relative z-10 flex min-h-[inherit] items-center">
            <div class="mx-auto w-full max-w-7xl px-4 pb-24 pt-32 sm:px-6 lg:px-8 lg:pb-20">
                <div class="grid items-center gap-12 lg:grid-cols-12">
                    <div class="text-center lg:col-span-7 lg:text-left">
                        <p class="glass mb-8 inline-flex animate-fade-up items-center gap-2 rounded-full px-5 py-2.5 text-sm font-medium text-white">
                            <span class="h-2 w-2 animate-pulse rounded-full bg-accent-300"></span> Baja, media y alta tensión · Todo el Perú
                        </p>
                        <h1 class="mb-6 animate-fade-up font-heading text-4xl font-extrabold leading-[1.06] tracking-tight text-white [animation-delay:.15s] sm:text-5xl lg:text-6xl xl:text-7xl">
                            Ingeniería <span class="underline-brand">Eléctrica</span> y <span class="text-gradient">Electromecánica de Alto Nivel</span>
                        </h1>
                        <p class="mx-auto mb-10 max-w-2xl animate-fade-up text-lg leading-relaxed text-white/85 [animation-delay:.3s] sm:text-xl lg:mx-0">
                            Soluciones integrales en <strong class="font-semibold text-white">baja, media y alta tensión</strong> para proyectos industriales, mineros e infraestructura: tableros BT/MT, subestaciones, variadores y automatización.
                        </p>
                        <div class="flex animate-fade-up flex-col justify-center gap-4 [animation-delay:.45s] sm:flex-row lg:justify-start">
                            <a href="{wa()}" target="_blank" rel="noopener" data-track="hero" class="btn-whatsapp !px-8 !py-4 text-base">{solid(WA_PATH)} Solicitar cotización</a>
                            <a href="#servicios" class="btn-ghost !px-8 !py-4 text-base">Ver servicios {icon('down','w-4 h-4')}</a>
                        </div>
                    </div>
                    <div class="hidden flex-col items-end gap-5 lg:col-span-5 lg:flex">
                        {stat('150+', 'Proyectos ejecutados', 'check', 'from-primary-500 to-primary-800 text-white')}
                        {stat('50+', 'Clientes', 'users', 'from-accent-300 to-accent-500 text-navy-dark', 'mr-10 [animation-delay:-2.3s]')}
                        {stat('10+', 'Años de experiencia', 'bolt', 'from-navy to-primary-500 text-white', '[animation-delay:-4.6s]')}
                    </div>
                </div>
                <div class="mx-auto mt-12 grid max-w-md grid-cols-3 gap-3 lg:hidden">
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">150+</div><div class="text-xs text-slate-500">Proyectos</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">50+</div><div class="text-xs text-slate-500">Clientes</div></div>
                    <div class="stat-card rounded-xl p-3 text-center"><div class="font-heading text-2xl font-extrabold text-navy">10+</div><div class="text-xs text-slate-500">Años</div></div>
                </div>
            </div>
        </div>
        <a href="#servicios" class="scroll-cue absolute bottom-6 left-1/2 z-10 -ml-20 hidden w-40 flex-col items-center text-white/75 hover:text-white sm:flex">
            <span class="mb-1 text-[11px] font-semibold uppercase tracking-[.2em]">Descubre más</span>{icon('down','w-6 h-6')}
        </a>
    </section>

    <!-- FRANJA -->
    <div class="border-b border-slate-200 bg-white">
        <div class="mx-auto flex max-w-7xl flex-wrap items-center justify-center gap-x-8 gap-y-3 px-4 py-5 text-sm font-semibold text-slate-600 sm:px-6 lg:px-8">
            <span class="flex items-center gap-2">{icon('layout','w-4 h-4 text-accent-600')} Tableros hasta 36 kV</span>
            <span class="flex items-center gap-2">{icon('shield','w-4 h-4 text-accent-600')} Garantía en todos los trabajos</span>
            <span class="flex items-center gap-2">{icon('clock','w-4 h-4 text-accent-600')} Respuesta en menos de 24 h</span>
            <span class="flex items-center gap-2">{icon('doc','w-4 h-4 text-accent-600')} Protocolos, planos y manuales</span>
        </div>
    </div>

    <!-- SERVICIOS -->
    <section id="servicios" class="relative py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Nuestros servicios', 'Soluciones integrales en <span class="text-primary-600">ingeniería eléctrica</span>', 'Ofrecemos servicios especializados para garantizar la continuidad operativa de su empresa.', ic='bolt')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3 lg:gap-8">
{services_html}
            </div>
        </div>
    </section>

    <!-- CÓMO TRABAJAMOS -->
    <section class="relative bg-gradient-to-b from-primary-50/70 to-slate-50 py-24">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Cómo trabajamos', 'Un proceso claro, <span class="text-primary-600">de principio a fin</span>', 'Sabe qué esperar en cada etapa y recibe toda la documentación técnica de su proyecto.', ic='clipboard')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
{steps_html}
            </div>
        </div>
    </section>

    <!-- SECTORES -->
    <section id="sectores" class="relative overflow-hidden bg-brand-dark py-24 lg:py-28">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Sectores que atendemos', 'Experiencia en <span class="text-accent-300">múltiples industrias</span>', dark=True, ic='building')}
            <div class="grid grid-cols-2 gap-4 sm:grid-cols-4 lg:grid-cols-7">
{sectors_html}
            </div>
        </div>
    </section>

    <!-- PROYECTOS -->
    <section id="proyectos" class="relative bg-slate-50 py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Proyectos destacados', 'Casos de <span class="text-primary-600">éxito</span>', 'Soluciones implementadas que generan resultados medibles.', ic='photo')}
            <div class="grid gap-8 md:grid-cols-3">
{projects_html}
            </div>
            <div class="reveal mt-14 text-center">
                <a href="{wa('Hola IMECTEC, deseo conocer más proyectos')}" target="_blank" rel="noopener" data-track="proyectos" class="btn-primary !px-8 !py-4">Ver más proyectos {icon('arrow','w-5 h-5')}</a>
            </div>
        </div>
    </section>

    <!-- NOSOTROS -->
    <section id="nosotros" class="relative bg-white py-24 lg:py-32">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('¿Por qué IMECTEC?', 'Nuestros <span class="text-primary-600">diferenciadores</span>', 'Más de 10 años impulsando la industria peruana con ingeniería eléctrica y electromecánica para proyectos exigentes.', ic='badge')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
{diffs_html}
            </div>
        </div>
    </section>

    <!-- PREGUNTAS FRECUENTES -->
    <section id="preguntas" class="bg-slate-50 py-24 lg:py-32">
        <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            {section_head('Preguntas frecuentes', 'Resolvemos sus <span class="text-primary-600">dudas</span>', ic='chat')}
            <div class="reveal space-y-4">
                {faq_list(HOME_FAQS)}
            </div>
        </div>
    </section>

    <!-- CONTACTO -->
    <section id="contacto" class="relative overflow-hidden bg-brand-dark py-24 lg:py-32">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="grid gap-16 lg:grid-cols-2">
                <div class="reveal">
                    <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('mail','w-4 h-4')} Contacto</span>
                    <h2 class="mb-6 font-heading text-3xl font-extrabold tracking-tight text-white sm:text-4xl lg:text-5xl">¿Listo para su <span class="text-accent-300">proyecto?</span></h2>
                    <p class="mb-10 text-lg text-slate-300">Contáctenos y reciba una cotización en menos de 24 horas.</p>
                    <div class="space-y-4">
                        <a href="{wa()}" target="_blank" rel="noopener" data-track="contacto" class="group flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4 transition-all hover:border-green-400/50 hover:bg-white/10">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-green-500/20 text-green-400 transition-colors group-hover:bg-[#1fae53] group-hover:text-white">{solid(WA_PATH,'w-6 h-6')}</span>
                            <span><span class="block font-semibold text-white">WhatsApp · Respuesta inmediata</span><span class="block text-sm text-slate-400">{WA_DISPLAY}</span></span>
                            {icon('arrow','ml-auto w-5 h-5 text-slate-500 transition-all group-hover:translate-x-1 group-hover:text-white')}
                        </a>
                        <a href="mailto:{EMAIL}" data-track="contacto" class="group flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4 transition-all hover:border-accent-400/50 hover:bg-white/10">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-accent-400/20 text-accent-300 transition-colors group-hover:bg-accent-400 group-hover:text-navy-dark">{icon('mail')}</span>
                            <span><span class="block font-semibold text-white">Email · Cotizaciones formales</span><span class="block text-sm text-slate-400">{EMAIL}</span></span>
                            {icon('arrow','ml-auto w-5 h-5 text-slate-500 transition-all group-hover:translate-x-1 group-hover:text-white')}
                        </a>
                        <div class="flex items-center gap-4 rounded-xl border border-white/10 bg-white/5 p-4">
                            <span class="flex h-12 w-12 items-center justify-center rounded-xl bg-primary-400/20 text-primary-200">{icon('pin')}</span>
                            <span><span class="block font-semibold text-white">Cobertura</span><span class="block text-sm text-slate-400">Lima, Perú · Proyectos en todo el país</span></span>
                        </div>
                    </div>
                </div>
                <div class="reveal rounded-3xl bg-white p-8 shadow-2xl lg:p-10">
                    <h3 class="mb-2 font-heading text-2xl font-bold text-navy">Envíenos su solicitud</h3>
                    <p class="mb-6 text-sm text-slate-500">Al enviar se abrirá WhatsApp con su mensaje listo.</p>
                    <form id="contact-form" class="space-y-5">
                        <div class="grid gap-5 sm:grid-cols-2">
                            <div><label for="nombre" class="{label}">Nombre completo *</label><input type="text" id="nombre" name="nombre" autocomplete="name" required class="{field}" placeholder="Su nombre"></div>
                            <div><label for="empresa" class="{label}">Empresa</label><input type="text" id="empresa" name="empresa" autocomplete="organization" class="{field}" placeholder="Nombre de su empresa"></div>
                        </div>
                        <div class="grid gap-5 sm:grid-cols-2">
                            <div><label for="email" class="{label}">Email *</label><input type="email" id="email" name="email" autocomplete="email" required class="{field}" placeholder="correo@empresa.com"></div>
                            <div><label for="telefono" class="{label}">Teléfono *</label><input type="tel" id="telefono" name="telefono" autocomplete="tel" required class="{field}" placeholder="+51 999 999 999"></div>
                        </div>
                        <div><label for="servicio" class="{label}">Servicio de interés</label><select id="servicio" name="servicio" class="{field}"><option value="">Seleccione un servicio</option>{options}</select></div>
                        <div><label for="mensaje" class="{label}">Descripción del proyecto *</label><textarea id="mensaje" name="mensaje" rows="4" required class="{field} resize-none" placeholder="Cuéntenos sobre su proyecto o requerimiento: tensión, potencia, ubicación, plazos..."></textarea></div>
                        <label class="flex items-start gap-3 text-sm text-slate-500"><input type="checkbox" required class="mt-1 h-4 w-4 rounded border-slate-300 text-primary-600 focus:ring-accent-500"> <span>Acepto el tratamiento de mis datos según la <a href="politica-de-privacidad/" class="font-medium text-primary-700 underline">política de privacidad</a>.</span></label>
                        <button type="submit" class="btn-primary w-full !py-4">Enviar solicitud {solid(WA_PATH)}</button>
                    </form>
                    <div id="form-success" class="mt-6 hidden rounded-xl border border-green-200 bg-green-50 p-4" role="status">
                        <div class="flex items-center gap-3">{icon('check','w-6 h-6 text-green-600')}<div><p class="font-semibold text-green-800">¡Solicitud lista!</p><p class="text-sm text-green-700">Lo estamos llevando a WhatsApp para continuar la conversación.</p></div></div>
                    </div>
                </div>
            </div>
        </div>
    </section>
    </main>
"""
    html += footer(root, hp)
    write("index.html", html)


# =========================================================================== PÁGINAS DE SERVICIO
SERVICE_CONTENT = {
    "tableros-electricos": dict(
        title="Tableros Eléctricos BT/MT en Lima y Perú | Fabricación hasta 36 kV | IMECTEC",
        desc="Diseño, fabricación y ensamble de tableros eléctricos de baja y media tensión hasta 36 kV en Perú: distribución, control, ATS, CCM, arranque de motores y variadores. Garantía de 1 año.",
        h1="Tableros eléctricos BT/MT: diseño, fabricación y ensamble",
        kicker="Servicio · Tableros eléctricos",
        lead="Fabricamos tableros de distribución, control y potencia en baja y media tensión hasta 36 kV, a medida de su instalación, con protecciones bien coordinadas y documentación completa.",
        img="servicio-tableros", img_alt="Tablero eléctrico de baja tensión en fabricación en el taller de IMECTEC",
        includes=[
            ("layout", "Tableros de distribución", "Tableros generales y de distribución con interruptores, barras y protecciones dimensionadas para su carga."),
            ("calc", "Tableros de control", "Control y mando de procesos con relés, contactores, PLC y señalización."),
            ("bolt", "Transferencia automática (ATS)", "Conmutación red–grupo electrógeno para mantener la continuidad del suministro."),
            ("columns", "CCM y arranque de motores", "Centros de control de motores con arranque directo, estrella-triángulo, arrancador suave o variador."),
            ("chart", "Tableros de medición", "Medición de energía y parámetros eléctricos con analizadores de red."),
            ("doc", "Ingeniería y documentación", "Planos unifilares y de detalle, protocolos de pruebas y manual de operación."),
        ],
        apps=["Plantas industriales y manufactura", "Operaciones mineras", "Plantas de tratamiento y saneamiento", "Edificaciones y construcción", "Pesca y agroindustria", "Ampliación o reemplazo de tableros antiguos"],
        quote_data=["Tipo de tablero y su función", "Tensión de servicio y potencia o corriente nominal", "Diagrama unifilar o lista de cargas", "Grado de protección y lugar de instalación (interior/exterior)", "Marcas de equipos preferidas, si las hay", "Plazo requerido"],
        faqs=[HOME_FAQS[0], HOME_FAQS[3],
              ("¿Qué garantía tienen los tableros?", "Los tableros fabricados por IMECTEC tienen 1 año de garantía en fabricación.")],
        cta="Hola IMECTEC, necesito información sobre tableros eléctricos",
        related=["variadores-de-frecuencia", "automatizacion-plc-scada"],
    ),
    "mantenimiento-electrico": dict(
        title="Mantenimiento Eléctrico Industrial en Lima y Perú | Preventivo y Correctivo | IMECTEC",
        desc="Mantenimiento eléctrico preventivo, predictivo y correctivo para industria, minería y comercio en Perú: termografía, inspecciones, limpieza y ajustes. Contratos mensuales, trimestrales o semestrales.",
        h1="Mantenimiento eléctrico industrial preventivo y correctivo",
        kicker="Servicio · Mantenimiento eléctrico",
        lead="Evite paradas no programadas. Mantenemos sus sistemas eléctricos en condiciones seguras y confiables con planes preventivos, inspecciones predictivas y atención correctiva rápida.",
        img="servicio-mantenimiento", img_alt="Técnico de IMECTEC realizando mantenimiento en un tablero eléctrico",
        includes=[
            ("shield", "Mantenimiento preventivo", "Inspección, limpieza, ajuste de conexiones y verificación de protecciones según un plan programado."),
            ("search", "Termografía", "Detección de puntos calientes en tableros y conexiones antes de que provoquen una falla."),
            ("bolt", "Mantenimiento correctivo", "Diagnóstico y reparación de fallas eléctricas para restablecer la operación."),
            ("calc", "Pruebas eléctricas", "Mediciones de aislamiento, continuidad y verificación de equipos de protección."),
            ("clock", "Contratos de mantenimiento", "Frecuencia mensual, trimestral o semestral según sus necesidades."),
            ("doc", "Informes técnicos", "Reporte con hallazgos, fotos, mediciones y recomendaciones priorizadas."),
        ],
        apps=["Tableros generales y de distribución", "Centros de control de motores", "Plantas industriales", "Operaciones mineras", "Edificios comerciales", "Plantas de saneamiento"],
        quote_data=["Tipo de instalación y equipos a mantener", "Cantidad de tableros o equipos", "Ubicación de la planta", "Frecuencia deseada (único o contrato)", "Horarios disponibles para cortes de energía", "Último mantenimiento realizado, si lo conoce"],
        faqs=[HOME_FAQS[4],
              ("¿Qué es la termografía y para qué sirve?", "Es una inspección con cámara infrarroja que muestra la temperatura de conexiones y equipos. Permite detectar puntos calientes por conexiones flojas o sobrecargas antes de que causen una falla o un incendio."),
              ("¿Atienden emergencias?", "Sí. Atendemos emergencias y cotizaciones en menos de 24 horas. Escríbanos por WhatsApp para una respuesta inmediata.")],
        cta="Hola IMECTEC, necesito información sobre mantenimiento eléctrico",
        related=["subestaciones", "tableros-electricos"],
    ),
    "subestaciones": dict(
        title="Mantenimiento de Subestaciones Eléctricas en Perú | Preventivo y Predictivo | IMECTEC",
        desc="Mantenimiento preventivo y predictivo de subestaciones eléctricas en Perú: transformadores, celdas de media tensión, seccionadores, protecciones y puesta a tierra. Para minería, energía e industria.",
        h1="Mantenimiento de subestaciones eléctricas",
        kicker="Servicio · Subestaciones",
        lead="Mantenimiento preventivo y predictivo de subestaciones para asegurar la continuidad del suministro eléctrico de su operación, con personal calificado y estrictas medidas de seguridad.",
        img="galeria-03", img_alt="Técnico de IMECTEC trabajando en la estructura de una subestación eléctrica",
        includes=[
            ("bolt", "Transformadores", "Inspección, limpieza, ajustes y pruebas eléctricas de transformadores de potencia y distribución."),
            ("layout", "Celdas de media tensión", "Mantenimiento de celdas, interruptores, seccionadores y barras."),
            ("shield", "Protecciones", "Verificación de relés de protección y coordinación con el sistema."),
            ("globe", "Puesta a tierra", "Medición de resistencia de puesta a tierra y mejora del sistema cuando se requiere."),
            ("search", "Mantenimiento predictivo", "Termografía e inspecciones para anticipar fallas y planificar intervenciones."),
            ("doc", "Protocolos e informe", "Protocolos de pruebas, registro fotográfico y recomendaciones."),
        ],
        apps=["Subestaciones de operaciones mineras", "Centrales de generación", "Plantas industriales", "Plantas de saneamiento", "Subestaciones de edificaciones", "Ampliaciones y reubicaciones"],
        quote_data=["Ubicación de la subestación", "Nivel de tensión y potencia del transformador", "Tipo (convencional, compacta, intemperie)", "Equipos a intervenir", "Ventana de corte disponible", "Requisitos de seguridad del sitio"],
        faqs=[("¿Cada cuánto se debe hacer mantenimiento a una subestación?", "Depende del tipo de instalación, la carga y el entorno. Lo habitual es un mantenimiento preventivo al menos una vez al año, complementado con inspecciones predictivas como la termografía."),
              ("¿Trabajan en subestaciones de zonas alejadas?", "Sí. Atendemos proyectos en todo el Perú, incluyendo operaciones mineras en zonas alejadas."),
              HOME_FAQS[2]],
        cta="Hola IMECTEC, necesito información sobre mantenimiento de subestaciones",
        related=["mantenimiento-electrico", "tableros-electricos"],
    ),
    "automatizacion-plc-scada": dict(
        title="Automatización Industrial PLC, HMI y SCADA en Perú | IMECTEC",
        desc="Automatización industrial en Perú: programación de PLC, pantallas HMI y sistemas SCADA para control y supervisión remota de procesos en minería, saneamiento e industria.",
        h1="Automatización industrial con PLC, HMI y SCADA",
        kicker="Servicio · Automatización",
        lead="Automatizamos sus procesos para reducir errores y costos de operación: programación de PLC, pantallas HMI y sistemas SCADA con supervisión remota.",
        img="proyecto-03", img_alt="Técnico realizando pruebas en celdas de una sala eléctrica",
        includes=[
            ("calc", "Programación de PLC", "Lógica de control para arranque, secuencias, enclavamientos y alarmas."),
            ("layout", "Pantallas HMI", "Interfaces de operación claras para visualizar y controlar el proceso en campo."),
            ("chart", "Sistemas SCADA", "Supervisión centralizada, históricos, tendencias y alarmas de toda la planta."),
            ("globe", "Supervisión remota", "Acceso a la información del proceso desde la sala de control o a distancia."),
            ("columns", "Tableros de control", "Fabricación de tableros de automatización y cableado de instrumentación."),
            ("doc", "Pruebas y documentación", "Pruebas, puesta en marcha, capacitación y entrega de programas y planos."),
        ],
        apps=["Plantas de tratamiento de agua (PTAR/PTAP)", "Estaciones de bombeo", "Fajas transportadoras", "Procesos industriales", "Plantas mineras", "Modernización de sistemas antiguos"],
        quote_data=["Proceso a automatizar y su estado actual", "Equipos existentes (PLC, variadores, instrumentos)", "Cantidad aproximada de señales", "Necesidad de supervisión remota", "Ubicación de la planta", "Plazo requerido"],
        faqs=[("¿Qué beneficios tiene automatizar con PLC y SCADA?", "Permite operar de forma continua y segura, reducir errores manuales, registrar datos del proceso y supervisarlo a distancia."),
              ("¿Pueden modernizar un sistema de control antiguo?", "Sí. Evaluamos el sistema actual y proponemos la migración a PLC y HMI actuales, aprovechando lo que se pueda reutilizar."),
              ("¿Entregan los programas y la documentación?", "Sí. Entregamos planos, protocolos de pruebas y manuales de operación.")],
        cta="Hola IMECTEC, necesito información sobre automatización PLC/HMI",
        related=["variadores-de-frecuencia", "tableros-electricos"],
    ),
    "variadores-de-frecuencia": dict(
        title="Variadores de Frecuencia en Perú | Instalación y Puesta en Marcha | IMECTEC",
        desc="Instalación, configuración y puesta en marcha de variadores de frecuencia para control de motores en bombas, fajas y ventiladores. Ahorro de energía y arranques suaves. Perú.",
        h1="Variadores de frecuencia: instalación y puesta en marcha",
        kicker="Servicio · Variadores de frecuencia",
        lead="Controle la velocidad de sus motores y reduzca el consumo de energía. Instalamos, configuramos y ponemos en marcha variadores de frecuencia para bombas, fajas, ventiladores y compresores.",
        img="galeria-02", img_alt="Tablero de control con cableado y equipos de maniobra",
        includes=[
            ("search", "Evaluación y selección", "Análisis del motor y la carga para seleccionar el variador adecuado."),
            ("layout", "Tableros para variadores", "Fabricación de tableros con ventilación, protecciones y filtros necesarios."),
            ("calc", "Configuración", "Parametrización, rampas de aceleración y control PID de presión, caudal o nivel."),
            ("bolt", "Puesta en marcha", "Pruebas en vacío y con carga, ajuste fino y verificación de protecciones."),
            ("chart", "Ahorro energético", "Operación a la velocidad necesaria para reducir el consumo eléctrico."),
            ("doc", "Documentación", "Planos, parámetros configurados y manual de operación."),
        ],
        apps=["Bombas de agua y saneamiento", "Fajas transportadoras", "Ventiladores y extractores", "Compresores", "Procesos industriales", "Minería"],
        quote_data=["Potencia, tensión y corriente del motor (datos de placa)", "Tipo de carga (bomba, faja, ventilador…)", "Tipo de control deseado (velocidad fija, PID, remoto)", "Lugar de instalación del tablero", "Variador existente, si lo hay", "Plazo requerido"],
        faqs=[("¿Cuánta energía se puede ahorrar con un variador?", "Depende de la aplicación. En bombas y ventiladores que no necesitan trabajar siempre al 100% el ahorro puede ser importante; en uno de nuestros proyectos con fajas transportadoras logramos una reducción del 35% en consumo eléctrico."),
              ("¿Qué es el control PID en un variador?", "Es un control automático que ajusta la velocidad del motor para mantener una variable, como la presión o el nivel, en el valor deseado."),
              ("¿Instalan variadores de cualquier marca?", "Trabajamos con las principales marcas del mercado y le recomendamos la opción más adecuada para su aplicación.")],
        cta="Hola IMECTEC, necesito información sobre variadores de frecuencia",
        related=["automatizacion-plc-scada", "tableros-electricos"],
    ),
}


def build_service(slug):
    c = SERVICE_CONTENT[slug]
    name = next(n for s, n, _ in SERVICE_PAGES if s == slug)
    root, hp = "../", "../"
    url = f"{SITE}/{slug}/"
    ld = jsonld([
        org_schema(),
        {"@type": "Service", "@id": url + "#servicio", "name": name, "serviceType": name, "description": c["desc"], "url": url,
         "provider": {"@id": ORG_ID}, "areaServed": {"@type": "Country", "name": "Perú"}, "image": f"{SITE}/images/web/{c['img']}.jpg"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Servicios", "item": SITE + "/#servicios"},
            {"@type": "ListItem", "position": 3, "name": name, "item": url}]},
        faq_schema(c["faqs"]),
    ])
    includes = "\n".join(f"""                <div class="reveal card card-hover p-7">
                    <div class="icon-tile mb-5 !h-12 !w-12">{icon(ic,'w-6 h-6')}</div>
                    <h3 class="mb-2 font-heading text-lg font-bold text-navy">{t}</h3>
                    <p class="text-slate-600">{d}</p>
                </div>""" for ic, t, d in c["includes"])
    apps = "\n".join(f'                    <li class="flex items-start gap-3 text-slate-200">{icon("check","w-6 h-6 flex-shrink-0 text-accent-300")}<span>{a}</span></li>' for a in c["apps"])
    qd = "\n".join(f'                        <li class="flex items-start gap-3">{icon("check","w-5 h-5 mt-0.5 flex-shrink-0 text-primary-600")}<span>{a}</span></li>' for a in c["quote_data"])
    related = "\n".join(f"""                <a href="../{s}/" class="card card-hover group flex items-center gap-4 p-6">
                    <span class="icon-tile !h-12 !w-12">{icon(ic,'w-6 h-6')}</span>
                    <span class="flex-1 font-heading text-lg font-bold text-navy">{n}</span>
                    {icon('arrow','w-5 h-5 text-primary-600 transition-transform group-hover:translate-x-1')}
                </a>""" for s, n, ic in SERVICE_PAGES if s in c["related"])

    html = head(title=c["title"], description=c["desc"], path=f"/{slug}/", root=root, jsonld_html=ld)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido">
    <section class="relative overflow-hidden bg-brand-dark pb-20 pt-32 lg:pb-28 lg:pt-40">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto grid max-w-7xl items-center gap-12 px-4 sm:px-6 lg:grid-cols-2 lg:px-8">
            <div>
                <nav aria-label="Ruta de navegación" class="mb-6 text-sm text-slate-400">
                    <ol class="flex flex-wrap items-center gap-2"><li><a href="../" class="hover:text-white">Inicio</a></li><li aria-hidden="true">/</li><li><a href="../#servicios" class="hover:text-white">Servicios</a></li><li aria-hidden="true">/</li><li class="text-accent-300" aria-current="page">{name}</li></ol>
                </nav>
                <p class="mb-3 text-sm font-semibold uppercase tracking-[.18em] text-accent-300">{c['kicker']}</p>
                <h1 class="mb-6 font-heading text-4xl font-extrabold leading-tight tracking-tight text-white sm:text-5xl">{c['h1']}</h1>
                <p class="mb-8 text-lg leading-relaxed text-slate-300">{c['lead']}</p>
                <div class="flex flex-col gap-4 sm:flex-row">
                    <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="hero_{slug}" class="btn-whatsapp !px-7 !py-4">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                    <a href="mailto:{EMAIL}?subject={name.replace(' ','%20')}" data-track="hero_{slug}" class="btn-ghost !px-7 !py-4">{icon('mail','w-5 h-5')} {EMAIL}</a>
                </div>
            </div>
            <div class="relative">
                <div class="absolute -inset-3 rounded-3xl bg-gradient-to-br from-accent-400/40 to-primary-500/30 blur-2xl"></div>
                {img(c['img'], c['img_alt'], 1000, 750, 'relative aspect-[4/3] w-full rounded-3xl object-cover shadow-2xl ring-1 ring-white/10', lazy=False, prefix='../')}
            </div>
        </div>
    </section>

    <section class="py-20 lg:py-28">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            {section_head('Qué incluye', f'Alcance del servicio', ic='clipboard')}
            <div class="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
{includes}
            </div>
        </div>
    </section>

    <section class="relative overflow-hidden bg-brand-dark py-20 lg:py-24">
        <div class="bg-grid absolute inset-0"></div>
        <div class="relative mx-auto grid max-w-7xl gap-12 px-4 sm:px-6 lg:grid-cols-2 lg:px-8">
            <div class="reveal">
                <span class="eyebrow mb-4 bg-white/10 text-accent-300">{icon('building','w-4 h-4')} Aplicaciones</span>
                <h2 class="mb-8 font-heading text-3xl font-extrabold text-white sm:text-4xl">¿Dónde aplicamos este servicio?</h2>
                <ul class="grid gap-4 sm:grid-cols-2">
{apps}
                </ul>
            </div>
            <div class="reveal rounded-3xl bg-white p-8 shadow-2xl lg:p-10">
                <h2 class="mb-2 font-heading text-2xl font-bold text-navy">¿Qué necesitamos para cotizar?</h2>
                <p class="mb-6 text-slate-500">Con esta información le enviamos una propuesta más rápida y precisa. Si no la tiene completa, le ayudamos a levantarla.</p>
                <ul class="mb-8 space-y-3 text-slate-700">
{qd}
                </ul>
                <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="datos_{slug}" class="btn-whatsapp w-full">{solid(WA_PATH)} Enviar datos por WhatsApp</a>
            </div>
        </div>
    </section>

    <section class="bg-white py-20 lg:py-28">
        <div class="mx-auto max-w-4xl px-4 sm:px-6 lg:px-8">
            {section_head('Preguntas frecuentes', 'Dudas <span class="text-primary-600">frecuentes</span>', ic='chat')}
            <div class="reveal space-y-4">
                {faq_list(c['faqs'])}
            </div>
        </div>
    </section>

    <section class="bg-slate-50 py-20">
        <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <div class="reveal mb-12 overflow-hidden rounded-3xl bg-gradient-to-r from-navy via-primary-700 to-primary-600 p-10 text-center shadow-xl lg:p-14">
                <h2 class="mb-4 font-heading text-3xl font-extrabold text-white sm:text-4xl">¿Listo para su <span class="text-accent-300">proyecto?</span></h2>
                <p class="mx-auto mb-8 max-w-2xl text-lg text-white/90">Contáctenos y reciba una cotización en menos de 24 horas.</p>
                <div class="flex flex-col justify-center gap-4 sm:flex-row">
                    <a href="{wa(c['cta'])}" target="_blank" rel="noopener" data-track="cta_{slug}" class="btn-accent">{solid(WA_PATH)} Cotizar por WhatsApp</a>
                    <a href="../#contacto" class="btn-ghost">Ir al formulario</a>
                </div>
            </div>
            <h2 class="mb-6 font-heading text-xl font-bold text-navy">Servicios relacionados</h2>
            <div class="grid gap-6 md:grid-cols-2">
{related}
            </div>
        </div>
    </section>
    </main>
"""
    html += footer(root, hp)
    write(f"{slug}/index.html", html)


# =========================================================================== PRIVACIDAD
def build_privacy():
    root, hp = "../", "../"
    html = head(title="Política de Privacidad | IMECTEC", description="Política de privacidad y tratamiento de datos personales de IMECTEC Ingeniería & Proyectos S.A.C., conforme a la Ley N.° 29733 del Perú.",
                path="/politica-de-privacidad/", root=root)
    html += navbar(root, hp)
    html += f"""
    <main id="contenido" class="bg-white pb-24 pt-32 lg:pt-40">
        <article class="prose-ing mx-auto max-w-3xl px-4 sm:px-6 lg:px-8">
            <h1 class="mb-4 font-heading text-4xl font-extrabold text-navy">Política de privacidad</h1>
            <p class="!text-base !text-slate-500">Última actualización: {date.today().strftime('%d/%m/%Y')}</p>
            <p>En IMECTEC Ingeniería &amp; Proyectos S.A.C. (en adelante, "IMECTEC") respetamos la privacidad de las personas que nos contactan. Esta política explica cómo tratamos los datos personales que recibimos a través de este sitio web, de acuerdo con la Ley N.° 29733, Ley de Protección de Datos Personales, y su reglamento.</p>
            <h2>1. Datos que recopilamos</h2>
            <p>Cuando usa nuestro formulario de contacto o nos escribe por WhatsApp o correo electrónico, podemos recibir su nombre, empresa, correo electrónico, teléfono, el servicio de su interés y el contenido de su mensaje.</p>
            <h2>2. Finalidad</h2>
            <p>Usamos estos datos únicamente para responder sus consultas, preparar cotizaciones y propuestas técnicas, y mantener la comunicación relacionada con los servicios que solicita. No vendemos ni cedemos sus datos a terceros con fines comerciales.</p>
            <h2>3. Cómo se envía el formulario</h2>
            <p>El formulario de este sitio no almacena información en nuestro servidor: al enviarlo, se abre WhatsApp con su mensaje para que lo envíe directamente. El uso de WhatsApp está sujeto a las condiciones y políticas de privacidad de dicho servicio.</p>
            <h2>4. Medición y cookies</h2>
            <p>Utilizamos herramientas de Google (como Google Ads y, de ser el caso, Google Analytics) para medir de forma agregada el uso del sitio y la efectividad de nuestros anuncios. Estas herramientas pueden usar cookies. Puede bloquearlas o eliminarlas desde la configuración de su navegador.</p>
            <h2>5. Conservación</h2>
            <p>Conservamos sus datos solo durante el tiempo necesario para atender su solicitud y la relación comercial que de ella se derive, o el plazo que exija la ley.</p>
            <h2>6. Sus derechos</h2>
            <p>Puede ejercer sus derechos de acceso, rectificación, cancelación y oposición (derechos ARCO) escribiendo a <a href="mailto:{EMAIL}" class="font-semibold text-primary-700 underline">{EMAIL}</a>, indicando su nombre y el derecho que desea ejercer.</p>
            <h2>7. Contacto</h2>
            <p>Para cualquier consulta sobre esta política, escríbanos a <a href="mailto:{EMAIL}" class="font-semibold text-primary-700 underline">{EMAIL}</a> o al WhatsApp {WA_DISPLAY}.</p>
        </article>
    </main>
"""
    html += footer(root, hp)
    write("politica-de-privacidad/index.html", html)


def build_404():
    root = "/"
    html = head(title="Página no encontrada | IMECTEC", description="La página que busca no existe.", path="/404.html", root=root)
    html = html.replace('content="index, follow, max-image-preview:large"', 'content="noindex"')
    html += navbar(root, "/")
    html += f"""
    <main id="contenido" class="flex min-h-[70vh] items-center bg-brand-dark px-4 pb-20 pt-32">
        <div class="mx-auto max-w-xl text-center">
            <img src="/images/logo-256.png" alt="" width="128" height="128" class="mx-auto mb-8 h-28 w-28">
            <p class="mb-2 font-heading text-6xl font-extrabold text-accent-300">404</p>
            <h1 class="mb-4 font-heading text-3xl font-bold text-white">Página no encontrada</h1>
            <p class="mb-8 text-slate-300">Es posible que el enlace haya cambiado. Vuelva al inicio o escríbanos directamente.</p>
            <div class="flex flex-col justify-center gap-4 sm:flex-row">
                <a href="/" class="btn-accent">Ir al inicio</a>
                <a href="{wa()}" target="_blank" rel="noopener" data-track="404" class="btn-whatsapp">{solid(WA_PATH)} WhatsApp</a>
            </div>
        </div>
    </main>
"""
    html += footer(root, "/")
    write("404.html", html)


def build_seo_files():
    today = date.today().isoformat()
    urls = [("/", "1.0")] + [(f"/{s}/", "0.9") for s, _, _ in SERVICE_PAGES] + [("/politica-de-privacidad/", "0.3")]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{today}</lastmod><priority>{p}</priority></url>\n" for u, p in urls)
    sm += "</urlset>\n"
    write("sitemap.xml", sm)
    bots = ["Googlebot", "Bingbot", "Google-Extended", "GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User",
            "PerplexityBot", "Perplexity-User", "Applebot", "Applebot-Extended", "Amazonbot", "meta-externalagent", "DuckAssistBot", "CCBot"]
    robots = "# Buscadores y asistentes de IA: bienvenidos. Queremos que encuentren y citen a IMECTEC.\n"
    robots += "".join(f"User-agent: {b}\n" for b in bots) + "Allow: /\n\n"
    robots += "User-agent: *\nAllow: /\nDisallow: /tools/\nDisallow: /src/\n\n"
    robots += f"Sitemap: {SITE}/sitemap.xml\n"
    write("robots.txt", robots)
    write("llms.txt", build_llms_txt())


def build_llms_txt():
    """Resumen en texto plano para asistentes de IA (estándar llms.txt)."""
    L = ["# IMECTEC Ingeniería & Proyectos S.A.C.", "",
         "> Empresa peruana de ingeniería eléctrica y electromecánica: diseño, fabricación y ensamble de tableros eléctricos BT/MT hasta 36 kV, "
         "mantenimiento eléctrico industrial, mantenimiento de subestaciones, variadores de frecuencia, automatización PLC/HMI/SCADA, protecciones y sincronismo, "
         "puesta a tierra, canalización y cableado, e ingeniería de detalle, para industria, minería, energía, saneamiento, construcción, pesca e hidrocarburos en todo el Perú.", "",
         "- Ubicación: Lima, Perú. Atiende proyectos en todo el Perú.",
         f"- WhatsApp: {WA_DISPLAY} · Email: {EMAIL} · Web: {SITE}/",
         "- Garantía: 1 año en fabricación de tableros; de 6 meses a 1 año en instalaciones según el trabajo.",
         "- Atención de emergencias y cotizaciones en menos de 24 horas.", "",
         "## Servicios"]
    for slug, name, _ in SERVICE_PAGES:
        L.append(f"- [{name}]({SITE}/{slug}/): {SERVICE_CONTENT[slug]['desc']}")
    L += ["- Protecciones y sincronismo; puesta a tierra y pararrayos; canalización y cableado; ingeniería de detalle (cálculos, memorias, planos unifilares).", "",
          "## Casos de éxito"]
    for _, sec, t, pb, so, rs, _a in PROJECTS:
        L.append(f"- {t} (sector {sec}): {pb} Solución: {so} Resultado: {rs}")
    L += ["", "## Preguntas frecuentes"]
    for q, a in HOME_FAQS:
        L.append(f"- {q} {a}")
    L += ["", "## Empresa relacionada",
          "- INGDELCA Ingeniería & Consultoría S.A.C. (https://ingdelca.com): ingeniería y obras hidráulicas, topografía con dron, modelamiento, defensas ribereñas y sistemas de bombeo. Certificada ISO 9001, 14001, 45001 y 37001."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    build_home()
    for s, _, _ in SERVICE_PAGES:
        build_service(s)
    build_privacy()
    build_404()
    build_seo_files()
