# Portuguese Language file
#
# Copyright 2020-2021 nunopenim @github
# Copyright 2020-2021 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

NAME = "Português"


class AdminText(object):
    ADMINS_IN_CHAT = "Administradores em **{}**"
    UNABLE_GET_ADMINS = ("`Não foi possível obter os administratores "
                         "neste chat`")
    FAIL_CHAT = "`Não foi possível identificar o chat!`"
    NO_GROUP_CHAN = "`Este chat não é um grupo ou canal!`"
    NO_GROUP_CHAN_ARGS = ("`Este chat, ou o chat dado, não é um grupo ou "
                          "canal!`")
    NO_ADMIN = ("`São necessários privilégios de Admin para executar "
                "esta ação!`")
    NO_BAN_PRIV = ("`É necessária permissão para Banir utilizadores para "
                   "executar esta ação!`")
    DELETED_ACCOUNT = "Conta excluída"
    CANNOT_BAN_SELF = "`Não posso banir-me a mim próprio!`"
    CANNOT_BAN_ADMIN = "`Não posso banir este admin`"
    BAN_SUCCESS_REMOTE = "{} foi banido de **{}**"
    BAN_SUCCESS = "{} foi banido!"
    BAN_FAILED = "`Falha ao banir esta pessoa!`"
    CANNOT_UNBAN_SELF = "`Não posso desbanir-me a mim próprio`"
    UNBAN_SUCCESS_REMOTE = "{} foi desbanido de **{}**"
    UNBAN_SUCCESS = "{} foi desbanido!"
    UNBAN_FAILED = "`Falha ao desbanir esta pessoa!`"
    CANNOT_KICK_SELF = "`Não me posso kickar a mim mesmo`"
    KICK_SUCCESS_REMOTE = "{} foi kickado de **{}**"
    KICK_SUCCESS = "{} foi kickado!"
    KICK_FAILED = "`Falha ao kickar esta pessoa!`"
    PERSON_ANONYMOUS = "Este utilizador é anónimo"
    CANNOT_PROMOTE_CHANNEL = "Não consigo promover um canal!"
    NO_ONE_TO_PROMOTE = "`Não há ninguém para promover!`"
    NOT_USER = "`O Username ou ID dado não é um utilizador!`"
    CANNOT_PROMOTE_SELF = "`Não me posso promover a mim próprio!`"
    ADMIN_ALREADY_SELF = "`Já sou imortal!`"
    ADMIN_ALREADY = "`Esta pessoa já é imortal!`"
    ADMIN_NOT_ENOUGH_PERMS = ("`Não tenho direitos de administração "
                              "suficientes para promover esta pessoa!`")
    ADD_ADMINS_REQUIRED = ("`Permissão para adicionar administradores é "
                           "requerida.`")
    PROMOTE_SUCCESS = "{} foi promovido com poderes imortais!"
    TOO_MANY_ADMINS = "`Este chat já tem muitos administradores`"
    EMOJI_NOT_ALLOWED = ("`Não são permitidos emojis nos títulos de "
                         "administradores`")
    GET_ENTITY_FAILED = "Falha ao obter identidade."
    PROMOTE_FAILED = "`Falha ao promover esta pessoa.`"
    CANNOT_DEMOTE_CHANNEL = "Não consigo despromover um canal!"
    NO_ONE_TO_DEMOTE = "`Não há ninguém para despromover`"
    CANNOT_DEMOTE_SELF = "`Não posso despromover-me a mim próprio!`"
    DEMOTED_ALREADY = "`Esta pessoa já é um mortal.`"
    DEMOTE_SUCCESS = "{} foi despromovido!"
    CANNOT_DEMOTE_ADMIN = "`Este chat já tem muitos administradores`"
    DEMOTE_FAILED = "`Falha ao despromover esta pessoa.`"
    NO_GROUP_ARGS = "`Este chat, ou o chat fornecido, não é um grupo!`"
    NOT_MUTE_SUB_CHAN = "`Impossível silenciar subscritores de um canal!`"
    CANNOT_MUTE_SELF = "`Não consigo silenciar-me a mim próprio`"
    MUTE_SUCCESS_REMOTE = "{} foi silenciado em **{}**"
    MUTE_SUCCESS = "{} foi silenciado"
    MUTE_FAILED = "`Falha ao silenciar esta pessoa`"
    NOT_UNMUTE_SUB_CHAN = "`Falha na remoção do silenciamento desta pessoa.`"
    CANNOT_UNMUTE_SELF = "`Não posso remover o meu próprio silenciamento`"
    UNMUTE_SUCCESS_REMOTE = "Foi removido o silenciamento de {} em **{}**"
    UNMUTE_SUCCESS = "Removido o silenciamento de {}"
    INVALID_ID = "`Invalid ID given`"  # translation needed
    INVALID_USERNAME = "`Invalid username or link given`"  # translation needed
    UNMUTE_FAILED = "`Falha ao remover o silenciamento desta pessoa.`"
    TRY_DEL_ACCOUNTS = "`Tentando remover contas excluídas...`"
    DEL_ACCS_COUNT = "`Foram encontradas {} contas excluídas`"
    # translation needed
    DEL_ACCS_COUNT_REMOTE = "`{} deleted accounts found in {}`"
    REM_DEL_ACCS_COUNT = "`Removidas {} contas excluídas`"
    # translation needed
    REM_DEL_ACCS_COUNT_REMOTE = "`Removed {} deleted accounts in {}`"
    REM_DEL_ACCS_COUNT_EXCP = ("`Não foi possivel remover {} contas "
                               "(de admin) excluídas`")
    NO_DEL_ACCOUNTS = "`Não existem contas excluídas neste chat.`"
    # translation needed
    NO_DEL_ACCOUNTS_REMOTE = "`No deleted accounts found in {}`"


class SystemToolsText(object):
    UBOT = "Projeto Userbot: "
    SYSTEM_STATUS = "Estado do sistema"
    VER_TEXT = "Versão: "
    USR_TEXT = "Utilizador: "
    SAFEMODE = "Modo seguro: "
    ON = "Ligado"
    OFF = "Desligado"
    LANG = "Idioma: "
    RTT = "RTT: "
    TELETON_VER = "Versão do Telethon: "
    PYTHON_VER = "Versão do Python: "
    GITAPI_VER = "Versão do GitHub API: "
    CASAPI_VER = "Versão do CAS API: "
    COMMIT_NUM = "Revisão: "
    ERROR = "ERRO!"
    DAYS = "dias"
    BOT_UPTIMETXT = "Uptime do bot: "
    MAC_UPTIMETXT = "Uptime do servidor: "
    SHUTDOWN = "`A desligar...`"
    SHUTDOWN_LOG = "O bot está a desligar por pedido do utilizador"
    SYSD_GATHER_INFO = "`A obter informação de sistema...`"
    SYSD_NEOFETCH_REQ = ("`O pacote neofetch é necessário para apresentar "
                         "informações do sistema!`")
    RESTART = "`A reiniciar...`"
    # translation needed
    RESTART_UNSUPPORTED = ("`Reboot isn't supported on Windows but heads "
                           "up! Ctrl+C still does the job`")
    RESTART_LOG = "O Userbot está a reiniciar!"
    RESTARTED = "Reinicio completo!"
    GENERAL = "General"  # translation needed
    STORAGE = "Armazenamento"
    STORAGE_TOTAL = "Total"
    STORAGE_USED = "Usado"
    STORAGE_FREE = "Livre"
    USED_BY_HYPERUBOT = "Used by HyperUBot"  # translation needed
    STORAGE_SYSTEM = "Módulos de sistema"
    STORAGE_USER = "Módulos de utilizador"
    STORAGE_USERDATA = "User data"  # translation needed
    STORAGE_TEMP_DL = "Temporary downloads"  # translation needed
    STORAGE_HDD = "HDD"
    UPLD_LOG = "`A fazer upload do log...`"
    SUCCESS_UPLD_LOG = "`O Log do HyperUBot foi enviado com sucesso!`"
    FAILED_UPLD_LOG = "`Falha ao realizar upload do log`"


