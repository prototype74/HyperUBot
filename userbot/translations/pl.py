# Polish Language file
#
# Copyright 2020-2023 nunopenim @github
# Copyright 2020-2023 prototype74 @github
# Copyright 2020-2023 pawix25 @github

#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

NAME = "Polski"


class AdminText(object):
    ADMINS_IN_CHAT = "Administratorzy w **{}**"
    UNABLE_GET_ADMINS = "`Nie można pobrać administratorów z tej rozmowy`"
    FAIL_CHAT = "`Nie udało się pobrać rozmowy`"
    NO_GROUP_CHAN = "`Ta rozmowa nie jest grupą ani kanałem`"
    NO_GROUP_CHAN_ARGS = "`Ta rozmowa lub podana rozmowa nie jest grupą ani kanałem`"
    NO_ADMIN = "`Do wykonania tej akcji wymagane są uprawnienia administratora`"
    NO_BAN_PRIV = "`Do wykonania tej akcji wymagane są uprawnienia do banowania`"
    DELETED_ACCOUNT = "Konto usunięte"
    CANNOT_BAN_LINKED = "`Nie mogę zbanować tego kanału, ponieważ jest powiązany z '{}'`"
    CANNOT_BAN_CHANNEL_SELF = "`Nie mogę zbanować własnego kanału`"
    CANNOT_BAN_CHANNEL_ITSELF = "`Nie mogę zbanować kanału w jego własnym kanale!?`"
    CANNOT_BAN_SELF = "`Nie mogę zbanować samego siebie`"
    CANNOT_BAN_ADMIN = "`Nie mogę zbanować tego administratora`"
    BAN_SUCCESS_REMOTE = "{} został zbanowany z **{}**"
    BAN_SUCCESS = "{} został zbanowany!"  # user name
    BAN_FAILED = "`Nie udało się zbanować tej osoby`"
    CANNOT_UNBAN_CHANNEL_ITSELF = ("`Nie mogę odbanować kanału we własnym "
                                   "kanale!?`")
    CANNOT_UNBAN_SELF = "`Nie mogę odbanować samego siebie`"
    UNBAN_SUCCESS_REMOTE = "{} został odbanowany z **{}**"
    UNBAN_SUCCESS = "{} został odbanowany!"  # user name
    UNBAN_FAILED = "`Nie udało się odbanować tej osoby`"
    UNKNOWN_THING = "`Nie wiem, co to za 'rzecz'`"
    KICK_PERSONS_ONLY = "`Mogę wyrzucić tylko boty i osoby`"
    CANNOT_KICK_SELF = "`Nie mogę wyrzucić samego siebie`"
    KICK_SUCCESS_REMOTE = "{} został wyrzucony z **{}**"
    KICK_SUCCESS = "{} został wyrzucony!"  # user name
    KICK_FAILED = "`Nie udało się wyrzucić tej osoby`"
    PERSON_ANONYMOUS = "Osoba jest anonimowa"
    CANNOT_PROMOTE_CHANNEL = "Nie mogę awansować kanału!"
    NO_ONE_TO_PROMOTE = "`Nie ma nikogo do awansowania`"
    NOT_USER = "`Podana nazwa użytkownika lub ID nie jest użytkownikiem`"
    CANNOT_PROMOTE_SELF = "`Nie mogę awansować samego siebie`"
    ADMIN_ALREADY = "`Ta osoba jest już nieśmiertelna`"
    ADMIN_NOT_ENOUGH_PERMS = ("`Nie mam wystarczających praw administratora, aby "
                              "awansować tę osobę`")
    ADD_ADMINS_REQUIRED = ("`Do wykonania tej akcji wymagane są uprawnienia do "
                           "dodawania administratorów`")
    PROMOTE_SUCCESS = "{} został awansowany z nieśmiertelną mocą!"  # user name
    TOO_MANY_ADMINS = "`Ta rozmowa ma już zbyt wielu administratorów`"
    EMOJI_NOT_ALLOWED = "`Emotikony nie są dozwolone w tytułach administratora`"
    GET_ENTITY_FAILED = "Nie udało się pobrać jednostki"
    PROMOTE_FAILED = "`Nie udało się awansować tej osoby`"
    CANNOT_DEMOTE_CHANNEL = "Nie mogę degradować kanału!"
    NO_ONE_TO_DEMOTE = "`Nie ma nikogo do degradacji`"
    CANNOT_DEMOTE_SELF = "`Nie mogę degradować samego siebie`"
    DEMOTED_ALREADY = "`Ta osoba jest już śmiertelna`"
    DEMOTE_SUCCESS = "{} został zdegradowany!"  # user name
    CANNOT_DEMOTE_ADMIN = "`Nie mogę degradować tego administratora`"
    DEMOTE_FAILED = "`Nie udało się zdegradować tej osoby`"
    NO_GROUP_ARGS = "`Ta rozmowa lub podana rozmowa nie jest grupą`"
    MUTE_PERSONS_ONLY = "`Mogę wyciszyć tylko boty i osoby`"
    NOT_MUTE_SUB_CHAN = "`Nie można wyciszyć subskrybentów w kanale`"
    CANNOT_MUTE_SELF = "`Nie mogę wyciszyć samego siebie`"
    MUTE_SUCCESS_REMOTE = "{} został wyciszony w **{}**"  # user name, chat tile
    MUTE_SUCCESS = "{} jest wyciszony"  # user name
    MUTE_FAILED = "`Nie udało się wyciszyć tej osoby`"
    UNMUTE_PERSONS_ONLY = "`Mogę odciszyć tylko boty i osoby`"
    NOT_UNMUTE_SUB_CHAN = "`Nie można odciszyć subskrybentów w kanale`"
    CANNOT_UNMUTE_SELF = "`Nie mogę odciszyć samego siebie`"
    UNMUTE_SUCCESS_REMOTE = "{} został odciszony w **{}**"
    UNMUTE_SUCCESS = "{} jest odciszony"  # user name
    UNMUTE_FAILED = "`Nie udało się odciszyć tej osoby`"
    INVALID_ID = "`Podane ID jest nieprawidłowe`"
    INVALID_USERNAME = "`Podana nazwa użytkownika lub link jest nieprawidłowy`"
    TRY_DEL_ACCOUNTS = "`Próba usunięcia kont usuniętych...`"
    DEL_ACCS_COUNT = "`Znaleziono {} usuniętych kont w tej rozmowie`"
    DEL_ACCS_COUNT_REMOTE = "`Znaleziono {} usuniętych kont w {}`"
    REM_DEL_ACCS_COUNT = "`Usunięto {} usuniętych kont`"
    REM_DEL_ACCS_COUNT_REMOTE = "`Usunięto {} usuniętych kont w {}`"
    REM_DEL_ACCS_COUNT_EXCP = "`Nie udało się usunąć {} usuniętych (admin) kont`"
    NO_DEL_ACCOUNTS = "`Nie znaleziono usuniętych kont w tej rozmowie`"
    NO_DEL_ACCOUNTS_REMOTE = "`Nie znaleziono usuniętych kont w {}`"

