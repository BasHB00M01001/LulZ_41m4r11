
# LulZ_41m4r11
Herramienta que combina varias herramientas ; Escaneo completo de puertos con Masscan ==> Escaneo servicios web con httpx ==> Escaneo de vulnerabilidades con Nuclei y  Xray
Para utilizar esta herramienta tienes que clonar dentro de esta carpeta estos repositorios;
* **[masscan](https://github.com/robertdavidgraham/masscan)**
* **[httpx](https://github.com/projectdiscovery/httpx/releases/)**
* **[nuclei](https://github.com/projectdiscovery/nuclei/releases)**
* **[xray](https://github.com/chaitin/xray/releases/tag/1.8.4)**

Una vez clonado Massscan y extraidos los zip el comando de ataque es el siguiente;

python3 LulZ_41m4r11.py -i ip.txt -p 1-65535 --rate 2000

Antes de iniciar scaneo abrir el archivo ip.txt e introducir las Ips que se quiera scanear

LulZ_41m4r11 is a Tool that combines several tools; Full port scanning with Masscan ==> Scanning web services with httpx ==> Vulnerability scanning with Nuclei and Xray 
To use this tool you have to clone these repositories inside this folder;
* **[masscan](https://github.com/robertdavidgraham/masscan)**
* **[httpx](https://github.com/projectdiscovery/httpx/releases/)**
* **[nuclei](https://github.com/projectdiscovery/nuclei/releases)**
* **[xray](https://github.com/chaitin/xray/releases/tag/1.8.4)**

Once Massscan has been cloned and the zip extracted, the attack command is as follows;

python3 LulZ_41m4r11.py -i ip.txt -p 1-65535 --rate 2000

Before starting scanning, open the ip.txt file and enter the IPs you want to scan
![aimar](https://github.com/user-attachments/assets/0d02244b-0528-4783-a22b-3bf993834e83)

![aimar2](https://github.com/user-attachments/assets/0119348e-5873-4b45-8a98-b77b68b35ca9)