class DeletionsText(object):
    CANNOT_DEL_MSG = "`Não posso apagar esta mensagem`"
    DEL_MSG_FAILED = "`Falha ao apahar esta mensagem`"
    REPLY_DEL_MSG = "`Responde à mensagem de alguém para a apagar`"
    NO_ADMIN_PURGE = ("`São necessários privilégios de administração "
                      "para apagar mensagens`")
    NO_DEL_PRIV = ("`Permissão para apagar mensagens é necessária para "
                   "apagar mensagens`")
    PURGE_MSG_FAILED = "`Falha ao apagar mensagem(s)`"
    PURGE_COMPLETE = "Apagar em massa completo! Foram apagadas `{}` mensagens!"
    LOG_PURGE = "Apagadas `{}` mensagens"
    REPLY_PURGE_MSG = ("`Responde a uma mensagem para começar a apagar "
                       "em massa.`")


class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analisando o chat...`"
    EXCEPTION = "`Um erro inesperado ocorreu`"
    REPLY_NOT_CHANNEL = "`Esta mensagem não é um canal`"
    CANNOT_GET_CHATINFO = "`Não consigo obter informação de '{}'!`"
    YES_BOLD = "<b>Sim</b>"
    NO_BOLD = "<b>Não</b>"
    YES = "Sim"
    NO = "Não"
    DELETED_ACCOUNT = "Conta Excluída"
    CHATINFO = "<b>Info do chat</b>\n\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHANNEL = "Canal"
    GROUP = "Grupo"
    CHAT_TYPE = "Tipo de chat: {} ({})\n"
    CHAT_NAME = "Nome do chat: {}\n"
    FORMER_NAME = "Nome anterior: {}\n"
    CHAT_PUBLIC = "Publico"
    CHAT_PRIVATE = "Privado"
    GROUP_TYPE = "Tipo de grupo"
    GROUP_TYPE_GIGAGROUP = "Grupo de Broadcast"
    GROUP_TYPE_SUPERGROUP = "Supergrupo"
    GROUP_TYPE_NORMAL = "Normal"
    OWNER = "Criador: {}\n"
    OWNER_WITH_URL = "Criador: <a href=\"tg://user?id={}\">{}</a>\n"
    CREATED_NOT_NULL = "Criado em: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Criado em: <code>{} - {} {}</code> {}\n"
    DCID = "ID do Data Center: {}\n"
    VIEWABLE_MSG = "Mensagens visíveis: <code>{}</code>\n"
    DELETED_MSG = "Mensagens apagadas: <code>{}</code>\n"
    SENT_MSG = "Mensagens enviadas: <code>{}</code>\n"
    SENT_MSG_PRED = "Mensagens enviadas: <code>{}</code> {}\n"
    MEMBERS = "Membros: <code>{}</code>\n"
    ADMINS = "Administradores: <code>{}</code>\n"
    BOT_COUNT = "Bots: <code>{}</code>\n"
    ONLINE_MEM = "Online: <code>{}</code>\n"
    RESTRICTED_COUNT = "Utilizadores restritos: <code>{}</code>\n"
    BANNEDCOUNT = "Utilizadores banidos: <code>{}</code>\n"
    GRUP_STICKERS = ("Stickers do chat: "
                     "<a href=\"t.me/addstickers/{}\">{}</a>\n")
    LINKED_CHAT = "Chat ligado: {}\n"
    LINKED_CHAT_TITLE = "> Nome: {}\n"
    SLW_MODE = "Modo lento: {}"
    SLW_MODE_TIME = ", <code>{}s</code>\n\n"
    RESTR = "Restrito: {}\n"
    PFORM = "> Plataforma: {}\n"
    REASON = "> Razão: {}\n"
    TEXT = "> Texto: {}\n\n"
    SCAM = "Burla: <b>Yes</b>\n\n"
    VERFIED = "Verificado pelo Telegram: {}\n\n"
    DESCRIPTION = "Descrição: \n<code>{}</code>\n"
    UNKNOWN = "Desconhecido"
    INVALID_CH_GRP = "Canal ou Grupo inválido!"
    PRV_BAN = "Este canal/grupo é privado, ou então estou banido de lá."
    NOT_EXISTS = "Este canal ou supergrupo não existe!"
    CID_TEXT = "O ID deste chat é `{}`"
    CID_NO_GROUP = "`Este chat não é um canal ou grupo!`"
    LINK_INVALID_ID = "`O ID ou Link fornecido é inválido!`"
    LINK_INVALID_ID_GROUP = "`O ID ou Link fornecido não é de um grupo`"
    LINK_TEXT = "Aqui está o Link para convidar, do chat **{}**"
    NO_LINK = "`Este chat não tem Link para convite`"
    NO_ADMIN_PERM = ("`Privilégios de Administração são necessários para "
                     "executar esta ação`")
    NO_INVITE_PERM = "`É necessária permissão para adicionar utilizadores!`"
    UNABLE_GET_LINK = "`Falha ao obter o Link de convite deste chat!`"


class MemberInfoText(object):
    SCAN = "`A examinar a informação deste membro...`"
    FAIL_GET_MEMBER_CHAT = ("`Falha ao obter informação sobre o membro: "
                            "impossível encontrar o chat!`")
    FAIL_GET_MEMBER = "`Falha ao obter informação sobre o membro!`"
    NOT_SUPERGROUP = "`Este chat, ou o ID fornecido, não é um Supergrupo!`"
    INVALID_CHAT_ID = "`ID de Chat inválido!`"
    ME_NOT_PART = "`Não sou um integrante de {}`"
    USER_NOT_PART = "`Este utilizador não é um integrante de {}`"
    FAIL_GET_PART = "`Falha ao obter informação do integrante`"
    DELETED_ACCOUNT = "Conta Excluída"
    TIME_FOREVER = "Para sempre"
    ME_NOT_MEMBER = "`Não sou um membro de {}`"
    USER_NOT_MEMBER = "`Este utilizador não é um membro de {}`"
    MEMBERINFO = "Info do membro"
    GENERAL = "Geral"
    MINFO_ID = "ID"
    FIRST_NAME = "Primeiro nome"
    USERNAME = "Nome de utilizador"
    GROUP = "Grupo"
    GROUP_NAME = "Nome"
    STATUS = "Estado"
    STATUS_OWNER = "Dono"
    STATUS_ADMIN = "Admin"
    STATUS_MEMBER = "Membro"
    STATUS_BANNED = "Banido"
    STATUS_MUTED = "Silenciado"
    STATUS_RESTRICTED = "Limitado"
    STATUS_MUTED_NOT_MEMBER = "Não é membro, mas está silenciado"
    STATUS_RESTRICTED_NOT_MEMBER = "Não é membro, mas está limitado"
    STATUS_BANNED_UNTIL = "Banido até"
    STATUS_MUTED_UNTIL = "Silenciado até"
    STATUS_RESTRICTED_UNTIL = "Limitado até"
    STATUS_BANNED_BY = "Banido por"
    STATUS_MUTED_BY = "Silenciado por"
    STATUS_RESTRICTED_BY = "Limitado por"
    ADMIN_TITLE = "Título"
    PERMISSIONS = "Permissões"
    CHANGE_GROUP_INFO = "Mudar info do grupo"
    DELETE_MESSAGES = "Apagar mensagens"
    BAN_USERS = "Banir utilizadores"
    INVITE_USERS = "Adicionar/convidar utilizadores"
    PIN_MESSAGES = "Fixar mensagens"
    ADD_ADMINS = "Adicionar administradores"
    ANONYMOUS = "Enviar anonimamente"
    MANAGE_CALLS = "Gerir mensagens de voz"
    ROOT_RIGHTS = "Permissões root"
    SEND_MESSAGES = "Enviar mensagens"
    SEND_MEDIA = "Enviar média"
    SEND_GIFS_STICKERS = "Enviar stickers e GIFs"
    SEND_POLLS = "Criar votações"
    EMBED_LINKS = "Links Embebidos"
    WARN_ADMIN_PRIV = ("Privilégios de admin são necessários para aceder a "
                       "permissões não convêncionais")
    PROMOTED_BY = "Promovido por"
    ADDED_BY = "Adicionado por"
    JOIN_DATE = "Data de entrada"


