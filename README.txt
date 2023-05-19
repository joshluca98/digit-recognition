Background Info:
	The goal of this project was to build a machine learning model with Keras/Tensorflow that could analyze a handwritten digit, and output a prediction of what value is represented. I chose to implement this project using Python as suggested by the textbook for this course. At this stage of the project, one must use the command line to interact with the script and run the model. I may implement more features (including a GUI) later down the road if I choose to continue development of this project.

General Info:
	The 'use_model.py' script was designed for the end user to execute directly. When launched, this script will determine if there are any existing models available in the 'generated-models' folder (generated from same script at an earlier time, no third party models). If there is, it will use the existing model to perform the upcoming digit analysis. 

	If there is no existing model found, one will be generated (with user permission) by calling the appropriate functions in the 'generate_model.py' script. The model will be evaluated and output relevant numbers (as a decimal value) representing model accuracy and loss. For example, "0.9733" for model accuracy would represent a 97.33% success rate of the model's predictions on the preinputted test values sourced from the MNIST dataset.

	Once the model has been generated (or found in the existing models folder), it will then be loaded into memory. The default directory for sample digits to run through the model is the 'digit-recognition' directory, which has been preloaded with images of the proper resolution (28x28) and naming scheme (digit0, digit1, digit2, etc). The program will attempt to read each image and make a prediction. Once all the digits have been processed, the script will terminate.

Notes:
- If you wish to use your own images, they must be 28x28 pixels, PNG format, and named as the default images are named: "digit0.png, digit1.png, digit2.png, digit3.png, digit4.png, digit5.png, digit6.png, digit7.png, digit8.png, digit9.png. The default images were created using Microsoft Paint.

Usage:
1. Run the use_model.py script. 
2. Existing model will be located and used if possible, or script will ask to generate a model.
3. Provide a directory name for digit images you wish to test or use the default directory with default images.
4. The model will output its prediction in the command line.