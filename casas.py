#Importamos las librerias que necesitamos 
import requests
from bs4 import BeautifulSoup
from datetime import datetime,date
#req=requests.get('https://casas.hendyla.com')
req=requests.get('https://www.hendyla.com/casas.html')
soup= BeautifulSoup(req.content,'html.parser')
#casas= soup.find_all('article',class_ ='product-item clasificado')
casas=soup.find_all("a", class_="imgLiquidFill imgLiquid") 
precio= soup.find_all('div',class_='precio left')
imagen=soup.select('figure.img img')[0].get('src')
indice=0
detalles=[]
precio2=[]
link=[]
link_imagen=[]

for elemento in casas:
    aux=elemento.img.get("alt")                                                     # parseamos el atributo ALT
    detalles.append(aux)                                                            #Agregamos la salida a la lista 'detalles'
    aux2=elemento.img.get('src')                                                    #parseamos el atributo src
    link_imagen.append(aux2)                                                        #Agregamos la salida a la lista 'link_imagenes'
    aux3=elemento.get('href')                                                       #parseamos el atributo href
    link.append(aux3)                                                               #Agregamos la salida a la lista link
    elemento=precio[indice].p.get_text()[25:50]                                     #parseamos el precio de la variable 'precio'
    precio2.append(elemento)                                                        #Agregamos la salida a la lista precio2
    print('Detalles: ', detalles[indice])                                              
    print ('Precio: ', precio2[indice])
    print ('Link de la Publicación: ',link[indice])
    print ('Link de la imagen de la publicación:  ',link_imagen[indice],'\n')
    indice+=1