class SystemToolsText(object):
    UBOT = "Projekt Użytkownika: "
    SYSTEM_STATUS = "Stan Systemu"
    VER_TEXT = "Wersja: "
    USR_TEXT = "Użytkownik: "
    SAFEMODE = "Tryb bezpieczny: "
    ON = "Włączony"
    OFF = "Wyłączony"
    LANG = "Język: "
    RTT = "RTT: "
    TELETON_VER = "Wersja Telethona: "
    PYTHON_VER = "Wersja Pythona: "
    GITAPI_VER = "Wersja API GitHub: "
    COMMIT_NUM = "Wersja: "
    ERROR = "BŁĄD!"
    DAYS = "dni"
    BOT_UPTIMETXT = "Czas działania bota: "
    MAC_UPTIMETXT = "Czas działania serwera: "
    SHUTDOWN = "`Wyłączanie...`"
    SHUTDOWN_LOG = "Bot jest wyłączany na żądanie użytkownika!"
    SYSD_GATHER_INFO = "`Zbieranie informacji o systemie...`"
    SYSD_NEOFETCH_REQ = ("`Wymagany jest pakiet neofetch, aby wyświetlić "
                         "informacje o systemie`")
    RESTART = "`Ponowne uruchamianie...`"
    RESTART_UNSUPPORTED = ("`Ponowne uruchamianie nie jest obsługiwane w systemie Windows, "
                           "ale uwaga! Ctrl+C i tak działa`")
    RESTART_LOG = "Użytkownik ponownie uruchomił bota!"
    RESTARTED = "Ponowne uruchomienie zakończone!"
    GENERAL = "Ogólne"
    STORAGE = "Przechowywanie"
    STORAGE_TOTAL = "Całkowite"
    STORAGE_USED = "Używane"
    STORAGE_FREE = "Wolne"
    USED_BY_HYPERUBOT = "Używane przez HyperUBot"
    STORAGE_SYSTEM = "Moduły wbudowane"
    STORAGE_USER = "Moduły użytkownika"
    STORAGE_USERDATA = "Dane użytkownika"
    STORAGE_TEMP_DL = "Tymczasowe pobrania"
    STORAGE_HDD = "Dysk twardy"
    UPLD_LOG = "`Przesyłanie dziennika użytkownika...`"
    SUCCESS_UPLD_LOG = "`Dziennik HyperUBot został pomyślnie przesłany!`"
    FAILED_UPLD_LOG = "`Nie udało się przesłać pliku dziennika`"

class DeletionsText(object):
    CANNOT_DEL_MSG = "`Nie mogę usunąć tej wiadomości`"
    DEL_MSG_FAILED = "`Nie udało się usunąć tej wiadomości`"
    REPLY_DEL_MSG = "`Odpowiedz na wiadomość, aby ją usunąć`"
    NO_ADMIN_PURGE = "`Do wykonania akcji usuwania wiadomości potrzebne są uprawnienia administratora`"
    NO_DEL_PRIV = "`Do wykonania akcji usuwania wiadomości potrzebne są uprawnienia do usuwania`"
    PURGE_MSG_FAILED = "`Nie udało się usunąć wiadomości(e)`"
    PURGE_COMPLETE = "Usuwanie zakończone! Usunięto `{}` wiadomości(e)!"
    LOG_PURGE = "Usunięto `{}` wiadomości(e)"
    REPLY_PURGE_MSG = "`Odpowiedz na wiadomość, aby rozpocząć usuwanie`"


class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analizowanie czatu...`"
    EXCEPTION = "`Wystąpił nieoczekiwany błąd!`"
    REPLY_NOT_CHANNEL = "`Ta wiadomość nie pochodzi z kanału`"
    CANNOT_GET_CHATINFO = "`Nie mogę uzyskać informacji o czacie z '{}'!`"
    YES_BOLD = "<b>Tak</b>"
    NO_BOLD = "<b>Nie</b>"
    YES = "Tak"
    NO = "Nie"
    DELETED_ACCOUNT = "Konto Usunięte"
    CHATINFO = "<b>Informacje o czacie</b>\n\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHANNEL = "Kanał"
    GROUP = "Grupa"
    CHAT_TYPE = "Rodzaj czatu: {} ({})\n"  # group/channel, private/public
    CHAT_NAME = "Nazwa czatu: {}\n"
    FORMER_NAME = "Poprzednia nazwa: {}\n"
    CHAT_PUBLIC = "Publiczny"
    CHAT_PRIVATE = "Prywatny"
    GROUP_TYPE = "Rodzaj grupy"
    GROUP_TYPE_GIGAGROUP = "Grupa nadawcza"
    GROUP_TYPE_SUPERGROUP = "Supergrupa"
    GROUP_TYPE_NORMAL = "Normalna"
    OWNER = "Właściciel: {}\n"
    OWNER_WITH_URL = "Właściciel: <a href=\"tg://user?id={}\">{}</a>\n"
    CREATED_NOT_NULL = "Utworzono: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Utworzono: <code>{} - {} {}</code> {}\n"
    DCID = "ID centrum danych: {}\n"
    VIEWABLE_MSG = "Wiadomości widoczne: <code>{}</code>\n"
    DELETED_MSG = "Usunięte wiadomości: <code>{}</code>\n"
    SENT_MSG = "Wysłane wiadomości: <code>{}</code>\n"
    SENT_MSG_PRED = "Wysłane wiadomości: <code>{}</code> {}\n"
    MEMBERS = "Użytkownicy: <code>{}</code>\n"
    ADMINS = "Administratorzy: <code>{}</code>\n"
    BOT_COUNT = "Boty: <code>{}</code>\n"
    ONLINE_MEM = "Obecnie online: <code>{}</code>\n"
    RESTRICTED_COUNT = "Użytkownicy z ograniczeniami: <code>{}</code>\n"
    BANNEDCOUNT = "Zbanowani użytkownicy: <code>{}</code>\n"
    GRUP_STICKERS = "Naklejki czatu: <a href=\"t.me/addstickers/{}\">{}</a>\n"
    LINKED_CHAT = "Połączony czat: {}\n"
    LINKED_CHAT_TITLE = "> Nazwa: {}\n"
    SLW_MODE = "Tryb spowolniony: {}"
    SLW_MODE_TIME = ", <code>{}s</code>\n\n"
    RESTR = "Ograniczenia: {}\n"
    PFORM = "> Platforma: {}\n"
    REASON = "> Powód: {}\n"
    TEXT = "> Tekst: {}\n\n"
    SCAM = "Oszustwo: <b>Tak</b>\n\n"
    VERFIED = "Zweryfikowane przez Telegram: {}\n\n"
    DESCRIPTION = "Opis: \n<code>{}</code>\n"
    UNKNOWN = "Nieznane"
    INVALID_CH_GRP = "Nieprawidłowy kanał/grupa!"
    PRV_BAN = "To jest kanał/grupa prywatna lub jestem tam zbanowany!"
    NOT_EXISTS = "Kanał lub supergrupa nie istnieje!"
    CID_TEXT = "ID tego czatu to `{}`"
    CID_NO_GROUP = "`Ten czat nie jest kanałem ani grupą`"
    LINK_INVALID_ID = "`Podane ID lub link jest nieprawidłowe`"
    LINK_INVALID_ID_GROUP = "`Podane ID lub link nie pochodzi z kanału ani grupy`"
    LINK_TEXT = "Oto link do zaproszenia dla **{}**"
    NO_LINK = "`Ten czat nie ma linku zaproszenia`"
    NO_ADMIN_PERM = "`Do wykonania tej akcji wymagane są uprawnienia administratora`"
    NO_INVITE_PERM = ("`Wymagane są uprawnienia do zapraszania użytkowników do wykonania "
                      "tej akcji`")
    UNABLE_GET_LINK = "`Nie można pobrać linku zaproszenia do czatu`"


