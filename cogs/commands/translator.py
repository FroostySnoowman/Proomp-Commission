"""
Responsible for /translate.
"""

import discord
import datetime
import asyncio
import yaml
import re
from discord.ext import commands
from discord import app_commands
from mtranslate import translate

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

embed_color = data["General"]["EMBED_COLOR"]
show_original_message = data["Translator"]["SHOW_ORIGINAL_MESSAGE"]
show_language_type = data["Translator"]["SHOW_LANGUAGE_TYPE"]
show_translated_language = data["Translator"]["SHOW_TRANSLATED_LANGUAGE"] # TO-DO
author_display = data["Translator"]["AUTHOR_DISPLAY"]
automatic_delete_translated_message = data["Translator"]["AUTOMATIC_DELETE_TRANSLATED_MESSAGE"]
automatic_delete_translated_message_duration = data["Translator"]["AUTOMATIC_DELETE_TRANSLATED_MESSAGE_DURATION"]
translate_type = data["Translator"]["TRANSLATE_TYPE"]
works_in_all_categories = data["Translator"]["WORK_IN_ALL_CATEGORIES"]
categories = data["Translator"]["CATEGORIES"]

class TranslatorCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="translate", description="Translates messages!")
    @app_commands.describe(message="What is the original message?")
    @app_commands.describe(languages="What language(s) should the message be translated to?")
    async def translate(self, interaction: discord.Interaction, message: str, languages: str) -> None:
        await interaction.response.defer(thinking=True)

        if translate_type == "command":
            if works_in_all_categories:
                pass
            else:
                if interaction.channel.category.id in categories:
                    pass
                else:
                    embed = discord.Embed(description="This category has been disabled.", color=discord.Color.red())
                    await interaction.followup.send(embed=embed)
                    return
            
            languages_list = [lang.strip().lower() for lang in languages.split(',')]

            langs = []
            for lang in languages_list:
                if lang not in self.bot.valid_langs:
                    pass
                else:
                    langs.append(lang)

            translated_messages = {}

            if show_translated_language:
                for lang in langs:
                    translated = translate(message, lang)
                    if show_language_type == "language-flag":
                        flag = self.bot.language_flags.get(lang, "")
                        output = f"{flag} {translated}"
                    else:
                        output = f"{lang}: {translated}"
                    translated_messages[lang] = output
            
            else:
                for lang in langs:
                    translated = translate(message, lang)
                    output = f"{translated}"
                    translated_messages[lang] = output

            output = "\n\n".join([f"{translated_messages[lang]}" for lang in langs])

            if show_original_message:
                embed = discord.Embed(title="Translated Message", description=f"""
**__Original Message__**
{message}

**__Translated Messages__**
{output}
""", color=discord.Color.from_str(embed_color))
            else:
                embed = discord.Embed(title="Translated Message", description=f"""
**__Translated Messages__**
{output}
""", color=discord.Color.from_str(embed_color))
            
            if author_display == "username":
                embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
            else:
                if interaction.user.nick:
                    embed.set_author(name=interaction.user.nick, icon_url=interaction.user.display_avatar.url)
                else:
                    embed.set_author(name=interaction.user, icon_url=interaction.user.display_avatar.url)
            
            embed.timestamp = datetime.datetime.now()

            if interaction.guild.icon:
                embed.set_footer(icon_url=interaction.guild.icon.url)
            
            await interaction.followup.send(embed=embed)
            if automatic_delete_translated_message:
                msg = await interaction.original_response()

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
        else:
            embed = discord.Embed(description="The **TRANSLATE_TYPE** for this server is configured as `automatic`.", color=discord.Color.red())
            embed.set_footer(text="Deleting in 10 seconds...")

            await interaction.followup.send(embed=embed)

            msg = await interaction.original_response()

            await asyncio.sleep(10)
            await msg.delete()

async def setup(bot):
    await bot.add_cog(TranslatorCog(bot))