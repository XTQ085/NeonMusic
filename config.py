from os import getenv

from dotenv import load_dotenv

load_dotenv()

# VARS

get_queue = {}
BOT_TOKEN = getenv("BOT_TOKEN", "5332462277:AAFfa-Dx5NAEba4IOy6AOFz_9lO0OgmZvds")
API_ID = int(getenv("API_ID", 11661168 ))
API_HASH = getenv("API_HASH", "30cc640b6977480660e650f71d52d1ae")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "10"))
ASSISTANT_PREFIX = list(getenv("ASSISTANT_PREFIX", ".").split())
MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://nusrte:Nusret.2006@cluster0.r8ckx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5371871534").split()))
OWNER_ID = list(map(int, getenv("OWNER_ID", "5297429324").split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001697370051"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "NeonMusicbot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "f59616ee-b2c1-4455-9db0-47ab3ef48631")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "LuksMusicbot")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO", "https://github.com/XTQ085/NeonMusic"
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

if str(getenv("SUPPORT_CHANNEL", "NeonBots")).strip() == "":
    SUPPORT_CHANNEL = None
else:
    SUPPORT_CHANNEL = str(getenv("SUPPORT_CHANNEL", "LuksBots))
if str(getenv("SUPPORT_GROUP")).strip() == "":
    SUPPORT_GROUP = None
else:
    SUPPORT_GROUP = str(getenv("SUPPORT_GROUP", "NeonSUP"))


if str(getenv("STRING_SESSION1")).strip() == "AQAwA7v77X3sRIXn_wXnmU2ek2Z2vvsyf0PhQJbJC-idAepFGUqWsdAx5msFbOcPqzq4Pnj-_AJoX6IyfZ9XSLdPuDQ5xnVnrrkuFYuQBPCqUh0qgyWagSmXAAZ2-fLywEHrD__JzrfqGUTmyEF1hE-FoR2fJkJ_FQLIu8DqB7A-y7O9IU8cNeUZwhvtCyoIGkjciLzFK4V7sXgLZNka0LOc9fNj3BlNvA8vWVEGzrHu0aUjQfOqIhJ1SeFAbhqSpEaY639Mp6_nYnJqwOAS65zglJSjmXvZmERAIKC8Jq0msIrS_Fgjr-JkO4nlDOgmjWA8sBS5O7W7Yk9vuc1IuWaOAAAAATR7T2EA":
    STRING1 = str(None)
else:
    STRING1 = str(getenv("STRING_SESSION1", "AQAwA7v77X3sRIXn_wXnmU2ek2Z2vvsyf0PhQJbJC-idAepFGUqWsdAx5msFbOcPqzq4Pnj-_AJoX6IyfZ9XSLdPuDQ5xnVnrrkuFYuQBPCqUh0qgyWagSmXAAZ2-fLywEHrD__JzrfqGUTmyEF1hE-FoR2fJkJ_FQLIu8DqB7A-y7O9IU8cNeUZwhvtCyoIGkjciLzFK4V7sXgLZNka0LOc9fNj3BlNvA8vWVEGzrHu0aUjQfOqIhJ1SeFAbhqSpEaY639Mp6_nYnJqwOAS65zglJSjmXvZmERAIKC8Jq0msIrS_Fgjr-JkO4nlDOgmjWA8sBS5O7W7Yk9vuc1IuWaOAAAAATR7T2EA"))

if str(getenv("STRING_SESSION2")).strip() == "":
    STRING2 = str(None)
else:
    STRING2 = str(getenv("STRING_SESSION2"))

if str(getenv("STRING_SESSION3")).strip() == "":
    STRING3 = str(None)
else:
    STRING3 = str(getenv("STRING_SESSION3"))

if str(getenv("STRING_SESSION4")).strip() == "":
    STRING4 = str(None)
else:
    STRING4 = str(getenv("STRING_SESSION4"))

if str(getenv("STRING_SESSION5")).strip() == "":
    STRING5 = str(None)
else:
    STRING5 = str(getenv("STRING_SESSION5"))

if str(getenv("LOG_SESSION")).strip() == "":
    LOG_SESSION = str(None)
else:
    LOG_SESSION = str(getenv("LOG_SESSION"))
