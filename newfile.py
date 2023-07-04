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

    async def репчинаcmd(self, message):
        """| малой зачитал репчину"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/12",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def гимнcmd(self, message):
        """| гимн бабахаводов"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/13",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def мойдедcmd(self, message):
        """| Мой дед блядь, бахал, нахуй французов, блядь, чтобы ты сейчас ебалась и дрочила свою пизду, блядь, а не отсасывала ёбаном французом, нахуй немцам. Сука, ты ёбаная, чтоб сдохла ты."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/11",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def напидорасcmd(self, message):
        """| малой посылает пидораса"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/15",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def даунcmd(self, message):
        """| даун обосанный"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/16",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def сынокcmd(self, message):
        """| Окей сыночек ебаный прутодичный залупной творожник и покажи мне удел свой терпила, ёбаная способная лишь показывать, насколько ты умеешь сосать мой огромный хуец и три пластовенный хуйровище, но так Получи же, очередную порцию, харчей в свой тупоеду ебальничек, некогда выебанную утюгом. Ты просто ещё не понимаешь, что рано или поздно за реальные копипастой. Я буду ставить тебя раком, а затем после того, как твой же Отец обрубок вытрахает тебя насквозь и получишь мою пятку себе промеж шейных позвонков."""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/21",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

    async def фактcmd(self, message):
        """| раскидка по фактам"""

        reply = await message.get_reply_message()
        await message.delete()
        await message.client.send_file(
            message.to_id,
            "https://t.me/tankovnacoco/22",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
        return

                        
