# German Language file
#
# Copyright 2021-2023 nunopenim @github
# Copyright 2021-2023 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

NAME = "Deutsch"


class AdminText(object):
    ADMINS_IN_CHAT = "Administratoren in **{}**"
    UNABLE_GET_ADMINS = ("`Admins aus diesem Chat konnten nicht aufgerufen "
                         "werden`")
    FAIL_CHAT = "`Fehler beim aufrufen des Chats`"
    NO_GROUP_CHAN = "`Dieser Chat ist keine Gruppe oder ein Kanal`"
    NO_GROUP_CHAN_ARGS = ("`Dieser oder der gegebene Chat ist keine Gruppe "
                          "oder ein Kanal`")
    NO_ADMIN = "`Adminrechte sind erforderlich, um diese Aktion auszuführen`"
    NO_BAN_PRIV = ("`Die Ban-Berechtigung ist erforderlich, um diese Aktion "
                   "auszuführen`")
    DELETED_ACCOUNT = "Gelöschtes Konto"
    CANNOT_BAN_LINKED = ("`Ich kann diesen Kanal nicht bannen, da es mit '{}' "
                         "verlinkt ist`")
    CANNOT_BAN_CHANNEL_SELF = "`Ich kann meinen eigenen Kanal nicht bannen`"
    CANNOT_BAN_CHANNEL_ITSELF = ("`Ich kann einen Kanal in seinem eigenen "
                                 "Kanal nicht bannen!?`")
    CANNOT_BAN_SELF = "`Ich kann mich selbst nicht bannen`"
    CANNOT_BAN_ADMIN = "`Ich kann diesen Admin nicht bannen`"
    BAN_SUCCESS_REMOTE = "{} wurde aus **{}** gebannt"
    BAN_SUCCESS = "{} wurde gebannt!"
    BAN_FAILED = "`Diese Person konnte nicht gebannt werden`"
    CANNOT_UNBAN_CHANNEL_ITSELF = ("`Ich kann einen Kanal in seinem eigenen "
                                   "Kanal nicht entbannen!?`")
    CANNOT_UNBAN_SELF = "`Ich kann mich selbst nicht entbannen`"
    UNBAN_SUCCESS_REMOTE = "{} wurde aus **{}** entbannt"
    UNBAN_SUCCESS = "{} wurde entbannt!"
    UNBAN_FAILED = "`Diese Person konnte nicht entbannt werden`"
    UNKNOWN_THING = "`Ich weiß nicht, was für ein 'ding' das ist!`"
    KICK_PERSONS_ONLY = "`Ich kann nur Bots und Personen kicken`"
    CANNOT_KICK_SELF = "`Ich kann mich selbst nicht kicken`"
    KICK_SUCCESS_REMOTE = "{} wurde aus **{}** gekickt"
    KICK_SUCCESS = "{} wurde gekickt!"
    KICK_FAILED = "`Diese Person konnte nicht gekickt werden``"
    PERSON_ANONYMOUS = "Person ist anonym"
    CANNOT_PROMOTE_CHANNEL = "Ich kann kein Kanal befördern!"
    NO_ONE_TO_PROMOTE = "`Es gibt niemanden zum befördern`"
    NOT_USER = ("`Der angegebene Benutzername oder die angegebene ID ist "
                "kein User`")
    CANNOT_PROMOTE_SELF = "`Ich kann mich selbst nicht befördern`"
    ADMIN_ALREADY = "`Diese Person ist bereits unsterblich`"
    ADMIN_NOT_ENOUGH_PERMS = ("`Ich hab nicht genung an "
                              "Administratoren-Rechte, um diese Person "
                              "zu befördern`")
    ADD_ADMINS_REQUIRED = ("`Die Berechtigung, um neue Admins hinzuzufügen, "
                           "ist erforderlich, um diese Aktion auzuführen`")
    PROMOTE_SUCCESS = "{} wurde mit unsterblicher Macht befördert!"
    TOO_MANY_ADMINS = "`Dieser Chat hat bereits zu viele Admins`"
    EMOJI_NOT_ALLOWED = "`Emoji sind in Admin-Bezeichnungen nicht erlaubt`"
    GET_ENTITY_FAILED = "Fehler beim aufrufen des Entitäts"
    PROMOTE_FAILED = "`Diese Person konnte nicht befördert werden`"
    CANNOT_DEMOTE_CHANNEL = "Ich kann kein Kanal degradieren!"
    NO_ONE_TO_DEMOTE = "`Es gibt niemanden zum degradieren`"
    CANNOT_DEMOTE_SELF = "`Ich kann mich selbst nicht degradieren`"
    DEMOTED_ALREADY = "`Diese Person ist bereits sterblich`"
    DEMOTE_SUCCESS = "{} wurde degradiert!"
    CANNOT_DEMOTE_ADMIN = "`Ich kann diesen Admin nicht degradieren`"
    DEMOTE_FAILED = "`Diese Person konnte nicht degradieren werden`"
    NO_GROUP_ARGS = "`Dieser oder der gegebene Chat ist keine Gruppe`"
    MUTE_PERSONS_ONLY = "`Ich kann nur Bots und Personen stummgeschalten`"
    NOT_MUTE_SUB_CHAN = ("`Abonnenten aus diesem Kanal können nicht "
                         "stummgeschaltet werden`")
    CANNOT_MUTE_SELF = "`Ich kann mich selbst nicht stummschalten`"
    MUTE_SUCCESS_REMOTE = "{} wurde in **{}** stummgeschaltet"
    MUTE_SUCCESS = "{} wurde stummgeschaltet"
    MUTE_FAILED = "`Diese Person konnte nicht stummgeschaltet werden`"
    UNMUTE_PERSONS_ONLY = ("`Ich kann die Stummschaltung nur von Bots und "
                           "Personen aufheben`")
    NOT_UNMUTE_SUB_CHAN = ("`Stummschaltung von Abonnenten aus diesem "
                           "Kanal können nicht aufgehoben werden`")
    CANNOT_UNMUTE_SELF = ("`Ich kann meine eigene Stummschaltung nicht "
                          "aufheben`")
    UNMUTE_SUCCESS_REMOTE = ("Die Stummschaltung von {} wurde in **{}** "
                             "aufgehoben")
    UNMUTE_SUCCESS = "Die Stummschaltung von {} wurde aufgehoben"
    UNMUTE_FAILED = ("`Die Stummschaltung dieses Persones konnte nicht "
                     "aufgehoben werden`")
    INVALID_ID = "`Angegebene ID ist ungültig`"
    INVALID_USERNAME = "`Angegebene Benutzername oder Link ist ungültig`"
    TRY_DEL_ACCOUNTS = "`Versuche gelöschte Konten zu entfernen...`"
    DEL_ACCS_COUNT = "`{} gelöschte(s) Konto/Konten in diesem Chat gefunden`"
    DEL_ACCS_COUNT_REMOTE = "`{} gelöschte(s) Konto/Konten in {} gefunden`"
    REM_DEL_ACCS_COUNT = "`{} gelöschte(s) Konto/Konten wurden entfernt`"
    REM_DEL_ACCS_COUNT_REMOTE = ("`{} gelöschte(s) Konto/Konten wurde(n) "
                                 "aus {} entfernt`")
    REM_DEL_ACCS_COUNT_EXCP = ("`{} gelöschte(s) (Admin-)Konto/Konten "
                               "konnte(n) nicht entfernt werden`")
    NO_DEL_ACCOUNTS = "`Keine gelöschte Konten in diesem Chat gefunden`"
    NO_DEL_ACCOUNTS_REMOTE = "`Keine gelöschte Konten in {} gefunden`"


