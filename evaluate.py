import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np

# Load model
model = tf.keras.models.load_model(
    "models/plant_disease_model.keras"
)

# Test Data
test_datagen = ImageDataGenerator(rescale=1./255)

test_generator = test_datagen.flow_from_directory(
    "Datasets/test",
    target_size=(224,224),
    batch_size=32,
    class_mode='categorical',
    shuffle=False
)

# Evaluate
loss, accuracy = model.evaluate(test_generator)

print(f"\nTest Accuracy: {accuracy*100:.2f}%")

# Predictions
preds = model.predict(test_generator)

y_pred = np.argmax(preds, axis=1)
y_true = test_generator.classes

print("\nClassification Report:\n")

print(
    classification_report(
        y_true,
        y_pred,
        target_names=list(test_generator.class_indices.keys())
    )
)

# Confusion Matrix
print("\nConfusion Matrix:\n")

print(confusion_matrix(y_true, y_pred))