import discord
import yaml
import sys
from discord.ext.commands import CommandNotFound
from discord.ext import commands
from cogs.checks.checks import checks, bcolors

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

embed_color = data["General"]["EMBED_COLOR"]
status = data["General"]["STATUS"].lower()
token = data["General"]["TOKEN"]

if status == "online":
    _status = getattr(discord.Status, status)
elif status == "idle":
    _status = getattr(discord.Status, status)
elif status == "dnd":
    _status = getattr(discord.Status, status)
elif status == "invisible":
    _status = getattr(discord.Status, status)
else:
    sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}STATUS{bcolors.ENDC}
{bcolors.WARNING}This value must be {bcolors.OKGREEN}online{bcolors.WARNING}, {bcolors.OKGREEN}idle{bcolors.WARNING}, {bcolors.OKGREEN}dnd{bcolors.WARNING}, or {bcolors.OKGREEN}invisible{bcolors.WARNING}.{bcolors.ENDC}
""")

intents = discord.Intents.all()
intents.message_content = True

initial_extensions = [
                      'cogs.commands.translator',
                      'cogs.events.messageevents'
                      ]

class TranslatorBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents, status=_status)

    async def on_ready(self):

        print(f'Signed in as {self.user}')
        print('Attempting to sync slash commands...')
        await self.tree.sync()
        print('Synced')

    async def setup_hook(self):
        await checks()

        for extension in initial_extensions:
            await self.load_extension(extension)

client = TranslatorBot()
client.remove_command('help')
client.valid_langs = [
    'af', 'sq', 'am', 'ar', 'hy', 'as', 'ay', 'az', 'bm', 'eu', 'be', 'bn', 'bh', 'bs', 'bg', 'my', 'ca', 'ceb', 'ny', 'zh-CN', 'zh-TW',
    'co', 'hr', 'cs', 'da', 'dv', 'doi', 'nl', 'en', 'eo', 'et', 'ee', 'tl', 'fi', 'fr', 'fy', 'gl', 'ka', 'de', 'el', 'gn', 'gu', 'ht',
    'ha', 'haw', 'he', 'hi', 'hmn', 'hu', 'is', 'ig', 'ilo', 'id', 'ga', 'it', 'ja', 'jv', 'kn', 'ks', 'kk', 'km', 'rw', 'kok', 'ko',
    'kri', 'ku', 'ckb', 'ky', 'lo', 'la', 'lv', 'lv', 'lt', 'lg', 'lb', 'mk', 'mai', 'mg', 'ms', 'ml', 'mt', 'mni', 'mi', 'mr', 'lus',
    'mn', 'ne', 'no', 'or', 'om', 'ps', 'fa', 'pl', 'pt', 'pa', 'ro', 'ru', 'sm', 'sa', 'gd', 'nso', 'sr', 'st', 'sn', 'sd', 'si', 'sk',
    'sl', 'so', 'es', 'su', 'sw', 'sv', 'tg', 'ta', 'tt', 'te', 'th', 'ti', 'ts', 'tr', 'tk', 'tw', 'uk', 'ur', 'ug', 'uz', 'vi', 'cy',
    'yi', 'yo', 'zu', 'afrikaans', 'albanian', 'amharic', 'arabic', 'armenian', 'assamese', 'aymara', 'azerbaijani', 'bambara', 'basque',
    'belarusian', 'bengali', 'bhojpuri', 'bosnian', 'bulgarian', 'burmese', 'aatalan', 'cebuano', 'chichewa', 'chinese', 'corsican',
    'croatian', 'czech', 'danish', 'dhivehi', 'dogri', 'dutch', 'english', 'esperanto', 'estonian', 'ewe', 'filipino', 'finnish', 'french',
    'frisian', 'galician', 'georgian', 'german', 'greek', 'guaraní', 'gujarati', 'haitian creole', 'hausa', 'hawaiian', 'hebrew', 'hindi',
    'hmong', 'hungarian', 'icelandic', 'igbo', 'ilokano', 'indonesian', 'irish', 'italian', 'japanese', 'javanese', 'kannada', 'kashmiri',
    'kazakh', 'khmer', 'kinyarwanda', 'konkani', 'korean', 'krio', 'kurdish', 'kyrgyz', 'lao', 'latin', 'latvian', 'lingala', 'lithuanian',
    'luganda', 'luxembourgish', 'macedonian', 'maithili', 'malagasy', 'malay', 'malayalam', 'maltese', 'manipuri', 'maori', 'marathi',
    'mizo', 'mongolian', 'nepali', 'norwegian', 'odia', 'oromo', 'pashto', 'persian', 'polish', 'portuguese', 'punjabi', 'romanian',
    'russian', 'samoan', 'sanskrit', 'scottish gaelic', 'sepedi', 'serbian', 'sesotho', 'shona', 'sindhi', 'sinhala', 'slovak', 'slovenian',
    'somali', 'spanish', 'sundanese', 'swahili', 'swedish', 'tajik', 'tamil', 'tatar', 'telugu', 'thai', 'tigrinya', 'tsonga', 'turkish',
    'turkmen', 'twi', 'ukrainian', 'urdu', 'uyghur', 'zzbek', 'vietnamese', 'welsh', 'yiddish', 'yoruba', 'zulu'
]

client.language_flags = {
    "af": ":flag_za:",  # Afrikaans
    "sq": ":flag_al:",  # Albanian
    "am": ":flag_et:",  # Amharic
    "ar": ":flag_sa:",  # Arabic
    "hy": ":flag_am:",  # Armenian
    "as": ":flag_in:",  # Assamese
    "ay": ":flag_bo:",  # Aymara
    "az": ":flag_az:",  # Azerbaijani
    "bm": ":flag_ml:",  # Bambara
    "eu": ":flag_es:",  # Basque
    "be": ":flag_by:",  # Belarusian
    "bn": ":flag_bd:",  # Bengali
    "bh": ":flag_in:",  # Bhojpuri
    "bs": ":flag_ba:",  # Bosnian
    "bg": ":flag_bg:",  # Bulgarian
    "my": ":flag_mm:",  # Burmese
    "ca": ":flag_es:",  # Catalan
    "ceb": ":flag_ph:",  # Cebuano
    "ny": ":flag_mw:",  # Chichewa
    "zh-CN": ":flag_cn:",  # Chinese (Simplified)
    "zh-TW": ":flag_tw:",  # Chinese (Traditional)
    "co": ":flag_fr:",  # Corsican
    "hr": ":flag_hr:",  # Croatian
    "cs": ":flag_cz:",  # Czech
    "da": ":flag_dk:",  # Danish
    "dv": ":flag_mv:",  # Dhivehi
    "doi": ":flag_in:",  # Dogri
    "nl": ":flag_nl:",  # Dutch
    "en": ":flag_gb:",  # English
    "eo": ":flag_pl:",  # Esperanto
    "et": ":flag_ee:",  # Estonian
    "ee": ":flag_gh:",  # Ewe
    "tl": ":flag_ph:",  # Filipino
    "fi": ":flag_fi:",  # Finnish
    "fr": ":flag_fr:",  # French
    "fy": ":flag_nl:",  # Frisian
    "gl": ":flag_es:",  # Galician
    "ka": ":flag_ge:",  # Georgian
    "de": ":flag_de:",  # German
    "el": ":flag_gr:",  # Greek
    "gn": ":flag_py:",  # Guaraní
    "gu": ":flag_in:",  # Gujarati
    "ht": ":flag_ht:",  # Haitian Creole
    "ha": ":flag_ng:",  # Hausa
    "haw": ":flag_us:",  # Hawaiian
    "he": ":flag_il:",  # Hebrew
    "hi": ":flag_in:",  # Hindi
    "hmn": ":flag_cn:",  # Hmong
    "hu": ":flag_hu:",  # Hungarian
    "is": ":flag_is:",  # Icelandic
    "ig": ":flag_ng:",  # Igbo
    "ilo": ":flag_ph:",  # Ilokano
    "id": ":flag_id:",  # Indonesian
    "ga": ":flag_ie:",  # Irish
    "it": ":flag_it:",  # Italian
    "ja": ":flag_jp:",  # Japanese
    "jv": ":flag_id:",  # Javanese
    "kn": ":flag_in:",  # Kannada
    "ks": ":flag_in:",  # Kashmiri
    "kk": ":flag_kz:",  # Kazakh
    "km": ":flag_kh:",  # Khmer
    "rw": ":flag_rw:",  # Kinyarwanda
    "kok": ":flag_in:",  # Konkani
    "ko": ":flag_kr:",  # Korean
    "kri": ":flag_sl:",  # Krio
    "ku": ":flag_ir:",  # Kurdish (Kurmanji)
    "ckb": ":flag_ir:",  # Kurdish (Sorani)
    "ky": ":flag_kg:",  # Kyrgyz
    "lo": ":flag_la:",  # Lao
    "la": ":flag_va:",  # Latin
    "lv": ":flag_lv:",  # Latvian
    "ln": ":flag_cd:",  # Lingala
    "lt": ":flag_lt:",  # Lithuanian
    "lg": ":flag_ug:",  # Luganda
    "lb": ":flag_lu:",  # Luxembourgish
    "mk": ":flag_mk:",  # Macedonian
    "mai": ":flag_in:",  # Maithili
    "mg": ":flag_mg:",  # Malagasy
    "ms": ":flag_my:",  # Malay
    "ml": ":flag_in:",  # Malayalam
    "mt": ":flag_mt:",  # Maltese
    "mni": ":flag_in:",  # Manipuri
    "mi": ":flag_nz:",  # Maori
    "mr": ":flag_in:",  # Marathi
    "lus": ":flag_in:",  # Mizo
    "mn": ":flag_mn:",  # Mongolian
    "ne": ":flag_np:",  # Nepali
    "no": ":flag_no:",  # Norwegian
    "or": ":flag_in:",  # Odia (Oriya)
    "om": ":flag_et:",  # Oromo
    "ps": ":flag_af:",  # Pashto
    "fa": ":flag_ir:",  # Persian
    "pl": ":flag_pl:",  # Polish
    "pt": ":flag_pt:",  # Portuguese
    "pa": ":flag_in:",  # Punjabi
    "ro": ":flag_ro:",  # Romanian
    "ru": ":flag_ru:",  # Russian
    "sm": ":flag_ws:",  # Samoan
    "sa": ":flag_in:",  # Sanskrit
    "gd": ":flag_gb:",  # Scottish Gaelic
    "nso": ":flag_za:",  # Sepedi
    "sr": ":flag_rs:",  # Serbian
    "st": ":flag_ls:",  # Sesotho
    "sn": ":flag_zw:",  # Shona
    "sd": ":flag_pk:",  # Sindhi
    "si": ":flag_lk:",  # Sinhala
    "sk": ":flag_sk:",  # Slovak
    "sl": ":flag_si:",  # Slovenian
    "so": ":flag_so:",  # Somali
    "es": ":flag_es:",  # Spanish
    "su": ":flag_id:",  # Sundanese
    "sw": ":flag_ug:",  # Swahili
    "sv": ":flag_se:",  # Swedish
    "tg": ":flag_tj:",  # Tajik
    "ta": ":flag_in:",  # Tamil
    "tt": ":flag_ru:",  # Tatar
    "te": ":flag_in:",  # Telugu
    "th": ":flag_th:",  # Thai
    "ti": ":flag_er:",  # Tigrinya
    "ts": ":flag_za:",  # Tsonga
    "tr": ":flag_tr:",  # Turkish
    "tk": ":flag_tm:",  # Turkmen
    "tw": ":flag_gh:",  # Twi
    "uk": ":flag_ua:",  # Ukrainian
    "ur": ":flag_pk:",  # Urdu
    "ug": ":flag_cn:",  # Uyghur
    "uz": ":flag_uz:",  # Uzbek
    "vi": ":flag_vn:",  # Vietnamese
    "cy": ":flag_gb:",  # Welsh
    "yi": ":flag_il:",  # Yiddish
    "yo": ":flag_ng:",  # Yoruba
    "zu": ":flag_za:",  # Zulu

    "afrikaans": ":flag_za:",  # af
    "albanian": ":flag_al:",  # sq
    "amharic": ":flag_et:",  # am
    "arabic": ":flag_sa:",  # ar
    "armenian": ":flag_am:",  # hy
    "assamese": ":flag_in:",  # as
    "aymara": ":flag_bo:",  # ay
    "azerbaijani": ":flag_az:",  # az
    "bambara": ":flag_ml:",  # bm
    "basque": ":flag_es:",  # eu
    "belarusian": ":flag_by:",  # be
    "bengali": ":flag_bd:",  # bn
    "bhojpuri": ":flag_in:",  # bh
    "bosnian": ":flag_ba:",  # bs
    "bulgarian": ":flag_bg:",  # bg
    "burmese": ":flag_mm:",  # my
    "aatalan": ":flag_es:",  # ca
    "cebuano": ":flag_ph:",  # ceb
    "chichewa": ":flag_mw:",  # ny
    "chinese": ":flag_cn:",  # zh-CN
    "corsican": ":flag_fr:",  # co
    "croatian": ":flag_hr:",  # hr
    "czech": ":flag_cz:",  # cs
    "danish": ":flag_dk:",  # da
    "dhivehi": ":flag_mv:",  # dv
    "dogri": ":flag_in:",  # doi
    "dutch": ":flag_nl:",  # nl
    "english": ":flag_gb:",  # en
    "esperanto": ":flag_pl:",  # eo
    "estonian": ":flag_ee:",  # et
    "ewe": ":flag_gh:",  # ee
    "filipino": ":flag_ph:",  # tl
    "finnish": ":flag_fi:",  # fi
    "french": ":flag_fr:",  # fr
    "frisian": ":flag_nl:",  # fy
    "galician": ":flag_es:",  # gl
    "georgian": ":flag_ge:",  # ka
    "german": ":flag_de:",  # de
    "greek": ":flag_gr:",  # el
    "guaraní": ":flag_py:",  # gn
    "gujarati": ":flag_in:",  # gu
    "haitian creole": ":flag_ht:",  # ht
    "hausa": ":flag_ng:",  # ha
    "hawaiian": ":flag_us:",  # haw
    "hebrew": ":flag_il:",  # he
    "hindi": ":flag_in:",  # hi
    "hmong": ":flag_cn:",  # hmn
    "hungarian": ":flag_hu:",  # hu
    "icelandic": ":flag_is:",  # is
    "igbo": ":flag_ng:",  # ig
    "ilokano": ":flag_ph:",  # ilo
    "indonesian": ":flag_id:",  # id
    "irish": ":flag_ie:",  # ga
    "italian": ":flag_it:",  # it
    "japanese": ":flag_jp:",  # ja
    "javanese": ":flag_id:",  # jv
    "kannada": ":flag_in:",  # kn
    "kashmiri": ":flag_in:",  # ks
    "kazakh": ":flag_kz:",  # kk
    "khmer": ":flag_kh:",  # km
    "kinyarwanda": ":flag_rw:",  # rw
    "konkani": ":flag_in:",  # kok
    "korean": ":flag_kr:",  # ko
    "krio": ":flag_sl:",  # kri
    "kurdish": ":flag_ir:",  # ku
    "kyrgyz": ":flag_kg:",  # ky
    "lao": ":flag_la:",  # lo
    "latin": ":flag_va:",  # la
    "latvian": ":flag_lv:",  # lv
    "lingala": ":flag_cd:",  # ln
    "lithuanian": ":flag_lt:",  # lt
    "luganda": ":flag_ug:",  # lg
    "luxembourgish": ":flag_lu:",  # lb
    "macedonian": ":flag_mk:",  # mk
    "maithili": ":flag_in:",  # mai
    "malagasy": ":flag_mg:",  # mg
    "malay": ":flag_my:",  # ms
    "malayalam": ":flag_in:",  # ml
    "maltese": ":flag_mt:",  # mt
    "manipuri": ":flag_in:",  # mni
    "maori": ":flag_nz:",  # mi
    "marathi": ":flag_in:",  # mr
    "mizo": ":flag_in:",  # lus
    "mongolian": ":flag_mn:",  # mn
    "nepali": ":flag_np:",  # ne
    "norwegian": ":flag_no:",  # no
    "odia": ":flag_in:",  # or
    "oromo": ":flag_et:",  # om
    "pashto": ":flag_af:",  # ps
    "persian": ":flag_ir:",  # fa
    "polish": ":flag_pl:",  # pl
    "portuguese": ":flag_pt:",  # pt
    "punjabi": ":flag_in:",  # pa
    "romanian": ":flag_ro:",  # ro
    "russian": ":flag_ru:",  # ru
    "samoan": ":flag_ws:",  # sm
    "sanskrit": ":flag_in:",  # sa
    "scottish gaelic": ":flag_gb:",  # gd
    "sepedi": ":flag_za:",  # nso
    "serbian": ":flag_rs:",  # sr
    "sesotho": ":flag_ls:",  # st
    "shona": ":flag_zw:",  # sn
    "sindhi": ":flag_pk:",  # sd
    "sinhala": ":flag_lk:",  # si
    "slovak": ":flag_sk:",  # sk
    "slovenian": ":flag_si:",  # sl
    "somali": ":flag_so:",  # so
    "spanish": ":flag_es:",  # es
    "sundanese": ":flag_id:",  # su
    "swahili": ":flag_ug:",  # sw
    "swedish": ":flag_se:",  # sv
    "tajik": ":flag_tj:",  # tg
    "tamil": ":flag_in:",  # ta
    "tatar": ":flag_ru:",  # tt
    "telugu": ":flag_in:",  # te
    "thai": ":flag_th:",  # th
    "tigrinya": ":flag_er:",  # ti
    "tsonga": ":flag_za:",  # ts
    "turkish": ":flag_tr:",  # tr
    "turkmen": ":flag_tm:",  # tk
    "twi": ":flag_gh:",  # tw
    "ukrainian": ":flag_ua:",  # uk
    "urdu": ":flag_pk:",  # ur
    "uyghur": ":flag_cn:",  # ug
    "zzbek": ":flag_uz:",  # uz
    "vietnamese": ":flag_vn:",  # vi
    "welsh": ":flag_gb:",  # cy
    "yiddish": ":flag_il:",  # yi
    "yoruba": ":flag_ng:",  # yo
    "zulu": ":flag_za:",  # zu
}

#\\\\\\\\\\\\Error Handler////////////
@client.event
async def on_command_error(ctx: commands.Context, error):
    if isinstance(error, CommandNotFound):
        return
    raise error

try:
    client.run(token)
except:
    sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}TOKEN{bcolors.ENDC}
{bcolors.WARNING}Please assure that you generated a new token and set it up with correct permissions and intents.{bcolors.ENDC}
""")