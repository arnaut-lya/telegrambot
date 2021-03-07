import sys
from win32.win32api import MessageBox

try:
    import logging
    import time
    import os

    from aiogram import Bot, Dispatcher, executor, types
    from aiogram.contrib.fsm_storage.memory import MemoryStorage
    from aiogram.dispatcher import FSMContext
    from aiogram.dispatcher.filters.state import StatesGroup, State

    import config
    import AquilaLoginLogout
    import VPN

    logging.basicConfig(level=logging.INFO)

    workBot = Bot(config.TOKEN)
    storage = MemoryStorage()
    disp = Dispatcher(workBot, storage=storage)
    aquila = AquilaLoginLogout.AquilaClass()
    vpn = VPN


    class Form(StatesGroup):
        token = State()


    @disp.message_handler(commands=["start"])
    async def cmd_start(message: types.Message):
        poll_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        poll_keyboard.add(types.KeyboardButton(text="Aquila Login"))
        poll_keyboard.add(types.KeyboardButton(text="Aquila Logout"))
        poll_keyboard.add(types.KeyboardButton(text="Connect VPN"))
        poll_keyboard.add(types.KeyboardButton(text="shutdown"))
        poll_keyboard.add(types.KeyboardButton(text="Help"))
        await message.answer("Good news everyone ! \n I m alive ! \nWhat do you want from me ?!",
                             reply_markup=poll_keyboard)
        await workBot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIF3mBD6qreYHT5aAfukUzeXjTPnW4UAAL4CAACXAJlA'
                                                         '-FWmSnQ1wdJHgQ')


    @disp.message_handler(lambda message: message.text == "Aquila Login")
    async def action_login_aquila(message: types.Message):
        if message.text == 'Aquila Login':
            await workBot.send_message(message.from_user.id, "Wait ...")
            if aquila.loadPageAndLogin(1):
                await workBot.send_photo(message.from_user.id, open("bot/package/screen/screen.png", "rb"))


    @disp.message_handler(lambda message: message.text == "shutdown")
    async def shutdown_pc(message: types.Message):
        if message.text == 'shutdown':
            await workBot.send_message(message.from_user.id, "Your pc death )")
            os.system('shutdown -s')


    @disp.message_handler(lambda message: message.text == "Aquila Logout")
    async def action_logout_aquila(message: types.Message):
        if message.text == 'Aquila Logout':
            await workBot.send_message(message.from_user.id, "Wait ...")
            if aquila.loadPageAndLogin(0):
                await workBot.send_photo(message.from_user.id, open("bot/package/screen/screen.png", "rb"))


    @disp.message_handler(lambda message: message.text == "Connect VPN")
    async def connect_vpn(msg: types.Message):
        if msg.text == 'Connect VPN':
            await Form.token.set()
            await msg.reply("Send me a Token")
            await workBot.send_sticker(msg.from_user.id, 'CAACAgIAAxkBAAIF4GBD7TaUWOhDgQ5zjAdJT_FjO'
                                                         'iMrAAIKAAM48KIaJ8P3EMmONPUeBA')
            time.sleep(15)

            @disp.message_handler(state=Form.token)
            async def process_token(message: types.Message, state: FSMContext):
                await workBot.send_message(message.from_user.id, "Wait ...")
                async with state.proxy() as data:
                    data['token'] = message.text
                    if data['token'] != '':
                        vpn.loginVPN(data['token'])
                        await workBot.send_message(message.from_user.id, "Done !")
                        await workBot.send_photo(message.from_user.id, open(config.imgPath, "rb"))
                        data['token'] = ''
                        await state.finish()
                    else:
                        await message.reply("Wrong message ...")
                        data['token'] = ''
                        await state.finish()


    @disp.message_handler(lambda message: message.text == "Help")
    async def action_help(message: types.Message):
        if message.text == 'Help':
            await workBot.send_message(message.from_user.id, "What do you need from me ?! leave me alone ! ↓ ↓ ↓")
            await workBot.send_sticker(message.from_user.id, 'CAACAgIAAxkBAAIF3GBD6K7Ve1Xg7YdtLSky'
                                                             '-Wz35XcHAAL5CAACXAJlA_kGTim2beilHgQ')


    if __name__ == '__main__':
        executor.start_polling(disp, skip_updates=True)
except Exception:
    import traceback
    exc_type, exc_value, exc_tb = sys.exc_info()
    traceback_exception = traceback.TracebackException(exc_type, exc_value, exc_tb)
    MessageBox(0, ''.join(traceback_exception.format()), "Error message", 0)
input("Press Enter for exit")