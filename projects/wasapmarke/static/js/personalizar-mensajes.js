// ====== DATOS DE PLANTILLAS (Con variables dinámicas) ======
  const plantillasData = {
    soporte: {
      nombre: "🛠️ Soporte",
      plantillas: [
        { titulo: "Bienvenida", texto: "¡Hola {nombre}! 👋 Gracias por contactarnos. ¿En qué podemos ayudarte hoy con respecto a {producto}?" },
        { titulo: "Caso recibido", texto: "Hola {nombre}, hemos recibido tu solicitud sobre {producto}. Nuestro equipo técnico ya la está revisando (Ticket: {pedido}). Te responderemos a la brevedad. 🙏" },
        { titulo: "Solicitar info", texto: "Hola {nombre}, para poder ayudarte mejor con {producto}, ¿podrías proporcionarnos más detalles o capturas de pantalla del problema? 📝" },
        { titulo: "Solución", texto: "¡Hola {nombre}! ✅ Hemos encontrado una solución para tu caso. Por favor, prueba lo siguiente y cuéntanos si funciona." },
        { titulo: "Seguimiento", texto: "Hola {nombre}, ¿pudiste resolver el problema con {producto}? Estamos aquí para ayudarte si necesitas más asistencia. 💪" }
      ]
    },
    quejas: {
      nombre: "⚠️ Quejas / Reclamos",
      plantillas: [
        { titulo: "Disculpa formal", texto: "Hola {nombre}, lamentamos mucho el inconveniente que has experimentado. 😔 Estamos trabajando para solucionarlo lo antes posible." },
        { titulo: "Producto defectuoso", texto: "Hola {nombre}, sentimos que {producto} no haya cumplido tus expectativas. 📦 Por favor, confirma si el Nº de Pedido {pedido} es correcto para gestionar el cambio o reembolso inmediato." },
        { titulo: "Demora en entrega", texto: "Hola {nombre}, entendemos tu frustración por la demora del pedido {pedido}. 🚚 Estamos verificando el estado con la paquetería y te daremos una actualización hoy mismo." },
        { titulo: "Compensación", texto: "Hola {nombre}, como disculpa por el inconveniente con {producto}, nos gustaría ofrecerte un código de descuento del 15% para tu próxima compra. 🎁 ¿Te parece bien?" },
        { titulo: "Escalamiento", texto: "Hola {nombre}, he escalado tu caso (Ticket {pedido}) a nuestro equipo especializado de calidad. 👨‍💼 Te contactaremos en las próximas 24 horas con una solución definitiva." }
      ]
    },
    ventas: {
      nombre: "💰 Ventas",
      plantillas: [
        { titulo: "Promoción", texto: "¡Hola {nombre}! 🎉 Tenemos una promoción especial esta semana en {producto}. ¿Te gustaría que te envíe los detalles y precios?" },
        { titulo: "Seguimiento", texto: "Hola {nombre}, ¿tuviste la oportunidad de revisar nuestra oferta sobre {producto}? Estoy aquí para resolver cualquier duda que tengas. 🤝" }
      ]
    }
  };

  const emojisData = [
    "👍 👎 👏 🙏 💪 ✌️ 🤝",
    "😊 😃 😄 😅 😂 🤣 😇 🥰 😍 🤩",
    "😐 😒 😏 😬 😴 😷 🤒 🤕 🤢 🤧",
    "🤠 🥳 😎 🤓 🧐 😟 😕 🙁 ☹️ 😮",
    "😧 😨 😰 😥 😢 😭 😱 😖 😞 😓",
    "😡 😠 🤬 😈 👿 💀 ☠️ 💩 🤡 👹",
    "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 💔 ❣️",
    "✅ ❌ ⚠️ 🚫 🔴 🟡 🟢 🔵 🟣 ⚫",
    "📱 💻 🖥️ ⌨️ 🖱️ 📷 📞 ☎️ 📺 ⏰",
    "📦 🚚 🛒 🎁 🛍️ 💳 💵 💰 🏷️ 📝"
  ];

  // ====== INICIALIZACIÓN ======
  document.addEventListener('DOMContentLoaded', () => {
    const categoriasContainer = document.getElementById('categorias');
    const plantillasLista = document.getElementById('plantillas-lista');
    const emojisLista = document.getElementById('emojis-lista');
    const textarea = document.getElementById('plantilla');
    const botonRestaurar = document.getElementById('restaurar');

    // Inputs de variables
    const varNombre = document.getElementById('var-nombre');
    const varProducto = document.getElementById('var-producto');
    const varPedido = document.getElementById('var-pedido');

    let categoriaActiva = 'soporte';

    // Función para procesar el texto dinámicamente
    function procesarTextoDinamico(textoOriginal) {
      let texto = textoOriginal;
      
      // 1. Reemplazar variables de los inputs (si están vacíos, deja el placeholder)
      const nombreVal = varNombre.value.trim() || '{nombre}';
      const productoVal = varProducto.value.trim() || '{producto}';
      const pedidoVal = varPedido.value.trim() || '{pedido}';

      texto = texto.replace(/{nombre}/gi, nombreVal);
      texto = texto.replace(/{producto}/gi, productoVal);
      texto = texto.replace(/{pedido}/gi, pedidoVal);

      // 2. Reemplazar variables automáticas del sistema
      const hoy = new Date();
      const fechaStr = hoy.toLocaleDateString('es-ES', { day: 'numeric', month: 'long', year: 'numeric' });
      const horaStr = hoy.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit' });
      
      texto = texto.replace(/{fecha}/gi, fechaStr);
      texto = texto.replace(/{hora}/gi, horaStr);

      return texto;
    }

    function renderizarCategorias() {
      categoriasContainer.innerHTML = '';
      Object.keys(plantillasData).forEach(cat => {
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = 'categoria-chip' + (cat === categoriaActiva ? ' activa' : '');
        chip.textContent = plantillasData[cat].nombre;
        chip.addEventListener('click', () => {
          categoriaActiva = cat;
          renderizarCategorias();
          renderizarPlantillas();
        });
        categoriasContainer.appendChild(chip);
      });
    }

    function renderizarPlantillas() {
      plantillasLista.innerHTML = '';
      plantillasData[categoriaActiva].plantillas.forEach(p => {
        const btn = document.createElement('button');
        btn.type = 'button';
        btn.className = 'plantilla-item';
        btn.textContent = p.titulo;
        
        btn.addEventListener('click', () => {
          // Procesar el texto con las variables actuales
          const textoProcesado = procesarTextoDinamico(p.texto);
          textarea.value = textoProcesado;
          textarea.focus();

          // UX: Seleccionar el primer placeholder que quede sin rellenar para edición rápida
          const match = textoProcesado.match(/{[^}]+}/);
          if (match) {
            const index = textoProcesado.indexOf(match[0]);
            textarea.setSelectionRange(index, index + match[0].length);
          }
        });
        
        plantillasLista.appendChild(btn);
      });
    }

    function renderizarEmojis() {
      emojisLista.innerHTML = '';
      emojisData.forEach(grupo => {
        grupo.split(' ').forEach(emoji => {
          const btn = document.createElement('button');
          btn.type = 'button';
          btn.className = 'emoji-boton';
          btn.textContent = emoji;
          btn.addEventListener('click', () => {
            const pos = textarea.selectionStart;
            const antes = textarea.value.substring(0, pos);
            const despues = textarea.value.substring(pos);
            textarea.value = antes + emoji + despues;
            textarea.focus();
            textarea.selectionStart = textarea.selectionEnd = pos + emoji.length;
          });
          emojisLista.appendChild(btn);
        });
      });
    }

    // Botón restaurar/limpiar
    botonRestaurar.addEventListener('click', () => {
      textarea.value = '';
      varNombre.value = '';
      varProducto.value = '';
      varPedido.value = '';
      textarea.focus();
    });

    // Inicializar
    renderizarCategorias();
    renderizarPlantillas();
    renderizarEmojis();
  });