class MemberInfoText(object):
    SCAN = "`Skanowanie informacji o tym użytkowniku...`"
    FAIL_GET_MEMBER_CHAT = "`Nie udało się uzyskać informacji o użytkowniku: nie można pobrać czatu`"
    PERSONS_ONLY = "`To nie jest bot ani osoba`"
    FAIL_GET_MEMBER = "`Nie udało się uzyskać informacji o użytkowniku`"
    NOT_SUPERGROUP = "`Ten czat lub podane ID czatu nie jest supergrupą!`"
    INVALID_CHAT_ID = "`Nieprawidłowe ID czatu!`"
    ME_NOT_PART = "`Nie jestem uczestnikiem {}`"
    USER_NOT_PART = "`Ten użytkownik nie jest uczestnikiem {}`"
    FAIL_GET_PART = "`Nie udało się uzyskać informacji o uczestniku`"
    DELETED_ACCOUNT = "Konto Usunięte"
    TIME_FOREVER = "Na zawsze"
    ME_NOT_MEMBER = "`Nie jestem członkiem {}`"
    USER_NOT_MEMBER = "`Ten użytkownik nie jest członkiem {}`"
    MEMBERINFO = "Informacje o użytkowniku"
    GENERAL = "Ogólne"
    MINFO_ID = "ID"
    FIRST_NAME = "Imię"
    USERNAME = "Nazwa użytkownika"
    GROUP = "Grupa"
    GROUP_NAME = "Nazwa"
    STATUS = "Status"
    STATUS_OWNER = "Właściciel"
    STATUS_ADMIN = "Administrator"
    STATUS_MEMBER = "Członek"
    STATUS_BANNED = "Zbanowany"
    STATUS_MUTED = "Wyciszony"
    STATUS_RESTRICTED = "Ograniczony"
    STATUS_MUTED_NOT_MEMBER = "Nie jest członkiem, ale wyciszony"
    STATUS_RESTRICTED_NOT_MEMBER = "Nie jest członkiem, ale ograniczony"
    STATUS_BANNED_UNTIL = "Zbanowany do"
    STATUS_MUTED_UNTIL = "Wyciszony do"
    STATUS_RESTRICTED_UNTIL = "Ograniczony do"
    STATUS_BANNED_BY = "Zbanowany przez"
    STATUS_MUTED_BY = "Wyciszony przez"
    STATUS_RESTRICTED_BY = "Ograniczony przez"
    ADMIN_TITLE = "Tytuł"
    PERMISSIONS = "Uprawnienia"
    CHANGE_GROUP_INFO = "Zmiana informacji o grupie"
    DELETE_MESSAGES = "Usuwanie wiadomości"
    BAN_USERS = "Banowanie użytkowników"
    INVITE_USERS = "Dodawanie/Zapraszanie użytkowników"
    PIN_MESSAGES = "Przypinanie wiadomości"
    ADD_ADMINS = "Dodawanie nowych administratorów"
    MANAGE_CALLS = "Zarządzanie rozmowami głosowymi"
    ANONYMOUS = "Wysyłanie anonimowo"
    ROOT_RIGHTS = "Prawa roota"
    SEND_MESSAGES = "Wysyłanie wiadomości"
    SEND_MEDIA = "Wysyłanie mediów"
    SEND_GIFS_STICKERS = "Wysyłanie naklejek i gifów"
    SEND_POLLS = "Wysyłanie ankiet"
    EMBED_LINKS = "Osadzanie linków"
    WARN_ADMIN_PRIV = ("Uprawnienia administratora są wymagane do uzyskania dostępu do niestandardowych "
                       "uprawnień")
    PROMOTED_BY = "Awansowany przez"
    ADDED_BY = "Dodany przez"
    JOIN_DATE = "Data dołączenia"


class MessagesText(object):
    NO_ADMIN = "`Wymagane są uprawnienia administratora do wykonania tej akcji`"
    CHANNEL_PERSONS_ONLY = ("`Mogę liczyć wiadomości tylko od botów, kanałów "
                            "i użytkowników`")
    FAIL_CHAT = "`Nie udało się pobrać czatu`"
    CANNOT_COUNT_DEL = "`Nie można liczyć wiadomości od usuniętego użytkownika`"
    CANNOT_QUERY_FWD = "`Nie można zapytać o przekazywane wiadomości z kanału`"
    FAIL_COUNT_MSG = "`Nie można zapytać o przekazywane wiadomości z kanału`"
    USER_HAS_SENT = "{} wysłał(a) `{}` wiadomości w tym czacie"
    CANNOT_COUNT_MSG = "`Nie można liczyć wiadomości w tym czacie!`"
    PIN_REPLY_TO_MSG = "`Odpowiedz na wiadomość, aby ją przypiąć`"
    PIN_SUCCESS = "`Wiadomość pomyślnie przypięta`"
    PIN_FAILED = "`Nie udało się przypiąć tej wiadomości`"
    LOG_PIN_MSG_ID = "ID wiadomości"
    UNPIN_REPLY_TO_MSG = ("`Odpowiedz na wiadomość, aby ją odpiąć, lub użyj "
                          "\".unpin all\" aby odpiąć wszystkie wiadomości`")
    UNPIN_ALL_SUCCESS = "`Wszystkie wiadomości pomyślnie odpięte`"
    UNPIN_SUCCESS = "`Wiadomość pomyślnie odpięta`"
    UNPIN_FAILED = "`Nie udało się odpiąć tej wiadomości`"
    LOG_UNPIN_ALL_TEXT = "Wszystkie wiadomości odpięte"


class ScrappersText(object):
    NO_TEXT_OR_MSG = "`Brak tekstu lub wiadomości do przetłumaczenia`"
    TRANSLATING = "`Tłumaczenie...`"
    SAME_SRC_TARGET_LANG = "`Język tekstu źródłowego jest taki sam jak język docelowy`"
    DETECTED_LANG = "Wykryty język"
    TARGET_LANG = "Język docelowy"
    ORG_TEXT = "Oryginalny tekst"
    TRANS_TEXT = "Przetłumaczony tekst"
    MSG_TOO_LONG = "`Przetłumaczony tekst jest zbyt długi!`"
    FAIL_TRANS_MSG = "`Nie udało się przetłumaczyć tej wiadomości`"
    FAIL_TRANS_TEXT = "`Nie udało się przetłumaczyć podanego tekstu`"
    MEDIA_FORBIDDEN = ("`Nie można odtworzyć TTS: Przesyłanie mediów nie jest dozwolone na tym "
                       "czacie`")
    NO_TEXT_TTS = "`Brak tekstu lub wiadomości do przekształcenia na mowę`"
    FAIL_TTS = "`Nie udało się przekształcić na mowę`"
    FAIL_API_REQ = "`Nieudane żądanie API`"
    INVALID_LANG_CODE = "`Nieprawidłowy kod języka lub język nie jest obsługiwany`"
    NOT_EGH_ARGS = "`Zbyt mało argumentów podanych!`"
    INVALID_AMOUNT_FORMAT = "`Nieprawidłowy format ilości`"
    CC_ISO_UNSUPPORTED = "`'{}' nieobsługiwana waluta krajowa ISO`"
    CC_HEADER = "Konwerter walut"
    CFROM_CTO = "**{}** na **{}**"  # z cc iso, na docelowe cc iso
    INVALID_INPUT = "Nieprawidłowe dane wejściowe"
    UNABLE_TO_CC = "`Nie można przekonwertować waluty`"
    CC_LAST_UPDATE = "Ostatnia aktualizacja"
    REPLY_TO_VM = "`Odpowiedz na wiadomość głosową`"
    WORKS_WITH_VM_ONLY = "`Działa tylko z wiadomościami głosowymi`"
    CONVERT_STT = "`Konwertowanie mowy na tekst...`"
    FAILED_LOAD_AUDIO = "`Nie udało się załadować dźwięku`"
    STT = "Mowa na tekst"
    STT_TEXT = "Tekst"
    STT_NOT_RECOGNIZED = "`Nie można rozpoznać mowy z dźwięku`"
    STT_REQ_FAILED = "`Nieudane żądanie na serwerze`"
    STT_OUTPUT_TOO_LONG = "`Wyjście z konwersji mowy na tekst jest zbyt długie!`"
    UNABLE_TO_STT = "`Nie można przekształcić mowy na tekst`"
    SCRLANG = "Język modułu Scrappers w HyperUBot to obecnie: `{}`"
    MULT_ARGS = "`Proszę użyj jednego argumentu!`"
    INV_CT_CODE = ("Nieprawidłowa wartość! Użyj jednego z poniższych kodów kraju "
                   "składających się z 2 liter!\n\nDostępne kody:\n{}")
    SUCCESS_LANG_CHANGE = "Język został pomyślnie zmieniony na: `{}`"


