from telethon.sync import TelegramClient
from telethon.tl.functions.messages import SendMessageRequest
import os
import time
from tqdm import tqdm

# ==== Configuration ====
api_id = 'YOUR_API_ID'
api_hash = 'YOUR_API_HASH'
target_channel = 'https://t.me/yourchannel'
log_file = 'upload_log.txt'
ignore_files = ['uploader_session', 'uploader_session.session', 'uploader_session.session-journal', 'telegram_uploader.py', log_file]
upload_folder = os.getcwd()
max_file_size = 2 * 1024 * 1024 * 1024  # 2GB

# ==== Load previously uploaded files ====
if os.path.exists(log_file):
    with open(log_file, 'r') as f:
        uploaded_files = set(line.strip() for line in f.readlines())
else:
    uploaded_files = set()

# ==== Start Client ====
client = TelegramClient('uploader_session', api_id, api_hash)
client.start()

uploaded_this_session = []

def is_file_valid(file_path):
    filename = os.path.basename(file_path)
    return (
        os.path.isfile(file_path) and
        os.path.getsize(file_path) <= max_file_size and
        filename not in ignore_files and
        filename not in uploaded_files
    )

def log_upload(file_name):
    with open(log_file, 'a') as f:
        f.write(file_name + '\n')
    uploaded_this_session.append(file_name)

print("🚀 Starting upload...")

for root, _, files in os.walk(upload_folder):
    for file in tqdm(files, desc="Uploading files", unit="file"):
        file_path = os.path.join(root, file)

        if not is_file_valid(file_path):
            continue

        try:
            print(f"[UPLOAD] Sending {file}")
            client.send_file(target_channel, file_path, caption=file)
            log_upload(file)
            time.sleep(5)
        except Exception as e:
            print(f"[ERROR] Failed to send {file}: {e}")
            time.sleep(30)

# ==== Send log summary to Saved Messages ====
if uploaded_this_session:
    summary = "✅ Uploaded files this session:\n" + "\n".join(uploaded_this_session)
else:
    summary = "📂 No new files were uploaded."

client(SendMessageRequest('me', summary))  # 'me' means "Saved Messages"

print("✅ Upload finished. Summary sent to Saved Messages.")
client.disconnect()
