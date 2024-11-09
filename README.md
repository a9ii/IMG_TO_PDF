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
