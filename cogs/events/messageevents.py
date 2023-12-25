"""
Responsible for messaging all jury channels if another jury/staff types in a channel and automatically uploading a Minecraft log to mclogs.
"""

import discord
import datetime
import asyncio
import yaml
import re
from discord.ext import commands
from mtranslate import translate

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

embed_color = data["General"]["EMBED_COLOR"]
show_original_message = data["Translator"]["SHOW_ORIGINAL_MESSAGE"]
show_language_type = data["Translator"]["SHOW_LANGUAGE_TYPE"]
show_translated_language = data["Translator"]["SHOW_TRANSLATED_LANGUAGE"]
author_display = data["Translator"]["AUTHOR_DISPLAY"]
automatic_delete_translated_message = data["Translator"]["AUTOMATIC_DELETE_TRANSLATED_MESSAGE"]
automatic_delete_translated_message_duration = data["Translator"]["AUTOMATIC_DELETE_TRANSLATED_MESSAGE_DURATION"]
translate_type = data["Translator"]["TRANSLATE_TYPE"]
translator_languages = data["Translator"]["TRANSLATOR_LANGUAGES"]
works_in_all_categories = data["Translator"]["WORK_IN_ALL_CATEGORIES"]
categories = data["Translator"]["CATEGORIES"]

class MessageEventsCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if message.guild:
            if translate_type == "automatic":
                if works_in_all_categories:
                    pass
                else:
                    if message.channel.category.id in categories:
                        pass
                    else:
                        return
                
                languages_list = [lang.strip().lower() for lang in translator_languages.split(',')]

                langs = []
                for lang in languages_list:
                    if lang not in self.bot.valid_langs:
                        pass
                    else:
                        langs.append(lang)

                translated_messages = {}

                if show_translated_language:
                    for lang in langs:
                        translated = translate(message.content, lang)
                        if show_language_type == "language-flag":
                            flag = self.bot.language_flags.get(lang, "")
                            output = f"{flag} {translated}"
                        else:
                            output = f"{lang}: {translated}"
                        translated_messages[lang] = output
                
                else:
                    for lang in langs:
                        translated = translate(message.content, lang)
                        output = f"{translated}"
                        translated_messages[lang] = output

                output = "\n\n".join([f"{translated_messages[lang]}" for lang in langs])

                if show_original_message:
                    embed = discord.Embed(title="Translated Message", description=f"""
**__Original Message__**
{message.content}

**__Translated Messages__**
{output}
""", color=discord.Color.from_str(embed_color))
                else:
                    embed = discord.Embed(title="Translated Message", description=f"""
**__Translated Messages__**
{output}
""", color=discord.Color.from_str(embed_color))
                
                if author_display == "username":
                    embed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
                else:
                    if message.author.nick:
                        embed.set_author(name=message.author.nick, icon_url=message.author.display_avatar.url)
                    else:
                        embed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
                
                embed.timestamp = datetime.datetime.now()

                if message.guild.icon:
                    embed.set_footer(icon_url=message.guild.icon.url)
                
                msg = await message.reply(embed=embed, mention_author=False)
                if automatic_delete_translated_message:

                    time_list = re.split('(\d+)', automatic_delete_translated_message_duration)
                    if time_list[2] == "s":
                        time_in_s = int(time_list[1])
                    if time_list[2] == "m":
                        time_in_s = int(time_list[1]) * 60
                    if time_list[2] == "h":
                        time_in_s = int(time_list[1]) * 60 * 60
                    if time_list[2] == "d":
                        time_in_s = int(time_list[1]) * 60 * 60 * 24
                    
                    await asyncio.sleep(time_in_s)
                    await msg.delete()

async def setup(bot):
    await bot.add_cog(MessageEventsCog(bot))