color 2
::Убиваем процесс программы
taskkill /f /im "Password generator.exe"
:: Запускает комплицию проекта с помощью pyinstaller
:: Предварительно установите кодировку - Кирилица OEM 866
pyinstaller --onefile --noconsole --icon=ico.ico "Password generator.py"
:: Запускаем программу после компиляции
cd dist
start "Password generator" "Password generator.exe"