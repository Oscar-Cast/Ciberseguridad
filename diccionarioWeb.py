import requests

def probar_recursos():

    target_url = input("Ingresa la direccion base (ej. http://example.com/): ").strip()
    diccionario_path = "palabras.txt"
    
    if not target_url.endswith("/"):
        target_url += "/"

    print(f"\n Iniciando busqueda de recursos en {target_url}")

    try:
        with open(diccionario_path, "r") as archivo:
            palabras = archivo.readlines()

        encontrados = []
        for palabra in palabras:
            recurso = palabra.strip()
            if not recurso: continue 
            
            full_url = f"{target_url}{recurso}"
            
            try:
                respuesta = requests.head(full_url, allow_redirects=True, timeout=5)
                
                if respuesta.status_code == 200:
                    print(f" {full_url} (Codigo: 200)")
                    encontrados.append(full_url)
                elif respuesta.status_code == 403:
                    print(f" {full_url} (Codigo: 403)")
                    encontrados.append(full_url)
                    
            except requests.exceptions.RequestException:
                pass

        print("\n Resumen Final ")
        print(f"Total de recursos detectados: {len(encontrados)}")

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{diccionario_path}'")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")

if __name__ == "__main__":
    probar_recursos()
