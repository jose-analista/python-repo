/**
 * Sistema de temas WasapMarke
 * Modos: claro, oscuro, aleatorio (genera paleta única cada vez)
 */
(function () {
  'use strict';

  const TEMA_KEY = 'wasapmarke-tema';
  const SEMILLA_KEY = 'wasapmarke-semilla'; // Guarda el hue para consistencia
  const TEMAS = ['claro', 'oscuro', 'aleatorio'];

  const ICONOS = {
    claro: '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
    oscuro: '<svg class="ico" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    aleatorio: '<svg class="ico" viewBox="0 0 24 24"><path d="M16 3h5v5M4 20L21 3M21 16v5h-5M15 15l6 6M4 4l5 5"/></svg>'
  };

  /**
   * Genera un número aleatorio entre min y max
   */
  function random(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  /**
   * Convierte HSL a string CSS
   */
  function hsl(h, s, l) {
    return `hsl(${h}, ${s}%, ${l}%)`;
  }

  /**
   * Genera una paleta de colores coherente a partir de un hue base
   * Los colores derivados se calculan matemáticamente para que siempre combinen
   */
  function generarPaleta(hue) {
    return {
      // Color principal (verde de la app → ahora es el color aleatorio)
      '--verde': hsl(hue, 55, 35),
      '--verde-osc': hsl(hue, 60, 25),
      '--verde-claro': hsl(hue, 40, 88),

      // Colores de acento (complementarios)
      '--peligro': hsl((hue + 150) % 360, 65, 45),
      '--peligro-claro': hsl((hue + 150) % 360, 60, 92),
      '--aviso': hsl((hue + 40) % 360, 70, 40),
      '--aviso-claro': hsl((hue + 40) % 360, 65, 90),

      // Fondos y superficies
      '--papel': hsl(hue, 15, 94),
      '--superficie': '#ffffff',
      '--chat': hsl(hue, 40, 15),
      '--burbuja': hsl(hue, 45, 85),

      // Textos y bordes
      '--tinta': hsl(hue, 30, 12),
      '--suave': hsl(hue, 15, 45),
      '--borde': hsl(hue, 20, 85),

      // Variables derivadas
      '--fondo-body': hsl(hue, 15, 94),
      '--texto-principal': hsl(hue, 30, 12),
      '--texto-secundario': hsl(hue, 15, 45),
      '--sombra-suave': `hsla(${hue}, 20%, 15%, 0.06)`,
      '--sombra-fuerte': `hsla(${hue}, 20%, 15%, 0.14)`,
      '--icono-sidebar': hsl(hue, 15, 45),
      '--focus-ring': `hsla(${hue}, 55%, 35%, 0.45)`,
    };
  }

  /**
   * Aplica una paleta al documento via CSS custom properties
   */
  function aplicarPaleta(paleta) {
    const root = document.documentElement;
    Object.entries(paleta).forEach(([prop, valor]) => {
      root.style.setProperty(prop, valor);
    });
  }

  /**
   * Limpia las variables inline (vuelve al CSS por defecto)
   */
  function limpiarPaleta() {
    const root = document.documentElement;
    const props = [
      '--verde', '--verde-osc', '--verde-claro',
      '--peligro', '--peligro-claro', '--aviso', '--aviso-claro',
      '--papel', '--superficie', '--chat', '--burbuja',
      '--tinta', '--suave', '--borde',
      '--fondo-body', '--texto-principal', '--texto-secundario',
      '--sombra-suave', '--sombra-fuerte', '--icono-sidebar', '--focus-ring'
    ];
    props.forEach(prop => root.style.removeProperty(prop));
  }

  /**
   * Genera un hue aleatorio (evita tonos muy cercanos al gris)
   */
  function generarHueAleatorio() {
    // Evita saturaciones muy bajas (grises) y muy altas (neón)
    return random(0, 360);
  }

  /**
   * Aplica el tema seleccionado
   */
  function aplicarTema(tema) {
    if (tema === 'aleatorio') {
      // Generar nuevo hue o reusar el guardado
      let hue = localStorage.getItem(SEMILLA_KEY);
      if (!hue) {
        hue = generarHueAleatorio();
        localStorage.setItem(SEMILLA_KEY, hue);
      } else {
        hue = parseInt(hue, 10);
      }
      aplicarPaleta(generarPaleta(hue));
      document.documentElement.setAttribute('data-theme', 'aleatorio');
    } else {
      // Claro u oscuro: limpiar variables inline y usar CSS puro
      limpiarPaleta();
      document.documentElement.setAttribute('data-theme', tema);
    }
    actualizarBoton(tema);
  }

  /**
   * Actualiza el botón de tema
   */
  function actualizarBoton(tema) {
    const btn = document.getElementById('btn-toggle-tema');
    if (!btn) return;
    const etiquetas = { claro: 'Modo Claro', oscuro: 'Modo Oscuro', aleatorio: 'Color Aleatorio' };
    btn.innerHTML = `${ICONOS[tema]} ${etiquetas[tema]}`;
  }

  /**
   * Obtiene el tema guardado
   */
  function obtenerTema() {
    const guardado = localStorage.getItem(TEMA_KEY);
    return TEMAS.includes(guardado) ? guardado : 'claro';
  }

  /**
   * Rota al siguiente tema
   */
  function rotarTema() {
    const actual = obtenerTema();
    const indice = TEMAS.indexOf(actual);
    const siguiente = TEMAS[(indice + 1) % TEMAS.length];
    
    // Si pasa a aleatorio, generar nueva semilla
    if (siguiente === 'aleatorio') {
      localStorage.removeItem(SEMILLA_KEY); // Forzar nuevo color
    }
    
    localStorage.setItem(TEMA_KEY, siguiente);
    aplicarTema(siguiente);
  }

  /**
   * Fuerza un nuevo color aleatorio (botón "refresh")
   */
  function nuevoColorAleatorio() {
    if (obtenerTema() !== 'aleatorio') return;
    localStorage.removeItem(SEMILLA_KEY);
    aplicarTema('aleatorio');
  }

  /**
   * Inicialización
   */
  function init() {
    const temaInicial = obtenerTema();
    
    // Aplicar inmediatamente para evitar flash
    if (temaInicial === 'aleatorio') {
      const hue = localStorage.getItem(SEMILLA_KEY) || generarHueAleatorio();
      if (!localStorage.getItem(SEMILLA_KEY)) {
        localStorage.setItem(SEMILLA_KEY, hue);
      }
      aplicarPaleta(generarPaleta(parseInt(hue, 10)));
      document.documentElement.setAttribute('data-theme', 'aleatorio');
    } else {
      document.documentElement.setAttribute('data-theme', temaInicial);
    }

    document.addEventListener('DOMContentLoaded', () => {
      actualizarBoton(temaInicial);

      const btn = document.getElementById('btn-toggle-tema');
      if (btn) {
        btn.addEventListener('click', rotarTema);
      }

      // Botón opcional para refrescar color (si existe)
      const btnRefresh = document.getElementById('btn-nuevo-color');
      if (btnRefresh) {
        btnRefresh.addEventListener('click', nuevoColorAleatorio);
      }
    });
  }

  init();
})();