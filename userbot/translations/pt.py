# Portuguese Language file!
#
# Copyright 2020 nunopenim @github
# Copyright 2020 prototype74 @github
#
# Licensed under the PEL (Penim Enterprises License), v1.0
#
# You may not use this file or any of the content within it, unless in
# compliance with the PE License

class AdminText(object): # Admin module
    ADMINS_IN_CHAT = "Administradores em **{}**"
    UNABLE_GET_ADMINS = "`Não foi possível obter os administratores neste chat`"
    FAIL_CHAT = "`Não foi possível identificar o chat!`"
    NO_GROUP_CHAN = "`Este chat não é um grupo ou canal!`"
    NO_GROUP_CHAN_ARGS = "`Este chat, ou o chat dado, não é um grupo ou canal!`"
    NO_ADMIN = "`São necessários privilégios de Admin para executar esta ação!`"
    NO_BAN_PRIV = "`É necessária permissão para Banir utilizadores para executar esta ação!`"
    DELETED_ACCOUNT = "Conta excluída"
    CANNOT_BAN_SELF = "`Não posso banir-me a mim próprio!`"
    CANNOT_BAN_ADMIN = "`Não posso banir este admin`"
    BAN_SUCCESS_REMOTE = "{} foi banido de **{}**"  # user name, chat tile
    BAN_SUCCESS = "{} foi banido!"  # user name
    BAN_FAILED = "`Falha ao banir esta pessoa!`"
    CANNOT_UNBAN_SELF = "`Não posso desbanir-me a mim próprio`"
    UNBAN_SUCCESS_REMOTE = "{} foi desbanido de **{}**"  # user name, chat tile
    UNBAN_SUCCESS = "{} foi desbanido!"  # user name
    UNBAN_FAILED = "`Falha ao desbanir esta pessoa!`"
    CANNOT_KICK_SELF = "`Não me posso kickar a mim mesmo`"
    KICK_SUCCESS_REMOTE = "{} foi kickado de **{}**"  # user name, chat tile
    KICK_SUCCESS = "{} foi kickado!"  # user name
    KICK_FAILED = "`Falha ao kickar esta pessoa!`"
    NO_ONE_TO_PROMOTE = "`Não há ninguém para promover!`"
    NOT_USER = "`O Username ou ID dado não é um utilizador!`"
    CANNOT_PROMOTE_SELF = "`Não me posso promover a mim próprio!`"
    ADMIN_ALREADY_SELF = "`Já sou imortal!`"
    ADMIN_ALREADY = "`Esta pessoa já é imortal!`"
    ADMIN_NOT_ENOUGH_PERMS = "`Não tenho direitos de administração suficientes para promover esta pessoa!`"
    ADD_ADMINS_REQUIRED = "`Permissão para adicionar administradores é requerida.`"
    PROMOTE_SUCCESS = "{} foi promovido com poderes imortais!"  # user name
    TOO_MANY_ADMINS = "`Este chat já tem muitos administradores`"
    EMOJI_NOT_ALLOWED = "`Não são permitidos emojis nos títulos de administradores`"
    GET_ENTITY_FAILED = "Falha ao obter identidade."
    PROMOTE_FAILED = "`Falha ao promover esta pessoa.`"
    NO_ONE_TO_DEMOTE = "`Não há ninguém para despromover`"
    CANNOT_DEMOTE_SELF = "`Não posso despromover-me a mim próprio!`"
    DEMOTED_ALREADY = "`Esta pessoa já é um mortal.`"
    DEMOTE_SUCCESS = "{} foi despromovido!"  # user name
    CANNOT_DEMOTE_ADMIN = "`Este chat já tem muitos administradores`"
    DEMOTE_FAILED = "`Falha ao despromover esta pessoa.`"
    NO_GROUP_ARGS = "`Este chat, ou o chat fornecido, não é um grupo!`"
    NOT_MUTE_SUB_CHAN = "`Impossível silenciar subscritores de um canal!`"
    CANNOT_MUTE_SELF = "`Não consigo silenciar-me a mim próprio`"
    MUTE_SUCCESS_REMOTE = "{} foi silenciado em **{}**"  # user name, chat tile
    MUTE_SUCCESS = "{} foi silenciado"  # user name
    MUTE_FAILED = "`Falha ao silenciar esta pessoa`"
    NOT_UNMUTE_SUB_CHAN = "`Falha na remoção do silenciamento desta pessoa.`"
    CANNOT_UNMUTE_SELF = "`Não posso remover o meu próprio silenciamento`"
    UNMUTE_SUCCESS_REMOTE = "Foi removido o silenciamento de {} em **{}**"  # user name, chat tile
    UNMUTE_SUCCESS = "Removido o silenciamento de {}"  # user name
    UNMUTE_FAILED = "`Falha ao remover o silenciamento desta pessoa.`"
    TRY_DEL_ACCOUNTS = "`Tentando remover contas excluídas...`"
    DEL_ACCS_COUNT = "`Foram encontradas {} contas excluídas`"
    REM_DEL_ACCS_COUNT = "`Removidas {} de {} contas excluídas presentes`"  # rem count, total count
    NO_DEL_ACCOUNTS = "`Não existem contas excluídas neste chat.`"
    REPLY_TO_MSG = "`Responde a uma mensagem para a fixar.`"
    PIN_SUCCESS = "`Mensagem fixada com sucesso.`"
    PINNED_ALREADY = "`Esta mensagem já está fixada!`"
    PIN_FAILED = "`Falha ao fixar a mensagem!`"
    LOG_PIN_MSG_ID = "ID da Mensagem"

