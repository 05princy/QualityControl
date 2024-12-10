import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

# Load the TensorFlow model
model = load_model("tasks\m.h5")

# Class names
class_names = {
    0: 'fresh_apple',
    1: 'fresh_banana',
    2: 'fresh_bitter_gourd',
    3: 'fresh_capsicum',
    4: 'fresh_orange',
    5: 'fresh_tomato',
    6: 'stale_apple',
    7: 'stale_banana',
    8: 'stale_bitter_gourd',
    9: 'stale_capsicum',
    10: 'stale_orange',
    11: 'stale_tomato'
}

def detect_freshness(image_path):
    """Detect freshness of produce."""
    img = load_img(image_path, target_size=(128, 128))
    img_array = img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_index = np.argmax(prediction, axis=-1)[0]
    return class_names.get(class_index, "Unknown")
