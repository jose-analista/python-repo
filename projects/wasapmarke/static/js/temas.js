/**
 * Sistema de temas para WasapMarke
 * Soporta: claro, oscuro y automático (según preferencia del sistema)
 * La preferencia se guarda en localStorage
 */
(function () {
  'use strict';

  const TEMA_KEY = 'wasapmarke-tema';
  const TEMAS = ['claro', 'oscuro', 'auto'];
  const ICONOS = {
    claro: '<svg class="ico" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M4.93 19.07l1.41-1.41M17.66 6.34l1.41-1.41"/></svg>',
    oscuro: '<svg class="ico" viewBox="0 0 24 24"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>',
    auto: '<svg class="ico" viewBox="0 0 24 24"><rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8M12 17v4"/></svg>'
  };

  /**
   * Detecta el tema efectivo (resuelve "auto" según el sistema)
   */
  function temaEfectivo(tema) {
    if (tema === 'auto') {
      return window.matchMedia('(prefers-color-scheme: oscuro)').matches ? 'oscuro' : 'claro';
    }
    return tema;
  }

  /**
   * Aplica el tema al documento
   */
  function aplicarTema(tema) {
    const efectivo = temaEfectivo(tema);
    document.documentElement.setAttribute('data-theme', efectivo);
    actualizarBoton(tema);
  }

  /**
   * Actualiza el texto e icono del botón de tema
   */
  function actualizarBoton(tema) {
    const btn = document.getElementById('btn-toggle-tema');
    if (!btn) return;

    const etiquetas = { claro: 'Modo Claro', oscuro: 'Modo Oscuro', auto: 'Automático' };
    btn.innerHTML = `${ICONOS[tema]} ${etiquetas[tema]}`;
  }

  /**
   * Obtiene el tema guardado o el default
   */
  function obtenerTema() {
    const guardado = localStorage.getItem(TEMA_KEY);
    return TEMAS.includes(guardado) ? guardado : 'auto';
  }

  /**
   * Cambia al siguiente tema en el ciclo
   */
  function rotarTema() {
    const actual = obtenerTema();
    const indice = TEMAS.indexOf(actual);
    const siguiente = TEMAS[(indice + 1) % TEMAS.length];
    localStorage.setItem(TEMA_KEY, siguiente);
    aplicarTema(siguiente);
  }

  /**
   * Inicializa el sistema de temas
   */
  function init() {
    // Aplicar tema inicial SIN flash (antes de que se renderice)
    const temaInicial = obtenerTema();
    document.documentElement.setAttribute('data-theme', temaEfectivo(temaInicial));

    // Cuando el DOM esté listo, configurar el botón
    document.addEventListener('DOMContentLoaded', () => {
      actualizarBoton(temaInicial);

      const btn = document.getElementById('btn-toggle-tema');
      if (btn) {
        btn.addEventListener('click', rotarTema);
      }

      // Escuchar cambios en la preferencia del sistema (si está en "auto")
      window.matchMedia('(prefers-color-scheme: oscuro)').addEventListener('change', (e) => {
        if (obtenerTema() === 'auto') {
          aplicarTema('auto');
        }
      });
    });
  }

  // Ejecutar inmediatamente para evitar flash
  init();
})();