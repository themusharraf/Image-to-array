from PIL import Image
import numpy as np

image_path = 'taxi.jpg'  # O'zingizning tasvirning joylashgan manzilini yozing # noqa
img = Image.open(image_path)

# Tasvirni massivga o'zlashtirish  # noqa
img_array = np.array(img)

# Natijani tekshirish  # noqa
print(img_array)
