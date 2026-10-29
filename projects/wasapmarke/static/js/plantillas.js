/**
 * Sistema de Plantillas Rápidas para WasapMarke
 * Categorías: Ventas, Soporte, Cobranza, Seguimiento, Agradecimiento, Recordatorio
 */
(function () {
  'use strict';

  // ============================================
  // BASE DE DATOS DE PLANTILLAS
  // ============================================
  const PLANTILLAS = {
    ventas: {
      etiqueta: '🛒 Ventas',
      items: [
        {
          nombre: '👋 Saludo inicial',
          texto: '¡Hola {nombre}! 👋 Soy [Tu nombre] de [Tu empresa]. ¿En qué puedo ayudarte hoy? '
        },
        {
          nombre: '🎯 Presentación producto',
          texto: 'Hola {nombre} 🌟 Te comparto info sobre nuestro producto estrella. ¿Te gustaría conocer los detalles? 📦✨'
        },
        {
          nombre: '💰 Oferta especial',
          texto: '¡{nombre}!  Tenemos una oferta exclusiva para ti: 20% de descuento solo hoy. ¿Te interesa? 🔥💸'
        },
        {
          nombre: '📋 Cotización',
          texto: 'Hola {nombre} 📊 Te envío la cotización que solicitaste. Quedo atento a tus dudas. ¿Agendamos una llamada? 📞'
        },
        {
          nombre: '🤝 Cierre de venta',
          texto: '¡Excelente {nombre}! 🎊 Confirmo tu pedido. Te envío los datos de pago. ¡Gracias por confiar en nosotros! 💚'
        }
      ]
    },
    soporte: {
      etiqueta: '🛠️ Soporte',
      items: [
        {
          nombre: '🔧 Bienvenida soporte',
          texto: 'Hola {nombre} ‍♂️ Soy del equipo de soporte. Cuéntame, ¿qué problema tienes? Estoy aquí para ayudarte. 💪'
        },
        {
          nombre: ' En proceso',
          texto: '{nombre}, ya estoy revisando tu caso 🔍 Te doy una respuesta en breve. ¡Gracias por tu paciencia! ️'
        },
        {
          nombre: '✅ Problema resuelto',
          texto: '¡{nombre}! ✅ Tu problema ha sido resuelto. ¿Hay algo más en lo que pueda ayudarte? 😊'
        },
        {
          nombre: ' Escalar caso',
          texto: '{nombre}, para darte mejor atención voy a pasar tu caso con un especialista 🧑‍ Te contactará en menos de 1 hora. 🕐'
        },
        {
          nombre: '📝 Seguimiento',
          texto: 'Hola {nombre} 👋 Quería saber si todo sigue funcionando bien después de nuestra última conversación. ¿Necesitas algo más? 🤔'
        }
      ]
    },
    cobranza: {
      etiqueta: '💵 Cobranza',
      items: [
        {
          nombre: '🔔 Recordatorio suave',
          texto: 'Hola {nombre} 😊 Te recuerdo que tienes una factura pendiente. ¿Puedes revisar cuando tengas un momento? Gracias 🙏'
        },
        {
          nombre: '⚠️ Segundo aviso',
          texto: '{nombre}, tu pago sigue pendiente 📋 Por favor regulariza tu situación para evitar inconvenientes. ¿Necesitas ayuda? 💬'
        },
        {
          nombre: '📄 Envío de factura',
          texto: 'Hola {nombre}  Te envío tu factura del mes. Total: [monto]. Datos de pago: [datos]. ¡Gracias! 💚'
        },
        {
          nombre: '🤝 Plan de pago',
          texto: '{nombre}, entiendo tu situación 🤝 Podemos armar un plan de pago cómodo. ¿Te parece si conversamos? 📞'
        }
      ]
    },
    seguimiento: {
      etiqueta: '🔄 Seguimiento',
      items: [
        {
          nombre: ' Después de compra',
          texto: '¡Hola {nombre}!  ¿Cómo va todo con tu compra? ¿Necesitas ayuda con algo? Estamos para servirte. 💚'
        },
        {
          nombre: '⭐ Pedir reseña',
          texto: '{nombre}, si estás feliz con nuestro servicio, ¿nos dejas una reseña? ⭐ Nos ayuda mucho. ¡Gracias! 🙏'
        },
        {
          nombre: ' Cliente recurrente',
          texto: '¡{nombre}! 🎉 Como cliente frecuente, tienes un beneficio especial. ¿Te cuento? 🎁'
        },
        {
          nombre: '📅 Reunión agendada',
          texto: '{nombre}, confirmo nuestra reunión para el [fecha] a las [hora] 📅 Te envío el link: [link]. ¡Nos vemos! '
        }
      ]
    },
    agradecimiento: {
      etiqueta: '💚 Agradecimiento',
      items: [
        {
          nombre: ' Gracias por comprar',
          texto: '¡{nombre}! 💚 Mil gracias por tu compra. Valoramos mucho tu confianza. ¡Vuelve pronto! 🎉'
        },
        {
          nombre: ' Cumpleaños',
          texto: '¡Feliz cumpleaños {nombre}! 🎈 Te regalamos un 15% de descuento para celebrar. Código: CUMPLE15 🎁'
        },
        {
          nombre: '🏆 Aniversario cliente',
          texto: '{nombre}, ¡hoy cumples 1 año con nosotros! 🏆 Gracias por ser parte de nuestra familia. Tenemos un regalo para ti 🎁'
        },
        {
          nombre: '💬 Feedback positivo',
          texto: '{nombre}, leímos tu reseña positiva y nos alegró el día 🌟 ¡Gracias por tus palabras! Seguimos trabajando para ti. 💪'
        }
      ]
    },
    recordatorio: {
      etiqueta: '⏰ Recordatorio',
      items: [
        {
          nombre: '📅 Cita mañana',
          texto: 'Hola {nombre} ⏰ Te recuerdo tu cita para mañana a las [hora] en [lugar]. ¿Confirmas tu asistencia? ✅'
        },
        {
          nombre: '💳 Pago próximo',
          texto: '{nombre}, tu próximo pago vence el [fecha] 💳 Monto: [monto]. ¿Necesitas el link de pago? '
        },
        {
          nombre: '📦 Entrega programada',
          texto: '¡{nombre}! 📦 Tu pedido sale en camino hoy. Llegará entre [hora] y [hora]. ¿Estarás disponible? 🚚'
        },
        {
          nombre: '🔄 Renovación',
          texto: 'Hola {nombre} 🔄 Tu suscripción vence en 7 días. ¿Deseas renovarla? Te mantengo los mismos beneficios. 💚'
        }
      ]
    }
  };

  // Emojis más usados en WhatsApp business
  const EMOJIS_RAPIDOS = [
    '', '😊', '🙏', '💚', '✨', '🎉', '🔥', '💪',
    '📞', '📱', '', '✅', '❌', '', '📅', '📦',
    '💰', '💳', '🎁', '🎊', '⭐', '🌟', '❤️', '',
    '👍', '👎', '😄', '', '😅', '', '👀', ''
  ];

  // ============================================
  // REFERENCIAS DOM
  // ============================================
  const textarea = document.getElementById('plantilla');
  const contenedorCategorias = document.getElementById('categorias');
  const contenedorPlantillas = document.getElementById('plantillas-lista');
  const contenedorEmojis = document.getElementById('emojis-lista');
  const btnRestaurar = document.getElementById('restaurar');

  let categoriaActiva = 'ventas';

  // ============================================
  // FUNCIONES PRINCIPALES
  // ============================================

  /**
   * Inserta texto en la posición del cursor del textarea
   */
  function insertarEnCursor(texto) {
    if (!textarea) return;

    const inicio = textarea.selectionStart;
    const fin = textarea.selectionEnd;
    const valorActual = textarea.value;

    // Insertar texto en la posición del cursor (o reemplazar selección)
    const nuevoValor = valorActual.substring(0, inicio) + texto + valorActual.substring(fin);
    textarea.value = nuevoValor;

    // Reposicionar cursor después del texto insertado
    const nuevaPosicion = inicio + texto.length;
    textarea.setSelectionRange(nuevaPosicion, nuevaPosicion);
    textarea.focus();

    // Disparar evento input para que otros listeners reaccionen
    textarea.dispatchEvent(new Event('input', { bubbles: true }));
  }

  /**
   * Renderiza los chips de categorías
   */
  function renderCategorias() {
    if (!contenedorCategorias) return;
    contenedorCategorias.innerHTML = '';

    Object.keys(PLANTILLAS).forEach(key => {
      const cat = PLANTILLAS[key];
      const chip = document.createElement('button');
      chip.type = 'button';
      chip.className = 'cat-chip' + (key === categoriaActiva ? ' activo' : '');
      chip.textContent = cat.etiqueta;
      chip.addEventListener('click', () => {
        categoriaActiva = key;
        renderCategorias(); // Re-render para actualizar "activo"
        renderPlantillas();
      });
      contenedorCategorias.appendChild(chip);
    });
  }

  /**
   * Renderiza las plantillas de la categoría activa
   */
  function renderPlantillas() {
    if (!contenedorPlantillas) return;
    contenedorPlantillas.innerHTML = '';

    const cat = PLANTILLAS[categoriaActiva];
    if (!cat) return;

    cat.items.forEach(item => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'plantilla-btn';
      btn.textContent = item.nombre;
      btn.title = item.texto; // Tooltip con el texto completo
      btn.addEventListener('click', () => {
        // Si hay texto seleccionado, lo reemplaza; si no, agrega al final
        if (textarea.selectionStart !== textarea.selectionEnd) {
          insertarEnCursor(item.texto);
        } else {
          // Agregar con salto de línea si ya hay contenido
          const separador = textarea.value.length > 0 ? '\n\n' : '';
          insertarEnCursor(separador + item.texto);
        }
      });
      contenedorPlantillas.appendChild(btn);
    });
  }

  /**
   * Renderiza los emojis rápidos
   */
  function renderEmojis() {
    if (!contenedorEmojis) return;
    contenedorEmojis.innerHTML = '';

    EMOJIS_RAPIDOS.forEach(emoji => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'emoji-btn';
      btn.textContent = emoji;
      btn.addEventListener('click', () => insertarEnCursor(emoji));
      contenedorEmojis.appendChild(btn);
    });
  }

  /**
   * Restaura el texto original (placeholder por defecto)
   */
  function restaurarTexto() {
    if (!textarea) return;
    const textoOriginal = 'Hola {nombre} 👋\n\nGracias por contactarnos. ¿En qué podemos ayudarte hoy? 😊';
    textarea.value = textoOriginal;
    textarea.dispatchEvent(new Event('input', { bubbles: true }));
  }

  // ============================================
  // INICIALIZACIÓN
  // ============================================
  function init() {
    renderCategorias();
    renderPlantillas();
    renderEmojis();

    if (btnRestaurar) {
      btnRestaurar.addEventListener('click', restaurarTexto);
    }

    // Atajo de teclado: Ctrl+Shift+P para abrir el panel
    document.addEventListener('keydown', (e) => {
      if (e.ctrlKey && e.shiftKey && e.key === 'P') {
        e.preventDefault();
        const details = document.querySelector('.personalizar');
        if (details) details.open = !details.open;
      }
    });
  }

  // Ejecutar cuando el DOM esté listo
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();