import instaloader
import requests
from bs4 import BeautifulSoup
import re
import asyncio
import aiohttp
from colorama import init, Fore, Style

init(autoreset=True) # Para colores en la consola

# ==========================================
# 1. ANALIZADOR DE ENLACE DE BIOGRAFÍA
# ==========================================
def analizar_enlace_externo(url):
    if not url or url == "":
        return "⚠️ No hay enlace en la biografía."
    
    print(f"\n{Fore.CYAN}🔗 Analizando enlace externo: {url}{Style.RESET_ALL}")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        response = requests.get(url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        texto_completo = soup.get_text()

        hallazgos = []
        
        # Buscar emails con Regex
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', texto_completo)
        if emails:
            hallazgos.append(f"📧 Emails encontrados: {', '.join(set(emails))}")
            
        # Buscar números de teléfono (formato básico internacional)
        phones = re.findall(r'\+?\d[\d -]{8,12}\d', texto_completo)
        if phones:
            hallazgos.append(f"📞 Teléfonos encontrados: {', '.join(set(phones))}")
            
        # Buscar otras redes sociales en los href
        redes = set()
        for a_tag in soup.find_all('a', href=True):
            href = a_tag['href']
            if 'twitter.com' in href or 'x.com' in href: redes.add("Twitter/X")
            elif 'tiktok.com' in href: redes.add("TikTok")
            elif 'youtube.com' in href: redes.add("YouTube")
            elif 't.me' in href or 'telegram.me' in href: redes.add("Telegram")
            
        if redes:
            hallazgos.append(f"🌐 Otras redes en el enlace: {', '.join(redes)}")

        if not hallazgos:
            return "✅ El enlace no contiene datos OSINT obvios (emails, teléfonos u otras redes)."
        
        return "\n".join(hallazgos)

    except Exception as e:
        return f"❌ Error al analizar el enlace: {e}"

# ==========================================
# 2. CORRELACIÓN DE USUARIO (Async para velocidad)
# ==========================================
PLATAFORMAS = {
    "Twitter/X": "https://twitter.com/{}",
    "TikTok": "https://www.tiktok.com/@{}",
    "GitHub": "https://github.com/{}",
    "Reddit": "https://www.reddit.com/user/{}",
    "Telegram": "https://t.me/{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "Tumblr": "https://{}.tumblr.com/",
    "Vimeo": "https://vimeo.com/{}",
    "Flickr": "https://www.flickr.com/photos/{}",
    "SoundCloud": "https://soundcloud.com/{}"
}

async def check_platform(session, nombre, url_format, username):
    try:
        # Usamos HEAD para no descargar todo el contenido, solo verificar si existe
        async with session.head(url_format.format(username), timeout=8, allow_redirects=True) as response:
            if response.status == 200:
                return f"{Fore.GREEN}✅ {nombre}: @{username} existe"
            else:
                return f"{Fore.RED}❌ {nombre}: No encontrado"
    except Exception:
        return f"{Fore.YELLOW}⚠️ {nombre}: Bloqueado o error"

async def buscar_username_en_todas_partes(username):
    print(f"\n{Fore.MAGENTA}🕵️ Buscando correlación del usuario '@{username}' en otras plataformas...{Style.RESET_ALL}")
    async with aiohttp.ClientSession() as session:
        tareas = [check_platform(session, nombre, url, username) for nombre, url in PLATAFORMAS.items()]
        resultados = await asyncio.gather(*tareas)
        for res in resultados:
            print(f"   {res}")

# ==========================================
# 3. MOTOR PRINCIPAL DE INSTAGRAM
# ==========================================
def analizar_perfil_instagram(username):
    print(f"{Fore.BLUE}{'='*60}")
    print(f"   INICIANDO ANÁLISIS OSINT DE INSTAGRAM: @{username}")
    print(f"{'='*60}{Style.RESET_ALL}")

    L = instaloader.Instaloader()
    
    # ⚠️ ADVERTENCIA CRÍTICA: Instagram requiere login incluso para ver perfiles públicos a veces.
    # Usa una cuenta SECUNDARIA ("burner account") NUNCA tu cuenta personal.
    # Descomenta las siguientes líneas y crea un archivo 'session.txt' con tu sesión si te pide login:
    # L.load_session_from_file("tu_usuario_secundario", "session_file")
    
    try:
        perfil = instaloader.Profile.from_username(L.context, username)
        
        print(f"\n{Fore.GREEN}📊 DATOS DEL PERFIL:{Style.RESET_ALL}")
        print(f"   👤 Nombre completo: {perfil.full_name}")
        print(f"   📝 Biografía: {perfil.biography.replace(chr(10), ' | ')}") # Reemplaza saltos de línea
        print(f"   🔗 Enlace en Bio: {perfil.external_url}")
        print(f"   📈 Seguidores: {perfil.followers} | Siguiendo: {perfil.followees}")
        print(f"   📸 Publicaciones: {perfil.mediacount}")
        print(f"   🔒 Es privado: {'SÍ (OSINT limitado)' if perfil.is_private else 'NO'}")
        print(f"   ✅ Verificado: {'SÍ' if perfil.is_verified else 'NO'}")
        
        # URL de la foto de perfil en alta resolución (truco OSINT)
        # Instaloader no da la URL directa HD fácilmente, pero podemos construirla o usar el contexto
        print(f"\n{Fore.YELLOW}🖼️ URL de Foto de Perfil (para Reverse Image Search en Yandex/Google):{Style.RESET_ALL}")
        print(f"   {perfil.profile_pic_url}")

        # Analizar el enlace externo si existe
        if perfil.external_url:
            print("\n" + analizar_enlace_externo(perfil.external_url))
        else:
            print("\n⚠️ No hay enlace externo para analizar.")

        # Ejecutar búsqueda de correlación de username
        asyncio.run(buscar_username_en_todas_partes(username))

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"\n{Fore.RED}❌ El perfil @{username} NO existe.{Style.RESET_ALL}")
    except instaloader.exceptions.LoginRequiredException:
        print(f"\n{Fore.RED}❌ Instagram exige inicio de sesión. Debes configurar una sesión de Instaloader con una cuenta secundaria.{Style.RESET_ALL}")
    except Exception as e:
        print(f"\n{Fore.RED}❌ Error inesperado: {e}{Style.RESET_ALL}")

# ==========================================
# EJECUCIÓN
# ==========================================
if __name__ == "__main__":
    target = input("Introduce el usuario de Instagram a investigar (sin @): ")
    analizar_perfil_instagram(target)