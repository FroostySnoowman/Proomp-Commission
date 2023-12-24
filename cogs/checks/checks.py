import yaml
import sys
import re

with open('config.yml', 'r') as file:
    data = yaml.safe_load(file)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

valid_langs = [
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

async def checks():
    try:
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
    except:
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid YAML File{bcolors.ENDC}
{bcolors.WARNING}Please reset the config.yml file.{bcolors.ENDC}
""")
    
    if not type(show_original_message) is bool:
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}SHOW_ORIGINAL_MESSAGE{bcolors.ENDC}
{bcolors.WARNING}This value must be True/False.{bcolors.ENDC}
""")
    
    if show_language_type != "language-flag" and show_language_type != "language-code":
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}SHOW_LANGUAGE_TYPE{bcolors.ENDC}
{bcolors.WARNING}This value must be {bcolors.OKGREEN}language-flag{bcolors.WARNING} or {bcolors.OKGREEN}language-code{bcolors.WARNING}.{bcolors.ENDC}
""")
    
    if not type(show_translated_language) is bool:
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}SHOW_TRANSLATED_LANGUAGE{bcolors.ENDC}
{bcolors.WARNING}This value must be True/False.{bcolors.ENDC}
""")
    
    if author_display != "username" and author_display != "nickname":
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}AUTHOR_DISPLAY{bcolors.ENDC}
{bcolors.WARNING}This value must be {bcolors.OKGREEN}username{bcolors.WARNING} or {bcolors.OKGREEN}nickname{bcolors.WARNING}.{bcolors.ENDC}
""")
    
    if not type(automatic_delete_translated_message) is bool:
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}AUTOMATIC_DELETE_TRANSLATED_MESSAGE{bcolors.ENDC}
{bcolors.WARNING}This value must be True/False.{bcolors.ENDC}
""")
    
    if automatic_delete_translated_message:
        try:
            time_list = re.split('(\d+)', automatic_delete_translated_message_duration)
            if time_list[2] == "s":
                time_in_s = int(time_list[1])
            if time_list[2] == "m":
                time_in_s = int(time_list[1]) * 60
            if time_list[2] == "h":
                time_in_s = int(time_list[1]) * 60 * 60
            if time_list[2] == "d":
                time_in_s = int(time_list[1]) * 60 * 60 * 24
            seconds = time_in_s
        except:
            sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}AUTOMATIC_DELETE_TRANSLATED_MESSAGE_DURATION{bcolors.ENDC}
{bcolors.WARNING}This value must be a valid time. Example: {bcolors.OKGREEN}1d{bcolors.WARNING}, {bcolors.OKGREEN}1h{bcolors.WARNING}, {bcolors.OKGREEN}1m{bcolors.WARNING}, or {bcolors.OKGREEN}1s{bcolors.WARNING}.{bcolors.ENDC}
""")
    
    if translate_type != "command" and translate_type != "automatic":
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}TRANSLATE_TYPE{bcolors.ENDC}
{bcolors.WARNING}This value must be {bcolors.OKGREEN}command{bcolors.WARNING} or {bcolors.OKGREEN}automatic{bcolors.WARNING}.{bcolors.ENDC}
""")
    
    if translate_type == "automatic":
        languages_list = [lang.strip().lower() for lang in translator_languages.split(',')]
        for language in languages_list:
            if language not in valid_langs:
                sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value Language For {bcolors.OKCYAN}TRANSLATOR_LANGUAGES{bcolors.ENDC}
{bcolors.OKBLUE}{language} {bcolors.WARNING}is not a valid language.{bcolors.ENDC}
{bcolors.OKCYAN}{bcolors.BOLD}Valid Languages:{bcolors.ENDC}
{bcolors.OKGREEN}{valid_langs}{bcolors.ENDC}
""")

    if not type(works_in_all_categories) is bool:
        sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value For {bcolors.OKCYAN}WORK_IN_ALL_CATEGORIES{bcolors.ENDC}
{bcolors.WARNING}This value must be True/False.{bcolors.ENDC}
""")
    
    if works_in_all_categories:
        if not all(isinstance(category, int) for category in categories):
            sys.exit(f"""
{bcolors.FAIL}{bcolors.BOLD}ERROR:{bcolors.ENDC}
{bcolors.FAIL}Invalid Value(s) For {bcolors.OKCYAN}CATEGORIES{bcolors.ENDC}
{bcolors.WARNING}These value(s) must be integers (channel ids).{bcolors.ENDC}
""")