class MessagesText(object):
    NO_ADMIN = ("`Privilégios de administrador são necessários para "
                "executar esta ação`")
    FAIL_CHAT = "`Falha ao obter o chat.`"
    CANNOT_COUNT_DEL = "`Não posso contar mensagens de uma conta excluída`"
    CANNOT_QUERY_FWD = ("`Não posso fazer query de mensagens encaminhadas "
                        "por um canal!`")
    FAIL_COUNT_MSG = ("`Não posso fazer query de mensagens encaminhadas "
                      "por um canal!`")
    USER_HAS_SENT = "{} enviou `{}` mensagens neste chat!"
    USER_HAS_SENT_REMOTE = "{} enviou `{}` messagens em **{}**"
    CANNOT_COUNT_MSG = "`Não consigo contar mensagens neste chat`"
    CANNOT_COUNT_MSG_REMOTE = "`Não consigo contar mensagens em {}!`"
    PIN_REPLY_TO_MSG = "`Responde a uma mensagem para a fixar.`"
    PIN_SUCCESS = "`Mensagem fixada com sucesso.`"
    PIN_FAILED = "`Falha ao fixar a mensagem!`"
    LOG_PIN_MSG_ID = "ID da Mensagem"
    UNPIN_REPLY_TO_MSG = ("`Responde a uma mensagem para desafixar ou "
                          "usa \".unpin all\" para desafixar todas "
                          "as mensagens`")
    UNPIN_ALL_SUCCESS = "`Todas as mensagens desafixadas com sucesso`"
    UNPIN_SUCCESS = "`Mensagem desafixada com sucesso`"
    UNPIN_FAILED = "`Falha ao desafixar a mensagem`"
    LOG_UNPIN_ALL_TEXT = "Todas as mensagens desafixadas"


class ScrappersText(object):
    NO_TEXT_OR_MSG = "`Sem texto ou mensagem para traduzir!`"
    TRANSLATING = "`A traduzir...`"
    SAME_SRC_TARGET_LANG = ("`Linguagem de destino é igual à linguagem "
                            "de fonte.`")
    DETECTED_LANG = "Linguagem detetada"
    TARGET_LANG = "Linguagem de destino"
    ORG_TEXT = "Texto original"
    TRANS_TEXT = "Texto traduzido"
    MSG_TOO_LONG = "`Texto traduzido é demasiado grande!`"
    FAIL_TRANS_MSG = "`Falha ao traduzir esta mensagem!`"
    FAIL_TRANS_TEXT = "`Falha ao traduzir o texto fornecido!`"
    MEDIA_FORBIDDEN = ("`Impossível executar TTS: O upload de média "
                       "neste chat é proíbido!`")
    NO_TEXT_TTS = "`Sem texto ou mensagem para executar TTS`"
    FAIL_TTS = "`Falha ao realizar TTS`"
    FAIL_API_REQ = "`Requerimento à API falhou!`"
    INVALID_LANG_CODE = ("`Código de linguagem inválido, ou a linguagem "
                         "não é suportada!`")
    NOT_EGH_ARGS = "`Não foram fornecidos argumentos suficientes!`"
    INVALID_AMOUNT_FORMAT = "`Formato de quantidade inválido!`"
    CC_ISO_UNSUPPORTED = "`'{}' não é um código de Moeda ISO suportado!`"
    CC_HEADER = "Conversor de Moeda"
    CFROM_CTO = "**{}** para **{}**"
    INVALID_INPUT = "Input inválido"
    UNABLE_TO_CC = "`Falha ao converter Moeda`"
    CC_LAST_UPDATE = "Última atualização"
    REPLY_TO_VM = "`Responde a uma mensagem de voz!`"
    WORKS_WITH_VM_ONLY = "`Só funciona com mensagens de voz!`"
    CONVERT_STT = "`A converter voz em texto...`"
    FAILED_LOAD_AUDIO = "`Falha ao carregar aúdio`"
    STT = "Speech-to-text"
    STT_TEXT = "Texto"
    STT_NOT_RECOGNIZED = ("`Não foi possível reconhecer texto da "
                          "mensagem por voz enviada`")
    STT_REQ_FAILED = "Resultado do pedido inválido!"
    STT_OUTPUT_TOO_LONG = "`O output do Speech-to-text é demasiado longo!`"
    UNABLE_TO_STT = "`Impossível realizar speech-to-text`"
    SCRLANG = ("A linguagem do módulo de Scrappers do HyperUBot está "
               "definida para: `{}`")
    MULT_ARGS = "`Por favor, use apenas um argumento!`"
    INV_CT_CODE = ("Valor inválido! Use um dos seguintes códigos de duas "
                   "letras diponíveis!\n\nCódigos disponíveis:\n{}")
    SUCCESS_LANG_CHANGE = "Linguagem definida com sucesso para: `{}`"


