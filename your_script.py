import torch
import streamlit as st
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

model_path = "./emoji_math_model"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.pad_token = tokenizer.eos_token  # Ensure padding token

# Set quantization to reduce memory usage
quantization_config = BitsAndBytesConfig(load_in_8bit=True)  # Change to load_in_4bit=True if needed

# Load model with device auto-detection and offloading
try:
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="auto",  # Automatically selects best device (GPU if available)
        offload_folder="./offload_dir",  # Offloads large layers to disk if needed
        quantization_config=quantization_config  # Apply quantization
    )
except Exception as e:
    print(f"Failed to load on GPU, switching to CPU: {e}")
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        device_map="cpu"  # Fallback to CPU if necessary
    )

print("Model loaded successfully!")


# ✅ Streamlit UI
st.title("🤖PI'CASSO")
st.write("Enter an emoji-based math problem, and the AI will solve it!")

prompt = st.text_input("Enter an emoji math riddle:", "")

if st.button("Solve"):
    if prompt:
        input_text = f"Riddle: {prompt}\nAnswer:"
        device = "cuda" if torch.cuda.is_available() else "cpu"
        inputs = tokenizer(input_text, return_tensors="pt").to(device)

        # ✅ Generate response
        output = model.generate(
            **inputs, max_length=60, num_return_sequences=1,
            do_sample=True, temperature=0.7, top_p=0.9
        )
        result = tokenizer.decode(output[0], skip_special_tokens=True)

        st.success(f"🤖 Answer: {result}")
    else:
        st.warning("Please enter a valid riddle.")