class UserText(object):
    CANNOT_LEAVE = "`Ten czat nie wydaje się być grupą ani kanałem`"
    LEAVING = "`Opuszczanie czatu...`"
    STATS_PROCESSING = "`Obliczanie statystyk...`"
    STATS_HEADER = "Moje statystyki Telegrama"
    STATS_USERS = "Rozmowy PW z **{}** osobami"
    STATS_BLOCKED = "Zablokowano **{}** z nich"
    STATS_BOTS = "Uruchomiono **{}** botów"
    STATS_BLOCKED_TOTAL = "Zablokowano **{}** botów/osób ogółem"
    STATS_GROUPS = "Uczestnictwo w **{}** grupach"
    STATS_SGC_OWNER = "Posiadanie **{}** z nich"
    STATS_GROUPS_ADMIN = "Admin w **{}** grupach"
    STATS_SUPER_GROUPS = "Uczestnictwo w **{}** supergrupach"
    STATS_SG_ADMIN = "Admin w **{}** supergrupach"
    STATS_CHANNELS = "Subskrybowane **{}** kanały"
    STATS_CHAN_ADMIN = "Admin w **{}** kanałach"
    STATS_UNKNOWN = "**{}** nieznane czaty"
    STATS_TOTAL = "Wszystkie czaty"
    FETCH_INFO = "`Pobieranie informacji o użytkowniku...`"
    INFO_PERSONS_ONLY = ("`To nie jest bot ani osoba. Rozważ użycie .chatinfo, jeśli celem jest kanał lub grupa`")
    FAILED_FETCH_INFO = "`Nie udało się pobrać informacji o użytkowniku`"
    UNKNOWN = "Nieznane"
    DELETED_ACCOUNT = "Konto Usunięte"
    YES = "Tak"
    NO = "Nie"
    USR_NO_BIO = "Ten użytkownik nie ma biogramu"
    USR_INFO = "Informacje o użytkowniku"
    FIRST_NAME = "Imię"
    LAST_NAME = "Nazwisko"
    USERNAME = "Nazwa użytkownika"
    DCID = "ID Centrum Danych"
    PROF_PIC_COUNT = "Liczba Zdjęć Profilowych"
    PROF_LINK = "Stały Link do Profilu"
    ISBOT = "Bot"
    PREMIUM = "Premium"
    SCAMMER = "Oszust"
    ISRESTRICTED = "Ograniczony"
    ISVERIFIED = "Zweryfikowane przez Telegram"
    USR_ID = "ID"
    BIO = "Biogram"
    COMMON_SELF = "Wspólne rozmowy... O, patrz, to ja!"
    COMMON = "Wspólne rozmowy"
    UNABLE_GET_IDS = "`Nie można uzyskać ID użytkownika(y) z tej wiadomości`"
    ORIGINAL_AUTHOR = "Oryginalny autor"
    FORWARDER = "Przekazujący"
    DUAL_HAS_ID_OF = "{} ma ID `{}`"
    MY_ID = "Moje ID to `{}`"
    DEL_HAS_ID_OF = "Konto Usunięte ma ID `{}`"
    ID_NOT_ACCESSIBLE = "ID od {} nie jest dostępne"
    ORG_HAS_ID_OF = "Oryginalny autor {} ma ID `{}`"


class SystemUtilitiesText(object):
    CMD_STOPPED = "{} został zatrzymany!"


class GeneralMessages(object):
    FAIL_FETCH_ENTITY = "`Nie udało się pobrać kanału ani użytkownika`"
    UNSUPPORTED_ENTITY = "`Encja nie jest kanałem ani użytkownikiem`"
    PERSON_ANONYMOUS = "Osoba jest anonimowa"
    CANT_FETCH_REQ = "`Nie można pobrać encji „{}”`"
    LOG_USER = "Użytkownik"
    LOG_USERNAME = "Nazwa użytkownika"
    LOG_USER_ID = "ID użytkownika"
    LOG_CHAT_TITLE = "Tytuł czatu"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "ID czatu"
    UNKNOWN = "Nieznane"


class ModulesUtilsText(object):
    INVALID_ARG = "`Nieprawidłowy argument „{}”`"
    USAGE = "Użycie"
    AVAILABLE_MODULES = "Dostępne moduły"
    DISABLED_MODULES = "Wyłączone moduły"
    NAME_MODULE = "**Moduł {}**"
    MISSING_NUMBER_MODULE = "`Brakujący numer modułu`"
    MODULE_NOT_AVAILABLE = "`Moduł o numerze „{}” niedostępny`"
    MODULE_NO_DESC = "__Brak dostępnych opisów__"
    MODULE_NO_USAGE = "__Brak dostępnych informacji o użyciu__"
    ASTERISK = "Moduł użytkownika do odinstalowania"
    NOT_RUNNING_INFO = "Nie jest uruchomiony"
    UNKNOWN = "Nieznane"
    SYSTEM = "Wbudowany"
    SYSTEM_MODULES = "Moduły wbudowane"
    USER = "Użytkownik"
    USER_MODULES = "Moduły użytkownika"
    PKG_NAME = "Nazwa paczki"
    MODULE_TYPE = "Typ modułu"
    AUTHORS = "Autor(zy)"
    VERSION = "Wersja"
    SIZE = "Rozmiar"
    INSTALL_DATE = "Data instalacji"
    LISTCMDS_TITLE = "Wszystkie dostępne polecenia/funkcje"
    LISTCMDS_USAGE = ("Użyj '{} <nazwa polecenia/funkcji>', aby uzyskać więcej informacji o konkretnej komendzie.")
    LISTCMDS_ORIGIN_FEATURE = "Pochodzenie tej komendy/funkcji"
    ARGS_NOT_REQ = "nie wymaga argumentów"
    ARGS_NOT_AVAILABLE = "brak dostępnych argumentów"
    CMD_NOT_FOUND = "Nie znaleziono polecenia '{}'!"
    MOD_HELP = "Potrzebujesz pomocy? Wpisz {}"
    MOD_UTILS = "Moduły"


class WebToolsText(object):
    PING_SPEED = "Czas podróży w obie strony: "
    DCMESSAGE = ("Kraj: `{}`\n"
                 "To centrum danych: `{}`\n"
                 "Najbliższe centrum danych: `{}`")
    BAD_ARGS = "`Nieprawidłowe argumenty!`"
    INVALID_HOST = "`Wystąpił problem podczas analizy IP/Nazwy hosta`"
    PINGER_VAL = "DNS: `{}`\nPrędkość Ping: `{}`"
    SPD_TEST_SELECT_SERVER = "Wybieranie najlepszego serwera"
    SPD_TEST_DOWNLOAD = "Testowanie prędkości pobierania"
    SPD_TEST_UPLOAD = "Testowanie prędkości wysyłania"
    SPD_PROCESSING = "Przetwarzanie"
    SPD_FAILED = "Test prędkości nie powiódł się"
    SPD_NO_RESULT = "Brak wyników"
    SPD_NO_MEMORY = "Brak pamięci"
    SPD_FAIL_SEND_RESULT = "`Nie udało się wysłać wyniku testu prędkości`"
    SPD_MEGABITS = "Mbit/s"
    SPD_MEGABYTES = "MB/s"
    SPD_TIME = "Czas"
    SPD_DOWNLOAD = "Prędkość pobierania"
    SPD_UPLOAD = "Prędkość wysyłania"
    SPD_PING = "Ping"
    SPD_ISP = "Mój ISP"
    SPD_HOSTED_BY = "Hostowane przez"


class GitHubText(object):
    INVALID_URL = "Nieprawidłowa kombinacja użytkownik/repozytorium"
    NO_RELEASE = "Nie można znaleźć określonego wydania"
    AUTHOR_STR = "<b>Autor:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Nazwa wydania:</b> "
    ASSET = "<b>Zasób:</b> \n"
    SIZE = "Rozmiar: "
    DL_COUNT = "\nLiczba pobrań: "
    INVALID_ARGS = ("Nieprawidłowe argumenty! Upewnij się, że wpisujesz prawidłową "
                    "kombinację użytkownik/repozytorium")
    GITRATE_NO_DATA = "Brak dostępnych danych z GitHub"


class TerminalText(object):
    BASH_ERROR = ("Wystąpił nieokreślony błąd, prawdopodobnie złe "
                  "argumenty lub ta komenda nie istnieje")
    BASH_CRT_FILE_FAILED_RO = ("Nie udało się utworzyć pliku wyjściowego powłoki jako plik. "
                               "System plików tylko do odczytu?")
    BASH_CRT_FILE_FAILED = "Nie udało się utworzyć pliku wyjściowego powłoki jako plik"
    BASH_SEND_FILE_MTLO = ("Nie można wysyłać wyników powłoki jako pliku, ponieważ wysyłanie mediów "
                           "nie jest dozwolone w tej rozmowie")
    BASH_SEND_FILE_FAILED = "Nie można wysłać wyników powłoki jako pliku"