class UserText(object):
    # translation needed
    CANNOT_LEAVE = "`This chat doesn't seem to be a group or channel`"
    LEAVING = "`A abandonar chat...`"
    STATS_PROCESSING = "`A calcular estatísticas...`"
    STATS_HEADER = "Minhas estatísticas do Telegram"
    STATS_USERS = "Conversas privadas com **{}** pessoas"
    STATS_BLOCKED = "Bloqueadas **{}** destas"
    STATS_BOTS = "Iniciei conversa com **{}** bots"
    STATS_BLOCKED_TOTAL = "Bloquados **{}** bots/pessoas no geral."
    STATS_GROUPS = "Participante em **{}** grupos"
    STATS_SGC_OWNER = "Dono de **{}** deles"
    STATS_GROUPS_ADMIN = "Admin em **{}** grupos"
    STATS_SUPER_GROUPS = "Participant em **{}** supergrupos"
    STATS_SG_ADMIN = "Admin em **{}** supergrupos"
    STATS_CHANNELS = "Subscrito em **{}** canais"
    STATS_CHAN_ADMIN = "Admin em **{}** canais"
    STATS_UNKNOWN = "**{}** conversas desconhecidas"
    STATS_TOTAL = "Total de chats"
    FETCH_INFO = "`Adquirindo informação do utilizador...`"
    FAILED_FETCH_INFO = "`Falha ao adquirir informações!`"
    UNKNOWN = "Desconhecido"
    DELETED_ACCOUNT = "Conta excluída"
    YES = "Sim"
    NO = "Não"
    USR_NO_BIO = "Este utilizador não tem bio"
    USR_INFO = "Info do user"
    FIRST_NAME = "Primeiro nome"
    LAST_NAME = "Último nome"
    USERNAME = "Nome de utilizador"
    DCID = "ID do Data Center"
    PROF_PIC_COUNT = "Número de fotos de perfil"
    PROF_LINK = "Link permanente para o perfil"
    ISBOT = "Bot"
    SCAMMER = "Conta Falsa"
    ISRESTRICTED = "Limitado"
    ISVERIFIED = "Verificado pelo Telegram"
    USR_ID = "ID"
    BIO = "Bio"
    COMMON_SELF = "Chats comuns... ah sou eu..."
    COMMON = "Chats comuns"
    UNABLE_GET_IDS = "`Impossível obter o ID de utilizador desta mensagem`"
    ORIGINAL_AUTHOR = "Autor original"
    FORWARDER = "Encaminhador"
    DUAL_HAS_ID_OF = "{} tem um ID de `{}`"
    MY_ID = "O meu ID é `{}`"
    DEL_HAS_ID_OF = "A Conta Excluída tem um ID de `{}`"
    ID_NOT_ACCESSIBLE = "o ID de {} não é acessível"
    ORG_HAS_ID_OF = "O autor original {} tem um ID de `{}`"


class SystemUtilitiesText(object):
    CMD_STOPPED = "{} parou!"


class GeneralMessages(object):
    ERROR = "ERRO!"
    CHAT_NOT_USER = "`Canais não são objetos User`"
    FAIL_FETCH_USER = "`Falha ao adquirir informação do utilizador`"
    ENTITY_NOT_USER = "`A entidade não é um objeto User`"
    PERSON_ANONYMOUS = "A pessoa é anónima"
    CANT_FETCH_REQ_AS_USER = ("`Não foi possivel adquirir informação "
                              "sobre '{}', considerando que seja "
                              "um utilizador`")
    LOG_USER = "Utilizador"
    LOG_USERNAME = "Nome de utilizador"
    LOG_USER_ID = "ID de utilizador"
    LOG_CHAT_TITLE = "Título do Chat"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "ID do Chat"
    UNKNOWN = "Desconhecido"


class ModulesUtilsText(object):
    INVALID_ARG = "`Argumento \"{}\" inválido!`"
    USAGE = "Utilização"
    AVAILABLE_MODULES = "Módulos disponíveis"
    DISABLED_MODULES = "Módulos desativados"
    NAME_MODULE = "**Módulo {}**"
    MISSING_NUMBER_MODULE = "`Falta o número do módulo`"
    MODULE_NOT_AVAILABLE = "`Módulo número \"{}\" não encontrado!`"
    MODULE_NO_DESC = "__Descrição não disponível__"
    MODULE_NO_USAGE = "__Utilização não disponível__"
    ASTERISK = "Módulo de user desinstalável"
    NOT_RUNNING_INFO = "Não carregada"
    UNKNOWN = "Desconhecido"
    SYSTEM = "Sistema"
    SYSTEM_MODULES = "Módulos de sistema"
    USER = "Utilizador"
    USER_MODULES = "Módulos de utilizador"
    PKG_NAME = "Nome do pacote"
    MODULE_TYPE = "Tipo de módulo"
    AUTHORS = "Autor(es)"
    VERSION = "Versão"
    SIZE = "Tamanho"
    INSTALL_DATE = "Data de instalação"
    LISTCMDS_TITLE = "Comandos disponíveis"
    LISTCMDS_USAGE = ("Usa '{} <nome do comando>' para obter mais "
                      "informação sobre o comando")
    ARGS_NOT_REQ = "sem argumentos obrigatórios"
    ARGS_NOT_AVAILABLE = "sem argumentos"
    CMD_NOT_FOUND = "O comando '{}' não foi encontrado!"
    MOD_HELP = "Need help? Type {}"  # translation needed
    MOD_UTILS = "Módulos"


class WebToolsText(object):
    PING_SPEED = "Round-Trip Time: "
    DCMESSAGE = ("País : `{}`\n"
                 "Este Datacenter : `{}`\n"
                 "Datacenter mais próximo : `{}`")
    BAD_ARGS = "`Maus argumentos`"
    INVALID_HOST = "`Ocorreu um problema a interpretar o IP/Hostname`"
    PINGER_VAL = "DNS: `{}`\nVelocidade de ping: `{}`"
    SPD_TEST_SELECT_SERVER = "Escolhendo o melhor servidor"
    SPD_TEST_DOWNLOAD = "Testando velocidade de download"
    SPD_TEST_UPLOAD = "Testando velocidade de upload"
    SPD_PROCESSING = "Processando"
    SPD_FAILED = "Falha no teste de velocidade"
    SPD_NO_RESULT = "Sem resultados"
    SPD_NO_MEMORY = "Sem memória"
    SPD_FAIL_SEND_RESULT = "`Falha ao enviar o resultado do Speedtest`"
    SPD_MEGABITS = "Mbit/s"
    SPD_MEGABYTES = "MB/s"
    SPD_TIME = "Tempo"
    SPD_DOWNLOAD = "Velocidade de Download"
    SPD_UPLOAD = "Velocidade de Upload"
    SPD_PING = "Ping"
    SPD_ISP = "A minha ISP"
    SPD_HOSTED_BY = "Hospedado por"


class CasIntText(object):
    TOO_MANY_CAS = ("`Muitos utilizadores banidos no CAS. A fazer upload "
                    "da lista como ficheiro...`")
    FAIL_UPLOAD_LIST = "`Falha ao efetuar upload da lista`"
    SEND_MEDIA_FORBIDDEN = "`O envio de média neste chat não é permitido`"
    UPDATER_CONNECTING = "`Conectando ao servidor CAS...`"
    UPDATER_DOWNLOADING = "`A fazer Download da última informação CAS...`"
    FAIL_APPEND_CAS = "`Falha ao adicionar dados do CAS`"
    UPDATE_SUCCESS = "`Atualizado o CSV dos dados do CAS`"
    NO_CONNECTION = "`Falha na conecção com o servidor do CAS`"
    TIMEOUT = ("`Impossivel atualizar o CSV dado que o tempo de ligação "
               "excedeu o limite`")
    UPDATE_FAILED = "`Falha ao atualizar os dados do CSV do CAS`"
    GIVEN_ENT_INVALID = "`O ID, nome ou link dado é inváldio`"
    CAS_CHECK_FAIL_ND = ("`Verificação CAS falhou, visto que o CSV tem um "
                         "formato inválido`")
    CAS_CHECK_ND = ("`Dados CAS não encontrados. Por favor usa o comando "
                    ".casupdate para obter os últimos dados CAS`")
    CHECK_USER = "Verificando o estado CAS de {}..."
    CHECK_CHAT = "À procura de utilizadores banidos por CAS..."
    CHECK_USER_ID = "A verificar o estado CAS do ID `{}`..."
    DELETED_ACCOUNT = "Conta Excluída"
    USER_HEADER = "Dados do user"
    USER_ID = "ID"
    FIRST_NAME = "Primeiro nome"
    LAST_NAME = "Último nome"
    USERNAME = "Nome de utilizador"
    CAS_DATA = "Dados do CAS"
    RESULT = "Resultado"
    OFFENSES = "Total de Ofensas"
    BANNED = "Banido"
    BANNED_SINCE = "Banido desde"
    NOT_BANNED = "Não banido"
    USER_DETECTED = "Aviso! `{}` membro está banido no CAS em **{}**"
    USERS_DETECTED = "Aviso! `{}` membros estão banidos no CAS em **{}**"
    NO_USERS = "Nenhum utilizador banido no CAS encontrado em **{}**"
    NO_ADMIN = ("`São necessários privilégios de administração para "
                "realizar esta ação`")
    CAS_CHECK_FAIL = "`Verificação CAS falhou`"


