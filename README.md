# YaCut
Сервис укорачивания ссылок с web интерфейсом и REST API. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

Склонируйте репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```
Отредактируйте и переименуйте  `.env.template`. в  `.env`  
Примените миграции
```
flask db upgrade
```
Запустите сервер
```
flask run
```
web интервейс будет доступен по адресу http://localhost:5000/


## Над проектом работали
- [Косолапов Константин](https://t.me/KonstantinKosolapov)