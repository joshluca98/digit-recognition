import os
import tensorflow as tf
import absl.logging

# hide unnecessary warnings in command line
absl.logging.set_verbosity(absl.logging.ERROR)

# load and normalize MNIST dataset
def load_mnist():
    try:
        mnist = tf.keras.datasets.mnist
        (trainX, trainY), (testX, testY) = mnist.load_data()
        trainX = tf.keras.utils.normalize(trainX, axis=1)
        testX = tf.keras.utils.normalize(testX, axis=1)
        print("\nMNIST dataset imported successfully.\n")
        return trainX, trainY, testX, testY
    except:
        print("Error: failed to import MNIST dataset. Aborting...")
        exit()

# define, compile, and fit model
def build_model():
    try:
        model = tf.keras.models.Sequential()
        model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(128, activation='relu'))
        model.add(tf.keras.layers.Dense(10, activation='softmax'))
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(trainX, trainY, epochs=8)
        print(f"\nModel built successfully.\n")
        return model
    except:
        print("Error: failed to build model. Aborting...")
        exit()

# save model to the working directory allowing later use
def save_model():
    try:
        model.save('generated-models\digit-analysis-model')
        print("Model saved successfully.\n")
    except:
        print("Error: failed to save model to current directory. Aborting...")
        exit()

# load model from working directory to confirm successful save
def load_model():
    try:
        model = tf.keras.models.load_model('generated-models\digit-analysis-model')
        print("Model loaded successfully.\n")
        return model
    except:
        print("Error: failed to load model. Aborting...")
        exit()

# evaluate model performance on test data
def evaluate_model():
    try:
        loss, accuracy = model.evaluate(testX, testY)
        print("\nModel evaluated successfully:\n")
        print(f"    Model Accuracy: {accuracy}")
        print(f"    Model Loss: {loss}\n")
        return loss, accuracy
    except:
        print("Error: failed to evaluate model. Aborting...")
        exit()

if os.path.isdir("generated-models\digit-analysis-model"):
    print("Model already exists. Using existing model.")
else:
    confirmNewModel = input("\nNo model found. Press ENTER to generate model, or type \"a\" to abort: ")
    while confirmNewModel != "" and confirmNewModel != "a":
            confirmNewModel = input("No model found. Press ENTER to generate model, or type \"a\" to abort: ")
    if confirmNewModel == "a":
        print("Aborting...")
        exit()

    print("\nGenerating new model based on presets.")
    trainX, trainY, testX, testY = load_mnist()
    model = build_model()
    save_model()
    model = load_model()
    evaluate_model()
    print("Script ran successfully. Model has been generated and saved to working directory.")