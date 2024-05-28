import tkinter as tk
import random
import string
import pyperclip

# Функция для генерации пароля
def generate_password():
    # Получаем длину пароля из поля ввода
    length = int(length_entry.get())
    # Получаем значения выбранных флажков
    use_uppercase = uppercase_var.get()
    use_lowercase = lowercase_var.get()
    use_special_chars = special_chars_var.get()
    use_digits = digits_var.get()

    # Инициализируем строку для хранения всех возможных символов и список для пароля
    chars = ''
    password = []

    # Добавляем в возможные символы и в пароль по одному символу каждого выбранного типа
    if use_uppercase:
        chars += string.ascii_uppercase
        password.append(random.choice(string.ascii_uppercase))
    if use_lowercase:
        chars += string.ascii_lowercase
        password.append(random.choice(string.ascii_lowercase))
    if use_special_chars:
        chars += string.punctuation
        password.append(random.choice(string.punctuation))
    if use_digits:
        chars += string.digits
        password.append(random.choice(string.digits))

    # Проверяем, чтобы длина пароля не была меньше количества выбранных типов символов
    if len(password) > length:
        password_label.config(text="Длина слишком короткая")
        copy_button.config(state=tk.DISABLED)
        return

    # Заполняем оставшиеся символы случайными символами из всех выбранных типов
    while len(password) < length:
        password.append(random.choice(chars))

    # Перемешиваем пароль, чтобы символы каждого типа не стояли вместе
    random.shuffle(password)
    # Преобразуем список в строку
    password = ''.join(password)

    # Отображаем пароль в метке
    password_label.config(text=password)
    # Активируем кнопку копирования, если пароль был сгенерирован
    copy_button.config(state=tk.NORMAL if password else tk.DISABLED)

# Функция для копирования пароля в буфер обмена
def copy_password():
    # Получаем текст пароля из метки
    password = password_label.cget('text')
    # Копируем пароль в буфер обмена
    pyperclip.copy(password)

# Создание графического интерфейса
window = tk.Tk()
window.title("Генератор паролей")
window.resizable(width=False, height=False)

try:
    # Ставим иконку для заголовка приложения
    window.iconbitmap(r'ico.ico')
except:
    # Если иконки в каталоге нет, то ничего не делаем
    pass

# Метка и поле ввода для длины пароля
length_label = tk.Label(window, text="Длина пароля:")
length_label.pack()
length_entry = tk.Entry(window)
length_entry.insert(0, "12")  # Устанавливаем значение по умолчанию
length_entry.pack()

# Флажок для использования больших букв
uppercase_var = tk.IntVar(value=1)  # По умолчанию выбрано (использовать большие буквы)
uppercase_checkbtn = tk.Checkbutton(window, text="Использовать большие буквы", variable=uppercase_var)
uppercase_checkbtn.pack()

# Флажок для использования маленьких букв
lowercase_var = tk.IntVar(value=1)  # По умолчанию выбрано (использовать маленькие буквы)
lowercase_checkbtn = tk.Checkbutton(window, text="Использовать маленькие буквы", variable=lowercase_var)
lowercase_checkbtn.pack()

# Флажок для использования цифр
digits_var = tk.IntVar(value=1)
digits_checkbtn = tk.Checkbutton(window, text="Использовать цифры", variable=digits_var)
digits_checkbtn.pack()

# Флажок для использования специальных символов
special_chars_var = tk.IntVar()
special_chars_checkbtn = tk.Checkbutton(window, text="Использовать специальные символы", variable=special_chars_var)
special_chars_checkbtn.pack()

# Кнопка для генерации пароля
generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.pack()

# Метка для отображения сгенерированного пароля
password_label = tk.Label(window, text="", width=20, wraplength=150)
password_label.pack()

# Кнопка для копирования пароля в буфер обмена
copy_button = tk.Button(window, text="Копировать", state=tk.DISABLED, command=copy_password)
copy_button.pack()

# Функция для закрытия главного окна
def exit_root(event):
    window.quit()

# Закрыть главное окно и все дочерние окна через ESC
window.bind('<Escape>', exit_root)

# Запуск главного цикла обработки событий
window.mainloop()