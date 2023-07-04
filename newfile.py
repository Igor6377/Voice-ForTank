# модуль голсовые сообщения для танковни
# мой тг @igor637
from .. import loader


@loader.tds
class voiceForTank(loader.Module):
    """Голосовые сообщения танковни https://t.me/hatawot"""

    strings = {"name": "voiceWotHata"}

    async def малойcmd(self, message):
        """| Простите господин, это рофл? Если это не рофл, то твоего деда нахуй-нахуй посадил блять, я твою мать в рот ебал,и твоего отца,и тебя. Ты отсосал мой хуй и нахуй сперму мою пил нахуй, потому что ты: ебаный сука в рот-урод ебаный пидорас"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/3",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def шлвонcmd(self, message):
        """| На хуй говорю, иди с чата долбоёб ёбаный. Понял дурак, блядь."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/4",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def повезлоcmd(self, message):
        """| Тебе повезло, что сейчас добрый. Я бы сейчас я ебанул, там молнию метеорит. Что-то ещё да?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
             "https://t.me/tankovnacoco/5",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def стоныcmd(self, message):
        """| Стоны""";

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/6",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def чертилаcmd(self, message):
        """| Ты чертила обосанный закрой свой рот может у тебя мать сдохла, если ты такой даун с 5 iq  говоришь что мать сдохла ммм да мммм шутить про мать в 2020 году ты гений"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/7",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кринжcmd(self, message):
        """| Ты что Боже Боже чел. Ну, ты вообще калинж просто Блядь ну что-то несёшь. Ну не позорься, пожалуйста. я просто Кринжую просто с тебя."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/9",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def подождиcmd(self, message):
        """| подожди"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/201",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def спокcmd(self, message):
        """| спокойной ночи"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/202",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def ясноcmd(self, message):
        """| ясно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/203",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def обидcmd(self, message):
        """| я обиделась"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/204",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def тмнcmd(self, message):
        """| ты мне нравишся"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/205",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def мурcmd(self, message):
        """| мур"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/206",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def пжcmd(self, message):
        """| ну пожалуйста"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/207",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def спсcmd(self, message):
        """| спасибо"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/208",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def тыгдеcmd(self, message):
        """| Ну ты где?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/209",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def догcmd(self, message):
        """| Договорились"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/210",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def дутроcmd(self, message):
        """| Доброе утро"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/211",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def кснемогуcmd(self, message):
        """| К сожалению не могу"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/212",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нипонcmd(self, message):
        """| Нипоняла"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/213",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def интересноcmd(self, message):
        """| Расскажи мне интересно"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/214",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def чмокиcmd(self, message):
        """| Чмоки чмоки"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/215",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def спок2cmd(self, message):
        """| Спокойной ночи тебе"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/216",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def тыменялюбишьcmd(self, message):
        """| А ты меня любишь?"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/217",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def нукотикcmd(self, message):
        """| Ну котик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/218",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def котикcmd(self, message):
        """| Котик"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/219",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def блинcmd(self, message):
        """| Ну блин"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/220",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def скоробудуcmd(self, message):
        """| Скоро буду"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/radiofmonline/221",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return