class StatusText(object):
    UBOT = "Projeto Userbot: "
    SYSTEM_STATUS = "Estado do sistema: "
    ONLINE = "Online!"
    VER_TEXT = "Versão: "
    USR_TEXT = "Utilizador: "
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
    SYSD_NEOFETCH_REQ = "`O pacote neofetch é necessário para apresentar informações do sistema!`"
    RESTART = "`A reiniciar...`"
    RESTART_LOG = "O Userbot está a reiniciar!"
    RESTARTED = "Reinicio completo!"
    NO_GITHUB = "Não disponível"

class DeletionsText(object):
    CANNOT_DEL_MSG = "`Não posso apagar esta mensagem`"
    UNABLE_DEL_MSG = "`Impossível apagar esta mensagem`"
    DEL_MSG_FAILED = "`Falha ao apahar esta mensagem`"
    REPLY_DEL_MSG = "`Responde à mensagem de alguém para a apagar`"
    NO_ADMIN_PURGE = "`São necessários privilégios de administração para apagar mensagens`"
    NO_DEL_PRIV = "`Permissão para apagar mensagens é necessária para apagar mensagens`"
    PURGE_MSG_FAILED = "`Falha ao apagar mensagem(s)`"
    PURGE_COMPLETE = "Apagar em massa completo! Foram apagadas `{}` mensagens!"
    LOG_PURGE = "Apagadas `{}` mensagens"
    REPLY_PURGE_MSG = "`Responde a uma mensagem para começar a apagar em massa.`"

class ChatInfoText(object):
    CHAT_ANALYSIS = "`Analisando o chat...`"
    EXCEPTION = "`Um erro inesperado ocorreu`"
    REPLY_NOT_CHANNEL = "`Esta mensagem não é um canal`"
    CANNOT_GET_CHATINFO = "`Não consigo obter informação de '{}'!`"
    YES_BOLD = "<b>Sim</b>"
    NO_BOLD = "<b>Não</b>"
    YES = "Sim"
    NO = "Não"
    CHATINFO = "<b>INFO DO CHAT:</b>\n"
    CHAT_ID = "ID: <code>{}</code>\n"
    CHAT_TYPE = "Tipo de chat: {} ({})\n"  # group/channel, private/public
    CHAT_NAME = "Nome do chat: {}\n"
    FORMER_NAME = "Nome anterior: {}\n"
    CHAT_PUBLIC = "Publico"
    CHAT_PRIVATE = "Privado"
    OWNER = "Criador: {}\n"
    OWNER_WITH_URL = "Criador: <a href=\"tg://user?id={}\">{}</a>\n"
    CREATED_NOT_NULL = "Criado em: <code>{} - {} {}</code>\n"
    CREATED_NULL = "Criado em: <code>{} - {} {}</code> {}\n"
    DCID = "ID do Data Center: {}\n"
    CHAT_LEVEL = "Nível do chat: <code>{}</code>\n"
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
    GRUP_STICKERS = "Stickers do chat: <a href=\"t.me/addstickers/{}\">{}</a>\n"
    LINKED_CHAT = "Chat ligado: {}\n"
    LINKED_CHAT_TITLE = "> Nome: {}\n"
    SLW_MODE = "Modo lento: {}"
    SLW_MODE_TIME = ", <code>{}s</code>\n\n"
    SPER_GRP = "Supergrupo: {}\n\n"
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
    NO_ADMIN_PERM = "`Privilégios de Administração são necessários para executar esta ação`"
    NO_INVITE_PERM = "`É necessária permissão para adicionar utilizadores!`"
    UNABLE_GET_LINK = "`Falha ao obter o Link de convite deste chat!`"

