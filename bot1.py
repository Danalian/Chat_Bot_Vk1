import vk_api, random
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor

# API токен сообщества
mytoken = ''

keyboard = VkKeyboard(one_time=True, inline=True)
keyboard.add_button('Привет', color=VkKeyboardColor.NEGATIVE)
keyboard.add_button('Клавиатура', color=VkKeyboardColor.POSITIVE)
keyboard.add_line()
keyboard.add_location_button()
keyboard.add_line()
keyboard.add_vkpay_button(hash="action=transfer-to-group&group_id=198461809")


# Функция посылающая сообщение
def write_msg(user_id, message):
    random_id = vk_api.utils.get_random_id()
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})


def create_keyboard(response):
    keyboard = VkKeyboard(one_time=True)

    if response == 'привет':
        keyboard.add_button('Хочу тян', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Тян не нужны!', color=VkKeyboardColor.NEGATIVE)

    elif response == 'какой у меня выбор?':
        keyboard.add_button('Хочу тян', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Тян не нужны!', color=VkKeyboardColor.NEGATIVE)

    elif response == 'выбор?':
        keyboard.add_button('Хочу тян', color=VkKeyboardColor.POSITIVE)
        keyboard.add_button('Тян не нужны!', color=VkKeyboardColor.NEGATIVE)

    keyboard = keyboard.get_keyboard()
    return keyboard


def keyb():
    """ Пример создания клавиатуры для отправки ботом """

    keyboard = VkKeyboard(one_time=True)

    keyboard.one_time=True

    keyboard.add_button('Белая кнопка', color=VkKeyboardColor.DEFAULT)
    keyboard.add_button('Зелёная кнопка', color=VkKeyboardColor.POSITIVE)

    keyboard.add_line()  # Переход на вторую строку
    keyboard.add_button('Красная кнопка', color=VkKeyboardColor.NEGATIVE)

    keyboard.add_line()
    keyboard.add_button('Синяя кнопка', color=VkKeyboardColor.PRIMARY)

    # message = 'Пример клавиатуры',
    keyboard = keyboard.get_keyboard()
    return keyboard

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=mytoken)
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text.lower()
            response = request

            keyboard = create_keyboard(response)
            key = '068a77450545f9c980b134f4ecee1a25a8ccaf7e'
            server = ('https://lp.vk.com/wh198461809')
            ts = ('286')
            random_id = vk_api.utils.get_random_id()
            message = 'Привет!'
            user_id = event.user_id
            keyboard = keyboard
            # vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': random_id})
            vk.method('messages.send', {'user_id': user_id,
                                        'message': message,
                                        'random_id': random_id,
                                        'key': key,
                                        'server': server,
                                        'ts': ts
                                        })

            # Логика формирования ответа бота
            if ('Привет' in request):
                otvet = 'Ну привет, если не шутишь!'
                write_msg(event.user_id, otvet)
           # elif ('Клавиатура' in request):
                # keyboard = create_keyboard(response)
                # vk.method = messages.send(
                #     key=('068a77450545f9c980b134f4ecee1a25a8ccaf7e'),  # ВСТАВИТЬ ПАРАМЕТРЫ
                #     server=('https://lp.vk.com/wh198461809'),
                #     ts=('286'),
                #     random_id=get_random_id(),
                #     message='Привет!',
                #     chat_id=event.chat_id,
                #     keyboard=keyboard
                # )
            else:
                otvet = 'Я только на "Привет" реагирую'
                write_msg(event.user_id, otvet)