class GitHubText(object):
    INVALID_URL = "Combinação user/repo inválida"
    NO_RELEASE = "A release especificada não foi encontrada"
    AUTHOR_STR = "<b>Autor:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Nome da Release:</b> "
    ASSET = "<b>Recurso:</b> \n"
    SIZE = "Tamanho: "
    DL_COUNT = "\nNúmero de Downloads: "
    INVALID_ARGS = ("Argumentos inválidos! Certifica-te de que estás a "
                    "introduzir uma combinação user/repo válida!")


class TerminalText(object):
    BASH_ERROR = ("Ocorreu um erro generalizado. Geralmente acontece por "
                  "teres utilizado argumentos inválidos ou um comando "
                  "não existente.")
    BASH_CRT_FILE_FAILED_RO = ("Falha ao criar um ficheiro de output "
                               "shell. Será um sistema read-only?")
    BASH_CRT_FILE_FAILED = "Falha ao criar um ficheiro de output shell."
    BASH_SEND_FILE_MTLO = ("Não posso enviar o ficheiro de output shell, "
                           "porque o envio de média está restrito neste chat")
    BASH_SEND_FILE_FAILED = "Impossível enviar ficheiro de output shell."


class MiscText(object):
    COIN_LANDED_VAL = "A moeda caiu em: "
    THRWING_COIN = "`A lançar a moeda...`"
    HEADS = "Caras"
    TAILS = "Coroas"
    RAND_INVLD_ARGS = ("`Argumentos inválidos, certifica-te que tens "
                       "exatamente 2 números`")
    FRST_LIMIT_INVALID = "`O primeiro valor não é um número válido`"
    SCND_LIMIT_INVALID = "`O segundo valor não é um número válido`"
    RAND_NUM_GEN = "O número gerado entre `{}` e `{}`: **`{}`**"


class PackageManagerText(object):  # translation needed
    REPO_LIST_EMPTY = ("List of repositories is empty! Use "
                       "`.pkg update <owner/repo>` to add a new repository "
                       "or add them to your COMMUNITY_REPOS config")
    PACKAGES_UPDATER = "Packages updater"
    INVALID_REPO_URL = "Invalid repo URL format"
    UPDATING = "Updating {}..."
    UPDATE_SUCCESS = "Got latest data from {}"
    UPDATE_FAILED = "Failed to fetch {}"
    UPDATER_FINISHED = "Updater finished"
    LIST_OF_PACKAGES = "List of packages"
    INSTALLED_MODULES = "Installed modules"
    NO_MODULES_INSTALLED = "No user modules installed"
    MODULES_IN = "Modules in {}"
    AUTHOR = "Author"
    VERSION = "Version"
    REPO_NO_MODULES = "This repository has no modules"
    REPOS_NO_DATA = "No repository data. You may need to use {}"
    INSTALLED_UPGRADEABLE = "Installed and upgradeable"
    INSTALLED_NOTLOADED = "Installed but not loaded"
    START_FAILED = "Failed to start"
    DISABLED = "Disabled"
    EQUAL_NAME = "Equal name"
    NEVER = "Never"
    LAST_UPDATED = "Last updated"
    REBOOT_INFO = "Please reboot HyperUBot now to apply the recent changes"
    REBOOT = "Rebooting..."
    REBOOT_DONE = "Reboot complete!"
    INSTALL_EMPTY = "No module names given to install"
    PACKAGE_INSTALLER = "Package installer"
    NO_REPO_URL = "No repo URL given to install from!"
    INSTALL_EMPTY_REPO = "No module names given to install from specific repo!"
    UNKNOWN_REPO_URL = "Unknown repo URL given!"
    UNKNOWN_MODULES = "Unknown module(s)"
    DOWNLOADING = "Downloading {}..."
    DOWN_FAILED = "Failed to download {}"
    INSTALL_SUCCESS = "Installed {}"
    UPDATE_DATA_FAIL = "Failed to update data for {}"
    NO_INSTALL_QUEUED = "No installation queued"
    INSTALLER_FINISHED = "Installer finished"
    UNINSTALL_EMPTY = "No module names given to uninstall"
    PACKAGE_UNINSTALLER = "Package uninstaller"
    UNINSTALL_FAILED = "Failed to uninstall {}"
    UNINSTALL_SUCCESS = "Uninstalled {}"
    UNINSTALL_DATA = "Uninstalled {} but failed to remove data"
    MODULE_NOT_INSTALL = "{} not installed"
    UNINSTALLER_FINISHED = "Uninstaller finished"
    NO_REPO_NAMES = "No repo names given to remove"
    NO_REPO_REMOVE = "No repositories to remove"
    REPO_REMOVER = "Repo remover"
    CANNOT_REMOVE_REPO = "Can't remove {} (protected)"
    REMOVING = "Removing {}..."
    REMOVE_SUCCESS = "{} has been removed"
    REMOVE_FAILED = "Failed to remove {}"
    UNKNOWN_REPO = "Unknown repo"
    REMOVER_FINISHED = "Remover finished"
    LOAD_PGKS = "Loading package lists..."
    CANNOT_INSTALL_MODULES = "Can't install user modules in safe mode"
    PACKAGE_MANAGER = "Package Manager"
    UNKNOWN_OPTION = "Unknown option '{}'"
    NO_OPTION = "No option given"
    PKG_HELP = "Need help? Type {}"
    TEXT_TOO_LONG = ("The list is too long to display it here. The list is "
                     "printed in your bot's terminal")


class UpdaterText(object):
    CHECKING_UPDATES = "Verificando updates..."
    # translation needed
    GIT_REPO = "HyperUBot's directory is a local git repository"
    DOWNLOADING_RELEASE = "A fazer download da última release..."
    UPDATE_FAILED = "Atualização falhou"
    UPDATE_INTERNAL_FAILED = "Erro interno!"
    START_RECOVERY_FAILED = "Falha ao iniciar o modo recovery"
    ALREADY_UP_TO_DATE = "O HyperUBot já se encontra atualizado"
    LATEST = "Versão mais recente"
    CURRENT = "Versão Atual"
    UPDATE_AVAILABLE = "Atualização disponível"
    RELEASE_DATE = "Release date"  # translation needed
    CHANGELOG_AT = "Changelog em {}"
    DOWNLOAD_SUCCESS = ("Download completo. A desligar o bot para instalar "
                        "o pacote de atualizações...")
    DOWNLOAD_SUCCESS_WIN = ("Download successful and ready. Please "
                            "shutdown the bot and follow the instructions "
                            "in your terminal to apply the update package "
                            "manually")  # translation needed
    UPDATE_QUEUED = ("Usa `.update upgrade` para fazer download e "
                     "instalar o pacote de atualizações agora.")
    # translation needed
    UPDATE_SUCESS = "HyperUBot updated to {} successfully!"
    UPDATE_FAIL = "Failed to update HyperUBot to {}"  # translation needed


