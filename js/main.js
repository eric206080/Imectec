/* ==========================================================================
   IMECTEC - Script principal
   ========================================================================== */

/* ---------- 1. CONFIGURACIÓN DE MEDICIÓN (Google Analytics 4 / Google Ads) ----------
   La etiqueta de Google Ads (AW-17952331494) ya está instalada en el <head> de cada página.
   Aquí solo agregas el ID de GA4 si lo creas, y la etiqueta de conversión de Ads.
   - GA4:        Google Analytics > Administrar > Flujos de datos > ID de medición (G-XXXXXXXXXX)
   - Google Ads: Herramientas > Conversiones > Etiqueta de Google (AW-XXXXXXXXX)
   - ADS_LEAD_LABEL: etiqueta de la conversión "Contacto/Lead" (opcional, ej. 'AbC-D_efG12')   */
const GA4_ID = '';
const ADS_ID = 'AW-17952331494';
const ADS_LEAD_LABEL = '';

(function loadAnalytics() {
  // La etiqueta de Google (gtag.js) ya se carga en el <head>; aquí solo se agrega GA4 si existe.
  if (typeof window.gtag !== 'function') return;
  if (GA4_ID) gtag('config', GA4_ID);
})();

/** Registra un evento (WhatsApp, email, formulario...) en GA4 y como conversión en Ads */
function track(eventName, params = {}) {
  if (typeof window.gtag !== 'function') return;
  gtag('event', eventName, params);
  if (ADS_ID && ADS_LEAD_LABEL && ['whatsapp_click', 'generate_lead', 'email_click', 'phone_click'].includes(eventName)) {
    gtag('event', 'conversion', { send_to: ADS_ID + '/' + ADS_LEAD_LABEL });
  }
}

document.documentElement.classList.add('js');

document.addEventListener('DOMContentLoaded', () => {
  /* ---------- 2. Menú móvil ---------- */
  const menu = document.getElementById('mobile-menu');
  const overlay = document.getElementById('mobile-menu-overlay');
  const openBtn = document.getElementById('mobile-menu-btn');
  const closeBtn = document.getElementById('mobile-menu-close');
  const setMenu = (open) => {
    if (!menu) return;
    menu.dataset.open = overlay.dataset.open = String(open);
    menu.setAttribute('aria-hidden', String(!open));
    openBtn?.setAttribute('aria-expanded', String(open));
    document.body.style.overflow = open ? 'hidden' : '';
  };
  openBtn?.addEventListener('click', () => setMenu(true));
  closeBtn?.addEventListener('click', () => setMenu(false));
  overlay?.addEventListener('click', () => setMenu(false));
  menu?.querySelectorAll('a').forEach((a) => a.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') setMenu(false); });

  /* ---------- 3. Navbar y botón "volver arriba" ---------- */
  const navbar = document.getElementById('navbar');
  const toTop = document.getElementById('back-to-top');
  const onScroll = () => {
    const y = window.scrollY;
    navbar?.classList.toggle('shadow-lg', y > 40);
    navbar?.classList.toggle('bg-white', y > 40);
    if (toTop) {
      toTop.classList.toggle('opacity-0', y <= 600);
      toTop.classList.toggle('invisible', y <= 600);
    }
  };
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
  toTop?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  /* ---------- 4. Aparición suave al hacer scroll ---------- */
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-visible'));
  }

  /* ---------- 5. Videos del inicio (mismos videos, carga optimizada) ---------- */
  const video = document.getElementById('hero-video');
  if (video) {
    const sources = (video.dataset.sources || '').split(',').filter(Boolean);
    const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    const saveData = navigator.connection && navigator.connection.saveData;
    let idx = 0;
    const playCurrent = () => {
      video.src = sources[idx];
      video.load();
      video.play().catch(() => {});
    };
    if (!reduceMotion && !saveData && sources.length) {
      // Se carga después de la página para no retrasar la primera vista
      const start = () => { playCurrent(); video.addEventListener('playing', () => { video.style.opacity = '1'; }); };
      if (document.readyState === 'complete') start(); else window.addEventListener('load', start, { once: true });
      // Cambia de video cuando termina el actual (no lo corta a la mitad)
      video.addEventListener('ended', () => {
        video.style.opacity = '0';
        setTimeout(() => { idx = (idx + 1) % sources.length; playCurrent(); }, 500);
      });
      // Pausa cuando el hero no está a la vista (ahorra datos y batería)
      if ('IntersectionObserver' in window) {
        new IntersectionObserver(([en]) => {
          if (en.isIntersecting) video.play().catch(() => {}); else video.pause();
        }).observe(video);
      }
    }
  }

  /* ---------- 6. Formulario -> WhatsApp ---------- */
  const form = document.getElementById('contact-form');
  const ok = document.getElementById('form-success');
  form?.addEventListener('submit', (e) => {
    e.preventDefault();
    const v = (id) => (document.getElementById(id)?.value || '').trim();
    const lines = [
      'Hola IMECTEC, me contacto desde su web:', '',
      '*Nombre:* ' + v('nombre'),
      v('empresa') ? '*Empresa:* ' + v('empresa') : null,
      '*Email:* ' + v('email'),
      v('telefono') ? '*Teléfono:* ' + v('telefono') : null,
      v('servicio') ? '*Servicio de interés:* ' + v('servicio') : null,
      '', '*Mensaje:*', v('mensaje')
    ].filter((l) => l !== null);
    const url = 'https://wa.me/51980038307?text=' + encodeURIComponent(lines.join('\n'));
    track('generate_lead', { method: 'formulario_web', service: v('servicio') || 'sin_especificar' });
    ok?.classList.remove('hidden');
    setTimeout(() => window.open(url, '_blank', 'noopener'), 700);
    setTimeout(() => { form.reset(); ok?.classList.add('hidden'); }, 4000);
  });

  /* ---------- 7. Medición de clics de contacto ---------- */
  document.addEventListener('click', (e) => {
    const a = e.target.closest('a[href]');
    if (!a) return;
    const href = a.getAttribute('href');
    const where = a.dataset.track || 'enlace';
    if (href.includes('wa.me/')) track('whatsapp_click', { location: where });
    else if (href.startsWith('mailto:')) track('email_click', { location: where });
    else if (href.startsWith('tel:')) track('phone_click', { location: where });
  });

  /* ---------- 8. Año actual en el pie de página ---------- */
  document.querySelectorAll('[data-year]').forEach((el) => { el.textContent = new Date().getFullYear(); });
});