class SystemToolsText(object):
    UBOT = "Userbot-Projekt: "
    SYSTEM_STATUS = "Systemstatus"
    VER_TEXT = "Version: "
    USR_TEXT = "User: "
    SAFEMODE = "Abgesicherter Modus: "
    ON = "Ein"
    OFF = "Aus"
    LANG = "Sprache: "
    RTT = "RTT: "
    TELETON_VER = "Telethon-Version: "
    PYTHON_VER = "Python-Version: "
    GITAPI_VER = "GitHub API-Version: "
    COMMIT_NUM = "Revision: "
    ERROR = "FEHLER!"
    DAYS = "Tag(e)"
    BOT_UPTIMETXT = "Bot-Laufzeit: "
    MAC_UPTIMETXT = "Server-Laufzeit: "
    SHUTDOWN = "`Wird heruntergefahren...`"
    SHUTDOWN_LOG = "Bot wird auf Useranfrage heruntergefahren!"
    SYSD_GATHER_INFO = "`Hole Systeminformationen...`"
    SYSD_NEOFETCH_REQ = ("`Das Paket neofetch ist erforderlich, um "
                         "Systeminformation anzuzeigen`")
    RESTART = "`Wird neugestartet...`"
    RESTART_UNSUPPORTED = ("`Reboot wird auf Windows nicht unterstüzt aber "
                           "Kopf hoch! Strg+C funktioniert weiterhin noch`")
    RESTART_LOG = "Userbot wird neugestartet!"
    RESTARTED = "Neustart abgeschlossen!"
    GENERAL = "Allgemein"
    STORAGE = "Speicher"
    STORAGE_TOTAL = "Gesamt"
    STORAGE_USED = "Belegt"
    STORAGE_FREE = "Frei"
    USED_BY_HYPERUBOT = "Von HyperUBot belegt"
    STORAGE_SYSTEM = "Vorinstallierte Module"
    STORAGE_USER = "User-Module"
    STORAGE_USERDATA = "Benutzerdaten"
    STORAGE_TEMP_DL = "Temporäre Downloads"
    STORAGE_HDD = "HDD"
    UPLD_LOG = "`Das Userbot-Log wird hochgeladen...`"
    SUCCESS_UPLD_LOG = "`Das HyperUBot-Log wurde erfolgreich hochgeladen!`"
    FAILED_UPLD_LOG = "`Fehler beim hochladen der Log-Datei`"


class DeletionsText(object):
    CANNOT_DEL_MSG = "`Ich kann diese Nachricht nicht löschen`"
    DEL_MSG_FAILED = "`Fehler beim löschen dieser Nachricht`"
    REPLY_DEL_MSG = "`Antworte auf jemand's Nachricht, um diese zu löschen`"
    NO_ADMIN_PURGE = ("`Adminrechte sind erforderlich, um Nachrichten "
                      "zu purgen`")
    NO_DEL_PRIV = ("`Die Berechtigung Nachrichten löschen ist erforderlich, "
                   "um Nachrichten zu purgen`")
    PURGE_MSG_FAILED = "`Fehler beim purgen der Nachricht(en)`"
    PURGE_COMPLETE = ("Purge abgeschlossen! `{}` Nachricht(en) wurde(n) "
                      "gepurgt!")
    LOG_PURGE = "`{}` Nachricht(en) wurde(n) gepurgt"
    REPLY_PURGE_MSG = ("`Antworte auf jemand's Nachricht, um mit dem "
                       "purgen zu beginnen`")


class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analysiere den Chat...`"
    EXCEPTION = "`Ein unerwarteter Fehler ist aufgetreten!`"
    REPLY_NOT_CHANNEL = "`Diese Nachricht ist von keinem Kanal`"
    CANNOT_GET_CHATINFO = ("`Ich kann von '{}' keine Chatinformationen "
                           "erhalten!`")
    YES_BOLD = "<b>Ja</b>"
    NO_BOLD = "<b>Nein</b>"
    YES = "Ja"
    NO = "Nein"
    DELETED_ACCOUNT = "Gelöschtes Konto"
    CHATINFO = "<b>Chat-Info</b>\n\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHANNEL = "Kanal"
    GROUP = "Gruppe"
    CHAT_TYPE = "Chat-Typ: {} ({})\n"
    CHAT_NAME = "Name des Chats: {}\n"
    FORMER_NAME = "Ehemaliger Name: {}\n"
    CHAT_PUBLIC = "Öffentlich"
    CHAT_PRIVATE = "Privat"
    GROUP_TYPE = "Gruppen-Typ"
    GROUP_TYPE_GIGAGROUP = "Broadcast-Gruppe"
    GROUP_TYPE_SUPERGROUP = "Supergruppe"
    GROUP_TYPE_NORMAL = "Normal"
    OWNER = "Besitzer: {}\n"
    OWNER_WITH_URL = "Besitzer: <a href=\"tg://user?id={}\">{}</a>\n"
    CREATED_NOT_NULL = "Erstellt am: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Erstellt am: <code>{} - {} {}</code> {}\n"
    DCID = "Rechenzentrums-ID: {}\n"
    VIEWABLE_MSG = "Sichtbare Nachrichten: <code>{}</code>\n"
    DELETED_MSG = "Gelöschte Nachrichten: <code>{}</code>\n"
    SENT_MSG = "Verschickte Nachrichten: <code>{}</code>\n"
    SENT_MSG_PRED = "Verschickte Nachrichten: <code>{}</code> {}\n"
    MEMBERS = "Mitglieder: <code>{}</code>\n"
    ADMINS = "Administratoren: <code>{}</code>\n"
    BOT_COUNT = "Bots: <code>{}</code>\n"
    ONLINE_MEM = "Derzeit Online: <code>{}</code>\n"
    RESTRICTED_COUNT = "Beschränkte User: <code>{}</code>\n"
    BANNEDCOUNT = "Getbannte User: <code>{}</code>\n"
    GRUP_STICKERS = "Chat Sticker: <a href=\"t.me/addstickers/{}\">{}</a>\n"
    LINKED_CHAT = "Verlinkter Chat: {}\n"
    LINKED_CHAT_TITLE = "> Name: {}\n"
    SLW_MODE = "Langsamer Modus: {}"
    SLW_MODE_TIME = ", <code>{}s</code>\n\n"
    RESTR = "Eingeschränkt: {}\n"
    PFORM = "> Plattform: {}\n"
    REASON = "> Grund: {}\n"
    TEXT = "> Text: {}\n\n"
    SCAM = "Betrug: <b>Yes</b>\n\n"
    VERFIED = "Von Telegram verifiziert: {}\n\n"
    DESCRIPTION = "Beschreibung: \n<code>{}</code>\n"
    UNKNOWN = "Unbekannt"
    INVALID_CH_GRP = "Ungültige(r) Gruppe/Kanal!"
    PRV_BAN = ("Dies ist ein(e) private(r) Gruppe/Kanal oder ich bin von "
               "dort gebannt!")
    NOT_EXISTS = "Kanal oder Supergruppe existiert nicht!"
    CID_TEXT = "Die ID dieses Chats ist `{}`"
    CID_NO_GROUP = "`Dieser Chat ist keine Gruppe oder ein Kanal`"
    LINK_INVALID_ID = "`Die angegebene ID oder Link ist ungültig`"
    LINK_INVALID_ID_GROUP = ("`Die angegebene ID oder Link ist nicht von "
                             "einer Gruppe oder einem Kanal`")
    LINK_TEXT = "Hier ist der Einladungslink für **{}**"
    NO_LINK = "`Dieser Chat hat kein Einladungslink`"
    NO_ADMIN_PERM = ("`Adminrechte sind erforderlich, um diese Aktion "
                     "auszuführen`")
    NO_INVITE_PERM = ("`Die Berechtigung Nutzer per Link einzuladen ist "
                      "erforderlich, um diese Aktion auszuführen`")
    UNABLE_GET_LINK = ("`Der Einladungslink des Chats kann nicht abgerufen "
                       "werden`")