class MemberInfoText(object):
    SCAN = "`A examinar a informação deste membro...`"
    FAIL_GET_MEMBER_CHAT = "`Falha ao obter informação sobre o membro: impossível encontrar o chat!`"
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
    MEMBERINFO = "INFO DO MEMBRO"
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
    ROOT_RIGHTS = "Permissões root"
    SEND_MESSAGES = "Enviar mensagens"
    SEND_MEDIA = "Enviar média"
    SEND_GIFS_STICKERS = "Enviar stickers e GIFs"
    SEND_POLLS = "Criar votações"
    EMBED_LINKS = "Links Embebidos"
    WARN_ADMIN_PRIV = "Privilégios de admin são necessários para aceder a permissões não convêncionais"
    PROMOTED_BY = "Promovido por"
    ADDED_BY = "Adicionado por"
    JOIN_DATE = "Data de entrada"

class MessagesText(object):
    NO_ADMIN = "`Privilégios de administrador são necessários para executar esta ação`"
    FAIL_CHAT = "`Falha ao obter o chat.`"
    CANNOT_COUNT_DEL = "`Não posso contar mensagens de uma conta excluída`"
    CANNOT_QUERY_FWD = "`Não posso fazer query de mensagens encaminhadas por um canal!`"
    FAIL_COUNT_MSG = "`Não posso fazer query de mensagens encaminhadas por um canal!`"
    USER_HAS_SENT = "{} enviou `{}` mensagens neste chat!"  # userlink, msg count
    USER_HAS_SENT_REMOTE = "{} enviou `{}` messagens em **{}**"  # userlink, msg count, chat title
    CANNOT_COUNT_MSG = "`Não consigo contar mensagens neste chat`"
    CANNOT_COUNT_MSG_REMOTE = "`Não consigo contar mensagens em {}!`"
    NO_GROUP_CHAN = "`Este chat não é um grupo ou canal!`"
    PICKING_MEMBERS = "`A escolher os membros mais ativos. Isto pode demorar algum tempo...`"
    FAILED_TO_PICK = "`Falha ao escolher os membros mais ativos!`"
    TOP_USERS_TEXT = "Top **{}** de membros ativos em **{}**"  # count, chat title
    TOP_USERS_MSGS = "Mensagens"

class ScrappersText(object):
    NO_TEXT_OR_MSG = "`Sem texto ou mensagem para traduzir!`"
    TRANSLATING = "`A traduzir...`"
    SAME_SRC_TARGET_LANG = "`Linguagem de destino é igual à linguagem de fonte.`"
    DETECTED_LANG = "Linguagem detetada"
    TARGET_LANG = "Linguagem de destino"
    ORG_TEXT = "Texto original"
    TRANS_TEXT = "Texto traduzido"
    MSG_TOO_LONG = "`Texto traduzido é demasiado grande!`"
    FAIL_TRANS_MSG = "`Falha ao traduzir esta mensagem!`"
    FAIL_TRANS_TEXT = "`Falha ao traduzir o texto fornecido!`"
    MEDIA_FORBIDDEN = "`Impossível executar TTS: O upload de média neste chat é proíbido!`"
    NO_TEXT_TTS = "`Sem texto ou mensagem para executar TTS`"
    FAIL_TTS = "`Falha ao realizar TTS`"
    FAIL_API_REQ = "`Requerimento à API falhou!`"
    INVALID_LANG_CODE = "`Código de linguagem inválido, ou a linguagem não é suportada!`"
    NOT_EGH_ARGS = "`Não foram fornecidos argumentos suficientes!`"
    INVALID_AMOUNT_FORMAT = "`Formato de quantidade inválido!`"
    CC_ISO_UNSUPPORTED = "`'{}' não é um código de Moeda ISO suportado!`"
    CC_HEADER = "Conversor de Moeda"
    CFROM_CTO = "**{}** para **{}**"  # from cc iso, target cc iso
    INVALID_INPUT = "Input inválido"
    UNABLE_TO_CC = "`Falha ao converter Moeda`"
    CC_LAST_UPDATE = "Última atualização"
    REPLY_TO_VM = "`Responde a uma mensagem de voz!`"
    WORKS_WITH_VM_ONLY = "`Só funciona com mensagens de voz!`"
    CONVERT_STT = "`A converter voz em texto...`"
    FAILED_LOAD_AUDIO = "`Falha ao carregar aúdio`"
    STT = "Speech-to-text"
    STT_TEXT = "Texto"
    STT_NOT_RECOGNIZED = "`Não foi possível reconhecer texto da mensagem por voz enviada`"
    STT_REQ_FAILED = "Resultado do pedido inválido!"
    STT_OUTPUT_TOO_LONG = "`O output do Speech-to-text é demasiado longo!`"
    UNABLE_TO_STT = "`Impossível realizar speech-to-text`"

