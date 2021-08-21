from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver.v2 as UC
import requests

def Webscraping_manga_pag (url):
    
    '''options = UC.ChromeOptions()
    options.user_data_dir ='C:\este'
    options.add_argument('--no-first-run --no-service-autorun --password-store=basic')'''
    opt = Options()
    ua='test'
    opt.add_argument('--user-agent=%s' % ua)
    opt.add_argument('--no-first-run --no-service-autorun --password-store=basic')
    driver = webdriver.Chrome('F:\chromedriver.exe', options=opt)
    #driver=UC.Chrome(executable_path=r"C:\chromedriver.exe",chrome_options=ops)
    #driver = UC.Chrome('F:\chromedriver.exe', options=ops)

    html = url
    
    driver.get(html)
    elemento = WebDriverWait(driver,10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'main version-chap no-volumn active'))
    )
    print(elemento)
    driver.close()
    
    '''html = requests.get(url).text
    
    soup = BeautifulSoup(html,'lxml')
    print(soup.encode('utf-8'))
    lista_capitulos = []
    cata_capitulo = soup.find_all('div', class_ = 'listing-chapters_wrap cols-1 show-more')
    print(cata_capitulo)
    for teste in cata_capitulo:
        print('a')'''

url= 'teste'
url_cap = 'famigerado'
Webscraping_manga_pag()

def Webscraping_img_cap(url_cap):
    html = requests.get(url_cap).text

    soup = BeautifulSoup(html, 'lxml')
    lista_imagem = []
    cata_imagem = soup.find_all('img', class_ ='wp-manga-chapter-img img-responsive lazyload effect-fade')
    print(cata_imagem)
    '''for imagem in cata_imagem:
        temporario = imagem.get('data-src')
        lista_imagem.append(temporario.strip('\t\n'))
    return(lista_imagem)'''

#Webscraping_img_cap(url_cap)



'''def teste():
    html = requests.get('url').text
    soup = BeautifulSoup(html, 'lxml')
    #print(html.encode('utf-8'))
    test = url_cap
    lista_capitulos = []
    cata_capitulo = soup.findAll('a', href =re.compile(test))
    for cap in cata_capitulo:
        temp = cap.get('href')
        lista_capitulos.append(temp)
    print(lista_capitulos)
teste(url,url_cap)'''