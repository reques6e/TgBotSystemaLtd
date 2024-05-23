# Телеграм бот "Systema"

<img src='assets/imgs/camera_1.png.png'>
<details>
  <summary>Смотреть больше фото</summary>
  <img src='assets/imgs/pay-list.png'>
  <img src='assets/imgs/pay_create.png'>
  <img src='assets/imgs/pay_out.png'>
  <img src='assets/imgs/user_profile.png'>
  <img src='assets/imgs/admin_panel.png'>
</details>

# Установка
Установщик [installer.bash](https://github.com/reques6e/TgBotSystemaLtd/blob/main/installer.bash)
```
┌──(reques6e㉿kali)-[~/Desktop/Project/TgBotCyxym]
└─$ chmod +x installer.bash
Установка завершена.
```
Работает под сервисом `tg_bot_systema.service`:
```
#!/bin/bash

chmod +x main.py
sudo apt install python3-pip
pip3 install -r assets/requirements.txt

cat > /etc/systemd/system/tg_bot_systema.service <<EOF
[Unit]
Description=Flask App
After=network.target

[Service]
User=root
WorkingDirectory=$(pwd)
ExecStart=$(which python) main.py
Restart=always

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable tg_bot_systema
systemctl start tg_bot_systema

echo "Установка завершена."

```

### Поднятие CDN сервера

С релиза 1.0.2, используется CDN для загрузки файлов на сервер.

Репозиторий: https://github.com/reques6e/TotalFile-CDNServerLite

### Настройка CDN

В файле конфигурации `data/config.json`, требуется разрешить загрузку определённых форматов файлов.

```json
        "allowed_files": ["txt", "pdf", "png", "jpg", "jpeg", "gif", "html", "zip", "py", "json"],
```

### Работа с сервисом
> Полный путь к сервису: `/etc/systemd/system/tg_bot_systema.service`

Для того что бы остановить бота, через сервис,требуется ввести в консоль:
```sh
systemctl stop tg_bot_systema.service
```
Для того что бы перезапустить бота, через сервис,требуется ввести в консоль:
```sh
systemctl restart tg_bot_systema.service
```
Для того что бы запустить бота, через сервис,требуется ввести в консоль:
```sh
systemctl start tg_bot_systema.service
```

### Настройка файлов конфигурации
> Файл конфигурации бота: `config.py`
```python
bot_token = '' # Сюда требуется вставить токен бота который можно получить у https://t.me/BotFather, подробная инструкция: https://developers.sber.ru/help/salutebot/telegram-integration
cdn_domain = '' # Сюда добавляем ссылку на cdn, если хотите запустить бота без CDN, то оставьте это поле пустым.
```

### Структура базы данных
> путь к базе данных: `bot/database/db.db`

> [!WARNING]
> База данных не зашифрована. Получение доступа злоумышленниками к серверу может привести к утечке данных пользователей.

```sql
TABLE users
      user_id INTEGER PRIMARY KEY,
      token TEXT,
      id INTEGER,
      password TEXT,
      is_admin INTEGER

TABLE favorites
      user_id INTEGER PRIMARY KEY,
      cams TEXT
```

### Базовое окружение бота и системные требования
> Kali Linux (Python 3.11.8 (64-bit))
>> Ядер: 2, AMD/INTEL, 2 GB RAM, 15 GB HDD/M2 NvMe, 200 Мбит

## Исходники:

API Systema Ltd - [Docs](https://github.com/reques6e/SystemUtilis/blob/main/API.md) (API v1 для обычных пользователей)

API Yandex Weather - [Docs](https://yandex.ru/dev/weather/doc/ru/concepts/forecast-rest#req-example) (API v2 для безнеса)