class UserText(object):
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
    USR_INFO = "INFO DO USER"
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
    DUAL_HAS_ID_OF = "{} tem um ID de `{}`"  # name of person, ID
    MY_ID = "O meu ID é `{}`"
    DEL_HAS_ID_OF = "A Conta Excluída tem um ID de `{}`"
    ID_NOT_ACCESSIBLE = "o ID de {} não é acessível"
    ORG_HAS_ID_OF = "O autor original {} tem um ID de `{}`"  # name of person, ID

class GeneralMessages(object):
    ERROR = "ERRO!"
    CHAT_NOT_USER = "`Canais não são objetos User`"
    FAIL_FETCH_USER = "`Falha ao adquirir informação do utilizador`"
    ENTITY_NOT_USER = "`A entidade não é um objeto User`"
    CALL_UREQ_FAIL = "`O request para a chamada de User falhou`"
    LOG_USER = "Utilizador"
    LOG_USERNAME = "Nome de utilizador"
    LOG_USER_ID = "ID de utilizador"
    LOG_CHAT_TITLE = "Título do Chat"
    LOG_CHAT_LINK = "Link"
    LOG_CHAT_ID = "ID do Chat"

class HelpText(object):
    INVALID_ARG = "`Argumento \"{}\" inválido!`"
    USAGE = "Utilização"
    #NUMBER_OF_MODULE = "nome do módulo"  !! retranslation needed !!
    AVAILABLE_MODULES = "Módulos disponíveis"
    DISABLED_MODULES = "Módulos desativados"
    NAME_MODULE = "**Módulo {}**"
    #MISSING_NUMBER_MODULE = "`Falta o nome do módulo`"  !! retranslation needed !!
    #MODULE_NOT_AVAILABLE = "`Módulo \"{}\" não encontrado!`"  !! retranslation needed !!
    MODULE_NO_DESC = "__Descrição não disponível__"
    MODULE_NO_USAGE = "__Utilização não disponível__"
    ASTERISK = "__* Módulo de user desinstalável__"

class WebToolsText(object):
    PING_SPEED = "Round-Trip Time: "
    DCMESSAGE = "País : `{}`\nEste Datacenter : `{}`\nDatacenter mais próximo : `{}`"
    BAD_ARGS = "`Maus argumentos`"
    INVALID_HOST = "`Ocorreu um problema a interpretar o IP/Hostname`"
    PINGER_VAL = "DNS: `{}`\nVelocidade de ping: `{}`"
    SPD_START = "`A efetuar um teste de velocidade...`"
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
    TOO_MANY_CAS = "`Muitos utilizadores banidos no CAS. A fazer upload da lista como ficheiro...`"
    FAIL_UPLOAD_LIST = "`Falha ao efetuar upload da lista`"
    SEND_MEDIA_FORBIDDEN = "`O envio de média neste chat não é permitido`"
    UPDATER_CONNECTING = "`Conectando...`"
    UPDATER_DOWNLOADING = "`A fazer Download...`"
    FAIL_APPEND_CAS = "`Falha ao adicionar dados do CAS`"
    UPDATE_SUCCESS = "`Atualizado o CSV dos dados do CAS`"
    NO_CONNECTION = "`Falha na conecção com o servidor do CAS`"
    TIMEOUT = "`Impossivel atualizar o CSV dado que o tempo de ligação excedeu o limite`"
    UPDATE_FAILED = "`Falha ao atualizar os dados do CSV do CAS`"
    GIVEN_ENT_INVALID = "`O ID, nome ou link dado é inváldio`"
    AUTO_UPDATE = "`A realizar um auto-update dos dados do CAS...`"
    CAS_CHECK_FAIL_ND = "`Verificação CAS falhou, visto que o CSV tem um formato inválido`"
    CAS_CHECK_ND = "`Dados CAS não encontrados. Por favor usa o comando .casupdate para obter os últimos dados CAS`"
    PROCESSING = "`Processando...`"
    DELETED_ACCOUNT = "Conta Excluída"
    USER_HEADER = "DADOS DO USER"
    USER_ID = "ID"
    FIRST_NAME = "Primeiro nome"
    LAST_NAME = "Último nome"
    USERNAME = "Nome de utilizador"
    CAS_DATA = "DADOS DO CAS"
    RESULT = "Resultado"
    OFFENSES = "Total de Ofensas"
    BANNED_SINCE = "Banido desde"
    USER_DETECTED = "Aviso! `{}` membro está banido no CAS em **{}**"  # count, chat title
    USERS_DETECTED = "Aviso! `{}` membros estão banidos no CAS em **{}**"  # count, chat title
    NO_USERS = "Nenhum utilizador banido no CAS encontrado em **{}**"
    NO_ADMIN = "`São necessários privilégios de administração para realizar esta ação`"
    CAS_CHECK_FAIL = "`Verificação CAS falhou`"

