from telethon import TelegramClient, events, sync
import json
import asyncio
import time
import re

api_id = 29586810  # ваш API ID
api_hash = '200318c4007974487333005f24002075'  # ваш API Hash
admin_ids = [2127246009]  # Список ID администраторов
client = TelegramClient('userbot111', api_id, api_hash)

users_file = "users.json"
user_tasks = {}

# Загружаем или создаем файл с пользователями
def load_users():
    try:
        with open(users_file, "r") as file:
            data = json.load(file)
            if isinstance(data, dict):  # Убеждаемся, что data является словарем
                print('Убедились')
                return data
            else:
                return {}  # Возвращаем пустой словарь, если data не словарь
    except (FileNotFoundError, json.JSONDecodeError):
        return {}  # Возвращаем пустой словарь, если возникли ошибки при загрузке файла


def save_users(users):
    with open(users_file, "w") as file:
        json.dump(users, file)

users = load_users()

async def user_checker(user_id):
    print(f"Starting user_checker for {user_id}")  # Debug print
    initial_time = users.get(user_id, 0)

    try:
        # Series of messages and delays
        events = [
            (1209600, "Вітаю!\n\nУ нашій компанії сум-печаль:\nАсистенти плачуть, а керівник у депресії 😭\n\nЦе через те, що ми дуже сумуємо за Вашими завданнями 💔\n\nМоже, ми не виправдали очікування або у Вас є свої причини, але для нас Ви цінний клієнт і ми дістанемо \"зірку з неба\", щоб Ви повернулися.\n\nМи готові організувати зустріч із нашим директором, щоб Ви озвучили побажання, а ми їх реалізували.\n\nДавайте ми з ще більшою турботою та відповідальністю будемо допомагати Вам далі, а також Вашій дружині 🙌🏽\n\nНа честь Вашого повернення ми навіть підготували 🎁 приємний бонус.\n\nЯк Вам моя пропозиція?"),
            (2629743, "1.mp4"),
            (3944615, "🌟 Успіх - це коли наші клієнти говорять за нас!\n\nОзнайомтесь з відгуками та кейсами наших клієнтів в Телеграм-каналі [siripro_otziv](https://t.me/siripro_otziv) та Інсті [siri.pro](https://www.instagram.com/siri.pro?igshid=YmMyMTA2M2Y%3D). Приєднуйтесь 🔥"),
            (5259487, "📣 Якщо Ви хочете стати майстром з делегування, щоб Ваші задачі завжди виконувались - радимо подивитись круте інформативне відео без води з Дмитром Тетерваком та Олексієм Ронісом.\n\nВ цьому відео вони розповідають про найефективніші інструменти делегування🔥\n\nНе пропустіть таку можливість!😱🔝 [Дивіться відео 👇](https://www.youtube.com/watch?v=X7h8UMVJ4zw) 🎥"),
            (5259487, "https://www.youtube.com/watch?v=JrfhR_IW6bA"),
            (5259487, "2.mp4"),
            (5259487, "Хочете побачити скільки всього може виконати асистент? 😎\n\nЗаходьте та знайомтесь з реальними кейсами наших клієнтів ! 1000 і 1 задача асистента [тут 👉](https://www.notion.so/1000-1-Siri-Pro-f16de3c770d34958984ae0d4fab55a63?pvs=4) 📲"),
            (5259487, "Порівняйте, чому наша Siri Pro краща за офлайн асистента:\n\n✅ Відібрана, навчена та професійна - може розпочати виконувати Ваші завдання вже через 10 хвилин.\n\n✅ Досвідчена, адаптована і працює за стандартами, бізнес-процесами компанії.\n\n✅ Ніколи не хворіє і не ходить у відпустку.\n\n✅ З палаючими очима та великою мотивацією.\n\n✅ Можете користуватися сервісом коли Вам зручно, навіть по годинах.\n\n✅ Працює у нас на штатній основі - Вам не потрібно доплачувати нічого.\n\nОбирайте Siri Pro і отримуйте найкращий сервіс ! 💼💪🏆"),
            (5259487, "Маєте не багато задач, але вони все одно відбирають ваш час?\nУ нас є унікальний формат - погодинна співпраця⌛️\n\nВаша година коштує значно дорожче, ніж година роботи асистента!\n\nВи платите за виконані задачі, отримуєте звіт і насолоджуєтесь життям. Давайте затестуємо? 😉"),
            (5259487, "Привіт!\n\nВам не підходить віддалений асистент? Ви хотіли, щоб у Вас був асистент в команді? 😊\n\nМи з радістю підберемо Вам топового кандидата!\n\nМи маємо дуже великий досвід, свою базу асистентів, багато позитивних відгуків, а також гарантію на підібраного кандидата 🔝👍\n\nДля отримання безкоштовної консультації вже з підбору асистента в команду 📲"),
            (5259487, "посадова інструкція асистента.pdf"),
            (5259487, "Ой-ой!\n\nСплив рік, і нам так сумно без Вас! 🥺 Ми тут думали, можливо, Ви про нас забули? Але навіть якщо так – ми завжди тут, щоб виконувати Ваші задачі 😊\n\nЩо скажете, знову з нами в цьому році? Обіцяємо, що не будемо Вам набридати 😇\n\nЧекаємо на Вас, як завжди!🤗")
        ]



        for delay, content in events:
            await asyncio.sleep(delay)  # Wait for the specific delay

            current_time = time.time()
            if current_time - users.get(user_id, 0) < delay:
                print(f"Exiting user_checker for {user_id} due to activity")  # Debug print
                return  # User was active, so don't send the message

            try:
                if content.endswith('.mp4'):
                    print(f"Sending MP4 to {user_id}")  # Debug print
                    await client.send_file(int(user_id), content)  # Send the video
                    # Your logic to send MP4
                elif content.endswith('.pdf'):
                    print(f"Sending PDF file to {user_id}")  # Debug print
                    await client.send_file(int(user_id), content)  # Send the PDF
                else:
                    print(f"Sending message to {user_id}")  # Debug print
                    await client.send_message(int(user_id), content, link_preview=False, parse_mode='md')  # Send the message
            except Exception as e:
                print(f"Couldn't send to {user_id}, error: {e}")

            users[user_id] = current_time  # Update the last active time
            save_users(users)  # Save the updated time
    finally:
        # Clean up code, if any
        if user_id in user_tasks:
            del user_tasks[user_id]  # Clean up the task when done or cancelled


