import os
from keras import models
from keras import layers
from keras_preprocessing.image import ImageDataGenerator

DATA_DIR = os.path.join(os.getcwd(), "data")
TRAIN_DATA_DIR = os.path.join(DATA_DIR, "train")
TEST_DATA_DIR = os.path.join(DATA_DIR, "test")

training_datagen = ImageDataGenerator(
    rescale=1.0 / 255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode="nearest",
)

train_generator = training_datagen.flow_from_directory(
    TRAIN_DATA_DIR, target_size=(150, 150), class_mode="binary", batch_size=128
)

validation_datagen = ImageDataGenerator(rescale=1.0 / 255)

validation_generator = validation_datagen.flow_from_directory(
    TEST_DATA_DIR, target_size=(150, 150), class_mode="binary", batch_size=128
)

model = models.Sequential(
    [
        layers.Conv2D(64, (3, 3), activation="relu", input_shape=(150, 150, 3)),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(64, (3, 3), activation="relu"),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.MaxPooling2D(2, 2),
        layers.Conv2D(128, (3, 3), activation="relu"),
        layers.MaxPooling2D(2, 2),
        layers.Flatten(),
        layers.Dropout(0.5),
        layers.Dense(512, activation="relu"),
        layers.Dense(1, activation="sigmoid"),
    ]
)

model.compile(optimizer="rmsprop", loss="binary_crossentropy", metrics=["accuracy"])

model.fit(
    train_generator,
    validation_data=validation_generator,
    epochs=25,
    batch_size=128,
    verbose=1,
    validation_steps=3,
)

model.save(os.path.join(os.getcwd(), "models", "CatVsDog.h5"))