class GitHubText(object):
    INVALID_URL = "Combinação user/repo inválida"
    NO_RELEASE = "A release especificada não foi encontrada"
    AUTHOR_STR = "<b>Autor:</b> <a href='{}'>{}</a>\n"
    RELEASE_NAME = "<b>Nome da Release:</b> "
    ASSET = "<b>Recurso:</b> \n"
    SIZE = "Tamanho: "
    DL_COUNT = "\nNúmero de Downloads: "
    INVALID_ARGS = "Argumentos inválidos! Certifica-te de que estás a introduzir uma combinação user/repo válida!"

class TerminalText(object):
    BASH_ERROR = "Ocorreu um erro generalizado. Geralmente acontece por teres utilizado argumentos inválidos ou um comando não existente."

class MiscText(object):
    COIN_LANDED_VAL = "A moeda caiu em: "
    THRWING_COIN = "`A lançar a moeda...`"
    HEADS = "Caras"
    TAILS = "Coroas"
    RAND_INVLD_ARGS = "`Argumentos inválidos, certifica-te que tens exatamente 2 números`"
    FRST_LIMIT_INVALID = "`O primeiro valor não é um número válido`"
    SCND_LIMIT_INVALID = "`O segundo valor não é um número válido`"
    RAND_NUM_GEN = "O número gerado entre `{}` e `{}`: **`{}`**"

class PackageManagerText(object):
    INVALID_ARG = "Argumento inválido! Certifica-te que é **update**, **list**, **install** ou **uninstall**!"
    UPDATE_COMPLETE = "Foi atualizada a lista de módulos do(s) universo(s): **{}**"
    EMPTY_LIST = "\n\nA lista de módulos está vazia! Por favor executa primeiro `.pkg update`"
    FILES_IN = "\n**Ficheiros em {}:**\n"
    FILE_DSC = "{}. [{}]({}) - {}\n"
    NO_PKG = "`Nenhum pacote especificado para instalar! Processo interrompido!`"
    MOD_NOT_FOUND_INSTALL = "Nenhum módulo chamado `{}` foi encontrado nos repositórios! Processo interrompido!"
    DONE_RBT = "`Reiniciando o userbot...`"
    NO_UNINSTALL_MODULES = "Nenhum módulo desinstalável presente! Processo interrompido!"
    NO_UN_NAME = "Por favor especifica um nome de um módulo. Não posso desinstalar __nada__!"
    MULTIPLE_NAMES = "Por questões de segurança, apenas podes desinstalar um módulo de cada vez. Por favor fornece apenas um nome."
    NOT_IN_USERSPACE = "`{}` não é um módulo de utilizador válido! Processo interrompido!"
    UNINSTALLING = "`Desinstalando {}...`"
    REBOOT_DONE_INS = "Feito! Módulo(s) instalado(s): `{}`"
    REBOOT_DONE_UNINS = "Feito! Desinstalado `{}`!"
    INSTALL_LOG = "Userbot reiniciado! Módulo(s) instalado(s): `{}`"
    UNINSTALL_LOG = "Userbot reiniciado! Módulo desinstalado: `{}`"
    INSTALLED = "**MÓDULOS INSTALADOS:**\n"
    ALREADY_PRESENT = "\n__* Módulo presente, será atualizado__"

class UpdaterText(object):
    UPDATES_NOT_RAN = "Por favor usa apenas .update para verificar a existência de atualizações"
    NO_UPDATES = "Nenhuma atualização em fila. Se suspeitas que saiu uma atualização nova, usa .update!"
    UPDATING = "`A atualizar...`"
    UPD_ERROR = "Um erro inesperado aconteceu. O problema mais comum é não ter o git instalado ou bem configurado."
    UPD_SUCCESS = "Userbot atualizado! Reiniciando..."
    UNKWN_BRANCH = "Branch desconhecudo. Provavelmente estás a utilizar uma source modificada"
    LATS_VERSION = "{} já se encontra na versão mais recente!"
    UPD_AVAIL = "**ATUALIZAÇÕES DISPONÍVEIS**\n\n**Lista de mudanças:**\n"
    RUN_UPD = "\nPor favor executa `.update upgrade` para atualizar agora!"
    CHLG_TOO_LONG = "Novas atualizações disponíveis, no entanto a lista é demasiado grande para ser apresentada!\n\nPor favor executa `.update upgrade` para atualizar agora!"
    RBT_COMPLETE = "Atualização completa!"
    UPD_LOG = "O Userbot foi atualizado com sucesso e reinicializado!"

