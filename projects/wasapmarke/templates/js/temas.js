(function () {
  const TEMAS = [
    ["menta", "Menta", "#0f7a43", "#d9efe1"],
    ["blanco", "Blanco", "#18181b", "#ffffff"],
    ["noche", "Noche", "#2fc77a", "#0d1411"],
    ["corporativo", "Corporativo", "#1d5fd6", "#edf2f9"],
    ["boutique", "Boutique", "#c2386b", "#fbf0f2"],
    ["lujo", "Lujo", "#d4a73a", "#0b0b0a"],
    ["sabor", "Sabor", "#d9480f", "#fff3e6"],
    ["neon", "Neón", "#7c3aed", "#09091a"],
  ];
  const FUENTES = {
    boutique: "Fraunces:opsz,wght@9..144,600;9..144,700",
    lujo: "Fraunces:opsz,wght@9..144,600;9..144,700",
    neon: "Space+Grotesk:wght@600;700",
  };
  const raiz = document.documentElement;
  const porId = (id) => document.getElementById(id);

  function cargarFuente(tema) {
    const familia = FUENTES[tema];
    if (!familia || document.querySelector('link[data-fuente="' + familia + '"]')) return;
    const l = document.createElement("link");
    l.rel = "stylesheet";
    l.dataset.fuente = familia;
    l.href = "https://fonts.googleapis.com/css2?family=" + familia + "&display=swap";
    document.head.append(l);
  }

  function aplicar(id) {
    if (!TEMAS.some((t) => t[0] === id)) id = "menta";
    raiz.dataset.tema = id;
    try { localStorage.setItem("tema", id); } catch (e) {}
    cargarFuente(id);
    document.querySelectorAll(".tema-btn").forEach((b) =>
      b.setAttribute("aria-pressed", String(b.dataset.tema === id)));
  }

  // ---------- selector en la barra lateral ----------
  const cont = document.createElement("div");
  cont.className = "temas";
  const rotulo = document.createElement("p");
  rotulo.textContent = "Tema del panel";
  const lista = document.createElement("div");
  lista.className = "temas-lista";
  TEMAS.forEach(([id, nombre, c1, c2]) => {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "tema-btn";
    b.dataset.tema = id;
    b.title = nombre;
    b.setAttribute("aria-label", "Tema " + nombre);
    b.style.background = "linear-gradient(135deg," + c1 + " 50%," + c2 + " 50%)";
    b.addEventListener("click", () => aplicar(id));
    lista.append(b);
  });
  cont.append(rotulo, lista);
  porId("sidebar").append(cont);

  // ---------- modo video (9:16) ----------
  const ig = document.createElement("div");
  ig.id = "video-ig";
  ig.hidden = true;
  ig.innerHTML =
    '<div class="ig-marco">' +
      '<div class="ig-marca"><span class="marca-logo" aria-hidden="true">W</span>' +
      '<span contenteditable="true" spellcheck="false">Tu negocio</span></div>' +
      '<h2 class="ig-titulo" contenteditable="true" spellcheck="false">Cada cliente nuevo, atendido al instante</h2>' +
      '<div class="burbuja"><span id="ig-txt"></span><span class="burbuja-hora" id="ig-hora"></span></div>' +
      '<p class="ig-cta" contenteditable="true" spellcheck="false">Escríbenos por WhatsApp</p>' +
    '</div>' +
    '<div class="ig-ctrl" id="ig-ctrl">' +
      '<button type="button" class="btn btn-primario" id="ig-repetir">Repetir</button>' +
      '<button type="button" class="btn btn-borde" id="ig-salir" style="width:auto;margin:0">Salir</button>' +
      '<small>Haz clic en los textos para editarlos · H oculta los botones · Esc sale</small>' +
    '</div>';
  document.body.append(ig);

  let reloj;
  function reproducir() {
    clearInterval(reloj);
    const nombre = porId("nombre").value.trim() || "María";
    const completo = Array.from(window.construirMensaje(nombre, porId("link").value.trim()));
    const salida = porId("ig-txt");
    porId("ig-hora").textContent = new Date().toLocaleTimeString("es-CL", { hour: "2-digit", minute: "2-digit" });
    salida.textContent = "";
    if (matchMedia("(prefers-reduced-motion: reduce)").matches) {
      salida.textContent = completo.join("");
      return;
    }
    let i = 0;
    reloj = setInterval(() => {
      salida.textContent = completo.slice(0, ++i).join("");
      if (i >= completo.length) clearInterval(reloj);
    }, 32);
  }

  function abrirVideo() {
    ig.hidden = false;
    porId("ig-ctrl").hidden = false;
    reproducir();
  }
  function cerrarVideo() { clearInterval(reloj); ig.hidden = true; }

  const herramientas = document.querySelector(".herramientas");
  if (herramientas) {
    const b = document.createElement("button");
    b.type = "button";
    b.className = "btn btn-oscuro";
    b.textContent = "Modo video Instagram";
    b.addEventListener("click", abrirVideo);
    herramientas.prepend(b);
  }
  porId("ig-repetir").addEventListener("click", reproducir);
  porId("ig-salir").addEventListener("click", cerrarVideo);
  document.addEventListener("keydown", (ev) => {
    if (ig.hidden) return;
    if (ev.key === "Escape") cerrarVideo();
    const editando = ev.target.isContentEditable;
    if (!editando && (ev.key === "h" || ev.key === "H")) porId("ig-ctrl").hidden = !porId("ig-ctrl").hidden;
  });

  let guardado = "menta";
  try { guardado = localStorage.getItem("tema") || "menta"; } catch (e) {}
  aplicar(guardado);
})();