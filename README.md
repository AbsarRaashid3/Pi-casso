# Pi'casso - Emoji Math Solver 🤖

Pi'casso is an AI-powered application that solves emoji-based math riddles! It utilizes a 
custom-trained language model fine-tuned on a dataset of emoji math problems. 
Users can input riddles in the form of emoji equations, and the AI will 
provide the correct answer.

## Features
**Solve emoji-based math riddles such as "🚀 + 🚀 = 18".**
**Uses a fine-tuned language model for high accuracy.**
**Deploys the model with Streamlit to create an interactive web interface.**
**Optimized for GPU usage with quantization and offloading.**
**Accessible via a public URL using ngrok for easy sharing.**

## Installation
1)Clone the repository:
```
git clone https://github.com/absarraashid3/picasso.git
cd picasso
```

2)Set up a Python environment (optional but recommended):
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3)Install dependencies:
```
pip install -r requirements.txt
```
4)Install additional dependencies if required:
```
pip install pyngrok
```
**The requirements.txt file includes all the necessary dependencies such as torch, transformers, datasets, peft, and streamlit.**

## Dataset
The dataset used to train the model consists of emoji-based math problems. Each entry in the dataset contains an emoji math equation along with its solution. The data is in CSV format.
**You can find the dataset in the emoji_math_dataset_utf8.csv file.**

## Model Training
The model used in Pi'casso is based on the Qwen1.5-4B-Chat architecture and fine-tuned using LoRA (Low-Rank Adaptation) for efficient training.

## Steps for training the model:
### Preprocess the Dataset:
Convert the dataset to a format that can be used by Hugging Face’s datasets library.
Map the dataset to the required format for model training.
### Model Fine-Tuning:
Use LoRA for efficient fine-tuning, which helps to reduce the memory usage and improve training efficiency.
Quantize the model to 4-bit precision for even lower memory consumption, using BitsAndBytesConfig.
### Training the Model:
The model is fine-tuned for 9 epochs using the Trainer class from Hugging Face. A test set is also used for evaluation.
### Saving the Model:
After training, the model and tokenizer are saved for deployment.

## App Deployment
### Streamlit Interface:
Pi'casso comes with an interactive Streamlit UI. The app allows users to input emoji math riddles, and the AI generates answers.

### Model Loading:
The model is loaded with automatic device detection (GPU/CPU) for optimal performance.
Quantization is applied for memory optimization.

### Running the App:
Once the model is loaded, the user can enter a riddle and the model will generate the answer.
The app uses torch for generating predictions and streamlit for the user interface.

### Steps for deploying the app:
Run the Streamlit App: To start the app, run the following command:
```
streamlit run app.py
```
Expose the app publicly using ngrok: After starting the app, you can expose it to the public by using ngrok:
```
ngrok http 8501
```
This will provide a public URL that can be shared with others.


## Usage
**After running the app, follow these steps:**
Enter an Emoji Math Riddle:
Input an emoji equation such as:

"🚀 + 🚀 = 18"
"🍕 + 🍕 + 🍕 + 🍕 = 16"
Press the Solve Button:
The AI will process the input and generate an answer.
View the Answer:
The result will be displayed on the Streamlit app.