class SideloaderText(object):
    NOT_PY_FILE = "Este não é um ficheiro .py válido. Não é possível fazer sideload"
    DLOADING = "`A fazer download...`"
    MODULE_EXISTS = "Já existe um módulo de utilizador chamado `{}`. Se desejares prosseguir assim mesmo, por favor executa o comando com o argumento `force` !"
    SUCCESS = "Instalado `{}` com sucesso! A reiniciar..."
    LOG = "O módulo `{}` foi carregado sideload com sucesso!"
    RBT_CPLT = "Reinicio completo!"
    INVALID_FILE = "Por favor responde a um ficheiro válido!"

# Save your eyes from what may become the ugliest part of this userbot.
class ModuleDescriptions(object):
    ADMIN_DESC = "Um módulo para te ajudar a gerir um grupo teu ou de um amigo mais facilmente. Inclui comandos comuns como: ban, unban, promote etc.\
                 \n\nNota: muitos comandos deste módulo necessitam de permissões de administrador para funcionarem correctamente."
    CHATINFO_DESC = "Obtém a maior parte das informações de um canal, grupo ou supergrupo como data de criação, número de mensagens, mensagens apagadas, nome antigo, etc"
    DELETIONS_DESC = "Este módulo permite apagar as tuas mensagens ou mensagens de grupo rápido. Alguém fez spam no teu grupo? Usa o comando .purge para apagar tudo!\
                     \nTodos os comandos deste módulo requerem permissões de admin para apagar as mensagens de outras pessoas\
                     \n\n**Importante: não abuses deste módulo para apagares o histórico de mensagens do grupo de outra pessoa**, a sério, não o faças..."
    MEMBERINFO_DESC = "Fornece informação sobre um participante no chat como permissões, data de limitação, data de entrada, etc.\
                     \n\nNota: necessita de permissões de administrador para ver permissões de outros utilizadores."
    MESSAGES_DESC = "Este módulo inclui comandos que apenas funcionam com mensagens, como msgs ou topusers."
    SCRAPPERS_DESC = "Este módulo inclui ferramentas úteis, como o tradutor ou o text-to-speech"
    SYSTOOLS_DESC = "Este módulo contém um conjunto de ferramentas úteis para o bot. Permite ver o uptime do bot, o uptime do servidor, as versões de todos os componentes \
                    do bot, as especificações do servidor do bot, e contém alguns controlos de energia do bot."
    USER_DESC = "Contém ferramentas que fornecem informações sobre utilizadores, e a ferramenta kickme."
    WEBTOOLS_DESC = "Este módulo contém quase, se não mesmo todas, as ferramentas web do bot como ping, speedtest, calculadora RTT, e um método para mostrar o Datacenter atual."
    CAS_INTERFACE_DESC = "O interface para a API Combot Anti-Spam System. Permite verificar apenas um utilizador, ou procurar um grupo inteiro, por CAS bans, através dos comandos."
    GITHUB_DESC = "Um módulo que usa a API do GitHub. Este módulo permite ver releases de um repositório, de um utilizador do GitHub."
    TERMINAL_DESC = "Este módulo permite executar diretamente comandos shell, na máquina hospedeira.\
                    \n\n**Atenção:** Executar comandos shell no bot pode e vai modificar permanentemente o servidor! **Más coisas podem acontecer se executares o bot como root/sudo!**"
    MISC_DESC = "O módulo Misc contém diversos comandos e ferramentas que não serviam para incluir noutros módulos, mas ao mesmo tempo eram demasiado simples para ter o seu próprio módulo. Vê o help para mais detalhes."
    PACKAGE_MANAGER_DESC = "O módulo gestor de pacotes permite um utilizador gerir aplicações extra, de repositórios externos, tanto oficiais, como o repositório modules-universe, ou de fontes externas. Assim, permite aos utilizadores personalizar o seu bot mais do que o stock."
    UPDATER_DESC = "O módulo Updater permite ao utilizador verificar a existencia de atualizações e, se existirem, atualizar o bot."
    SIDELOADER_DESC = "O módulo sideloader permite carregar ficheiros extra facilmente. Para o fazer, apenas tens de enviar o comando .sideload como resposta a um ficheiro .py\n\n" \
                      "**INFORMAÇÃO**: Estes ficheiros têm de ser escritos de maneira a funcionar com o bot. Ao realizar um sideload de um ficheiro desconhecido, o utilizador pode obter um 'soft-brick', tendo que remover um módulo defeituoso do espaço de utilizador.\n\n" \
                      "**AVISO CRITICO**: Alguns ficheiros maliciosos podem enviar a tua informação (geralmente a API KEY e String Session, mas não está limitado a estes itens) para hackers com propósitos maliciosos! Faz apenas sideload de módulos que confies na fonte!"

