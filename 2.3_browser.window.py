from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary") # клацнуть на кнопку
    button.click()

    new_window = browser.window_handles[1]  # узнаем имя вкладки, через массив всех имен вкладок, просим вывести нужную по порядку (если знаем)
    browser.switch_to.window(new_window) #переход на новую вкладку, в скобках имя новой вкладки

    X = browser.find_element(By.CSS_SELECTOR, "[id='input_value']") # находим элемент x на странице
    x = X.text
    y = calc(x) # посчитать формулу
    print(y)

    Answer = browser.find_element(By.CSS_SELECTOR, "[id='answer']") # передать в поле значение
    Answer.send_keys(y)

    button2 = browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary") # клацнуть на кнопку
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    # пустая строка


#ALERT
#alert('Hello!');

#согласиться с ошибкой в модальном окне, чтобы закрыть его
#переходим на окно и соглашаемся
#alert = browser.switch_to.alert
#alert.accept()
#confirm.dismiss() #отказаться в модальном окне

#Чтобы получить текст из alert, используйте свойство text объекта alert:
#alert = browser.switch_to.alert
#alert_text = alert.text

#чтобы ввести текст в модальное окно
#prompt = browser.switch_to.alert
#prompt.send_keys("My answer")
#prompt.accept()

#BROWSER_WINDOW
#browser.switch_to.window(window_name) #переход на новую вкладку, в скобках имя новой вкладки
#new_window = browser.window_handles[1] #узнаем имя вкладки, через массив всех имен вкладок, просим вывести нужную по порядку (если знаем)
#first_window = browser.window_handles[0] #имя текущей вкладки, для дальнейшей работы с ней

#    X = browser.find_element(By.CSS_SELECTOR, "[id='input_value']") # находим элемент x на странице
#    x = X.text
#    y = calc(x) # посчитать формулу
#    print(y)
#    browser.execute_script("window.scrollTo(0, 180)") # прокрутить страницу на заданное кол-во пикселей

#    FirstName = browser.find_element(By.CSS_SELECTOR, "[placeholder='Enter first name']") # передать в поле значение
#    FirstName.send_keys("Artem")

#вставить файл
#    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
#    file_name = "for_add_txt_file.txt"
#    file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
#    element = browser.find_element(By.CSS_SELECTOR, "[id='file']")
#paste_manual    element.send_keys("C:\\Users/Minchenko_KL\\PycharmProjects\\Stepik\\venv\\for_add_txt_file.txt")
#paste_auto    element.send_keys(file_path)


#    StepSix = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']") #клацнуть на чекбокс
#    StepSix.click()

#    StepSeven = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")  # клацнуть на радиокнопку
#    StepSeven.click()

#    button = browser.find_element_by_tag_name("button")
#    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#    button.click()

#    select = Select(browser.find_element(By.TAG_NAME, "select"))
#    select.select_by_visible_text(str(x))


