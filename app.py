import streamlit as st
import time


PROMPTS = {
    "formal": "Improve the text professionally.",
    "friendly": "Make the text friendly and casual.",
    "concise": "Make the text short and clear."
}


def improve_text(text, mode):
    original_text = text
    selected_prompt = PROMPTS.get(mode, "")

    replacements = {
        "pls": "please",
        "asap": "as soon as possible",
        "i want": "I would like",
        "i need": "I am seeking"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    if mode == "formal":
        text = text.replace("pls", "")
        text = text.replace("please", "")
        text = text.replace("job", "a job opportunity")
        improved = (text.strip() + ".").capitalize()

    elif mode == "friendly":
        improved = "Hey! " + text.capitalize() + " 😊"

    elif mode == "concise":
        improved = text.capitalize()

    else:
        improved = text.capitalize()

    return {
        "input_text": original_text,
        "mode": mode,
        "prompt_used": selected_prompt,
        "improved_text": improved,
        "status": "success"
    }


st.title("🔥 AI Text Improver")
st.write("Improve your text in different styles using AI-like logic.")

user_input = st.text_area("Enter your text:")
mode = st.selectbox("Choose mode:", ["formal", "friendly", "concise"])


if st.button("✨ Improve Text"):
    st.write("Processing....")
    time.sleep(1)

    result = improve_text(user_input, mode)
    st.success("Text improved successfully!")

    st.json(result)