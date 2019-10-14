# Public Google Keep
Поделись заметками...  
Поддерживаются Python 3.6+.

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
