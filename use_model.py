import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from generate_model import *

# load existing model or generate model if not found
def this_load_model():
    try:
        model = tf.keras.models.load_model('generated-models\digit-analysis-model')
        print("\nModel loaded successfully.\n")
        return model
    except:
        print("Error: failed to load model. Aborting...")


# determine directory of files to be inputted to the model
def define_directory():
    print("\nEnter directory name where test images are stored or press ENTER to use default directory.\n")
    while True:
        directory = input("Directory Name: ")
        if directory == "a":
            print("Aborting...")
            exit()
        elif directory == "":
            directory = "test-digits"
            print("\nUsing default \"test-digits\" directory. ", end="")
            if os.path.isdir(directory):
                print("Directory has been found.")
                return directory
            else:
                print("Default directory is missing. Aborting..")
                exit()
        else:
            if os.path.isdir(directory):
                print(f"Using \"{directory}\" directory.")
                return directory
            else:
                print("Invalid directory, try again or type \"a\" to abort.")
    

# takes images as input to the model and outputs a prediction
def use_model():
    directory = define_directory()
    model = this_load_model()
        
    img_num = 0
    while os.path.isfile(f"{directory}/digit{img_num}.png"):
        try:
            img = cv2.imread(f"test-digits/digit{img_num}.png")[:,:,0]
            img = np.invert(np.array([img]))
            print(f"\"digit{img_num}.png\" read successfully.")
            prediction = model.predict(img)
            print("Image prediction made")
            print(f"Model Prediction: This digit is probably a {np.argmax(prediction)}.\n")
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()
        except:
            print("Error..moving on to next image.")
        finally:
            img_num += 1
    print("All images have been processed.\n")

# Function call to start the script
use_model()