class MemberInfoText(object):
    SCAN = "`Scanne die Informationen dieses Mitglieds`"
    FAIL_GET_MEMBER_CHAT = ("`Fehler beim aufrufen der Mitglieds-Info: "
                            "Konnte nicht den Chat aufrufen`")
    PERSONS_ONLY = ("`Hierbei handelt es sich nicht um einen Bot oder einer "
                    "Person`")
    FAIL_GET_MEMBER = "`Fehler beim aufrufen der Mitglieds-Info`"
    NOT_SUPERGROUP = "`Dieser oder der gegebene Chat ist keine Supergruppe!`"
    INVALID_CHAT_ID = "`Ungültiges Chat ID!`"
    ME_NOT_PART = "`Ich bin kein Teilnehmer von {}`"
    USER_NOT_PART = "`Dieser User ist kein Teilnehmer von {}`"
    FAIL_GET_PART = "`Fehler beim aufrufen der Teilnehmer-Info`"
    DELETED_ACCOUNT = "Gelöschtes Konto"
    TIME_FOREVER = "Dauerhaft"
    ME_NOT_MEMBER = "`Ich bin kein Mitglied von {}`"
    USER_NOT_MEMBER = "`Dieser User ist kein Mitglied von {}`"
    MEMBERINFO = "Mitglieds-Info"
    GENERAL = "Allgemein"
    MINFO_ID = "ID"
    FIRST_NAME = "Vorname"
    USERNAME = "Nachname"
    GROUP = "Gruppe"
    GROUP_NAME = "Titel"
    STATUS = "Status"
    STATUS_OWNER = "Besitzer"
    STATUS_ADMIN = "Admin"
    STATUS_MEMBER = "Mitglied"
    STATUS_BANNED = "Gebannt"
    STATUS_MUTED = "Gemutet"
    STATUS_RESTRICTED = "Eingeschränkt"
    STATUS_MUTED_NOT_MEMBER = "Kein Mitglied aber gemutet"
    STATUS_RESTRICTED_NOT_MEMBER = "Kein Mitglied aber eingeschränkt"
    STATUS_BANNED_UNTIL = "Gebannt bis"
    STATUS_MUTED_UNTIL = "Gemutet bis"
    STATUS_RESTRICTED_UNTIL = "Eingeschränkt bis"
    STATUS_BANNED_BY = "Gebannt von"
    STATUS_MUTED_BY = "Gemutet von"
    STATUS_RESTRICTED_BY = "Eingeschränkt von"
    ADMIN_TITLE = "Bezeichnung"
    PERMISSIONS = "Berechtigungen"
    CHANGE_GROUP_INFO = "Gruppen/Chat-Info ändern"
    DELETE_MESSAGES = "Nachrichten löschen"
    BAN_USERS = "Nutzer sperren"
    INVITE_USERS = "Nutzer einladen/hinzufügen"
    PIN_MESSAGES = "Nachrichten anheften"
    ADD_ADMINS = "Neue Admins hinzufügen"
    MANAGE_CALLS = "Sprachchats verwalten"
    ANONYMOUS = "Anonym bleiben"
    ROOT_RIGHTS = "Root-Rechte"
    SEND_MESSAGES = "Nachrichten senden"
    SEND_MEDIA = "Medien senden"
    SEND_GIFS_STICKERS = "Sticker & GIFs senden"
    SEND_POLLS = "Umfragen senden"
    EMBED_LINKS = "Linkvorschau senden"
    WARN_ADMIN_PRIV = ("Adminrechte sind erforderlich, um auf "
                       "nicht-standardmäßige Berechtigungen zuzugreifen")
    PROMOTED_BY = "Befördet von"
    ADDED_BY = "Hinzugefügt von"
    JOIN_DATE = "Beitrittsdatum"


class MessagesText(object):
    NO_ADMIN = "`Adminrechte sind erforderlich, um diese Aktion auszuführen`"
    CHANNEL_PERSONS_ONLY = ("`Ich kann die Nachrichten nur von Bots, Kanälen "
                            "und Usern zählen`")
    FAIL_CHAT = "`Fehler beim aufrufen des Chats`"
    CANNOT_COUNT_DEL = ("`Kann nicht die Nachrichten von gelöschte Konten "
                        "zählen`")
    CANNOT_QUERY_FWD = ("`Kann nicht weitergeleitete Nachrichten von "
                        "Kanälen abfragen!`")
    FAIL_COUNT_MSG = "`Fehler beim zählen der Nachrichten`"
    USER_HAS_SENT = "{} hat `{}` Nachrichten in diesem Chat geschickt"
    CANNOT_COUNT_MSG = "`Kann nicht Nachrichten in diesem Chat zählen!`"
    PIN_REPLY_TO_MSG = "`Antworte auf eine Nachricht, um sie anzuheften`"
    PIN_SUCCESS = "`Nachricht erfolgreich angeheftet`"
    PIN_FAILED = "`Fehler beim anheften der Nachricht`"
    LOG_PIN_MSG_ID = "Nachrichten-ID"
    UNPIN_REPLY_TO_MSG = ("`Antworte auf eine Nachricht, um sie loszulösen "
                          "oder nutze \".unpin all\", um alle angeheftete "
                          "Nachrichten loszulösen`")
    UNPIN_ALL_SUCCESS = ("`Alle angeheftete Nachrichten wurden erfolgreich "
                         "losgelöst`")
    UNPIN_SUCCESS = "`Nachricht erfolgreich losgelöst`"
    UNPIN_FAILED = "`Fehler beim loslösen der Nachricht`"
    LOG_UNPIN_ALL_TEXT = "Alle angeheftete Nachrichten wurden losgelöst"


class ScrappersText(object):
    NO_TEXT_OR_MSG = "`Kein Text oder Nachricht zum übersetzen`"
    TRANSLATING = "`Übersetze...`"
    SAME_SRC_TARGET_LANG = ("`Die Aussgangsprache entspricht bereits der "
                            "Zielsprache`")
    DETECTED_LANG = "Erkannte Sprache"
    TARGET_LANG = "Zielsprache"
    ORG_TEXT = "Original Text"
    TRANS_TEXT = "Übersetzer Text"
    MSG_TOO_LONG = "`Der übersetze Text ist zu groß!`"
    FAIL_TRANS_MSG = "`Fehler beim übersetzen der Nachricht`"
    FAIL_TRANS_TEXT = "`Fehler beim übersetzen des gegebenen Textes`"
    MEDIA_FORBIDDEN = ("`TTS fehlgeschlagen: Medien hochladen ist in "
                       "diesem Chat nicht erlaubt`")
    NO_TEXT_TTS = "`Keine Text oder Nachricht zum text-to-speech`"
    FAIL_TTS = "`Text-to-speech fehlgeschlagen`"
    FAIL_API_REQ = "`API-Anfrage fehlgeschlagen`"
    INVALID_LANG_CODE = ("`Sprachecode ungültig oder die Sprache wird "
                         "nicht unterstützt`")
    NOT_EGH_ARGS = "`Nicht genügend Argumente wurden gegeben!`"
    INVALID_AMOUNT_FORMAT = "`Ungültiges Betragsformat`"
    CC_ISO_UNSUPPORTED = "`'{}' ist ein nicht-unterstützes Länder-ISO-Währung`"
    CC_HEADER = "Währungsrechner"
    CFROM_CTO = "**{}** zu **{}**"
    INVALID_INPUT = "Ungültie Eingabe"
    UNABLE_TO_CC = "`Fehler beim konventieren der Währung`"
    CC_LAST_UPDATE = "Zuletzt aktualisiert"
    REPLY_TO_VM = "`Antworte auf eine Sprachnachricht`"
    WORKS_WITH_VM_ONLY = "`Funktioniert nur bei Sprachnachrichten`"
    CONVERT_STT = "`Konvertiere das Gesprochene in Text um...`"
    FAILED_LOAD_AUDIO = "`Fehler beim laden des Audios`"
    STT = "Speech-to-Text"
    STT_TEXT = "Text"
    STT_NOT_RECOGNIZED = "`Das Gesprochene aus dem Audio wurde nicht erkannt`"
    STT_REQ_FAILED = "`Die Ergebnis-Anfrage vom Server ist fehlgeschalgen`"
    STT_OUTPUT_TOO_LONG = "`Speech-to-text-Ausgabe ist zu groß!`"
    UNABLE_TO_STT = "`Fehler beim Speech-to-Text`"
    SCRLANG = "HyperUBot Scrappers-Modul-Sprache ist derzeit auf `{}` gesetzt"
    MULT_ARGS = "`Bitte nutze einen Argument!`"
    INV_CT_CODE = ("Ungültiger Wert! Nutz einer der 2-Buchstaben-"
                   "Ländercodes!\n\nVerfügbare Codes:\n{}")
    SUCCESS_LANG_CHANGE = "Die Sprache wurde erfolgreich auf `{}` geändert"


