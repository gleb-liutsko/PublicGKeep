# Public Google Keep
Шаринг заметок Google Keep

## Установка
1. Установить Python.
2. Установить virtualenv.
```bash
pip install virtualenv
```
3. Клонируем репозиторий. 
```bash
git clone https://github.com/gleb-liutsko/PublicGKeep.git
cd PublicGKeep
```
4. Создаем виртуальное пространство.
```bash
virtualenv venv
source venv/bin/activate
```
5. Устанавливаем зависимости.
```bash
pip install -r
pip install -r requirements.txt
```
6. Получаем токен.
```bash
python get_token.py
```
7. Настраиваем.
```bash
cp config.simple.py config.py
nano config.py
```
8. Настраиваем Web-Сервер и wsgi

## Скриншоты
### Телефон
![Главная Страница](https://github.com/gleb-liutsko/PublicGKeep/blob/master/img/Mobile/main_page.jpg)

---
![Заметка](https://github.com/gleb-liutsko/PublicGKeep/blob/master/img/Mobile/note_page.jpg)
### Десктоп
![Главная Страница](https://github.com/gleb-liutsko/PublicGKeep/blob/master/img/Desktop/main_page.png)

---
![Заметка](https://github.com/gleb-liutsko/PublicGKeep/blob/master/img/Desktop/note_page.png)