class MiscText(object):
    COIN_LANDED_VAL = "Moneta wylądowała na: "
    THRWING_COIN = "`Rzucanie monetą...`"
    HEADS = "Orzeł"
    TAILS = "Reszka"
    RAND_INVLD_ARGS = ("`Nieprawidłowe argumenty, upewnij się, że masz "
                       "dokładnie 2 liczby`")
    FRST_LIMIT_INVALID = "`Pierwsza wartość nie jest prawidłową liczbą!`"
    SCND_LIMIT_INVALID = "`Druga wartość nie jest prawidłową liczbą!`"
    RAND_NUM_GEN = "Twoja wygenerowana liczba pomiędzy `{}` a `{}`: **`{}`**"


class PackageManagerText(object):
    REPO_LIST_EMPTY = ("Lista repozytoriów jest pusta! Użyj "
                       "`.pkg update <właściciel/repozytorium>` aby dodać nowe repozytorium "
                       "lub dodaj je do konfiguracji COMMUNITY_REPOS")
    PACKAGES_UPDATER = "Aktualizator pakietów"
    INVALID_REPO_URL = "Nieprawidłowy format URL repozytorium"
    UPDATING_REPO_DATA = "Aktualizowanie danych repozytorium..."
    UPDATE_SUCCESS = "Otrzymano najnowsze dane z '{}'"
    UPDATE_FAILED = "Nie udało się pobrać danych '{}'"
    UPDATER_FINISHED = "Zakończono aktualizator"
    LIST_OF_PACKAGES = "Lista pakietów"
    INSTALLED_MODULES = "Zainstalowane moduły"
    NO_MODULES_INSTALLED = "Brak zainstalowanych modułów użytkownika"
    MODULES_IN = "Moduły w {}"
    AUTHOR = "Autor"
    VERSION = "Wersja"
    REPO_NO_MODULES = "To repozytorium nie ma modułów"
    REPOS_NO_DATA = "Brak danych repozytorium. Może musisz użyć {}"
    INSTALLED = "Zainstalowany"
    INSTALLED_NOTLOADED = "Zainstalowany, ale nie załadowany"
    UPGRADEABLE = "Możliwa aktualizacja"
    START_FAILED = "Nie udało się uruchomić"
    DISABLED = "Wyłączony"
    EQUAL_NAME = "Taka sama nazwa"
    NEVER = "Nigdy"
    LAST_UPDATED = "Ostatnio zaktualizowany"
    INSTALL_EMPTY = "Nie podano nazw modułów do zainstalowania"
    PACKAGE_INSTALLER = "Instalator pakietów"
    NO_REPO_URL = "Nie podano URL repozytorium do instalacji!"
    INSTALL_EMPTY_REPO = "Nie podano nazw modułów do instalacji z określonego repozytorium!"
    UNKNOWN_REPO_URL = "Podano nieznany URL repozytorium!"
    UNKNOWN_MODULES = "Nieznane moduły"
    INSTALLING_MODULES = ("Instalowanie modułów. Ten proces może trochę "
                          "potrwać...")
    DOWN_FAILED = "Nie udało się pobrać '{}'"
    INSTALL_FAILED = "Nie udało się zainstalować '{}'"
    INSTALL_SUCCESS = "Zainstalowano '{}'"
    UPDATE_DATA_FAIL = "Nie udało się zaktualizować danych dla '{}'"
    NO_INSTALL_QUEUED = "Brak oczekującej instalacji"
    INSTALLER_FINISHED = "Zakończono instalator"
    UNINSTALL_EMPTY = "Nie podano nazw modułów do odinstalowania"
    PACKAGE_UNINSTALLER = "Odinstalowywacz pakietów"
    UNINSTALLING_MODULES = "Odinstalowywanie modułów..."
    UNINSTALL_FAILED = "Nie udało się odinstalować '{}'"
    UNINSTALL_SUCCESS = "Odinstalowano '{}'"
    UNINSTALL_DATA = "Odinstalowano '{}', ale nie udało się usunąć danych"
    MODULE_NOT_INSTALL = "'{}' nie jest zainstalowany"
    UNINSTALLER_FINISHED = "Zakończono odinstalowywacz"
    NO_REPO_NAMES = "Nie podano nazw repozytoriów do usunięcia"
    NO_REPO_REMOVE = "Brak repozytoriów do usunięcia"
    REPO_REMOVER = "Usuwacz repozytoriów"
    CANNOT_REMOVE_REPO = "Nie można usunąć '{}' (chronione)"
    REMOVING_REPO_DATA = "Usuwanie danych repozytorium..."
    REMOVE_SUCCESS = "'{}' został usunięty"
    REMOVE_FAILED = "Nie udało się usunąć '{}'"
    UNKNOWN_REPO = "Nieznane repozytorium"
    REMOVER_FINISHED = "Zakończono usuwacz"
    LOAD_PGKS = "Ładowanie list pakietów..."
    CANNOT_INSTALL_MODULES = "Nie można instalować modułów użytkownika w trybie awaryjnym"
    PACKAGE_MANAGER = "Menedżer pakietów"
    UNKNOWN_OPTION = "Nieznana opcja '{}'"
    NO_OPTION = "Nie podano opcji"
    PKG_HELP = "Potrzebujesz pomocy? Wpisz {}"
    TEXT_TOO_LONG = ("Lista jest zbyt długa, aby ją tutaj wyświetlić. Lista jest "
                     "drukowana w terminalu twojego bota")


class UpdaterText(object):
    CHECKING_UPDATES = "Sprawdzanie aktualizacji..."
    GIT_REPO = "Katalog HyperUBot to lokalne repozytorium git"
    DOWNLOADING_RELEASE = "Pobieranie najnowszej wersji..."
    UPDATE_FAILED = "Aktualizacja nie powiodła się"
    UPDATE_INTERNAL_FAILED = "Wystąpił wewnętrzny błąd"
    START_RECOVERY_FAILED = "Nie udało się rozpocząć przywracania"
    ALREADY_UP_TO_DATE = "HyperUBot jest już aktualny"
    LATEST = "Najnowsza"
    CURRENT = "Obecna"
    UPDATE_AVAILABLE = "Dostępna aktualizacja"
    RELEASE_DATE = "Data wydania"
    CHANGELOG_AT = "Dziennik zmian dostępny pod adresem {}"
    DOWNLOAD_SUCCESS = ("Pobieranie zakończone powodzeniem. Wyłączam bota, aby zainstalować pakiet aktualizacji...")
    DOWNLOAD_SUCCESS_WIN = ("Pobieranie zakończone powodzeniem. Proszę wyłączyć bota i postępować zgodnie z instrukcjami w terminalu, aby ręcznie zainstalować pakiet aktualizacji.")
    UPDATE_QUEUED = ("Użyj `.update upgrade`, aby teraz pobrać i zainstalować pakiet aktualizacji.")
    UPDATE_SUCESS = "HyperUBot został pomyślnie zaktualizowany do wersji {}!"
    UPDATE_FAIL = "Nie udało się zaktualizować HyperUBot do wersji {}"
    NOTIFIER_HEADER = "Powiadamiacz Aktualizacji HyperUBot"
    NOTIFIER_INFO = "Dostępna jest nowa aktualizacja do {}!"


class SideloaderText(object):
    NOT_PY_FILE = "To nie jest prawidłowy plik .py! Nie można załadować tego modułu!"
    DLOADING = "`Pobieranie...`"
    MODULE_EXISTS = ("Moduł użytkownika o nazwie `{}` już istnieje. "
                     "Jeśli chcesz go nadpisać, uruchom polecenie z argumentem `force`!")
    SUCCESS = "Moduł `{}` został pomyślnie zainstalowany!"
    LOG = "Moduł `{}` został pomyślnie załadowany!"
    REBOOT_INFO = "Proszę teraz zrestartować HyperUBota, aby załadować załadowany moduł"
    INVALID_FILE = "Odpowiedz na prawidłowy plik!"


class FeatureMgrText(object):
    DISABLE_FTR = "Podaj nazwę polecenia lub funkcji, aby ją wyłączyć!"
    DISABLE_FTR_FAIL = "Wystąpił problem z wyłączeniem tego polecenia lub funkcji"
    DISABLE_FTR_SUCCESS = "Polecenie lub funkcja '`{}`' została wyłączona"
    DISABLED_FTRS = "Wyłączone funkcje"
    NO_DISABLED_FTRS = "Brak wyłączonych funkcji"
    ENABLE_FTR = "Podaj nazwę polecenia lub funkcji, aby ją włączyć!"
    ENABLE_FTR_FAIL = "Wystąpił problem z włączeniem tego polecenia lub funkcji"
    ENABLE_FTR_SUCCESS = "Polecenie lub funkcja '`{}`' została włączona"


