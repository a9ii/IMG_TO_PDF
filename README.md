# 🖼️ Telegram Bot: Image to PDF Converter

A Telegram bot that allows users to upload images and convert them into a single PDF file. This bot can process both single images and images inside a zip file. Built using Python's `telebot` library and `Pillow` for image processing.

## 🚀 Features
- Convert uploaded images or zipped image files into a PDF.
- User-friendly commands to start the process and manage files.
- Saves images temporarily and deletes them after PDF creation to free up resources.
  
## 🛠️ Prerequisites

- Python 3.x
- [pyTelegramBotAPI](https://pypi.org/project/pyTelegramBotAPI/) (Telebot)
- [Pillow](https://pillow.readthedocs.io/) for image handling.

To install the necessary libraries, use:
```bash
pip install pyTelegramBotAPI Pillow
```

1. Clone the repository:
   ```bash
   git clone https://github.com/a9ii/IMG_TO_PDF.git
   cd IMG_TO_PDF
   ```

2. Replace `'Your_Token'` with your bot token from [BotFather](https://core.telegram.org/bots#botfather).

3. Run the bot:
   ```bash
   python bot.py
   ```

## 📌 Bot Commands

- **`/start`**: Initializes the bot and welcomes the user.
- **`/pdf`**: Starts the process for uploading images. Users can upload images or zip files containing images after this command.
- **`/done`**: After uploading images, use this command to finalize and convert the images to a PDF.

## 🧩 Code Overview

### Key Parts of the Code

- **`user_image_files` Dictionary**: Stores user-specific images for PDF creation.
- **`@bot.message_handler(commands=['start'])`**: Initializes a session for each user and stores their uploaded images.
- **Image Upload Handling**: Accepts both photo files and zipped image files. Images are stored temporarily and added to the PDF.
- **PDF Generation**: Upon `/done`, all images are compiled into a PDF file and sent back to the user.

### Example Usage

1. **Start the bot** with `/start`.
2. **Upload images** one by one or in a zip file after `/pdf`.
3. **Create the PDF** by using the `/done` command. The bot will ask for a filename and then send the compiled PDF back.

## ⚠️ Important Notes

- **Temporary Storage**: Images are temporarily saved and deleted after PDF generation to conserve storage.
- **Image Formats**: Supports `jpg`, `jpeg`, `png`, and `gif` formats.
- **Error Handling**: Notifies the user if a file type is unsupported or if an error occurs during processing.

## 📄 Sample Code

```python
import os
import telebot
from PIL import Image
from io import BytesIO
import zipfile

# Initialize the bot
bot = telebot.TeleBot("Your_Token") 

# Code continues...
```

## 🤝 Contributing

Feel free to submit pull requests or open issues if you have ideas to improve this bot.

---

🌟 **If you find this bot useful, give this repository a star!** 🌟
