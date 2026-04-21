import os

def escaneo_red():
    red = "172.25.142"
    activos = []

    print(f"Escaneando dispositivos en la red {red}.0/24...")

    for i in range(1, 255):
        ip = f"{red}.{i}"
        comando = os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
        
        if comando == 0:
            print(f" Dispositivo encontrado: {ip}")
            activos.append(ip)

    print("\n Dispositivos que respondieron")
    for host in activos:
        print(host)

if __name__ == "__main__":
    escaneo_red()