class WelcomeText(object):
    WELCOME_TO_HYPERUBOT = "Witaj w HyperUBot!"
    INFO = ("Udało ci się uruchomić HyperUBota na swoim urządzeniu. Co dalej? Poniższe polecenia pomogą ci lepiej zrozumieć swojego nowego użytkownika i to, jakie opcje i funkcje oferuje HyperUBot.")
    INFO_STATUS = ("Pobierz bieżący status HyperUBota, takie jak wersja, czas działania itp. Przydatne, aby sprawdzić, czy bot jest rzeczywiście online.")
    INFO_OR = "lub"
    INFO_HELP = ("Wypisz wszystkie dostępne polecenia i funkcje ze wszystkich modułów do użycia. Przekaż nazwę polecenia lub funkcji (np. {}), aby uzyskać informacje o użyciu konkretnego polecenia lub funkcji.")
    INFO_MODULES = ("Wypisz wszystkie moduły wbudowane i użytkownika w jednym miejscu. "
                    "To polecenie przyjmuje argumenty, aby uzyskać dodatkowe informacje o module, takie jak opis lub sposób użycia.")
    INFO_PKG = ("Nasz menedżer pakietów pozwala zainstalować nowe moduły. Stworzyliśmy kilka modułów użytkownika, które można pobrać za pomocą tego polecenia, aby umożliwić użytkownikowi uzyskanie nowych modułów bez oczekiwania na nowe aktualizacje bota. Warto również sprawdzić moduły stworzone przez społeczność!")
    INFO_SUPPORT = ("Masz pytania dotyczące HyperUBota? Przeczytaj nasz {} lub "
                    "śmiało porozmawiaj z nami na naszym {}!")
    INFO_SUPPORT_LINK = "grupie wsparcia"
    INFO_SUPPORT_WIKI = "stronie wiki"
    INFO_FUN = "Baw się dobrze!"


# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = ("Moduł umożliwiający zarządzanie Twoją lub grupą Twojego "
                  "znajomego. Zawiera podstawowe komendy, takie jak ban, unban, "
                  "promote, itp.\n\n"
                  "Uwaga: większość komend w tym module wymaga uprawnień "
                  "administratora, aby działały poprawnie.")
    CHATINFO_DESC = ("Otrzymaj różne informacje z kanału, grupy "
                     "lub supergrupy, takie jak data utworzenia, liczba wiadomości, "
                     "usunięcia, poprzednia nazwa, itp.")
    DELETIONS_DESC = ("Ten moduł pozwala szybciej usuwać wiadomości w Twojej "
                      "grupie lub grupach. Ktoś zaspamował Twoją grupę? Użyj "
                      "komendy purge, aby je wszystkie usunąć!\n"
                      "Wszystkie komendy w tym module wymagają uprawnień "
                      "administratora, aby usunąć wiadomości innych osób.\n\n"
                      "**Ważne: nie nadużywaj tego modułu, aby usunąć "
                      "historię czyjejś innej grupy**, serio, po prostu tego nie rób...")
    MEMBERINFO_DESC = ("Dostarcza informacje o konkretnym uczestniku grupy, "
                       "takie jak uprawnienia, data ograniczenia, data dołączenia, itp.\n\n"
                       "Uwaga: wymaga uprawnień administratora, aby uzyskać dostęp do uprawnień "
                       "innych członków.")
    MESSAGES_DESC = ("Ten moduł zawiera komendy, które działają tylko z "
                     "wiadomościami, takie jak msgs lub pin.")
    SCRAPPERS_DESC = ("Nie do końca to, na co wygląda, ale mimo to ten "
                      "moduł zawiera przydatne funkcje, takie jak tłumaczenie "
                      "lub przekształcanie tekstu na mowę.")
    SYSTOOLS_DESC = ("Ten moduł zawiera zestaw narzędzi systemowych dla "
                     "bota. Umożliwia sprawdzenie czasu działania bota, czasu "
                     "działania serwera, wersji wszystkich komponentów bota, "
                     "specyfikacji systemu serwera oraz pewnych kontroli mocy bota.")
    USER_DESC = ("Dostarcza informacje o dowolnym użytkowniku, Twoje statystyki, "
                 "i zawiera narzędzie kickme.")
    WEBTOOLS_DESC = ("Ten moduł zawiera większość, jeśli nie wszystkie, narzędzia internetowe bota, "
                     "takie jak ping, speedtest, kalkulator RTT i aktualne centrum danych.")
    GITHUB_DESC = ("Moduł wykorzystujący interfejs API GitHub. Ten "
                   "moduł pozwala sprawdzać wydania od określonego użytkownika i repozytorium.")
    TERMINAL_DESC = ("Ten moduł dostarcza narzędzia do bezpośredniego uruchamiania poleceń "
                     "powłoki na maszynie hosta.\n\n"
                     "**Uwaga:** Uruchamianie poleceń powłoki w bocie "
                     "może i spowoduje trwałe zmiany w systemie hosta. **Złe rzeczy się wydarzą, jeśli uruchomisz bota jako sudo/root!**")
    MISC_DESC = ("Moduł różności zawiera mały zestaw narzędzi, "
                 "które nie do końca pasują do żadnego z innych modułów, ale "
                 "jednocześnie były zbyt proste, aby mieć swój własny moduł. Sprawdź pomoc, aby uzyskać więcej informacji.")
    PACKAGE_MANAGER_DESC = ("Moduł menedżera pakietów pozwala użytkownikowi "
                            "zarządzać dodatkowymi aplikacjami z zewnętrznych repozytoriów, "
                            "zarówno oficjalnych, takich jak repozytorium modules-universe, jak i zewnętrznych źródeł. "
                            "Umożliwia użytkownikom dostosowanie swoich botów bardziej niż wersja podstawowa.")
    UPDATER_DESC = ("Moduł aktualizacji umożliwia użytkownikowi sprawdzenie dostępności aktualizacji bota "
                    "i zaktualizowanie bota, jeśli istnieją nowe aktualizacje.")
    SIDELOADER_DESC = ("Moduł bocznego ładowania umożliwia łatwe pobieranie plików Pythona. Aby to zrobić, "
                       "wystarczy odpowiedzieć na przesłany w czacie plik .py jako dokument!\n\n"
                       "**INFORMACJE**: Te pliki muszą być napisane w taki sposób, aby działały z botem. "
                       "Próba załadowania nieznanych plików może skutkować „miękkim brickiem” bota, "
                       "co wymaga ręcznego usunięcia zepsutego modułu przestrzeni użytkownika!\n\n"
                       "**KRYTYCZNE OSTRZEŻENIE**: Niektóre złośliwe pliki mogą "
                       "wysłać niektóre z Twoich informacji (najczęściej klucz API lub / i "
                       "Sesja String) do złośliwego haker! Ładuj moduły boczne tylko wtedy, gdy ufasz źródłu!")
    FEATURE_MGR_DESC = ("Moduł Menedżera Funkcji pozwala użytkownikowi "
                        "włączać/wyłączać komendy lub funkcje w "
                        "czasie rzeczywistym i nie, komendy enable i disable "
                        "nie mogą być wyłączone.")


