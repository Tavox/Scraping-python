from bs4 import BeautifulSoup 
import requests
import io

r = requests.get("https://store.steampowered.com/app/1091500/Cyberpunk_2077/")
soup = BeautifulSoup(r.content, "lxml")

nombre = soup.find('div', class_="apphub_AppName").text
print(nombre)

precio = soup.find('div', class_="game_purchase_price price").text
print(precio.strip())


with io.open("log.txt", "a", encoding="utf8") as logfile:
	soup.find(nombre)
	logfile.write(nombre)
	logfile.write("\n")
	soup.find(precio)
	logfile.write(precio)
	logfile.write("\n")




