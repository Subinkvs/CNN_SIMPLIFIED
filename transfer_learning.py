from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model

# Load pretrained model
base_model = MobileNetV2(weights='imagenet', include_top=False)

# Freeze base model
for layer in base_model.layers:
    layer.trainable = False

# Add custom classifier
x = base_model.output
x = Flatten()(x)
output = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.summary()