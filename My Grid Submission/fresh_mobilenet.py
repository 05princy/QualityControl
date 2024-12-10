import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, ImageDataGenerator
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models
import numpy as np
from tensorflow.keras.preprocessing import image

import os
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img
import tensorflow as tf
from tensorflow.keras.models import load_model

# Visualizing sample images from the dataset
def visualize_sample_images(dataset_dir, categories):
    n = len(categories)
    fig, axs = plt.subplots(1, n, figsize=(20, 5))
    for i, category in enumerate(categories):
        folder = os.path.join(dataset_dir, category)
        image_file = os.listdir(folder)[0]
        img_path = os.path.join(folder, image_file)
        img = load_img(img_path)
        axs[i].imshow(img)
        axs[i].set_title(category)
    plt.tight_layout()
    plt.show()

dataset_base_dir = '/kaggle/input/fresh-and-stale-classification/dataset'  # Change this to your actual dataset path
train_dir = os.path.join(dataset_base_dir, 'Train')
# class_names = {
#     0: 'fresh_apple',
#     1: 'fresh_banana',
#     2: 'fresh_bitter_gourd',
#     3: 'fresh_capsicum',
#     4: 'fresh_orange',
#     5: 'fresh_tomato',
#     6: 'stale_apple',
#     7: 'stale_banana',
#     8: 'stale_bitter_gourd',
#     9: 'stale_capsicum',
#     10: 'stale_orange',
#     11: 'stale_tomato'
# }
categories = ['freshapples', 'rottenapples', 'freshbanana', 'rottenbanana']  # Add more categories as needed
visualize_sample_images(train_dir, categories)

# Image data generator
from tensorflow.keras.preprocessing.image import ImageDataGenerator

batch_size = 32
img_height = 180
img_width = 180

train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2)  # Using 20% of the data for validation

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',  # Use 'categorical' for more than two classes
    subset='training')

validation_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation')

# Importing MobileNetV2
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras import layers, models

# Load MobileNetV2 pre-trained model + higher level layers
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

# Freeze the base model to retain the pre-trained features
base_model.trainable = False

# Create the custom model on top of MobileNetV2
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    layers.Dense(len(categories), activation='softmax')  # Use softmax for multi-class classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='categorical_crossentropy',  # Use 'categorical_crossentropy' for multi-class
              metrics=['accuracy'])

# Train the model
epochs = 10
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size)

# Evaluate the model
eval_result = model.evaluate(validation_generator)
print(f"Validation Loss: {eval_result[0]}, Validation Accuracy: {eval_result[1]}")

# Save the model to .h5 file
model.save('m.h5')

