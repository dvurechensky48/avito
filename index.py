#/usr/bin/python3

from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from termcolor import colored
from time import sleep
import csv


def write_csv(data):
    with open('avito.csv', 'a') as f:
        writer = csv.writer(f)

        writer.writerow( (data['name'],
                          data['phone']) )
    pass

def login_avito(login,password,driver):
	driver.get('https://avito.ru')
	link = driver.find_element_by_class_name('js-header').find_element_by_tag_name('div').find_elements_by_tag_name('div')[1].find_element_by_tag_name('div').find_elements_by_tag_name('div')[1].find_element_by_tag_name('a')
	link.click()
	form = driver.find_elements_by_tag_name('form')[2]
	input_login = form.find_element_by_tag_name("input")
	input_login.click()
	input_login.send_keys(login)
	sleep_five_sec()
	input_pass = form.find_element_by_xpath("//input[@type='password']")
	input_pass.click()
	input_pass.send_keys(password)
	sleep_five_sec()
	input_subm = form.find_element_by_xpath("//button[@data-marker='login-form/submit']")
	input_subm.click()
	print('авторизовался')
	pass

def send_mess(driver,txt):
	try:
		butt = driver.find_element_by_class_name('js-write-message')
	except:
		return False
	butt.click()
	sleep(2)
	txt = driver.find_element_by_class_name('channel-footer-input')
	txt.click()
	txt.send_keys(txt)
	sleep(2)
	driver.find_element_by_class_name('channel-footer-send').click()
	return True

def sleep_five_sec():
	print(colored("1", 'red'))
	sleep(1)
	print(colored("2", 'red'))
	sleep(1)
	print(colored("3", 'red'))
	sleep(1)
	print(colored("4", 'red'))
	sleep(1)
	print(colored("5", 'red'))
	sleep(1)
	print(colored("6", 'red'))
	sleep(1)
	print(colored("7", 'red'))
	sleep(1)
	print(colored("8", 'red'))
	sleep(1)
	print(colored("9", 'red'))
	sleep(1)
	print(colored("10", 'red'))
	sleep(1)
	pass

CONS_TXT = "ЗАточкин\nПРОФЕССИОНАЛЬНАЯ ЗАТОЧКА ИНСТРУМЕНТА В Г. ЛИПЕЦКЕ\n- Парикмахерский инструмент (ножницы прямые и филировочные, конвекс, ножевые блоки машинок для стрижки).\n- Маникюрный/ педикюрный инструмент (кусачки, щипчики, пинцеты, шаберы).\n- Портновский инструмент (ножницы, ножи для оверлока, ножи для эл. ножниц)\nи многое другое.\n!!!ГАРАНТИЯ КАЧЕСТВА!!!\n____________________________________\nул. Шерстобитова, 8\nЗапись по тел. 200-578\nhttp://www.zatochkin.ru\nvk.com/zatochkalip"
print(colored("ПАРСЕР АВИТО ZET", 'green'))
sleep(1)
print(colored("Введите город", 'green'))
CONS_TOWN = input()
print(colored("Введите раздел", 'green'))
CONS_PAGE = input()
print(colored("Введите логин", 'green'))
CONS_LOGIN = input()
print(colored("Введите пароль", 'green'))
CONS_PASS = input()

CONS_URL = 'https://www.avito.ru/'+CONS_TOWN+'/'+CONS_PAGE
CONS_URL_M = 'https://m.avito.ru/'+CONS_TOWN+'/'+CONS_PAGE

#Открыть браузерls
driver = webdriver.Chrome('/home/nikita/Driver/chromedriver')
#авторизуемся
login_avito(CONS_LOGIN,CONS_PASS,driver)
sleep_five_sec()
driver.get(CONS_URL)
print(colored("Страница загружена  -  " + CONS_URL, 'green'))
#Получаем колличество страниц
counts = driver.find_elements_by_class_name('pagination-page')
count = counts[len(counts)-1]
count = count.get_attribute('href').split('=')[1].split('&')[0]
print(colored("Колличество страниц - " + count, 'green'))

#Начинаем парсить
for i in range(2,int(count)):
	sleep_five_sec()
	print(colored("Cтраницf - " + str(i), 'green'))
	driver.get(CONS_URL_M+'?p='+str(i))
	elements = driver.find_elements_by_class_name('item-link')
	count_elements = len(elements)
	for k in range(0,int(count_elements)-1):
		elements = driver.find_elements_by_class_name('item-link')
		print(k)
		sleep_five_sec()
		print(colored(str(elements[k].get_attribute('href')), 'yellow'))
		driver.get(str(elements[k].get_attribute('href')))
		try:
			phone =  driver.find_element_by_class_name('person-action')
			phone.click()
			sleep_five_sec()
		except:
			phone = ''
		try:
			phone =  driver.find_element_by_class_name('person-action').get_attribute('href').split(':')[1]
		except:
			phone = ''
		try:
			name = driver.find_element_by_class_name('person-name').text
		except:
			name = ''
		data = {'name':name,'phone':phone}
		print(data)
		write_csv(data)

		#написать сообщение
		send_mess(driver,CONS_TXT)
		
		driver.get(CONS_URL_M+'?p='+str(i))
		k = k +1
		pass
	pass

#Закрыть браузеры
driver.close()