class ModuleUsages(object):
    ADMIN_USAGE = "`.adminlist` [opcional: <link/id>] \
                 \nUso: apresenta uma lista de todos os admins de um canal ou grupo (remotamente). Requer permissões de admin nos canais.\
                 \n\n`.ban` [opcional: <username/id> <chat (id ou link)>] ou resposta\
                 \nUso: Bane um utilizador de um chat (remotamente). Precisa de permissão de administrador com direito de banir.\
                 \n\n`.unban` [opcional: <username/id> <chat (id ou link)>] ou resposta\
                 \nUso: Desbane um utilizador de um chat (remotamente). Precisa de permissão de administrador com direito de banir.\
                 \n\n`.kick` [opcional: <username/id> <chat (id ou link)>] ou resposta\
                 \nUso: Kicka um utilizador de um chat (remotamente). Precisa de permissão de administrador com direito de banir.\
                 \n\n`.promote` [optional: <username/id> e/ou <title>] ou resposta\
                 \nUso: Promove um utilizador com direitos imortais! Requer privilegios de administraçao com direitos de admin e uma segunda\
                 \npermissão de admin porque um promote nunca adiciona por defeito permissões de add admin. Comprimento do titulo tem de ser <= 16 caractéres.\
                 \n\n`.demote` [optional: <username/id>] ou resposta\
                 \nUso: Despromove um utilizador. É necessária permissão de add admin. Apenas funciona com admins promovidos por ti.\
                 \n\n`.mute` [optional: <username/id> <chat (id ou link)>] ou resposta\
                 \nUso: Silencia um utilizador de um chat (remotamente). Precisa de permissão de administrador com direito de banir.\
                 \n\n`.unmute` [optional: <username/id> <chat (id ou link)>] ou resposta\
                 \nUso: Des-silencia um utilizador de um chat (remotamente). Precisa de permissão de administrador com direito de banir.\
                 \n\n`.delaccs`\
                 \nUso: Tenta remover contas excluídas de um chat. Precisa de permissão de administrador com direito de banir.\
                 \nCaso contrário, apenas reporta o número de contas excluídas.\
                 \n\n`.pin` [argumento opcional \"loud\" para notificar todos os membros] ou resposta\
                 \nUso: Responde ao uma mensagem para fixares esta."

    CHATINFO_USAGE = "`.chatinfo` [opcional: <chat_id/link>] ou resposta (se canal)\
                 \nUso: Obtém informação de um chat. Alguma informação pode estar omissa por falta de permissões.\
                 \n\n`.chatid`\
                 \nUso: Obtém o ID do chat.\
                 \n\n`.link` [opcional: <chat_id/link>]\
                 \nUso: Obtém o link de convite partilhável do chat. Precisa de permissão de administrador com direito de convidar/adicionar utilizadores."

    DELETIONS_USAGE = "`.del`\
         \nUso: Apaga a mensagem respondida.\
         \n\n`.purge`\
         \nUso: Apaga todas as mensagens entre a última e a mensagem respondida. Precisa de permissão de administrador com direito de apagar mensagens são necessárias se estiveres em grupos ou canais.\
         \n**Nota: por favor não abuses deste comando para apagares o histórico de mensagens de grupos inteiros de outras pessoas**"

    MEMBERINFO_USAGE = "`.minfo` [opcional: <tag/id> <group>] ou resposta\
          \nUso: Obtém (remotamente) informações sobre um membro de um grupo."

    MESSAGES_USAGE = "`.msgs` [opcional: <username/id> <group>] ou resposta\
                \nUso: Obtém o total de mensagens d eum utilizador (inclui qualquer mensagem, como texto, voz, imagens, videos, etc...).\
                \nFunciona remotamente também\
                \n\n`.topusers` [opcional: <group>]\
                \nUso: Apresenta os 10 membros mais ativos de um grupo. Este processo demora bastante tempo e está dependente do número de utilizadores de um grupo."

    SCRAPPERS_USAGE = "`.trt` [opcional: <text>] ou resposta\
          \nUso: Traduz o texto ou mensagens fornecidos, para a linguagem de defeito do bot.\
          \n\n`.tts` [opcional: <text>] ou resposta\
          \nUso: Converte o texto dado em mensagem de voz. (text-to-speech).\
          \n\n`.stt` resposta apenas\
          \nUso: Converte a mensagem de voz em texto. (speech-to-text).\
          \n\n`.currency` <amount> <From ISO> [opcional: <To ISO>] \
          \nUso: Converte a Moeda dada para uma Moeda de destino (defeito: USD). Precisa código ISO da Moeda (EUR, USD, JPY etc.)."

    SYSTOOLS_USAGE = "`.status`\
         \nUso: Apresenta vários parâmetros de execução do bot.\
         \n\n`.shutdown`\
         \nUso: Desliga o bot.\
         \n\n`.reboot`\
         \nUso: Reinicia o bot.\
         \n\n`.sysd`\
         \nUso: Apresenta detalhes de sistema (Requer neofetch)"

    USER_USAGE = "`.info` [opcional: <username/id>] ou resposta\
        \nUso: Obtém informação de um utilizador.\
        \n\n`.stats`\
        \nUso: Obtém as tuas estatísticas.\
        \n\n`.kickme`\
        \nUso: Sais do grupo.\
        \n\n`.userid` [opcional: <username>] ou resposta\
        \nUso: Obtém o ID de um utilizador. Se a mensagem é encaminhada, obtém os IDs dos dois (autor original e quem encaminhou)."

    WEBTOOLS_USAGE = "`.rtt` \
                    \nUso: Obtém o Round-Trip Time atual.\
                    \n\n`.dc` \
                    \nUso: Procura o Datacenter do Telegram mais próximo.\
                    \n\n`.ping` <DNS/IP> \
                    \nUso: Faz ping do DNS/IP fornecido.\
                    \n\n`.speedtest` [argumento opcional \"pic\"] \
                    \nUso: Executa um teste de velocidade da ligação. Usando \"pic\" como argumento irá apresentar o resultado como uma imagem."

    CAS_INTERFACE_USAGE = "`.casupdate`\
                    \nUso: Atualiza os dados do CSV do CAS.\
                    \n\n`.cascheck` [opcional: <username/id/link>] ou resposta\
                    \nUso: Verifica se um utilizador está banido no CAS, ou se um grupo inteiro tem utilizadores banidos.\
                    \nNota: o comando cascheck apenas consegue ver grupos no máximo de 10.000 membros, devido a uma limitação nos servidores do Telegram."

    GITHUB_USAGE = "`.git` <user>/<repo> \
                  \nUso: Obtém a release mais recente de determinado repositório de um utilizador."

    TERMINAL_USAGE = "`.shell` <comando> \
                  \nUso: Executa na máquina hospedeira o comando shell fornecido (bash, powershell or zsh).\
                  \n\n**AVISO: se o Userbot está a ser executado com permissões root, isto pode causar dados irreversíveis. Procede com cuidado!**"

    MISC_USAGE = "`.coinflip` \
                 \nUso: Lança uma moeda e indica se o resultado foi cara ou coroa.\
                 \n\n`.dice` \
                 \nUso: Lança o emoji do dado. Os números são calculados pelo Telegram.\
                 \n\n`.rand` <limite inferior> <limite superior>\
                 \nUso: Dados dois limites inteiros, gera um número aleatório, inteiro também."

    PACKAGE_MANAGER_USAGE = "`.pkg update` \
                 \nUso: Atualiza a lista de pacotes. \
                 \n\n`.pkg list` \
                 \nUso: Apresenta a lista de pacotes (pode estar desatualizada!) \
                 \n\n`.pkg install <módulo 1> <módulo 2 (opcional)> <...>` \
                 \nUso: Instala a lista de módulos dados como argumento.\
                 \n\n`.pkg uninstall <módulo>` \
                 \nUso: Desinstala o módulo de utilizador. Por motivos de segurança, é possivel apenas desinstalar um módulo de cada vez."

    UPDATER_USAGE = "`.update` \
                 \nUso: Verifica por updates, e se existirem, apresenta a lista de mudanças.\
                 \n\n`.update upgrade` \
                 \nUso: Se o utilizador verificou por updates, e se existirem updates, isto instala."

    SIDELOADER_USAGE = "`.sideload` <argumento> \
                       \nUso: Carrega um script python no espaço de utilizador. Funciona apenas como resposta. Podes usar o argumento `force`, caso tenhas um módulo de utilizador com o mesmo nome já.\
                       \n\n**INFORMAÇÃO**: Estes ficheiros têm de ser escritos de maneira a funcionar com o bot. Ao realizar um sideload de um ficheiro desconhecido, o utilizador pode obter um 'soft-brick', tendo que remover um módulo defeituoso do espaço de utilizador.\
                       \n\n**AVISO CRITICO**: Alguns ficheiros maliciosos podem enviar a tua informação (geralmente a API KEY e String Session, mas não está limitado a estes itens) para hackers com propósitos maliciosos! Faz apenas sideload de módulos que confies na fonte!"
