class Texts:
    welcome_registration_text = """Добро пожаловать!
Данный бот не является официальным! Вы делаете всё на свой страх и риск, мы не несём ответственность за ваши действия.
\nДля начала работы введите ваш ID:"""
    
    welcome_registered_text = """👋 {user}, <b>добро пожаловать в Систему</b>
\nЗакрытый репозиторий для разработчиков бота: https://github.com/reques6e/TgBotSystemaLtd/"""

    send_me_your_password_text = """Теперь введите ваш пароль:"""
    
    take_action = """<b>❗️ Выберите действие:</b>"""

    menu_delete_text = """Меню удалено"""

    select_location_text = """Выберите локацию:"""

    password_or_login_error_text = """Неверный логин или пароль"""

    select_camera_text = """Выберите камеру:"""

    select_location_false_text = """Ошибка при получении локаций"""

    all_cameras_displayed_text = """Отображены все камеры"""
    
    all_cameras_displayed_false_text = """Ошибка при получении камер по локации"""

    get_camera_error_text = """Произошла ошибка при получении камеры"""

    camera_remove_from_favorites_text = """Камера удалена из избранного"""

    camera_remove_from_favorites_false_text = """Камера не найдена в избранном"""

    your_favorite_cameras_text = """Ваши избранные камеры:"""
    
    your_favorite_cameras_false_text = """Ваши избранные камеры пусты."""

    favorite_cameras_none_text = """У вас пока нет избранных камер."""

    is_lock_desc_text = """Заблокирован"""
    
    is_lock_desc_false_text = """Не заблокирован"""

    signed_in_on_another_device_text = """Выполнен вход на другом устройстве"""

    re_authorize = """\n\nВыполните команду для переавторизации:\n/re_auth"""

    add_to_favorites_text = """Камера добавлена в избранное"""

    add_to_favorites_error_text = """Вы достигли максимального количества избранных камер (9)"""

    menu_delete_notification_text = """✅ Успешно отменено"""

    message_delete_text = """Сообщение удалено"""

    delete_user_data_text = """Данные для пользователя с user_id {user_id} успешно удалены."""

    re_auth_true_text = """Профиль успешно переавторизован."""

    re_auth_false_text = """Не удалось выполнить переавторизацию."""

    re_auth_user_not_in_database_text = """Профиль не найден в базе данных."""

    notification_registration_text = """Новый пользователь зарегистрировался в боте, ID:"""
    
    weather_conditions_text = {
            'clear': 'Ясно',
            'partly-cloudy': 'Малооблачно',
            'cloudy': 'Облачно с прояснениями',
            'overcast': 'Пасмурно',
            'light-rain': 'Небольшой дождь',
            'rain': 'Дождь',
            'heavy-rain': 'Сильный дождь',
            'showers': 'Ливень',
            'wet-snow': 'Дождь со снегом',
            'light-snow': 'Небольшой снег',
            'snow': 'Снег',
            'snow-showers': 'Снегопад',
            'hail': 'Град',
            'thunderstorm': 'Гроза',
            'thunderstorm-with-rain': 'Дождь с грозой',
            'thunderstorm-with-hail': 'Гроза с градом'
        }


    profile_info_text = """🙋🏻‍♂️ Твой ID: [<code>{user_id}</code>]
💰 Баланс: <b>{balance}</b>
📜 Лицевой счет: <b>{account_number}</b>
💣 Статус блокировки: <b>{is_lock_desc}</b>
📅 Дата последнего платежа: <b>{last_payment_date}</b>
💳 Последнее пополнение: <b>{last_pay}</b>
🔍 Состояние: <b>{state}</b>
📶 Тариф: <b>{tariff}</b>"""
    
    profile_info_false_text = """Произошла ошибка при получении данных о профиле:\n<b>{error_description}</b>"""

    status_blocking_edited_text = """Статус блокировки изменён."""

    profile_not_found_text = """Ваш профиль не определён"""

    send_me_new_password_text = """Введите новый пароль:"""

    get_sms_code_text = """Введите SMS-код, который был отправлен на номер телефона +{rs['response']['phone']}:"""

    get_sms_code_false_text = """Не удалось отправить SMS-код.\n{rs['response']['message']}"""

    password_edited_text = """Пароль успешно изменён."""

    password_edited_false_text = """Ошибка при изменении пароля. Пожалуйста, попробуйте ещё раз."""

    payment_history_false_text = """Ошибка при получении истории платежей"""

    payment_history_none_text = """История платежей пуста."""

    your_payment_history_text = """Ваша история платежей
Веб-версия: {link}"""
    
    your_payment_history_no_cdn_text = """Ваша история платежей"""

    upload_file_to_cdn_error_text = """Ошибка при загрузке на CDN"""

    activate_promised_payment_text = """Обещанный платёж успешно активирован"""

    activate_promised_payment_false_text = """Обещанный платёж не был активирован"""

    subscribe_buy_text = """Введите сумму для пополнения баланса:"""

    process_amount_limit_text = """Введите сумму меньше {amount_limit}"""

    process_amount_text = """Ваша ссылка для пополнения лицевого счёта:
\n\n{pay_link}\n\n
Ссылка работает: <b>10 минут</b>
Сумма пополнения: <b>{amount}</b>
\n\n⚠️Ваш баланс автоматически пополнится после оплаты."""
    
    welcome_to_admin_panel_text = """🌟<b>Приветствую</b> <a href='tg://user?id={user_id}'>// {user_name}</a><b>, в админ-панели!</b>"""

    grant_access_text = """Введите ID пользователя, которому вы хотите предоставить доступ админа"""

    grant_access_true_text = """Пользователь с ID <code>{user_id}</code> получил доступ к админ панели."""

    grant_access_me_text = """Вы не можете выдать админа самому себе"""

    grant_access_is_admin_text = """Пользователь уже является администратором"""

    grant_access_false_text = """У вас нет прав на выдачу администраторских прав."""

    send_personal_text = """Введите ID пользователя, которому хотите отправить личное сообщение:"""
    
    send_personal_true_text = """Личное сообщение было успешно отправлено пользователю с ID <code>{user_id}</code>."""

    send_personal_false_text = """Произошла ошибка при отправке сообщения. Попробуйте еще раз."""
    
    process_personal_text = """Введите сообщение, которое хотите отправить этому пользователю:"""

    user_id_not_found = """Ошибка. Введите корректный ID пользователя."""

    revoke_access_text = """<b>Введите ID пользователя, у которого нужно отозвать доступ:</b>"""

    revoke_access_true_text = """У пользователя с ID <code>{user_id}</code> отозвали доступ к админ панели."""

    revoke_access_false_text = """Пользователь не является администратором"""

    process_content_input_text = """Начинаю рассылку..."""

    process_content_input_true_text = """Рассылка закончена."""

    process_content_input_false_text = """У вас нет прав."""

    mailing_text = """<i>Введите текст для рассылки или отправьте изображение</i>"""

    command_not_found_text = """К сожалению, я не смог распознать Вашу команду."""

    camera_info_text = """📷 Камера: <b>{channel}</b>
{description}
🌡️ Температура: <b>{temperature}°C</b>
☁️ Погодные условия: <b>{condition}</b>
💨 Скорость ветра: <b>{wind_speed} м/c</b>"""

    history_payment_text = """Ваша история платежей"""

    all_kino_displayed_text = """Отображены все фильмы"""

    kino_page_text = """<b>{name}</b>
    
{description}

<b>⭐Кинопоиск:</b> {rating}
<b>💫Рейтинг:</b> {likes}👍 / {dislikes}👎
"""

    send_film_name = """Выберите фильм:"""