class UserText(object):
    CANNOT_LEAVE = "`Dieser Chat scheint kein Kanal oder eine Gruppe zu sein`"
    LEAVING = "`Verlasse den Chat...`"
    STATS_PROCESSING = "`Berechne die Statistiken...`"
    STATS_HEADER = "Meine Telegram-Statistiken"
    STATS_USERS = "PM-Konversationen mit **{}** Personen"
    STATS_BOTS = "**{}** Bots gestartet"
    STATS_BLOCKED_TOTAL = "**{}** Bots/Personen insgesamt blockiert"
    STATS_GROUPS = "Teilnehmer in **{}** Gruppen"
    STATS_SGC_OWNER = "Besitze **{}** von Ihnen"
    STATS_GROUPS_ADMIN = "Admin in **{}** Gruppen"
    STATS_SUPER_GROUPS = "Teilnehmer in **{}** Supergruppen"
    STATS_SG_ADMIN = "Admin in **{}** Supergruppen"
    STATS_CHANNELS = "**{}** Kanäle abonniert"
    STATS_CHAN_ADMIN = "Admin in **{}** Kanäle"
    STATS_UNKNOWN = "**{}** unbekannte Chats"
    STATS_TOTAL = "Chats insgesamt"
    FETCH_INFO = "`Hole User-Info...`"
    INFO_PERSONS_ONLY = ("`Hierbei handelt es sich nicht um einen Bot oder "
                         "einer Person. Ziehe in betracht .chatinfo zu "
                         "nutzen, falls es sich hierbei um einen Kanal oder "
                         "einer Gruppe handeln sollte`")
    FAILED_FETCH_INFO = "`Fehler beim aufrufen der User-Info`"
    UNKNOWN = "Unbekannt"
    DELETED_ACCOUNT = "Gelöschtes Konto"
    YES = "Ja"
    NO = "Nein"
    USR_NO_BIO = "Dieser User hat keine Bio"
    USR_INFO = "User-Info"
    FIRST_NAME = "Vorname"
    LAST_NAME = "Nachname"
    USERNAME = "Benutzername"
    DCID = "Rechenzentrums-ID"
    PROF_PIC_COUNT = "Anzahl an Profilbilder"
    PROF_LINK = "Permanenter Link zum Profil"
    ISBOT = "Bot"
    PREMIUM = "Premium"
    SCAMMER = "Betrüger"
    ISRESTRICTED = "Eingeschränkt"
    ISVERIFIED = "Von Telegram verifiziert"
    USR_ID = "ID"
    BIO = "Bio"
    COMMON_SELF = "Gemeinsame Gruppen... oh, das bin ja ich!"
    COMMON = "Gemeinsame Gruppen"
    UNABLE_GET_IDS = ("`User-ID(s) konnten von dieser Nachricht nicht "
                      "aufgerufen werden`")
    ORIGINAL_AUTHOR = "Originalautor"
    FORWARDER = "Person, die die Nachricht weitergeleitet hat"
    DUAL_HAS_ID_OF = "{} hat eine ID von `{}`"
    MY_ID = "Meine ID lautet `{}`"
    DEL_HAS_ID_OF = "Gelöschtes Konto hat eine ID von `{}`"
    ID_NOT_ACCESSIBLE = "die ID von {} ist nicht zugreifbar"
    ORG_HAS_ID_OF = "Der Originalautor {} hat eine ID von `{}`"


class SystemUtilitiesText(object):
    CMD_STOPPED = "{} wurde angehalten!"


class GeneralMessages(object):
    FAIL_FETCH_ENTITY = "`Fehler bei Aufrufen eines Kanals oder Users`"
    UNSUPPORTED_ENTITY = "`Die Entität ist kein Kanal oder User`"
    PERSON_ANONYMOUS = "Person ist anonym"
    CANT_FETCH_REQ = "`Konnte die Entität '{}' nicht aufrufen`"
    LOG_USER = "User"
    LOG_USERNAME = "Benutzername"
    LOG_USER_ID = "User-ID"
    LOG_CHAT_TITLE = "Chat-Titel"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "Chat-ID"
    UNKNOWN = "Unbekannt"


class ModulesUtilsText(object):
    INVALID_ARG = "`Ungültiges Argument \"{}\"`"
    USAGE = "Anwendung"
    AVAILABLE_MODULES = "Verfügbare Module"
    DISABLED_MODULES = "Deaktivierte Module"
    NAME_MODULE = "**{}-Modul**"
    MISSING_NUMBER_MODULE = "`Die Modulnummer fehlt`"
    MODULE_NOT_AVAILABLE = "`Modulnummer \"{}\" ist nicht verfügbar`"
    MODULE_NO_DESC = "__Keine Beschreibung verfügbar__"
    MODULE_NO_USAGE = "__Keine Anwendungsbeschreibung verfügbar__"
    ASTERISK = "Deinstallierbarer Modul"
    NOT_RUNNING_INFO = "Angehalten"
    UNKNOWN = "Unbekannt"
    SYSTEM = "Vorinstalliert"
    SYSTEM_MODULES = "Vorinstallierte Module"
    USER = "User"
    USER_MODULES = "User-Module"
    PKG_NAME = "Paketname"
    MODULE_TYPE = "Modul-Typ"
    AUTHORS = "Author(en)"
    VERSION = "Version"
    SIZE = "Größe"
    INSTALL_DATE = "Installationsdatum"
    LISTCMDS_TITLE = "Alle verfügbare Befehle/Features"
    LISTCMDS_USAGE = ("Führe '{} <Name des Befehls/Features>' aus, um auf "
                      "weitere Informationen über ein bestimmten Befehl zu "
                      "erhalten.")
    LISTCMDS_ORIGIN_FEATURE = "Ursprung des Befehls/Features"
    ARGS_NOT_REQ = "keine Argumente nötig"
    ARGS_NOT_AVAILABLE = "keine Argumente verfügbar"
    CMD_NOT_FOUND = "Befehl '{}' wurde nicht gefunden!"
    MOD_HELP = "Hilfe nötig? Führe {} aus"
    MOD_UTILS = "Module"


class WebToolsText(object):
    PING_SPEED = "Round-Trip-Time: "
    DCMESSAGE = ("Land : `{}`\n"
                 "Dieser Rechenzentrum : `{}`\n"
                 "Nächster Rechenzentrum : `{}`")
    BAD_ARGS = "`Ungültige Argumente!`"
    INVALID_HOST = "`Fehler beim parsen des IPs/Hostname`"
    PINGER_VAL = "DNS: `{}`\nPing-Geschwindigkeit: `{}`"
    SPD_TEST_SELECT_SERVER = "Wähle den besten Server aus"
    SPD_TEST_DOWNLOAD = "Teste Download-Geschwindigkeit"
    SPD_TEST_UPLOAD = "Teste Upload-Geschwindigkeit"
    SPD_PROCESSING = "Wird bearbeitet"
    SPD_FAILED = "Speedtest fehlgeschlagen"
    SPD_NO_RESULT = "Kein Ergebnis"
    SPD_NO_MEMORY = "Nicht genügend Speicher vorhanden"
    SPD_FAIL_SEND_RESULT = "`Fehler beim senden des Speedtest-Ergebnisses`"
    SPD_MEGABITS = "Mbit/s"
    SPD_MEGABYTES = "MB/s"
    SPD_TIME = "Testzeitpunkt"
    SPD_DOWNLOAD = "Download-Geschwindigkeit"
    SPD_UPLOAD = "Upload-Geschwindigkeit"
    SPD_PING = "Ping"
    SPD_ISP = "Mein ISP"
    SPD_HOSTED_BY = "Gehostet von"


class GitHubText(object):
    INVALID_URL = "user/repo Kombination ist ungültig"
    NO_RELEASE = "Das angegebene Release konnte nicht gefunden werden"
    AUTHOR_STR = "<b>Autor:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Name des Releases:</b> "
    ASSET = "<b>Anlage:</b> \n"
    SIZE = "Größe: "
    DL_COUNT = "\nAnzahl an Downloads: "
    INVALID_ARGS = ("Ungültige Argumente! Stellen Sie sicher, dass Sie "
                    "eine gültige Kombination von user/repo angeben")
    GITRATE_NO_DATA = "Keine Daten von GitHub erhalten"


class TerminalText(object):
    BASH_ERROR = ("Ein unerwarteter Fehler ist aufgetreten, wahrscheinlich "
                  "aufgrund von ungültige Argumente oder der Befehl "
                  "existiert nicht")
    BASH_CRT_FILE_FAILED_RO = ("Fehler beim erstellen des Shell-Outputs "
                               "als eine Datei. Dateisystem nur lesbar?")
    BASH_CRT_FILE_FAILED = ("Fehler beim erstellen des Shell-Outputs als "
                            "eine Datei")
    BASH_SEND_FILE_MTLO = ("Das Shell-Output kann nicht erstellt werden, "
                           "da Medien hochladen in diesem Chat nicht "
                           "erlaubt ist")
    BASH_SEND_FILE_FAILED = ("Fehler beim senden des Shell-Outputs als "
                             "eine Datei")


class MiscText(object):
    COIN_LANDED_VAL = "Die Münze landete auf: "
    THRWING_COIN = "`Werfe Münze...`"
    HEADS = "Kopf"
    TAILS = "Zahl"
    RAND_INVLD_ARGS = ("`Ungültie Argumente, stellen Sie sicher, dass "
                       "Sie genau 2 Zahlen angeben`")
    FRST_LIMIT_INVALID = "`Der erste Wert ist keine gültige Zahl!`"
    SCND_LIMIT_INVALID = "`Der zweite Wert ist keine gültige Zahl!`"
    RAND_NUM_GEN = "Ihre generierte Zahl zwischen `{}` und `{}`: **`{}`**"


