from selenium.webdriver import Firefox
from time import sleep

def  find_by_text ( browser, tag , text ):
    
    elementos  =  browser.find_elements_by_tag_name ( tag )   # lista
    
    for  elemento  in  elementos :
        if elemento . text  ==  text :
            return elemento


url= 'http://newtours.demoaut.com/'
browser = Firefox()
browser.get(url)

nomes = ['SIGN-ON', 'REGISTER', 'SUPPORT', 'CONTACT','Home','Flights','Hotels','Cruises']

for nome in nomes:
    elementolink = find_by_text(browser,'a',nome).click()
    sleep(4.0)
    browser.back()
for nome in nomes:
    elementolink = find_by_text(browser,'a',nome).click()
    sleep(4.0)
    browser.forward()








