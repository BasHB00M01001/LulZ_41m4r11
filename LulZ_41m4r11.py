#coding:utf-8
import os
import time
import argparse

def biaoti():
    splash1 = """
        +----------------------------------+
        |         Aimar11                  |
        +----------------------------------+
        | by Kr0k3tⒶUn        LulZSeC      |
        +----------------------------------+
    """
    print(splash1)

def args():
    parser = argparse.ArgumentParser(description='Aimar11')
    parser.add_argument('-i', '--input', help='referencia masscan -iL', required=True)
    parser.add_argument('-p', '--port',help='referencia masscan -p', required=True)
    parser.add_argument('-rate','--rate', help='referencia masscan velocidad rate', required=True)
    args = parser.parse_args()
    return args

def update():
    splash00 = """
        +----------------------------------------+
        | nuclei&xray Buscar actualizaciones ing         
        +----------------------------------------+
    """
    print(splash00)
    os.system('./nuclei -update')
    os.system('./xray_linux_amd64 upgrade')
    splash03 = """
        +------------------------------------+
        | inspección completa, comienzo clean
        +------------------------------------+
    """
    print(splash03)


def check_args(args):
    if not os.path.exists(args.input):
        print('archivo sin ips')
        exit()
    if not args.port:
        print('parametros de puertos')
        exit()
    if not args.rate:
        print('tasa scaneo (ejemplo：-rate 2000)')
        exit()
    return args

def Aimar11(args):
    args = check_args(args)
    input_file = args.input
    port = args.port
    rate = args.rate
    os.system('masscan -iL ' + input_file + ' -p' + port + ' -oL masscan.txt --rate ' + rate)

def Aimar11_main():
    while True:
        if os.path.exists("masscan.txt"):
            break
        else:
            time.sleep(1)
    if os.path.getsize("masscan.txt") == 0:
        splash3 = """
            +----------------------------------+
            | No hay puertos abiertos!!         
            +----------------------------------+
        """
        print(splash3)
        exit()
    else :
        splash4 = """
            +----------------------------------+
            | Masscan ok analiza resultado httpx   
            +----------------------------------+
        """
        print(splash4)
        masscanfile = open("masscan.txt", "r")
        masscanfile.seek(0)
        for line in masscanfile:
            if line.startswith("#"):
                continue
            if line.startswith("open"):
                line = line.split(" ")
                with open("masscanconvert.txt", "a") as f:
                    f.write(line[3]+":"+line[2]+"\n")
                    f.close()
        masscanfile.close()
    if os.path.exists("masscan.txt"):
        os.system('./httpx -l masscanconvert.txt -nc -o httpxresult.txt')
        os.remove("masscan.txt")
        splash2 = """
            +----------------------------------+
            | Httpx is done !                  
            +----------------------------------+
        """
        print(splash2)
    else:
        splash5 = """
            +----------------------------------+
            | sin resultados d puertos masscan  
            +----------------------------------+
        """
        print(splash5)
        exit()
    if os.path.exists("httpxresult.txt"):
        os.system('./nuclei -l httpxresult.txt -s medium,high,critical -o nucleiresult.txt')
        os.system('./xray_linux_amd64 webscan -url-file httpxresult.txt --html-output xray.html')
        os.remove("httpxresult.txt")
        os.remove("masscanconvert.txt")
    else:
        print("protocolo http detectado")
        exit()
    if os.path.exists("nucleiresult.txt"):
        splash6 = """
            +----------------------------------+
            | documento scaneo nucleiresult.txt 
            +----------------------------------+
        """
        print(splash6)
    else:
        splash7 = """
            +----------------------------------+
            | nuclei no encontradas vuln m,h        
            +----------------------------------+
        """
        print(splash7)
    if os.path.exists("xray.html"):
        splash8 = """
            +----------------------------------+
            | documento scaneo xray.html        
            +----------------------------------+
        """
        print(splash8)
    else:
        splash9 = """
            +----------------------------------+
            | xray No se han encontrado vuln         
            +----------------------------------+
        """
        print(splash9)
    exit()


def main():
    biaoti()
    update()
    masscan2httpx2nuclei(args())
    masscan2httpx2nuclei_main()

if __name__ == '__main__':
    main()
    exit()
