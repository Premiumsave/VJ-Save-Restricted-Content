import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22473416"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "ca4a166df6f575a22497adcc1451cef6")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ynapxdzxecmclyalc12345678:ylaXTzNUzamSWHP1@cluster0.mr6n1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