class PackageManagerText(object):
    REPO_LIST_EMPTY = ("Die Repository-Liste ist leer! Führe "
                       "`.pkg update <owner/repo>` aus, um ein neuen "
                       "Repository hinzuzufügen oder füge sie an "
                       "COMMUNITY_REPOS-Config bei")
    PACKAGES_UPDATER = "Paketen-Updater"
    INVALID_REPO_URL = "Ungültiges Repository-URL-Format"
    UPDATING_REPO_DATA = "Repository-Daten werden aktualisiert..."
    UPDATE_SUCCESS = "Aktuelle Daten von '{}' erhalten"
    UPDATE_FAILED = "Fehler beim Holen der Daten von '{}'"
    UPDATER_FINISHED = "Updater beendet"
    LIST_OF_PACKAGES = "Paketen-Liste"
    INSTALLED_MODULES = "Installierte Module"
    NO_MODULES_INSTALLED = "Keine User-Module installiert"
    MODULES_IN = "Module in {}"
    AUTHOR = "Autor"
    VERSION = "Version"
    REPO_NO_MODULES = "Dieses Repository bietet keine Module an"
    REPOS_NO_DATA = ("Keine Repository-Daten. Möglicherweise hilft {} "
                     "auszuführen")
    INSTALLED = "Installiert"
    INSTALLED_NOTLOADED = "Installiert aber nicht gestartet"
    UPGRADEABLE = "Aktualisierbar"
    START_FAILED = "Starten fehlgeschlagen"
    DISABLED = "Deaktiviert"
    EQUAL_NAME = "Gleicher Name"
    NEVER = "Nie"
    LAST_UPDATED = "Zuletzt aktualisiert"
    INSTALL_EMPTY = "Keine Modulnamen für die Installation gegeben"
    PACKAGE_INSTALLER = "Paketen-Installer"
    NO_REPO_URL = "Keine Repository-URL für die Installation gegeben!"
    INSTALL_EMPTY_REPO = ("Keine Modulnamen für die Installation "
                          "von einem bestimmten Repository gegeben!")
    UNKNOWN_REPO_URL = "Angegebene Repository-URL ist unbekannt!"
    UNKNOWN_MODULES = "Unbekannte(r) Modul(e)"
    INSTALLING_MODULES = ("Module werden installiert. Dieser Prozess könnte "
                          "eine Weile dauern...")
    DOWN_FAILED = "Download von '{}' ist fehlgeschlagen"
    INSTALL_FAILED = "Fehler beim Installieren von '{}'"
    INSTALL_SUCCESS = "'{}' wurde installiert"
    UPDATE_DATA_FAIL = "Fehler beim Aktualisieren der Daten von {}"
    NO_INSTALL_QUEUED = "Keine Installation in der Warteschlange"
    INSTALLER_FINISHED = "Installer beendet"
    UNINSTALL_EMPTY = "Keine Modulnamen für die Deinstallation gegeben"
    PACKAGE_UNINSTALLER = "Paketen-Uninstaller"
    UNINSTALLING_MODULES = "Module werden deinstalliert..."
    UNINSTALL_FAILED = "Deinstallation von '{}' ist fehlgeschlagen"
    UNINSTALL_SUCCESS = "'{}' wurde deinstalliert"
    UNINSTALL_DATA = ("'{}' wurde deinstalliert jedoch konnten dessen Daten "
                      "nicht entfernt werden")
    MODULE_NOT_INSTALL = "'{}' ist nicht installiert"
    UNINSTALLER_FINISHED = "Uninstaller beendet"
    NO_REPO_NAMES = "Keine Repository-Namen zum Entfernen gegeben"
    NO_REPO_REMOVE = "Es gibt keine Repositorys zum Entfernen"
    REPO_REMOVER = "Repository-Remover"
    CANNOT_REMOVE_REPO = "'{}' kann nicht entfernt werden (geschützt)"
    REMOVING_REPO_DATA = "Repository-Daten werden entfernt..."
    REMOVE_SUCCESS = "'{}' wurde entfernt"
    REMOVE_FAILED = "Fehler beim Entfernen von '{}'"
    UNKNOWN_REPO = "Unbekannter Repository"
    REMOVER_FINISHED = "Remover beendet"
    LOAD_PGKS = "Paketlisten werden geladen..."
    CANNOT_INSTALL_MODULES = ("User-Module können im abgesicherten Modus "
                              "nicht installiert werden")
    PACKAGE_MANAGER = "Package-Manager"
    UNKNOWN_OPTION = "Unbekannte Option '{}'"
    NO_OPTION = "Keine Option gegeben"
    PKG_HELP = "Hilfe nötig? Führe {} aus"
    TEXT_TOO_LONG = ("Die Liste ist zu groß, um sie hier anzuzeigen. "
                     "Die Liste wurde im Terminal des Bots geschrieben")


class UpdaterText(object):
    CHECKING_UPDATES = "Prüfe auf Updates..."
    GIT_REPO = "Das Verzeichnis von HyperUBot ist ein lokales GIT-Repository"
    DOWNLOADING_RELEASE = "Das neuste Release wird heruntergeladen..."
    UPDATE_FAILED = "Update fehlgeschlagen"
    UPDATE_INTERNAL_FAILED = "Ein interner Fehler ist aufgetreten"
    START_RECOVERY_FAILED = "Fehler beim Starten des Recoverys"
    ALREADY_UP_TO_DATE = "HyperUBot ist bereits auf dem neusten Stand"
    LATEST = "Neuste"
    CURRENT = "Aktuell"
    UPDATE_AVAILABLE = "Update verfügbar"
    RELEASE_DATE = "Veröffentlichungsdatum"
    CHANGELOG_AT = "Changelog auf {}"
    DOWNLOAD_SUCCESS = ("Download abgeschlossen. Der Bot wird "
                        "heruntergefahren, um das Update-Paket zu "
                        "installieren...")
    DOWNLOAD_SUCCESS_WIN = ("Download abgeschlossen und bereit. Bitte "
                            "fahre HyperUBot herunter und folge die "
                            "Anweisungen im Terminal, um das Update-Paket "
                            "manuell zu installieren")
    UPDATE_QUEUED = ("Führe `.update upgrade` aus, um das Update-Paket "
                     "jetzt herunterzuladen und zu installieren")
    UPDATE_SUCESS = "HyperUBot wurde erfolgreich auf {} aktualisiert!"
    UPDATE_FAIL = "Die Aktualisierung von HyperUBot auf {} ist fehlgeschlagen"
    NOTIFIER_HEADER = "HyperUBots Updatemelder"
    NOTIFIER_INFO = "Ein neues Update auf {} ist verfügbar!"


class SideloaderText(object):
    NOT_PY_FILE = "Dies ist keine gültige .py-Datei! Sideload nicht möglich!"
    DLOADING = "`Wird heruntergeladen...`"
    MODULE_EXISTS = ("Ein Userspace-Modul mit dem Namen `{}` ist bereits "
                     "vorhanden. Bitte führe diesen Befehl mit dem "
                     "Argument `force` aus, wenn Sie sie überschreiben "
                     "möchten!")
    SUCCESS = "`{}` wurde erfolgreich installiert!"
    LOG = "Das Modul `{}` wurde erfolgrech aus dem Sideload installiert!"
    REBOOT_INFO = ("Bitte starte HyperUBot jetzt neu, um das geladene "
                   "Sideload-Modul zu starten")
    INVALID_FILE = "Bitte antworte auf eine gültige Datei!"


class FeatureMgrText(object):
    DISABLE_FTR = "Nenne einen Befehl oder ein Feature, um sie zu deaktiveren!"
    DISABLE_FTR_FAIL = ("Anscheinend kann ich diesen Befehl oder Feature "
                        "nicht deaktivieren")
    DISABLE_FTR_SUCCESS = ("Der Befehl oder das Feature '`{}`' wurde "
                           "deaktiviert")
    DISABLED_FTRS = "Deaktivierte Features"
    NO_DISABLED_FTRS = "Keine Features deaktiviert"
    ENABLE_FTR = "Nenne einen Befehl oder ein Feature, um sie zu aktiveren!"
    ENABLE_FTR_FAIL = ("Anscheinend kann ich diesen Befehl oder Feature "
                       "nicht aktivieren")
    ENABLE_FTR_SUCCESS = "Der Befehl oder das Feature '`{}`' wurde aktiviert"


