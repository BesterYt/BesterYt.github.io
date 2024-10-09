import webbrowser
import time
import tkinter as tk
from tkinter import messagebox
import sys  # Импортируем sys для использования exit()

# Функция для отображения всплывающего окна с ошибкой и завершения программы
def show_message():
    root = tk.Tk()
    root.withdraw()  # Скрываем основное окно
    root.attributes("-topmost", True)  # Окно поверх всех
    messagebox.showerror("Ты тупой", "Ты чё дибил?")  # Всплывающее окно с текстом
    root.destroy()  # Закрываем окно
    sys.exit()  # Завершаем программу

# Функция калькулятора
def calculator():
    print("Добро пожаловать в калькулятор!")
    print("Введите 'exit' для выхода.")
    
    while True:
        # Получение ввода от пользователя
        expression = input("Введите выражение (например, 2 + 2): ")
        
        if expression.lower() == 'exit':
            print("Вы вышли из калькулятора.")
            break  # Возвращаемся в основной цикл
        
        try:
            # Используем eval для вычисления выражения
            result = eval(expression)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)
            print("Пожалуйста, введите корректное математическое выражение.")

# Основная программа
print("Пройдите регистрацию!")
name = input("Напишите имя/ник или сразу нажмите Enter: ")
print(name, "Добро пожаловать в Bester OC")

print("Чтобы выбрать функции, напишите их без ошибок.")
print("Функции: Авторы  Калькулятор  Off")

# Счетчик неправильных попыток
wrong_attempts = 0

# Запускаем бесконечный цикл для ввода команд
while True:
    # Получаем ввод от пользователя
    user_input = input("Введите команду: ")

    # Проверяем введенный текст
    if user_input.lower() == "авторы":
        webbrowser.open('https://youtube.com/@bester_play?si=Nh42uxgXb7tufIJO', new=2)
        wrong_attempts = 0  # Сбрасываем счетчик при правильном вводе
    elif user_input.lower() == "далее":
        print("Тут пусто D:")
        wrong_attempts = 0  # Сбрасываем счетчик
    elif user_input.lower() == "off":
        print("Turning off...")
        time.sleep(2)
        break  # Завершение программы при команде "off"
    elif user_input.lower() == "калькулятор":
        calculator()  # Запускаем калькулятор
        wrong_attempts = 0  # Сбрасываем счетчик после работы калькулятора

    else:
        print("Команда не распознана. Попробуйте еще раз.")
        wrong_attempts += 1  # Увеличиваем счетчик неправильных попыток

    # Проверяем, достиг ли пользователь 3 неправильных попыток
    if wrong_attempts >= 3:
        show_message()  # Показываем всплывающее окно


