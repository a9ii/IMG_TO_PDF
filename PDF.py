import os
import telebot
from PIL import Image
from io import BytesIO
import zipfile

# Replace 'YOUR_BOT_TOKEN' with your bot's token
bot = telebot.TeleBot("YOUR_BOT_TOKEN")

# Dictionary to store image files for each user
user_image_files = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    user_id = message.from_user.id
    user_image_files[user_id] = []  # Initialize list for the user
    bot.reply_to(message, "مرحبًا! قم بإرسال الصور التي تريد تحويلها إلى ملف PDF باستخدام الأمر /pdf.")

@bot.message_handler(commands=['pdf'])
def request_pdf(message):
    user_id = message.from_user.id
    user_image_files[user_id] = []  # Initialize list for the user
    bot.reply_to(message, "قم بإرسال الصور التي تريد تحويلها إلى ملف PDF.")

@bot.message_handler(content_types=['photo', 'document'])
def receive_photo(message):
    user_id = message.from_user.id
    file_id = message.document.file_id if message.content_type == 'document' else message.photo[-1].file_id
    
    # Ensure user_id is in user_image_files dictionary
    if user_id not in user_image_files:
        user_image_files[user_id] = []

    # Check if file_id already exists for the user
    if file_id not in [file["file_id"] for file in user_image_files[user_id]]:
        file_info = bot.get_file(file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        if message.content_type == 'document':
            # Check if the document is a zip file
            if message.document.mime_type == 'application/zip':
                # Extract images from the zip file
                zip_file = zipfile.ZipFile(BytesIO(downloaded_file))
                for file_name in zip_file.namelist():
                    if file_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                        img_data = zip_file.read(file_name)
                        img = Image.open(BytesIO(img_data))
                        file_id = f"{file_id}_{file_name}"
                        file_name = f"image_{file_id}.jpg"
                        img.save(file_name)
                        user_image_files[user_id].append({"file_id": file_id, "file_name": file_name})
            else:
                bot.reply_to(message, "تم استلام الملف بنجاح.")
        else:
            file_extension = file_info.file_path.split('.')[-1].lower()
            if file_extension in ['jpg', 'jpeg', 'png', 'gif']:
                file_name = f"image_{file_id}.{file_extension}"
                # Save the file to the 'PDF' folder
                save_path = f"PDF/{file_name}"
                with open(save_path, 'wb') as new_file:
                    new_file.write(downloaded_file)
                user_image_files[user_id].append({"file_id": file_id, "file_name": save_path})
            else:
                bot.reply_to(message, "تم استلام الملف بنجاح.")

        num_images_received = len(user_image_files[user_id])
        bot.reply_to(message, f"تم استلام الصور بنجاح, عدد الصور المستلمة {num_images_received}.")
    else:
        bot.reply_to(message, "هذه الصورة تم استلامها مسبقًا.")

@bot.message_handler(commands=['done'])
def create_pdf(message):
    user_id = message.from_user.id
    if not user_image_files[user_id]:
        bot.reply_to(message, "لم يتم استلام أي صور بعد.")
        return

    bot.reply_to(message, "يرجى إرسال اسم الملف لتغييره:")
    bot.register_next_step_handler(message, process_filename)

def process_filename(message):
    user_id = message.from_user.id
    filename = message.text.strip() + "@al_safwa_ed24.pdf"
    pdf_path = f"PDF/{filename}"

    images = []

    for file in user_image_files[user_id]:
        try:
            with Image.open(file["file_name"]) as img:
                images.append(img.copy())  # Create a copy to avoid issues with file pointers
        except Exception as e:
            bot.reply_to(message, f"حدث خطأ أثناء فتح صورة: {e}")
            return

    if not images:
        bot.reply_to(message, "لم يتم العثور على صور صالحة.")
        return

    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    bot.send_document(message.chat.id, open(pdf_path, "rb"))

    # Remove the image files after creating the PDF
    for file in user_image_files[user_id]:
        os.remove(file["file_name"])
    del user_image_files[user_id]




bot.polling()