class WelcomeText(object):
    WELCOME_TO_HYPERUBOT = "Willkommen bei HyperUBot!"
    INFO = ("Sie haben es geschafft, HyperUBot erfolgreich auf ihrem Gerät "
            "zum laufen zu bringen. Was kommt als nächstes? Die folgenden "
            "Befehle werden ihnen helfen, ihren neuen Userbot besser zu "
            "verstehen und welche Optionen, Features usw. HyperUBot ihnen "
            "bieten kann")
    INFO_STATUS = ("holt den aktuellen Status von HyperUBot sowie die "
                   "Version, Laufzeit usw. Sehr nützlich, um zu prüfen, "
                   "ob ihr Userbot überhaupt online ist")
    INFO_OR = "oder"
    INFO_HELP = ("listet alle verfügbaren Befehle und Features von allen "
                 "nutzbaren Modulen. Übergeben Sie den Namen des Befehls oder "
                 "des Features (z.B. {}), um die Anwendung des bestimmten "
                 "Befehls oder Features zu erhalten")
    INFO_MODULES = ("listet alle bestehenden und User-Module an einen Ort an. "
                    "Dieses Befehl nimmt auch Argumente an, um auf weitere "
                    "Informationen zu gelangen, wie die Beschreibung oder "
                    "Anwendung eines Modules.")
    INFO_PKG = ("unser Package-Manager bietet ihnen die Möglichkeit an, neue "
                "Module zu installieren. Wir haben auch einige User-Module "
                "erstellt, die sie mit diesem Befehl herunterladen können. "
                "Dies ermöglicht es ihnen auf neue Module zuzugreifen ohne "
                "auf neue Bot-Updates zu warten. Übrigens, gibt es auch "
                "Module, die von der Community selbst erstellt wurden. Also "
                "probieren Sie die auch gerne aus!")
    INFO_SUPPORT = ("Noch Fragen über HyperUBot? Lesen Sie unseren {} oder "
                    "chatten Sie auch gerne mit uns in unserer {}!")
    INFO_SUPPORT_LINK = "Support-Gruppe"
    INFO_SUPPORT_WIKI = "Wiki"
    INFO_FUN = "Viel Spaß!"


# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = ("Ein Modul, dass ihr oder eines Freundes Gruppe einfacher "
                  "verwaltet. Enthält bekannte Befehle wie ban, unban, "
                  "promote usw.\n\n"
                  "Hinweis: Die meisten Befehle in diesem Modul erforderen "
                  "Adminrechte, um Ordnungsgemäß zu funktionieren.")
    CHATINFO_DESC = ("Erhalten Sie zahlreiche Informationen aus Kanälen, "
                     "Gruppen oder Supergruppen z.B. das Erstelldatum, "
                     "Anzahl an Nachrichten, Löschungen, "
                     "ehemaliger Name, usw.")
    DELETIONS_DESC = ("Dieses Modul ermöglicht es Ihnen, die Nachrichten, "
                      "ihrer oder die Gruppe eines anderen, schneller zu "
                      "löschen. Jemand hat ihre Gruppe gespammt? Nutze den "
                      "purge Befehl, um die Nachrichten zu beseitigen!\n"
                      "Alle Befehle in diesem Modul erfordern Adminrechte, "
                      "um die Nachrichten anderer zu löschen.\n\n"
                      "**Wichtiger Hinweis: Missbrauchen Sie diesen Modul "
                      "nicht, um den Chatverlauf anderer Gruppen komplett "
                      "zu löschen**, im ernst, tun Sie's nicht..")
    MEMBERINFO_DESC = ("Stellt Informationen von einem bestimmten "
                       "Gruppenteilnehmer wie dessen Berechtigungen, "
                       "Einschräkungsdatum, Beitrittsdatum usw. bereit\n\n"
                       "Hinweis: Erfordert Adminrechte, um auf die "
                       "Berechtigungen anderer Mitglieder zuzugreifen.")
    MESSAGES_DESC = ("Dieses Modul enthält Befehle, die nur mit Nachrichten "
                     "funktionieren, sowie msgs oder pin.")
    SCRAPPERS_DESC = ("Nicht genau wonach es sich anhört, dennoch enthält "
                      "dieses Modul nützliche Features wie Übersetzung "
                      "oder Text-to-Speech.")
    SYSTOOLS_DESC = ("Dieses Modul enthält eine Reihe an System-Tools für "
                     "den Bot bereit. Sie ermöglicht Ihnen die "
                     "Bot-Laufzeit, Server-Laufzeit, die Versionen aller "
                     "Komponenten des Bots, die technische Daten des "
                     "System-Servers und einige Leistungssteuerungen des "
                     "Bots zu überprüfen.")
    USER_DESC = ("Stellt informationen über jeden User bereit, ihre "
                 "Statistiken und enthält das Kickme-Tool.")
    WEBTOOLS_DESC = ("Dieses Modul enthält, wenn auch nicht alle, "
                     "Web-Tools des Bots, solche wie Ping, Speedtest, "
                     "RTT-Rechner und den aktuellen Rechenzentrum.")
    GITHUB_DESC = ("Ein Modul, dass den GitHub-API zum Gebrauch macht. "
                   "Dieses Modul ermöglicht es Ihnen nach einem Release "
                   "von einem bestimmten User und Repository zu prüfen.")
    TERMINAL_DESC = ("Dieses Modul führt Shell-Befehle direkt im "
                     "Host-Machine aus.\n\n"
                     "**Warnung:** Das Ausführen von Shell-Befehlen vom "
                     "Bot aus, kann und wird permanente Auswirkungen auf "
                     "das Host-System haben. **Falls das Bot mit "
                     "Sudo/Root-Rechten läuft, führt das zu negative "
                     "Auswirkungen**")
    MISC_DESC = ("Das Miscellaneous-Modul enthält einen kleinen Set von "
                 "Tools, dass nicht wirklich zu den bisherigen Modulen "
                 "passte aber gleichzeitig Kompakt genug sind, um ihr "
                 "eigenes Modul zu haben. Weitere Informationen finden "
                 "Sie in der Hilfe.")
    PACKAGE_MANAGER_DESC = ("Das Package-Manager-Modul erlaubt es dem "
                            "User extra Apps zu verwalten, von externen "
                            "Repos, entweder aus offiziellen, wie das "
                            "Module-Universe Repo oder aus externen "
                            "Quellen. Das bietet den Usern eine Möglichkeit "
                            "an, ihren Bot selbst anzupassen als "
                            "ursprünglich gesehen.")
    UPDATER_DESC = ("Das Updater-Modul erlaubt den User den Bot auf neue "
                    "Updates zu prüfen und, falls vorhanden, zu "
                    "akualisieren.")
    SIDELOADER_DESC = ("Das Sideloader-Modul erlaubt es Ihnen Python-Dateien "
                       "mit Leichtigkeit extern zu beziehen. Um dies zu "
                       "ermöglichen, müssen Sie nur auf eine .py-Datei "
                       "antworten, dass im Chat als Dokument gesendet "
                       "wurde!\n\n"
                       "**INFORMATION**: Diese Dateien müssen so geschrieben "
                       "worden sein, dass sie mit dem Bot funktionieren "
                       "können. Der Versuch unbekannte Dateien zu laden "
                       "könnte zu einem 'Soft-Brick' des Bots führen, dass "
                       "Sie auffordert, das Modul manuell aus dem Userspace "
                       "zu löschen!\n\n"
                       "**KRITISCHE WARNUNG**: Bösartige Dateien könnten "
                       "einige ihrer Informationen (beispielsweise das "
                       "API Key und/oder String Session) zu einem bösartigen "
                       "Hacker weiterleiten! Beziehen Sie Module nur "
                       "aus vertrauenswürdigen Quellen!")
    FEATURE_MGR_DESC = ("Das Feature-Manager-Modul erlaubt es dem Nutzer, "
                        "einen Befehl oder ein Feature in Echtzeit zu "
                        "(de)aktivieren, und Nein, die Enable- und Disable-"
                        "Befehle können nicht deaktiviert werden.")