async def new_message_handler(event):
    user_id = str(event.sender_id)
    if user_id in users:  # Проверяем, есть ли пользователь в списке отслеживания
        users[user_id] = time.time()  # Обновляем время последней активности
        save_users(users)

        if user_id in user_tasks:
            user_tasks[user_id].cancel()  # Отменяем существующую задачу
        # Создаем новую задачу для проверки сообщений пользователя
        user_tasks[user_id] = asyncio.create_task(user_checker(user_id))


@client.on(events.NewMessage(pattern='/add_user'))
async def add_user(event):
    if event.sender_id in admin_ids:
        user_id_to_add = re.search(r'/add_user (\d+)', event.message.text)
        if user_id_to_add:
            user_id_to_add = user_id_to_add.group(1)
            # Добавляем пользователя, если его еще нет в списке
            if user_id_to_add not in users:
                users[user_id_to_add] = time.time()  # Добавляем пользователя с текущим временем
                save_users(users)
                await event.respond(f"Пользователь {user_id_to_add} добавлен.")
                # Запускаем отслеживание для нового пользователя
                client.loop.create_task(user_checker(user_id_to_add))
            else:
                await event.respond("Пользователь уже добавлен.")
        else:
            await event.respond("Пожалуйста, укажите правильный ID пользователя.")


@client.on(events.NewMessage(pattern='/del_user'))
async def del_user(event):
    if event.sender_id in admin_ids:
        user_id_to_del = re.search(r'/del_user (\d+)', event.message.text)
        if user_id_to_del:
            user_id_to_del = user_id_to_del.group(1)
            if user_id_to_del in users:
                del users[user_id_to_del]  # Удаляем пользователя из слежения
                save_users(users)
                await event.respond(f"Пользователь {user_id_to_del} удален.")
            else:
                await event.respond("Пользователь не найден.")

@client.on(events.NewMessage(pattern='/list_users'))
async def list_users(event):
    if event.sender_id in admin_ids:
        message = "Список всех пользователей:\n" + "\n".join(users)
        await event.respond(message or "Список пользователей пуст.")
        
client.on(events.NewMessage(incoming=True))(new_message_handler)  # Обновляем обработчик для новых сообщений

client.start()
for user_id in users.keys():
    user_tasks[user_id] = client.loop.create_task(user_checker(user_id))

client.run_until_disconnected()