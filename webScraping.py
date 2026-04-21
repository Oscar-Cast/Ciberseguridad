import requests
import re

def extraer_datos():
    url = input("Ingresa la URL completa (con http/https): ")
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        respuesta = requests.get(url, headers=headers)
        html = respuesta.text

        comentarios = re.findall(r'', html, re.DOTALL)

        correos = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)
        correos_unicos = list(set(correos)) 

        with open("resultado_web.txt", "w", encoding="utf-8") as archivo:
            archivo.write(f"EXTRACCION DE: {url}\n\n")
            
            archivo.write(f" COMENTARIOS ({len(comentarios)}) \n")
            for c in comentarios:
                archivo.write(f"{c.strip()}\n")
            
            archivo.write(f"\n CORREOS ({len(correos_unicos)}) \n")
            for mail in correos_unicos:
                archivo.write(f"{mail}\n")

        print(" Datos almacenados  'resultado_web.txt'")

    except Exception as e:
        print(f"Ocurrio un error: {e}")

if __name__ == "__main__":
    extraer_datos()
