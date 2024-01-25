from PIL import Image
import numpy as np

# Tasvirni yuklab olish
image_path = 'taxi.jpg'  # O'zingizning tasvirning joylashgan manzilini yozing # noqa
img = Image.open(image_path)

# Tasvirni massivga o'zlashtirish  # noqa
img_array = np.array(img)

# Natijani tekshirish
print(img_array)
