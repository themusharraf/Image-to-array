import cv2
import numpy as np

# Tasvirni yuklab olish
image_path = 'download.jpeg'  # O'zingizning tasvirning joylashgan manzilini yozing
img = cv2.imread(image_path)

# Tasvirni massivga oʻzlashtirish
img_array = np.array(img)

# Yuz aniqlash uchun kaskad faylni yuklab olish
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Tasvirni grayscale qilish
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Yuzlarni aniqlash
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# Agar yuz topilsa
if len(faces) > 0:
    # Yuzni olish
    x, y, w, h = faces[0]  # Faqat birinchi yuzni olish
    face_img = img[y:y+h, x:x+w]

    # Yuzni massivga oʻzlashtirish

    face_array = np.array(face_img)

    # Massivlar bir biriga tengmi yoki teng emasligini tekshirish
    if np.array_equal(img_array, face_array):
        print("Rasm massivga oʻtkazildi va yuz topildi.")
    else:
        print("Rasm massivga oʻtkazildi, lekin yuz topilmadi.")
else:
    print("Yuz topilmadi.")
