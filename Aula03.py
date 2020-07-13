from selenium.webdriver import  Chrome

from time import sleep


url = 'https://curso-python-selenium.netlify.app/aula_03.html'

browser = Chrome()
browser.get(url)

sleep(3)

a = browser.find_element_by_tag_name('a')


for click in range(10):
    p = browser.find_elements_by_tag_name('p')
    a.click()
    print(f'Valor de p: {p[-1].text} valor do clock: {click}')
    print(f'Valor de p: {p[-1].text == str(click)}')

print(f'Texto de A: {a.text}')
#browser.quit()