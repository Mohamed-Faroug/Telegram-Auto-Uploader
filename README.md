# 📤 Telegram Auto Uploader

A Python-based tool to automatically upload files to a Telegram channel or group. Built using Telethon, with support for:

- ✅ Uploading from current directory
- ✅ Skipping already uploaded files
- ✅ Progress tracking with `tqdm`
- ✅ Logging uploads to a file
- ✅ Sending upload summary to Telegram Saved Messages
- ✅ Automation via Task Scheduler (every 3 hours)
- ✅ Optional live monitor: upload on file creation using `watchdog`

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
 git clone https://github.com/Mohamed-Faroug/Telegram-Auto-Uploader.git
```
  cd telegram-auto-uploader
## Install Requirements
 ```bash
  pip install -r requirements.txt
```

##🔧 Configuration
  ```bash
  api_id = 'YOUR_API_ID'
  api_hash = 'YOUR_API_HASH'
  target_channel = 'https://t.me/yourchannel'
```
To get your api_id and api_hash, visit: https://my.telegram.org


##📜 Scripts
###  telegram_uploader.py
Main script: Uploads all valid files from current directory.

###  auto_upload.bat
Windows batch file to automate uploads every 3 hours using Task Scheduler.

### watch_folder.py
Optional live monitor using watchdog to auto-upload files as soon as they're added.


## Automation Options
- 🔁 Every 3 Hours (Task Scheduler)
   Use auto_upload.bat
   
   Open Task Scheduler → Create Task
   
   Set trigger: Daily → Repeat every 3 hours
   
   Action: Start program → Point to the .bat file

-👁️ Live Watch Mode
Run:
```bash
    python watch_folder.py
```
This watches for new files in the current directory and uploads them instantly.


## 📄 Log File
 All uploaded files are tracked in upload_log.txt to prevent re-uploads.

## 🔐 Security Notes
- Your session is stored in uploader_session.session. Do not share this file.
- Make sure your api_id and api_hash are kept safe and never exposed publicly.

## 📬 License
MIT License. Free to use, modify, and share.

Made with ❤️ by Mohamed Faroug



