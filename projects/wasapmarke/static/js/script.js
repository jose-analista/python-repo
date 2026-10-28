/* ==========================================================================
   CAYTECH - Estilos principales
   ========================================================================== */

:root {
  --tinta: #13231c;
  --papel: #eef2ec;
  --superficie: #ffffff;
  --verde: #0f7a43;
  --verde-osc: #0a5c32;
  --verde-claro: #d9efe1;
  --suave: #5b6b62;
  --borde: #d8e0d6;
  --peligro: #b42318;
  --peligro-claro: #fde8e6;
  --aviso: #8a5300;
  --aviso-claro: #fdf0d5;
  --chat: #0b3d2a;
  --burbuja: #d9fdd3;
  --titulos: "Bricolage Grotesque", "Figtree", system-ui, sans-serif;
  --cuerpo: "Figtree", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

* { box-sizing: border-box; }

body {
  margin: 0;
  min-height: 100vh;
  background: var(--papel);
  color: var(--tinta);
  font-family: var(--cuerpo);
  font-size: 14px;
  line-height: 1.55;
}

button, input, textarea, select { font: inherit; }
button { cursor: pointer; }
[hidden] { display: none !important; }

:focus-visible {
  outline: 3px solid rgba(15, 122, 67, .45);
  outline-offset: 2px;
}

.ico {
  width: 18px;
  height: 18px;
  flex: none;
  fill: none;
  stroke: currentColor;
  stroke-width: 2;
  stroke-linecap: round;
  stroke-linejoin: round;
}

/* ---------- Barra lateral ---------- */
.sidebar {
  position: fixed;
  inset: 0 auto 0 0;
  z-index: 1000;
  width: 250px;
  padding: 26px 16px;
  background: var(--superficie);
  border-right: 1px solid var(--borde);
  transition: transform .25s ease;
}

.marca {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 2px 12px 28px;
}

.marca-logo {
  display: grid;
  place-items: center;
  width: 30px;
  height: 30px;
  border-radius: 9px 9px 9px 2px;
  background: var(--verde);
  color: #fff;
  font-family: var(--titulos);
  font-weight: 800;
  font-size: 16px;
}

.marca h2 {
  margin: 0;
  font-family: var(--titulos);
  font-size: 21px;
  font-weight: 800;
  letter-spacing: -.6px;
}

.nav-links {
  display: grid;
  gap: 4px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.nav-links a {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 11px 14px;
  border-radius: 10px;
  color: var(--suave);
  font-weight: 600;
  text-decoration: none;
}

.nav-links a:hover { background: var(--papel); color: var(--tinta); }
.nav-links a.activo { background: var(--verde-claro); color: var(--verde-osc); }
.nav-icon { width: 24px; text-align: center; font-size: 18px; }

/* ---------- Contenido ---------- */
.main-content {
  min-height: 100vh;
  margin-left: 250px;
  padding: 32px 36px 48px;
}

.cabecera {
  display: flex;
  flex-wrap: wrap;
  align-items: flex-end;
  justify-content: space-between;
  gap: 16px 24px;
  margin-bottom: 22px;
}

.cabecera h1 {
  margin: 0 0 4px;
  font-family: var(--titulos);
  font-size: clamp(28px, 3.4vw, 38px);
  font-weight: 800;
  letter-spacing: -1.3px;
  line-height: 1.1;
}

.cabecera p { margin: 0; max-width: 46ch; color: var(--suave); }

.menu-toggle {
  display: none;
  width: 42px;
  height: 42px;
  margin-bottom: 12px;
  border: 1px solid var(--borde);
  border-radius: 10px;
  background: #fff;
  font-size: 20px;
}

.herramientas { display: flex; flex-wrap: wrap; gap: 10px; }

/* ---------- Botones ---------- */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  min-height: 42px;
  padding: 9px 16px;
  border: 1px solid transparent;
  border-radius: 10px;
  font-weight: 700;
  font-size: 13px;
  text-align: center;
  text-decoration: none;
  transition: background .15s ease, border-color .15s ease;
}

.btn-primario { background: var(--verde); color: #fff; }
.btn-primario:hover:not(:disabled) { background: var(--verde-osc); }
.btn-oscuro { background: var(--tinta); color: #fff; }
.btn-oscuro:hover:not(.deshabilitado) { background: #2b3f35; }
.btn-borde { background: #fff; color: var(--tinta); border-color: var(--borde); }
.btn-borde:hover { border-color: #aebbaa; background: #fafcf9; }
.btn:disabled, .btn.deshabilitado { opacity: .45; cursor: not-allowed; pointer-events: none; }

.ib {
  display: inline-grid;
  place-items: center;
  width: 34px;
  height: 34px;
  border: 1px solid var(--borde);
  border-radius: 9px;
  background: #fff;
  color: var(--suave);
}

.ib:hover { color: var(--tinta); border-color: #aebbaa; }
.ib.eliminar:hover { color: var(--peligro); border-color: #f0b5af; background: var(--peligro-claro); }

/* ---------- Menú exportar ---------- */
.menu { position: relative; }
.menu > summary { list-style: none; cursor: pointer; }
.menu > summary::-webkit-details-marker { display: none; }

.menu-lista {
  position: absolute;
  right: 0;
  top: calc(100% + 6px);
  z-index: 50;
  width: 290px;
  padding: 6px;
  border: 1px solid var(--borde);
  border-radius: 12px;
  background: #fff;
  box-shadow: 0 14px 34px rgba(19, 35, 28, .14);
}

.menu-lista a {
  display: block;
  padding: 10px 12px;
  border-radius: 8px;
  color: var(--tinta);
  text-decoration: none;
}

.menu-lista a:hover { background: var(--papel); }
.menu-lista b { display: block; font-size: 13px; }
.menu-lista small { color: var(--suave); font-size: 12px; }

/* ---------- Resumen ---------- */
.resumen {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  margin-bottom: 22px;
  border: 1px solid var(--borde);
  border-radius: 14px;
  background: var(--superficie);
}

.resumen > div { padding: 16px 22px; }
.resumen > div + div { border-left: 1px solid var(--borde); }

.resumen strong {
  display: block;
  font-family: var(--titulos);
  font-size: 28px;
  font-weight: 700;
  line-height: 1.15;
  letter-spacing: -.8px;
}

.resumen span { color: var(--suave); font-size: 13px; }

/* ---------- Distribución ---------- */
.grid {
  display: grid;
  grid-template-columns: 400px minmax(0, 1fr);
  align-items: start;
  gap: 22px;
}

.lateral { position: sticky; top: 22px; display: grid; gap: 16px; }

.tarjeta {
  min-width: 0;
  padding: 24px;
  border: 1px solid var(--borde);
  border-radius: 14px;
  background: var(--superficie);
}

.tarjeta h2 {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 0 0 18px;
  font-family: var(--titulos);
  font-size: 20px;
  font-weight: 700;
  letter-spacing: -.5px;
}

/* ---------- Vista previa tipo chat ---------- */
.chat {
  padding: 16px 16px 18px;
  border-radius: 14px;
  background-color: var(--chat);
  background-image: radial-gradient(rgba(255, 255, 255, .07) 1px, transparent 1px);
  background-size: 14px 14px;
}

.chat small {
  display: block;
  margin-bottom: 10px;
  color: #a8d5bd;
  font-size: 12px;
  font-weight: 600;
}

.burbuja {
  position: relative;
  width: fit-content;
  max-width: 92%;
  margin-left: auto;
  padding: 9px 12px 20px;
  border-radius: 12px 12px 3px 12px;
  background: var(--burbuja);
  color: #111b15;
  font-size: 13.5px;
  overflow-wrap: anywhere;
  white-space: pre-wrap;
}

.burbuja-hora {
  position: absolute;
  right: 10px;
  bottom: 4px;
  color: #5d7a66;
  font-size: 10.5px;
}

/* ---------- Formulario ---------- */
.campo { margin-bottom: 16px; }

.campo label {
  display: block;
  margin-bottom: 6px;
  font-weight: 700;
  font-size: 13px;
}

.ayuda { color: var(--suave); font-size: 12px; font-weight: 400; }

.campo input, .buscador input, textarea {
  width: 100%;
  min-width: 0;
  padding: 11px 13px;
  border: 1px solid #cdd7ca;
  border-radius: 10px;
  background: #fff;
  color: var(--tinta);
  outline: none;
}

.campo input:focus, .buscador input:focus, textarea:focus {
  border-color: var(--verde);
  box-shadow: 0 0 0 4px rgba(15, 122, 67, .12);
}

input.invalido { border-color: var(--peligro) !important; }
.error-campo { margin-top: 4px; color: var(--peligro); font-size: 12px; }

details.personalizar {
  margin: 4px 0 18px;
  padding: 12px 14px;
  border: 1px solid var(--borde);
  border-radius: 10px;
  background: #f7faf6;
}

details.personalizar summary { cursor: pointer; font-weight: 700; font-size: 13px; }
details.personalizar textarea { min-height: 110px; margin-top: 12px; resize: vertical; line-height: 1.6; }

.enlace-texto {
  margin-top: 8px;
  padding: 0;
  border: 0;
  background: none;
  color: var(--verde-osc);
  font-weight: 700;
  font-size: 12px