class ModuleUsages(object):
    # KEEP CORRECT DICT FORMAT!!
    # {"cmd": {"args": ARGUMENTS, "usage": USAGE}} edit ARGUMENTS and
    # USAGE only!
    ADMIN_USAGE = {"adminlist": {"args": "[opcjonalnie: <link/id>]",
                                 "usage": ("wypisuje wszystkich administratorów z "
                                           "kanału lub grupy (zdalnie). "
                                           "Wymaga uprawnień administratora w "
                                           "kanałach.")},
                   "ban": {"args": ("[opcjonalnie: <nazwa użytkownika/id> <czat "
                                    "(id lub link)>] lub odpowiedź"),
                           "usage": ("Zbanuj określonego użytkownika z czatu "
                                     "(zdalnie). Wymaga uprawnień administratora "
                                     "z uprawnieniem do banowania.")},
                   "unban": {"args": ("[opcjonalnie: <nazwa użytkownika/id> <czat "
                                      "(id lub link)>] lub odpowiedź"),
                             "usage": ("Odblokuj określonego użytkownika w czacie "
                                       "(zdalnie). Wymaga uprawnień administratora "
                                       "z uprawnieniem do banowania.")},
                   "kick": {"args": ("[opcjonalnie: <nazwa użytkownika/id> <czat "
                                     "(id lub link)>] lub odpowiedź"),
                            "usage": ("Wyrzuć określonego użytkownika z czatu "
                                      "(zdalnie). Wymaga uprawnień administratora "
                                      "z uprawnieniem do banowania.")},
                   "promote": {"args": ("[opcjonalnie: <nazwa użytkownika/id> i/lub "
                                        "<tytuł>] lub odpowiedź"),
                               "usage": ("Awansuj użytkownika o nieśmiertelnym "
                                         "daniu! Wymaga uprawnień administratora "
                                         "z przynajmniej uprawnieniem do dodawania "
                                         "administratorów oraz drugiego "
                                         "uprawnienia administratora jako awans "
                                         "nigdy nie awansuje użytkownika z "
                                         "uprawnieniem do dodawania "
                                         "administratorów. Długość tytułu "
                                         "musi być <= 16 znaków.")},
                   "demote": {"args": "[opcjonalnie: <nazwa użytkownika/id>] lub odpowiedź",
                              "usage": ("Degraduj użytkownika do zwykłego użytkownika. "
                                        "Wymaga uprawnień administratora z uprawnieniem "
                                        "do dodawania administratorów. Działa tylko z "
                                        "administratorami awansowanymi przez Ciebie.")},
                   "mute": {"args": ("[opcjonalnie: <nazwa użytkownika/id> <czat "
                                     "(id lub link)>] lub odpowiedź"),
                            "usage": ("Wycisz określonego użytkownika w czacie "
                                      "(zdalnie). Wymaga uprawnień administratora "
                                      "z uprawnieniem do banowania.")},
                   "unmute": {"args": ("[opcjonalnie: <nazwa użytkownika/id> <czat "
                                       "(id lub link)>] lub odpowiedź"),
                              "usage": ("Odcisz określonego użytkownika w czacie "
                                        "(zdalnie). Wymaga uprawnień administratora "
                                        "z uprawnieniem do banowania.")},
                   "delaccs": {"args": "[opcjonalnie: <id czatu lub link>]",
                               "usage": ("Próbuje automatycznie usunąć usunięte konta "
                                         "z czatu, jeśli obecne są uprawnienia "
                                         "administratora z uprawnieniem do banowania. "
                                         "W przeciwnym razie raportuje liczbę usuniętych "
                                         "kont w danym czacie.")}}

    CHATINFO_USAGE = {"chatinfo": {"args": ("[opcjonalnie: <id czatu/link>] lub "
                                            "odpowiedź (jeśli kanał)"),
                                   "usage": ("Pobiera informacje o czacie. "
                                             "Niektóre informacje mogą być ograniczone "
                                             "z powodu braku uprawnień.")},
                      "chatid": {"args": None,
                                 "usage": ("Pobiera identyfikator kanału lub "
                                           "grupy.")},
                      "getlink": {"args": "[opcjonalnie: <id czatu/link>]",
                                  "usage": ("Pobiera łącze zaproszenia z kanału lub "
                                            "grupy, aby udostępnić je "
                                            "innym osobom. Wymaga uprawnień administratora "
                                            "z uprawnieniem do zapraszania "
                                            "użytkowników.")}}

    DELETIONS_USAGE = {"del": {"args": None,
                           "usage": "Usuwa odpowiedź na wiadomość."},
                   "purge": {"args": None,
                             "usage": ("Usuwa wszystkie wiadomości między "
                                       "najnowszą a odpowiedzoną wiadomością. "
                                       "Wymagane są uprawnienia administratora "
                                       "z uprawnieniem do usuwania, jeśli "
                                       "opcja purge jest używana na kanałach "
                                       "lub grupach.\n"
                                       "**Uwaga: Proszę nie nadużywać tej "
                                       "funkcji, aby usuwać historie grupowe "
                                       "innych osób!**")}}

    MEMBERINFO_USAGE = {"minfo": {"args": ("[opcjonalnie: <oznaczenie/id> <grupa>] lub "
                                       "odpowiedź"),
                              "usage": ("Pobiera (zdalnie) informacje o członku "
                                        "w supergrupie.")}}

    MESSAGES_USAGE = {"msgs": {"args": ("[opcjonalnie: <nazwa użytkownika/id>] lub odpowiedź"),
                           "usage": ("Pobiera liczbę wysłanych wiadomości "
                                     "przez użytkownika (obejmuje wszelkie "
                                     "wiadomości, takie jak wiadomości tekstowe, "
                                     "notatki dźwiękowe, filmy itp.).")},
                  "pin": {"args": ("[opcjonalny argument \"głośny\" "
                                   "do poinformowania wszystkich członków] lub odpowiedź"),
                          "usage": ("Odpowiedz na wiadomość kogoś, aby ją przypiąć "
                                    "w czacie.")},
                  "unpin": {"args": "[opcjonalny argument \"wszystko\"] lub odpowiedź",
                            "usage": ("Odpowiedz na wiadomość kogoś, aby ją odepnąć, "
                                      "lub wyślij \".unpin all\", aby odpiąć wszystkie wiadomości w czacie.")}}

    SCRAPPERS_USAGE = {"trt": {"args": "[opcjonalnie: <tekst>] lub odpowiedź",
                           "usage": ("Tłumaczy podany tekst lub odpowiedź "
                                     "na wiadomość na język docelowy bota.")},
                   "tts": {"args": "[opcjonalnie: <tekst>] lub odpowiedź",
                           "usage": ("Konwertuje tekst lub odpowiedź na wiadomość "
                                     "na wypowiedź głosową (tekst na mowę).")},
                   "stt": {"args": "tylko odpowiedź",
                           "usage": ("Konwertuje odpowiedź na wiadomość głosową "
                                     "na tekst (mowa na tekst).")},
                   "scrlang": {"args": None,
                               "usage": ("Pokazuje, który język jest obecnie "
                                         "ustawiony do tłumaczenia lub TTS przez bota.")},
                   "setlang": {"args": "[wartość ISO]",
                               "usage": ("Ustawia nowy język z listy wartości ISO.")},
                   "currency": {"args": ("<kwota> <ISO źródłowy> "
                                         "[opcjonalnie: <ISO docelowy>]"),
                                "usage": ("Konwertuje podaną walutę na docelową walutę "
                                          "(domyślnie: USD). Wymaga ISO kraju "
                                          "(EUR, USD, JPY itp.).")}}

    SYSTOOLS_USAGE = {"status": {"args": None,
                             "usage": ("Wpisz .status, aby sprawdzić różne "
                                       "informacje o bocie i czy jest włączony i działa.")},
                  "shutdown": {"args": None,
                               "usage": ("Wpisz .shutdown, aby wyłączyć "
                                         "bota.")},
                  "reboot": {"args": None,
                             "usage": "Ponownie uruchamia bota!"},
                  "storage": {"args": None,
                              "usage": ("Pokazuje informacje o pamięci HDD serwera bota.")},
                  "neofetch": {"args": None,
                               "usage": ("Pokazuje wszystkie istotne informacje systemowe "
                                         "(sprzętowe i oprogramowanie) hosta. Wymaga zainstalowanego pakietu Neofetch.")},
                  "sendlog": {"args": None,
                              "usage": ("Przesyła plik dziennika do bieżącego czatu.")}}

    USER_USAGE = {"info": {"args": "[opcjonalnie: <nazwa użytkownika/id>] lub odpowiedź",
                      "usage": "Pobiera informacje o użytkowniku."},
              "stats": {"args": None,
                        "usage": "Pobiera twoje statystyki."},
              "kickme": {"args": None,
                         "usage": "Pozwala ci opuścić grupę."},
              "id": {"args": "[opcjonalnie: <nazwa użytkownika>] lub odpowiedź",
                     "usage": ("Pobiera ID kanału lub użytkownika. Jeśli "
                               "odpowiesz na przekierowaną wiadomość, "
                               "pobierze ID zarówno od przekierowującego, jak "
                               "i od oryginalnego autora.")}}

    WEBTOOLS_USAGE = {"dc": {"args": None,
                         "usage": ("Znajduje najbliższe centrum danych "
                                   "dla twojego hosta userbota.")},
                  "ping": {"args": "<DNS/IP>",
                           "usage": "Wysyła ping do określonego adresu DNS lub IP."},
                  "rtt": {"args": None,
                          "usage": "Pobiera aktualny czas Round Trip Time (RTT)"},
                  "speedtest": {"args": "[opcjonalny argument \"pic\"]",
                                "usage": ("Przeprowadza test prędkości i "
                                          "wyświetla wynik jako tekst. "
                                          "Przekazanie argumentu \"pic\" "
                                          "zmieni wynik na obrazek.")}}

    GITHUB_USAGE = {"git": {"args": "<użytkownik>/<repozytorium>",
                        "usage": ("Sprawdza wydania dla "
                                  "określonej kombinacji użytkownik/repozytorium.")},
                "gitrate": {"args": None,
                            "usage": ("Pobiera twój aktualny limit wywołań z "
                                      "API GitHub, takiego jak API REST lub "
                                      "API wyszukiwania.\n\n"
                                      "Ponieważ niektóre funkcje bota zależą od "
                                      "usługi API GitHub do pobierania "
                                      "aktualizacji, nowych modułów itp. Te "
                                      "funkcje polegają na wywołaniach do API "
                                      "GitHub przy każdym wywołaniu. Jednak "
                                      "istnieje limit 60 wywołań na godzinę "
                                      "(API REST). Użyj tej komendy, aby "
                                      "sprawdzić, ile wywołań API pozostało.\n\n"
                                      "Informacje o API zostaną wyświetlone "
                                      "w formie:\n__NAZWA_API: POZOSTAŁO/MAX_LIMIT__")}}

    MODULES_UTILS_USAGE = {"lcmds": {"args": ("[opcjonalnie: <nazwa komendy>]"),
                                "usage": ("Wypisuje wszystkie dostępne i "
                                          "zarejestrowane komendy.")},
                      "mods": {"args": ("<-opcja> [numer modułu "
                                        "z listy]"),
                               "usage": ("\n`.mods -d [numer modułu "
                                         "z listy]`\n"
                                         "Wyświetla opis konkretnego modułu. "
                                         "Może zawierać ukryte informacje, kto wie?\n\n"
                                         "`.mods -i [numer modułu "
                                         "z listy]`\n"
                                         "Wyświetla informacje o "
                                         "konkretnym module, takie jak nazwa, "
                                         "autor, wersja itp.\n\n"
                                         "`.mods -u [numer modułu "
                                         "z listy]`\n"
                                         "Ujawnia tajemnice i "
                                         "użycie konkretnego modułu")}}

    TERMINAL_USAGE = {"shell": {"args": "<polecenie>",
                            "usage": ("Wykonuje podane polecenie w wierszu poleceń "
                                      "serwera (bash, powershell lub zsh).\n\n"
                                      "**OSTRZEŻENIE: Jeśli proces userbota "
                                      "działa jako root, może to potencjalnie "
                                      "nieodwracalnie uszkodzić Twój system! "
                                      "Postępuj ostrożnie!**")}}

    MISC_USAGE = {"coinflip": {"args": None,
                           "usage": ("Rzuca monetą i zwraca 'orzeł' "
                                     "lub 'reszkę', w zależności od wyniku.")},
              "dice": {"args": None,
                       "usage": ("Wyśle emoji kostki, "
                                 "Telegram zadba o wartość, "
                                 "całkowicie losowo.")},
              "rand": {"args": "<dolny limit> <górny limit>",
                       "usage": ("Podając górny i dolny limit "
                                 "(obie liczby całkowite), bot "
                                 "wygeneruje losową liczbę w podanym zakresie.")}}

    PACKAGE_MANAGER_USAGE = {"pkg": {"args": ("<opcja> [opcjonalne: "
                                          "<argumenty>]"),
                                 "usage": ("\n`.pkg update "
                                           "[opcjonalne: <lista "
                                           "kombinacji właściciel/nazwa_repozytorium>]`\n"
                                           "Aktualizuje dane wszystkich "
                                           "repozytoriów. Jeśli podane są adresy URL repozytoriów, "
                                           "np. '.pkg update "
                                           "nunopenim/module-universe', "
                                           "to zostaną zaktualizowane tylko "
                                           "określone repozytoria. "
                                           "To polecenie można również "
                                           "użyć do dodawania nowych repozytoriów "
                                           "za pomocą kombinacji <właściciel/nazwa_repozytorium>.\n\n"
                                           "`.pkg list [opcjonalne: "
                                           "<-zainstalowane lub -repozytoria>]`\n"
                                           "Wypisuje wszystkie zainstalowane moduły "
                                           "oraz wszystkie moduły znanego repozytorium. "
                                           "Użyj opcji -zainstalowane, aby pokazać "
                                           "tylko zainstalowane moduły, "
                                           "lub opcji -repozytoria, aby pokazać "
                                           "tylko moduły z repozytoriów.\n\n"
                                           "`.pkg install <lista "
                                           "modułów>`\nlub\n"
                                           "`.pkg install -repo "
                                           "<właściciel/nazwa_repozytorium> <lista "
                                           "modułów>`\n"
                                           "Instaluje listę modułów z podanego argumentu. "
                                           "Jeśli chcesz zainstalować moduły tylko z konkretnego "
                                           "repozytorium, użyj opcji -repozytorium "
                                           "i podaj kombinację właściciel/nazwa_repozytorium "
                                           "wraz z listą modułów jako argumentem.\n\n"
                                           "`.pkg uninstall/remove <lista "
                                           "modułów>`\n"
                                           "Odinstalowuje moduły z podanej listy.\n\n"
                                           "`.pkg rmrepo <lista "
                                           "kombinacji właściciel/nazwa_repozytorium>`\n"
                                           "Usuwa repozytoria z podanej listy kombinacji "
                                           "właściciel/nazwa_repozytorium z danych.")}}

    UPDATER_USAGE = {"update": {"args": "upgrade",
                            "usage": ("Sprawdza dostępność aktualizacji i jeśli są dostępne, "
                                      "wyświetla dziennik zmian.\n"
                                      "Jeśli użytkownik sprawdził aktualizacje, zaktualizuje bota "
                                      "do najnowszej wersji.")}}

    SIDELOADER_USAGE = {"sideload": {"args": "<argument>",
                                 "usage": ("Ładuje do bota skrypt pythona "
                                           "wysłany jako dokument do "
                                           "czatu. Odpowiedz w taki sposób. "
                                           "Możesz użyć argumentu `force` "
                                           "aby wymusić instalację, jeśli moduł "
                                           "o tej samej nazwie już istnieje.\n\n"
                                           "**INFORMACJA**: Te "
                                           "pliki muszą być napisane w taki sposób, "
                                           "aby działały z botem. "
                                           "Próba ładowania nieznanych "
                                           "plików może spowodować "
                                           "'miękkie uszkodzenie' bota, "
                                           "co wymaga ręcznego "
                                           "usunięcia źle napisanego modułu użytkownika!\n\n"
                                           "**POWIĄZANE OSTRZEŻENIE**: Niektóre "
                                           "złośliwe pliki mogą wysyłać "
                                           "część Twoich informacji "
                                           "(w szczególności klucz API i/lub "
                                           "Sesję String) do "
                                           "złośliwego haker! Ładuj moduły "
                                           "tylko wtedy, gdy ufasz źródłu!")}}

    FEATURE_MGR_USAGE = {"disable": {"args": ("<nazwa komendy/aliasu lub "
                                          "funkcji>"),
                                 "usage": ("Wyłącza daną komendę "
                                           "lub funkcję. Działa także z "
                                           "aliasami")},
                     "disabled": {"args": None,
                                  "usage": ("Wypisuje wszystkie wyłączone "
                                            "funkcje")},
                     "enable": {"args": ("<nazwa komendy/aliasu lub "
                                         "funkcji>"),
                                "usage": ("Włącza daną komendę "
                                          "lub funkcję. Działa także z "
                                          "aliasami")}}