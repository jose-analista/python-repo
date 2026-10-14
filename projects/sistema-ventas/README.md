# 🛒 Sistema de Ventas POS

> Sistema de Punto de Venta multiplataforma diseñado para negocios locales (almacenes, ferreterías, boutiques, farmacias). Gestiona inventario, ventas, clientes y reportes desde una sola plataforma.

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Flet](https://img.shields.io/badge/Flet-0.27.4-purple)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110+-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

##  Descripción

**Sistema de Ventas POS** es una solución SaaS (Software as a Service) que permite a pequeños y medianos negocios digitalizar su operación comercial. Ofrece un punto de venta rápido, control de inventario en tiempo real, gestión de clientes y reportes financieros, todo accesible desde web, escritorio o dispositivos móviles.

### 🎯 Público objetivo
- Almacenes de barrio y minimarkets
- Ferreterías
- Boutiques y tiendas de ropa
- Farmacias
- Pequeños restaurantes y cafeterías

---

## ✨ Características Principales

### 🛒 Punto de Venta (POS)
- Interfaz optimizada para lectores de código de barras y pantallas táctiles.
- Carrito de compras en tiempo real con autocompletado de productos.
- Múltiples métodos de pago (efectivo, tarjeta, transferencia).
- Descuentos y promociones automáticas.

### 📦 Inventario y Stock
- Control de stock en tiempo real.
- **Alertas de stock bajo** (semáforo visual y notificaciones).
- Bloqueo automático de ventas para productos agotados.
- Gestión de categorías, proveedores y ajustes de inventario.

###  Gestión de Clientes (CRM)
- Base de datos de clientes con historial de compras.
- Sistema de "fiado" o cuentas por cobrar controlado.
- Programa de puntos y fidelización.

### 📊 Reportes y Dashboard
- Ventas del día, semana y mes.
- Productos más vendidos y rentabilidad.
- Ganancia neta (ventas - costos).
- Gráficos visuales interactivos.

###  Seguridad y Multi-usuario
- Roles de usuario (Administrador, Cajero, Bodeguero).
- Cierre de caja diario con cuadre exacto de efectivo.
- Auditoría de transacciones y anulaciones.
- Autenticación segura con JWT.

### 🌐 Multiplataforma
- **Web**: Acceso desde cualquier navegador (ideal para cajeros).
- **Desktop**: Aplicación nativa para Windows/Mac/Linux (funciona en modo offline).
- **Móvil**: App para Android/iOS (consulta remota y reportes para el dueño).

---

## 🛠️ Stack Tecnológico

| Capa | Tecnología | Versión | Propósito |
|------|-----------|---------|-----------|
| **Frontend** | Flet | 0.27.4 | UI multiplataforma (Web/Desktop/Móvil) |
| **Backend API** | FastAPI | 0.110+ | API REST rápida, moderna y asíncrona |
| **Base de Datos** | PostgreSQL | 16+ | Datos relacionales robustos y escalables |
| **ORM** | SQLAlchemy | 2.0+ | Mapeo objeto-relacional |
| **Autenticación** | JWT + Passlib | - | Seguridad de usuarios y sesiones |
| **Cache** | Redis | 7+ | Sesiones, caché y datos frecuentes |
| **Contenedores** | Docker | - | Despliegue, orquestación y escalabilidad |

### Herramientas de Desarrollo
- **Pytest**: Tests unitarios y de integración.
- **Black + Ruff**: Formateo de código y linting.
- **Alembic**: Migraciones de base de datos.
- **Swagger UI**: Documentación automática de la API.

---

## 🏗️ Arquitectura del Sistema

```text
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENTES (Frontends)                      │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────────────┐ │
│  │     Web      │   │   Desktop    │   │       Móvil          │ │
│  │  (Flet Web)  │   │  (Flet App)  │   │  (Flet APK / IPA)    │ │
│  └─────────────┘   └─────────────┘   └─────────────────────┘ │
│         │                  │                       │             │
│         └──────────────────┴───────────────────────┘             │
│                              │                                    │
│                        HTTP / HTTPS                               │
└──────────────────────────────┼────────────────────────────────────┘
                               │
┌──────────────────────────────┼────────────────────────────────────┐
│                         BACKEND (API)                              │
│  ┌───────────────────────────┴───────────────────────────────┐    │
│  │                    FastAPI Server                         │    │
│  │  ┌───────────┐  ┌───────────┐  ┌───────────────────────┐ │    │
│  │  │   Auth    │  │  Sales    │  │      Inventory        │ │    │
│  │  │  Module   │  │  Module   │  │       Module          │ │    │
│  │  ───────────┘  └───────────┘  └───────────────────────┘ │    │
│  └───────────────────────────┬───────────────────────────────┘    │
│                              │                                    │
│  ┌───────────────────────────┴───────────────────────────────┐    │
│  │                      Data Layer                           │    │
│  │  ┌──────────────────┐  ┌───────────────────────────────┐  │    │
│  │  │   PostgreSQL     │  │            Redis              │  │    │
│  │  │  (Datos críticos)│  │     (Cache y Sesiones)        │  │    │
│  │  └──────────────────  └───────────────────────────────┘  │    │
│  └───────────────────────────────────────────────────────────┘    │
───────────────────────────────────────────────────────────────────