class SideloaderText(object):
    NOT_PY_FILE = ("Este não é um ficheiro .py válido. Não é possível "
                   "fazer sideload")
    DLOADING = "`A fazer download...`"
    MODULE_EXISTS = ("Já existe um módulo de utilizador chamado `{}`. "
                     "Se desejares prosseguir assim mesmo, por favor "
                     "executa o comando com o argumento `force` !")
    SUCCESS = "Instalado `{}` com sucesso! A reiniciar..."
    LOG = "O módulo `{}` foi carregado sideload com sucesso!"
    # translation needed
    REBOOT_WIN = "Please reboot HyperUBot now to load the sideloaded module"
    RBT_CPLT = "Reinicio completo!"
    INVALID_FILE = "Por favor responde a um ficheiro válido!"


class FeatureMgrText(object):  # translation needed
    DISABLE_FTR = "Name a command or feature to disable it!"
    DISABLE_FTR_FAIL = "Seems like I can't disable this command or feature"
    DISABLE_FTR_SUCCESS = "Command or feature '`{}`' has been disabled"
    ENABLE_FTR = "Name a command or feature to enable it!"
    ENABLE_FTR_FAIL = "Seems like I can't enable this command or feature"
    ENABLE_FTR_SUCCESS = "Command or feature '`{}`' has been enabled"


class WelcomeText(object):  # translation needed
    WELCOME_TO_HYPERUBOT = "Welcome to HyperUBot!"
    INFO = ("You made it to run HyperUBot on your machine successfully. So "
            "what's next? The following commands will help you to understand "
            "your new userbot better and what options, features etc. "
            "HyperUBot does offer for you")
    INFO_STATUS = ("get the current status of HyperUBot such as the "
                   "version, uptime etc. Useful to check if the bot is "
                   "actually online.")
    INFO_OR = "or"
    INFO_HELP = ("lists all available commands and features from all "
                 "modules to use. Pass the name of a command or feature "
                 "(e.g. {}) to get the usage of the specific command or "
                 "feature.")
    INFO_MODULES = ("lists all built-in and user modules at one place. "
                    "This command takes arguments to get further "
                    "information of a module such as the description "
                    "or usage.")
    INFO_PKG = ("our package manager allows you to install new modules. "
                "We made some user modules which can be downloaded with the "
                "help of this command to allow the user to get new modules "
                "without waiting for new updates for the bot. FIY there are "
                "also modules made by the community. So make sure to check "
                "them out too!")
    INFO_SUPPORT = ("Questions about HyperUBot? Feel free to chat with us "
                    "in our {}!")
    INFO_SUPPORT_LINK = "support group"
    INFO_FUN = "Have fun!"


# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = ("Um módulo para te ajudar a gerir um grupo teu ou de um "
                  "amigo mais facilmente. Inclui comandos comuns como: ban, "
                  "unban, promote etc.\n\n"
                  "Nota: muitos comandos deste módulo necessitam de "
                  "permissões de administrador para funcionarem "
                  "correctamente.")
    CHATINFO_DESC = ("Obtém a maior parte das informações de um canal, "
                     "grupo ou supergrupo como data de criação, número "
                     "de mensagens, mensagens apagadas, nome antigo, etc")
    DELETIONS_DESC = ("Este módulo permite apagar as tuas mensagens ou "
                      "mensagens de grupo rápido. Alguém fez spam no teu "
                      "grupo? Usa o comando .purge para apagar tudo!\n"
                      "Todos os comandos deste módulo requerem permissões de "
                      "admin para apagar as mensagens de outras pessoas\n\n"
                      "**Importante: não abuses deste módulo para apagares "
                      "o histórico de mensagens do grupo de outra pessoa**, "
                      "a sério, não o faças...")
    MEMBERINFO_DESC = ("Fornece informação sobre um participante no chat "
                       "como permissões, data de limitação, data de "
                       "entrada, etc.\n\n"
                       "Nota: necessita de permissões de administrador "
                       "para ver permissões de outros utilizadores.")
    MESSAGES_DESC = ("Este módulo inclui comandos que apenas funcionam "
                     "com mensagens, como msgs ou pin.")
    SCRAPPERS_DESC = ("Este módulo inclui ferramentas úteis, como o "
                      "tradutor ou o text-to-speech")
    SYSTOOLS_DESC = ("Este módulo contém um conjunto de ferramentas úteis "
                     "para o bot. Permite ver o uptime do bot, o uptime "
                     "do servidor, as versões de todos os componentes do "
                     "bot, as especificações do servidor do bot, e "
                     "contém alguns controlos de energia do bot.")
    USER_DESC = ("Contém ferramentas que fornecem informações sobre "
                 "utilizadores, e a ferramenta kickme.")
    WEBTOOLS_DESC = ("Este módulo contém quase, se não mesmo todas, as "
                     "ferramentas web do bot como ping, speedtest, "
                     "calculadora RTT, e um método para mostrar o "
                     "Datacenter atual.")
    CAS_INTERFACE_DESC = ("O interface para a API Combot Anti-Spam "
                          "System. Permite verificar apenas um utilizador, "
                          "ou procurar um grupo inteiro, por CAS bans, "
                          "através dos comandos.")
    GITHUB_DESC = ("Um módulo que usa a API do GitHub. Este módulo permite "
                   "ver releases de um repositório, de um utilizador do "
                   "GitHub.")
    TERMINAL_DESC = ("Este módulo permite executar diretamente comandos "
                     "shell, na máquina hospedeira.\n\n"
                     "**Atenção:** Executar comandos shell no bot pode e "
                     "vai modificar permanentemente o servidor! "
                     "**Más coisas podem acontecer se executares o bot "
                     "como root/sudo!**")
    MISC_DESC = ("O módulo Misc contém diversos comandos e ferramentas "
                 "que não serviam para incluir noutros módulos, mas "
                 "ao mesmo tempo eram demasiado simples para ter o seu "
                 "próprio módulo. Vê o help para mais detalhes.")
    PACKAGE_MANAGER_DESC = ("O módulo gestor de pacotes permite um "
                            "utilizador gerir aplicações extra, de "
                            "repositórios externos, tanto oficiais, "
                            "como o repositório modules-universe, "
                            "ou de fontes externas. Assim, permite aos "
                            "utilizadores personalizar o seu bot mais "
                            "do que o stock.")
    UPDATER_DESC = ("O módulo Updater permite ao utilizador verificar a "
                    "existencia de atualizações e, se existirem, "
                    "atualizar o bot.")
    SIDELOADER_DESC = ("O módulo sideloader permite carregar ficheiros "
                       "extra facilmente. Para o fazer, apenas tens de "
                       "enviar o comando .sideload como resposta a um "
                       "ficheiro .py\n\n"
                       "**INFORMAÇÃO**: Estes ficheiros têm de ser "
                       "escritos de maneira a funcionar com o bot. Ao "
                       "realizar um sideload de um ficheiro desconhecido, "
                       "o utilizador pode obter um 'soft-brick', tendo "
                       "que remover um módulo defeituoso do espaço de "
                       "utilizador.\n\n"
                       "**AVISO CRITICO**: Alguns ficheiros maliciosos "
                       "podem enviar a tua informação (geralmente a API "
                       "KEY e String Session, mas não está limitado a "
                       "estes itens) para hackers com propósitos "
                       "maliciosos! Faz apenas sideload de módulos que "
                       "confies na fonte!")
    # translation needed
    FEATURE_MGR_DESC = ("The Feature Manager module allows the user "
                        "to enable/disable a command or feature in "
                        "real time and no, the enable and disable "
                        "commands cannot be disabled.")


