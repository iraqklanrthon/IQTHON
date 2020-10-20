#"""@iqthon iraq ©
""" Google Translate
Available Commands:
.ترجمه LanguageCode as reply to a message
.ترجمه LangaugeCode | text to translate"""

import emoji
from googletrans import Translator
from userbot.utils import admin_cmd


@borg.on(admin_cmd("ترجمه ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    if "trim" in event.raw_text:
        
        return
    input_str = event.pattern_match.group(1)
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        text = previous_message.message
        lan = input_str or "ml"
    elif "|" in input_str:
        lan, text = input_str.split("|")
    else:
        await event.edit("**⌔︙ قم برد الى الكلمه المراد ترجمتها ⚠️**")
        return
    text = emoji.demojize(text.strip())
    lan = lan.strip()
    translator = Translator()
    try:
        translated = translator.translate(text, dest=lan)
        after_tr_text = translated.text
       
        output_str = """**الترجمه** من {} الى {}
{}""".format(
            translated.src,
            lan,
            after_tr_text
        )
        await event.edit(output_str)
    except Exception as exc:
        await event.edit(str(exc))