class ModuleUsages(object):
    ADMIN_USAGE = {"adminlist": {"args": "[optional: <Link/ID>]",
                                 "usage": ("Listet alle Admins (aus der "
                                           "Ferne) von einem Kanal oder "
                                           "Gruppe. Erfordert Adminrechte "
                                           "in Kanälen.")},
                   "ban": {"args": ("[optional: <Benutzername/ID> <Chat "
                                    "(ID oder Link)>] oder als Antwort"),
                           "usage": ("Bannt einen User (aus der Ferne) aus "
                                     "einem Chat aus. Erfordert Adminrechte "
                                     "mit Nutzer sperren Berechtigung.")},
                   "unban": {"args": ("[optional: <Benutzername/ID> <Chat "
                                      "(ID oder Link)>] oder als Antwort"),
                             "usage": ("Entbannt einen User (aus der Ferne) "
                                       "wieder aus einem Chat. Erfordert "
                                       "Adminrechte mit Nutzer sperren "
                                       "Berechtigung.")},
                   "kick": {"args": ("[optional: <Benutzername/ID> <Chat "
                                     "(ID oder Link)>] oder als Antwort"),
                            "usage": ("Kickt einen User (aus der Ferne) "
                                      "aus einem Chat aus. Erfordert "
                                      "Adminrechte mit Nutzer sperren "
                                      "Berechtigung.")},
                   "promote": {"args": ("[optional: <Benutzername/ID> "
                                        "und/oder <Bezeichnung>] oder als "
                                        "Antwort"),
                               "usage": ("Befördert einen User mit "
                                         "unsterblicher Macht! Erfordert "
                                         "Adminrechte mit neue Admins "
                                         "hinzufügen Berechtigung und einer "
                                         "zweiten Adminberechtigung, da "
                                         "promote nie einen User mit neue "
                                         "Admins hinzufügen Berechtigung "
                                         "befördert. Die Länge der "
                                         "Bezeichnung darf maximal "
                                         "16 Zeichen enthalten.")},
                   "demote": {"args": ("[optional: <Benutzername/ID>] oder "
                                       "als Antwort"),
                              "usage": ("Degradiert einen User zu einem "
                                        "sterblichen User. Erfordert "
                                        "Adminrechte mit neue Admins "
                                        "hinzufügen Berechtigung. "
                                        "Funktioniert nur mit Admins, die "
                                        "auch von ihnen befördert wurden.")},
                   "mute": {"args": ("[optional: <Benutzername/ID> <Chat "
                                     "(ID oder Link)>] oder als Antwort"),
                            "usage": ("Schaltet einen User (aus der Ferne) "
                                      "in einem Chat stumm. Erfordert "
                                      "Adminrechte mit Nutzer sperren "
                                      "Berechtigung.")},
                   "unmute": {"args": ("[optional: <Benutzername/ID> <Chat "
                                       "(ID oder Link)>] oder als Antwort"),
                              "usage": ("Hebt die Stummschaltung eines User "
                                        "(aus der Ferne) in einem Chat auf. "
                                        "Erfordert Adminrechte mit Nutzer "
                                        "sperren Berechtigung.")},
                   "delaccs": {"args": "[optional: <Chat-ID oder Link>]",
                               "usage": ("Versucht gelöschte Konten "
                                         "automatisch aus einem Chat zu "
                                         "entfernen, falls Adminrechte mit "
                                         "Ban-Berechtigung vorhanden sind.\n"
                                         "Ansonsten werden nur die Anzahl "
                                         "an gelöschten Konten im "
                                         "jeweiligen Chat angezeigt.")}}

    CHATINFO_USAGE = {"chatinfo": {"args": ("[optional: <Chat-ID/Link>] "
                                            "oder als Antwort (falls es "
                                            "sich um ein Kanal handelt)"),
                                   "usage": ("Holt die Informationen über "
                                             "einem Chat. Einige "
                                             "Informationen könnten "
                                             "aufgrund fehlender "
                                             "Berechtigungen eingeschränkt "
                                             "sein.")},
                      "chatid": {"args": None,
                                 "usage": ("Holt sich die ID eines "
                                           "Kanales oder einer Gruppe.")},
                      "getlink": {"args": "[optional: <Chat-ID/Link>]",
                                  "usage": ("Holt sich das Einladungslink "
                                            "des Kanales oder einer Gruppe, "
                                            "welches dann mit anderen "
                                            "geteilt werden kann. Erfordert "
                                            "Adminrechte mit Nutzer per "
                                            "Link einladen Berechtigung.")}}

    DELETIONS_USAGE = {"del": {"args": None,
                               "usage": ("Löscht auf die geantwortete "
                                         "Nachricht.")},
                       "purge": {"args": None,
                                 "usage": ("Purgt alle Nachrichten zwischen "
                                           "der neusten Nachricht und der "
                                           "geantworteten Nachricht. "
                                           "Adminrechte mit Nachrichten "
                                           "löschen Berechtigung sind "
                                           "erforderlich falls in Kanälen "
                                           "oder Gruppen gepurgt werden "
                                           "soll.\n"
                                           "**Hinweis: Bitte Missbrauchen "
                                           "Sie diesen Feature nicht, um "
                                           "ganze Gruppen-Chat-Verläufe von "
                                           "anderen Personen zu löschen!**")}}

    MEMBERINFO_USAGE = {"minfo": {"args": ("[optional: <Benutzername/ID> "
                                           "<Gruppe>] oder als Antwort"),
                                  "usage": ("Holt (aus der Ferne) die "
                                            "Informationen eines Mitglieds "
                                            "aus einer Supergruppe.")}}

    MESSAGES_USAGE = {"msgs": {"args": ("[optional: <Benutzername/ID>] "
                                        "oder als Antwort"),
                               "usage": ("Holt die Anzahl an gesendete "
                                         "Nachrichten von einem User "
                                         "(enthält jegliche Nachricht wie "
                                         "Textnachrichten, "
                                         "Sprachnachrichten, Videos usw.).")},
                      "pin": {"args": ("[optionales Argument \"loud\" um "
                                       "alle Mitglieder zu informieren] "
                                       "oder als Antwort"),
                              "usage": ("Antworte auf jemand's Nachricht, "
                                        "um diese in dem Chat anzuheften.")},
                      "unpin": {"args": ("[optionales Argument \"all\"] oder "
                                         "als Antwort"),
                                "usage": ("Antworte auf eine Nachricht, um "
                                          "sie loszulösen oder "
                                          "nutze \".unpin all\" um alle "
                                          "angeheftete Nachrichten in "
                                          "einem Chat loszulösen.")}}

    SCRAPPERS_USAGE = {"trt": {"args": "[optional: <Text>] oder als Antwort",
                               "usage": ("Der gegebene Text oder auf die "
                                         "geantwortete Nachricht wird "
                                         "auf die Zielspraches des Bots "
                                         "übersetzt.")},
                       "tts": {"args": "[optional: <Text>] oder als Antwort",
                               "usage": ("Konvertiert den Text oder auf "
                                         "die geantwortete Nachricht ins "
                                         "Gesprochene um (Text-to-Speech).")},
                       "stt": {"args": "nur als Antwort",
                               "usage": ("Konvertiert auf eine geantwortete "
                                         "Sprachnachricht in Text um "
                                         "(Speech-to-Text).")},
                       "scrlang": {"args": None,
                                   "usage": ("Zeigt die aktuelle Sprache "
                                             "des Bots an, indem übersetzt "
                                             "oder in TTS werden soll")},
                       "setlang": {"args": "[ISO-Wert]",
                                   "usage": ("Setzt die neue Sprache aus "
                                             "der ISO-Wert-Liste ein.")},
                       "currency": {"args": ("<Betrag> <Von ISO> "
                                             "[optional: <Zu ISO>]"),
                                    "usage": ("Konvertiert die eingegebene "
                                              "Währung in Zielwährung um "
                                              "(Standard: USD). Erfordert "
                                              "den ISO eines Landes "
                                              "(EUR, USD, JPY usw.).")}}

    SYSTOOLS_USAGE = {"status": {"args": None,
                                 "usage": ("Geben Sie .status ein, um "
                                           "zahlreiche Informationen des "
                                           "Bots zu prüfen und ob es am "
                                           "Laufen ist.")},
                      "shutdown": {"args": None,
                                   "usage": ("Geben Sie .shutdown ein, "
                                             "um den Bot herunterzufahren.")},
                      "reboot": {"args": None,
                                 "usage": "Startet den Bot neu!"},
                      "storage": {"args": None,
                                  "usage": ("Zeigt Informationen über den "
                                            "Bot's Serverspeicher an.")},
                      "neofetch": {"args": None,
                                   "usage": ("Zeigt alle relevanten "
                                             "Systeminformationen (sowohl "
                                             "Hardware als auch Software) "
                                             "vom Host an. Neofetch muss "
                                             "zuvor installiert sein.")},
                      "sendlog": {"args": None,
                                  "usage": ("Ladet die Log-Datei im "
                                            "aktuellen Chat hoch.")}}

    USER_USAGE = {"info": {"args": ("[optional: <Benutzername/ID>] oder "
                                    "als Antwort"),
                           "usage": "Holt Informationen über einen User."},
                  "stats": {"args": None,
                            "usage": "Holt Ihre eigenen Statistiken."},
                  "kickme": {"args": None,
                             "usage": "Entfernt Sie selbst aus einer Gruppe."},
                  "id": {"args": ("[optional: <Benutzername>] oder als "
                                  "Antwort"),
                         "usage": ("Holt die ID eines Kanals oder eines "
                                  "Users. Falls auf eine weitergeleitete "
                                  "Nachricht geantwortet wurde, holt es die "
                                  "ID des Kanals oder der Person, der die "
                                  "Nachricht weitergeleitet hat und vom "
                                  "Originalautor.")}}

    WEBTOOLS_USAGE = {"rtt": {"args": None,
                              "usage": ("Ruft den aktuellen "
                                        "Round-Trip-Time auf.")},
                      "dc": {"args": None,
                             "usage": ("Sucht nach dem nächstengelegenen "
                                       "Rechenzentrum ihres Userbots aus.")},
                      "ping": {"args": "<DNS/IP>",
                               "usage": ("Pingt einen bestimmten DNS- "
                                         "oder IP-Addresse an.")},
                      "speedtest": {"args": "[optionales Argument \"pic\"]",
                                    "usage": ("Führt einen Speedtest durch "
                                              "und zeigt Ihnen das Ergebnis "
                                              "als Text an. Das Übergeben "
                                              "von \"pic\" als Argument "
                                              "ändert das Ergebnis zu einem "
                                              "Bild.")}}

    GITHUB_USAGE = {"git": {"args": "<User>/<Repo>",
                            "usage": ("Prüft nach Releases aus dem "
                                      "angegebenen User/Repo-Kombination.")},
                    "gitrate": {"args": None,
                                "usage": ("Holt den aktuellen Stand des Rate "
                                          "Limits von GitHubs API wie REST "
                                          "API oder Search API.\n\n"
                                          "Da einige Bot-Features von GitHubs "
                                          "API abhängig sind um z.B Updates "
                                          "oder neue Module zu erhalten, "
                                          "triggert jedes Aufruf zur API "
                                          "einen Call. Es gibt einen Limit "
                                          "von 60 Calls pro Stunde zur API "
                                          "(REST API). Nutz diesen Befehl, um "
                                          "nachzuprüfen, wie viele Calls Dir "
                                          "noch zur API verbleiben.\n\n"
                                          "Die API-Informationen werden wie "
                                          "folgt angezeigt:\n__API_NAME: "
                                          "NOCH_ÜBRIG/MAX_LIMIT__")}}

    MODULES_UTILS_USAGE = {"lcmds": {"args": ("[optional: <Name des Befehls>]"),
                                     "usage": ("Listet alle verfügbare und "
                                               "registrierte Befehle")},
                           "mods": {"args": ("<-Option> [Modulnummer aus der "
                                             "Liste]"),
                                    "usage": ("\n`.mods -d [Modulnummer aus "
                                              "der Liste]`\n"
                                              "Zeigt die Beschreibung des "
                                              "jeweiligen Moduls an. Wer "
                                              "weiß, vielleicht sind da "
                                              "einige Informationen "
                                              "versteckt?\n\n"
                                              "`.mods -i [Modulnummer aus der "
                                              "Liste]`\n"
                                              "Zeigt Informationen über das "
                                              "jeweilige Modul an z.B. der "
                                              "Name, Autor, Version usw.\n\n"
                                              "`.mods -u [Modulnummer aus der "
                                              "Liste]`\n"
                                              "Enthüllt die Geheimnisse und "
                                              "die Anwendung des jeweiligen "
                                              "Moduls")}}

    TERMINAL_USAGE = {"shell": {"args": "<Befehl>",
                                "usage": ("Führt umgehend den gegebenen "
                                          "Befehl im Shell des Server-"
                                          "Machine aus (Bash, PowerShell "
                                          "oder Z shell)\n\n"
                                          "**WARNUNG: Falls der "
                                          "Userbot-Prozess mit Root-Rechten "
                                          "läuft, könnte dies potenziel "
                                          "ihr System unwiederruflich "
                                          "zerschießen! Mit Vorsicht "
                                          "fortfahren!**")}}

    MISC_USAGE = {"coinflip": {"args": None,
                               "usage": ("Wirft eine Münze und gibt "
                                         "entweder Kopf oder Zahl zurück, "
                                         "abhängig vom Ergebnis.")},
                  "dice": {"args": None,
                           "usage": ("Schickt das Würfel-Emoji, Telegram "
                                     "wird sich um ein komplett zufälligen "
                                     "Wert kümmern.")},
                  "rand": {"args": "<Untergrenze> <Obergrenze>",
                           "usage": ("Gegeben sei ein Unter- und Obergrenze "
                                     "(beides Integers), das Bot wird eine "
                                     "zufällige Zahl zwischen den beiden "
                                     "Werten generieren.")}}

    PACKAGE_MANAGER_USAGE = {"pkg": {"args": ("<option> [optional: "
                                              "<Argumente>]"),
                                     "usage": ("\n`.pkg update "
                                               "[optional: <Liste der "
                                               "Owner/Repo-Kombos>]`\n"
                                               "Aktualisiert die Daten aller "
                                               "Repositorys. Wenn "
                                               "Repository-URLs angegeben "
                                               "wurden z.B. '.pkg update "
                                               "nunopenim/module-universe', "
                                               "werden nur diese "
                                               "bestimmten Repositorys "
                                               "aktualisiert. Ebenfalls ist "
                                               "dadurch auch möglich, neue "
                                               "Repositorys mittels der "
                                               "Owner/Repo-Kombo "
                                               "hinzuzufügen.\n\n"
                                               "`.pkg list [optional: "
                                               "<-installed oder -repos>]`\n"
                                               "Listet alle installierte "
                                               "Module und sowie alle "
                                               "Module von bekannten "
                                               "Repositorys. Nutze diesen "
                                               "Befehl mit der Option "
                                               "-installed, um nur "
                                               "installierte Module "
                                               "anzuzeigen oder mit der "
                                               "Option -repos, um nur die "
                                               "Module der Repositorys "
                                               "anzuzeigen.\n\n"
                                               "`.pkg install <Modulliste>`"
                                               "\noder\n"
                                               "`.pkg install -repo "
                                               "<Owner/Repo> <Modulliste>`\n"
                                               "Führt die Installation "
                                               "jedes Modul vom übergebenen "
                                               "Modulliste durch. Falls Sie "
                                               "nur Module von einem "
                                               "bestimmten Repository "
                                               "installieren möchten, "
                                               "übergeben Sie die -repo "
                                               "Option mit einem "
                                               "Ower/Repo-Kombo zusammen "
                                               "mit einer Modulliste als "
                                               "Argument zu.\n\n"
                                               "`.pkg uninstall/remove "
                                               "<Modulliste>`\n"
                                               "Deinstalliert jedes Modul "
                                               "aus der gegebenen "
                                               "Modulliste.\n\n"
                                               "`.pkg rmrepo <Liste der "
                                               "Owner/Repo-Kombos>`\n"
                                               "Entfernt die Daten jedes "
                                               "Owner/Repo-Kombo aus der "
                                               "gegebenen Liste.")}}

    UPDATER_USAGE = {"update": {"args": "upgrade",
                                "usage": ("Prüft nach Updates und, falls "
                                          "vorhanden, zeigt es die "
                                          "Neuerungen an. Falls der User "
                                          "nach Updates geprüft hat, wird "
                                          "es den Bot auf die neuste "
                                          "Version aktualisieren.")}}

    SIDELOADER_USAGE = {"sideload": {"args": "<Argument>",
                                     "usage": ("Bezieht ein Python-Script-"
                                               "Datei, dass in einem Chat "
                                               "als Dokument geschickt "
                                               "wurde. Antworte auf diese "
                                               "Nachricht, um sie zu "
                                               "beziehen. Sie können auch "
                                               "das `force` Argument nutzen, "
                                               "um die Installation "
                                               "zwangsläufig durchzuführen, "
                                               "falls ein Modul mit dem "
                                               "gleichen Namen im Userspace "
                                               "existiert.\n\n"
                                               "**INFORMATION**: Diese "
                                               "Dateien müssen so "
                                               "geschrieben worden sein, "
                                               "dass sie mit dem Bot "
                                               "funktionieren können. Der "
                                               "Versuch unbekannte Dateien "
                                               "zu laden könnte zu einem "
                                               "'Soft-Brick' des Bots "
                                               "führen, dass Sie "
                                               "auffordert, das Modul "
                                               "manuell aus dem Userspace "
                                               "zu löschen!\n\n"
                                               "**KRITISCHE WARNUNG**: "
                                               "Bösartige Dateien könnten "
                                               "einige ihrer Informationen "
                                               "(beispielsweise das API Key "
                                               "und/oder String Session) zu "
                                               "einem bösartigen Hacker "
                                               "weiterleiten! Beziehen Sie "
                                               "Module nur aus "
                                               "vertrauenswürdigen Quellen!")}}

    FEATURE_MGR_USAGE = {"disable": {"args": ("<Name des Befehls/Alias oder "
                                              "Feature>"),
                                     "usage": ("Deakiviert ein gegebenen "
                                               "Befehl oder Feature. "
                                               "Funktioniert auch mit "
                                               "Aliase")},
                         "disabled": {"args": None,
                                      "usage": ("Listet alle deaktiverte "
                                                "Features auf")},
                         "enable": {"args": ("<Name des Befehls/Alias oder "
                                             "Feature>"),
                                    "usage": ("Akiviert ein gegebenen Befehl "
                                              "oder Feature. Funktioniert "
                                              "auch mit Aliase")}}