class ModuleUsages(object):
    # KEEP CORRECT DICT FORMAT!!
    # {"cmd": {"args": ARGUMENTS, "usage": USAGE}} edit ARGUMENTS and
    # USAGE only!
    ADMIN_USAGE = {"adminlist": {"args": "[opcional: <link/id>]",
                                 "usage": ("lista todos os admins de um "
                                           "canal ou grupo (remotamente). "
                                           "Necessita de permissões de "
                                           "administração")},
                   "ban": {"args": ("[opcional: <username/id> <chat "
                                    "(id ou link)>] ou resposta"),
                           "usage": ("Bane um utilizador de um chat "
                                     "(remotamente). Requer permissões de "
                                     "admin para banir")},
                   "unban": {"args": ("[opcional: <username/id> <chat "
                                      "(id ou link)>] ou resposta"),
                             "usage": ("Des-bane um utilizador de um "
                                       "chat (remotamente). Requer "
                                       "permissões de admin para banir.")},
                   "kick": {"args": ("[opcional: <username/id> <chat "
                                     "(id ou link)>] ou resposta"),
                            "usage": ("Dá kick um utilizador de um chat "
                                      "(remotamente). Requer permissões "
                                      "de admin para banir")},
                   "promote": {"args": ("[opcional: <username/id> e/ou "
                                        "<title>] ou resposta"),
                               "usage": ("Promove um utilizador com "
                                         "direitos imortais! Requer "
                                         "privilegios de administraçao com "
                                         "direitos de admin e uma segunda "
                                         "permissão de admin porque um "
                                         "promote nunca adiciona por "
                                         "defeito permissões de add admin. "
                                         "Comprimento do titulo tem "
                                         "de ser <= 16 caractéres.")},
                   "demote": {"args": "[opcional: <username/id>] ou resposta",
                              "usage": ("Despromove um utilizador. É "
                                        "necessária permissão de add "
                                        "admin. Apenas funciona com "
                                        "admins promovidos por ti.")},
                   "mute": {"args": ("[opcional: <username/id> <chat (id "
                                     "ou link)>] ou resposta"),
                            "usage": ("Silencia um utilizador de um chat "
                                      "(remotamente). Precisa de permissão "
                                      "de administrador com direito "
                                      "de banir.")},
                   "unmute": {"args": ("[opcional: <username/id> <chat "
                                       "(id ou link)>] ou resposta"),
                              "usage": ("Des-silencia um utilizador de "
                                        "um chat (remotamente). Precisa "
                                        "de permissão de administrador "
                                        "com direito de banir.")},
                   "delaccs": {"args": "[opcional: <chat id ou link>]",
                               "usage": ("Tenta remover contas excluídas "
                                         "de um chat. Precisa de "
                                         "permissão de administrador "
                                         "com direito de banir. Caso "
                                         "contrário, apenas reporta o "
                                         "número de contas excluídas.")}}

    CHATINFO_USAGE = {"chatinfo": {"args": ("[opcional: <chat_id/link>] ou "
                                            "resposta (se canal)"),
                                   "usage": ("Obtém informação de um chat. "
                                             "Alguma informação pode estar "
                                             "omissa por falta de "
                                             "permissões.")},
                      "chatid": {"args": None,
                                 "usage": "Obtém o ID do chat."},
                      "getlink": {"args": "[opcional: <chat_id/link>]",
                                  "usage": ("Obtém o link de convite "
                                            "partilhável do chat. "
                                            "Precisa de permissão de "
                                            "administrador com direito de "
                                            "convidar/adicionar "
                                            "utilizadores.")}}

    DELETIONS_USAGE = {"del": {"args": None,
                               "usage": "Apaga a mensagem respondida."},
                       "purge": {"args": None,
                                 "usage": ("Apaga todas as mensagens entre "
                                           "a última e a mensagem "
                                           "respondida. Precisa de "
                                           "permissão de administrador "
                                           "com direito de apagar "
                                           "mensagens são necessárias se "
                                           "estiveres em grupos ou canais.\n"
                                           "**Nota: por favor não abuses "
                                           "deste comando para apagares o "
                                           "histórico de mensagens de "
                                           "grupos inteiros de "
                                           "outras pessoas**")}}

    MEMBERINFO_USAGE = {"minfo": {"args": ("[opcional: <tag/id> <group>] "
                                           "ou resposta"),
                                  "usage": ("Obtém (remotamente) "
                                            "informações sobre um membro de "
                                            "um grupo.")}}

    MESSAGES_USAGE = {"msgs": {"args": ("[opcional: <username/id> <group>] "
                                        "ou resposta"),
                               "usage": ("Obtém o total de mensagens d "
                                         "eum utilizador (inclui "
                                         "qualquer mensagem, como texto, "
                                         "voz, imagens, videos, etc...).\n"
                                         "Funciona remotamente também")},
                      "pin": {"args": ("[argumento opcional \"loud\" para "
                                       "notificar todos os membros] ou "
                                       "resposta"),
                              "usage": ("Responde ao uma mensagem para "
                                        "fixares esta.")},
                      "unpin": {"args": ("[argumento opcional \"all\"] "
                                         "ou resposta"),
                                "usage": ("Responde a uma mensagem para "
                                          "desafixares ou "
                                          "usa \".unpin all\" para "
                                          "desafixar todas as mensagens "
                                          "no grupo")}}

    SCRAPPERS_USAGE = {"trt": {"args": "[opcional: <text>] ou resposta",
                               "usage": ("Traduz o texto ou mensagens "
                                         "fornecidos, para a linguagem "
                                         "de defeito do bot.")},
                       "tts": {"args": "[opcional: <text>] ou resposta",
                               "usage": ("Converte a mensagem de voz em "
                                         "texto. (speech-to-text).")},
                       "stt": {"args": "resposta só",
                               "usage": ("Converte a mensagem respondida "
                                         "em mensagem de voz "
                                         "(speech-to-text).")},
                       "scrlang": {"args": None,
                                   "usage": ("Apresenta a linguagem para "
                                             "a qual o bot vai traduzir "
                                             "ou realizar TTS para.")},
                       "setlang": {"args": "[ISO value]",
                                   "usage": ("Define uma nova linguagem "
                                             "para o tradutor.")},
                       "currency": {"args": ("<amount> <From ISO> "
                                             "[opcional: <To ISO>]"),
                                    "usage": ("Converte a Moeda dada para "
                                              "uma Moeda de destino "
                                              "(defeito: USD). Precisa "
                                              "código ISO da Moeda (EUR, "
                                              "USD, JPY etc.).")}}

    SYSTOOLS_USAGE = {"status": {"args": None,
                                 "usage": ("Apresenta vários parâmetros "
                                           "de execução do bot.")},
                      "shutdown": {"args": None,
                                   "usage": "Desliga o bot."},
                      "reboot": {"args": None,
                                 "usage": "Reinicia o bot."},
                      "storage": {"args": None,
                                  "usage": ("Apresenta informação sobre "
                                            "o armazenamento do servidor")},
                      "sysd": {"args": None,
                               "usage": ("Apresenta detalhes de sistema "
                                         "(Requer neofetch)")},
                      "sendlog": {"args": None,
                                  "usage": ("Faz upload do log do bot "
                                            "para o chat atual")}}

    USER_USAGE = {"info": {"args": "[opcional: <username/id>] ou resposta",
                           "usage": "Obtém informação de um utilizador."},
                  "stats": {"args": None,
                            "usage": "Obtém as tuas estatísticas."},
                  "kickme": {"args": None,
                             "usage": "Sais do grupo."},
                  "userid": {"args": "[opcional: <username>] ou resposta",
                             "usage": ("Obtém o ID de um utilizador. Se "
                                       "a mensagem é encaminhada, obtém os "
                                       "IDs dos dois (autor original e "
                                       "quem encaminhou).")}}

    WEBTOOLS_USAGE = {"dc": {"args": None,
                             "usage": ("Procura o Datacenter do Telegram "
                                       "mais próximo.")},
                      "ping": {"args": "<DNS/IP>",
                               "usage": "Faz ping do DNS/IP fornecido."},
                      "rtt": {"args": None,
                              "usage": "Obtém o Round-Trip Time atual"},
                      "speedtest": {"args": "[argumento opcional \"pic\"]",
                                    "usage": ("Executa um teste de "
                                              "velocidade da ligação. "
                                              "Usando \"pic\" como "
                                              "argumento irá apresentar "
                                              "o resultado como uma imagem.")}}

    CAS_INTERFACE_USAGE = {"casupdate": {"args": None,
                                         "usage": ("Atualiza os dados do "
                                                   "CSV do CAS.")},
                           "cascheck": {"args": ("[opcional: <username/id/"
                                                 "link>] ou resposta"),
                                        "usage": ("Verifica se um "
                                                  "utilizador está banido "
                                                  "no CAS, ou se um grupo "
                                                  "inteiro tem utilizadores "
                                                  "banidos.\n"
                                                  "Nota: o comando cascheck "
                                                  "apenas consegue ver "
                                                  "grupos no máximo de "
                                                  "10.000 membros, devido "
                                                  "a uma limitação nos "
                                                  "servidores do Telegram.")}}

    GITHUB_USAGE = {"git": {"args": "<user>/<repo>",
                            "usage": ("Obtém a release mais recente de "
                                      "determinado repositório de um "
                                      "utilizador.")}}

    MODULES_UTILS_USAGE = {"listcmds": {"args": ("[opcional: <nome do "
                                                 "comando>]"),
                                        "usage": ("Apresenta todos os "
                                                  "comandos disponíveis e "
                                                  "registados")},
                           "modules": {"args": ("<-option> [number of module "
                                                "from the list]"),
                                       "usage": ("\n`.modules -d [number of "
                                                 "module from the list]`\n"
                                                 "Shows the description of "
                                                 "the specific module. "
                                                 "Maybe some hidden "
                                                 "information are there, "
                                                 "who knows?\n\n"
                                                 "`.modules -i [number of "
                                                 "module from the list]`\n"
                                                 "Shows information about "
                                                 "the specific module like "
                                                 "the name, author, version "
                                                 "etc.\n\n"
                                                 "`.modules -u [number of "
                                                 "module from the list]`\n"
                                                 "Reveals the secrets and "
                                                 "the usage of the specific "
                                                 "module")}}

    TERMINAL_USAGE = {"shell": {"args": "<command>",
                                "usage": ("Executa na máquina hospedeira o "
                                          "comando shell fornecido (bash, "
                                          "powershell or zsh).\n\n"
                                          "**AVISO: se o Userbot está a ser "
                                          "executado com permissões root, "
                                          "isto pode causar dados "
                                          "irreversíveis. Procede com "
                                          "cuidado!**")}}

    MISC_USAGE = {"coinflip": {"args": None,
                               "usage": ("Lança uma moeda e indica se o "
                                         "resultado foi cara ou coroa.")},
                  "dice": {"args": None,
                           "usage": ("Lança o emoji do dado. Os números "
                                     "são calculados pelo Telegram.")},
                  "rand": {"args": "<lower limit> <upper limit>",
                           "usage": ("Dados dois limites inteiros, "
                                     "gera um número aleatório, inteiro "
                                     "também.")}}

    PACKAGE_MANAGER_USAGE = {"pkg": {"args": ("<option> [optional: "
                                              "<arguments>]"),
                                     "usage": ("\n`.pkg update "
                                               "[optional: <list of "
                                               "owner/repo combos>]`\n"
                                               "Updates data of all "
                                               "repositories. If repo urls "
                                               "are given e.g '.pkg update "
                                               "nunopenim/module-universe' "
                                               "then only the specific "
                                               "repo(s) will be updated. "
                                               "This command can also be "
                                               "used to add new repos by "
                                               "using the <owner/repo> "
                                               "combo.\n\n"
                                               "`.pkg list [optional: "
                                               "<-installed or -repos>]`\n"
                                               "Lists all installed modules "
                                               "and all modules from known "
                                               "repositories. Use the "
                                               "-installed option to show "
                                               "installed modules only or "
                                               "the -repos option to show "
                                               "modules from repositories "
                                               "only.\n\n"
                                               "`.pkg install <list of "
                                               "modules>`\nor\n"
                                               "`.pkg install -repo "
                                               "<owner/repo> <list of "
                                               "modules>`\n"
                                               "Installs the list of "
                                               "modules from given argument. "
                                               "If you want to install "
                                               "modules from a specific "
                                               "repo only, use the -repo "
                                               "option and pass the "
                                               "owner/repo combo along with "
                                               "the list of modules as "
                                               "argument.\n\n"
                                               "`.pkg uninstall/remove <list "
                                               "of modules>`\n"
                                               "Uninstalls modules from "
                                               "given list.\n\n"
                                               "`.pkg rmrepo <list of "
                                               "owner/repo combos>`\n"
                                               "Removes repos from given "
                                               "list of owner/repo combos "
                                               "from data.")}}

    UPDATER_USAGE = {"update": {"args": "upgrade",
                                "usage": ("Verifica por updates, e se "
                                          "existirem, apresenta a lista "
                                          "de mudanças.\n"
                                          "Se o utilizador verificou por "
                                          "updates, e se existirem "
                                          "updates, isto instala-as.")}}

    SIDELOADER_USAGE = {"sideload": {"args": "<argument>",
                                     "usage": ("Carrega um script python no "
                                               "espaço de utilizador. "
                                               "Funciona apenas como "
                                               "resposta. Podes usar o "
                                               "argumento `force`, caso "
                                               "tenhas um módulo de "
                                               "utilizador com o mesmo nome "
                                               "já.\n\n"
                                               "**INFORMAÇÃO**: Estes "
                                               "ficheiros têm de ser "
                                               "escritos de maneira a "
                                               "funcionar com o bot. Ao "
                                               "realizar um sideload de "
                                               "um ficheiro desconhecido, "
                                               "o utilizador pode obter um "
                                               "'soft-brick', tendo que "
                                               "remover um módulo defeituoso "
                                               "do espaço de utilizador.\n\n"
                                               "**AVISO CRITICO**: Alguns "
                                               "ficheiros maliciosos podem "
                                               "enviar a tua informação "
                                               "(geralmente a API KEY e "
                                               "String Session, mas não "
                                               "está limitado a estes itens) "
                                               "para hackers com propósitos "
                                               "maliciosos! Faz apenas "
                                               "sideload de módulos que "
                                               "confies na fonte!")}}
    # translation needed
    FEATURE_MGR_USAGE = {"disable": {"args": ("<name of command/alias or "
                                              "feature>"),
                                     "usage": ("Disable the given command "
                                               "or feature. Works with "
                                               "aliases too")},
                         "enable": {"args": ("<name of command/alias or "
                                             "feature>"),
                                    "usage": ("Enable the given command "
                                              "or feature. Works with "
                                              "aliases too")}}
