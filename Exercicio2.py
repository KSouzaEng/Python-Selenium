from selenium.webdriver import Chrome
from time import sleep

url = 'https://curso-python-selenium.netlify.app/exercicio_02.html#'

navegador = Chrome()
navegador.get(url)

sleep(3)

a = navegador.find_element_by_tag_name('a')
p = navegador.find_elements_by_tag_name('p')
a.click()
if(p[1] == p[-1]):
     print(a.text)
     print(p.text)
        
 






