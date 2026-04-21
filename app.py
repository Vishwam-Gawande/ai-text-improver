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
        text = text.replace("pls", "").replace("please", "")
        text = text.replace("job", "a job opportunity")
        improved = text.strip().capitalize()
        if not improved.endswith("."):
            improved += "."

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
st.markdown("Improve your text into professional, friendly, or concise style.")

user_input = st.text_area("Enter your text:")
mode = st.selectbox("Choose mode:", ["formal", "friendly", "concise"])


if st.button("✨ Improve Text"):
    if not user_input:
        st.warning("Please enter some text")
    else:
        with st.spinner("Processing..."):
            time.sleep(1)

        result = improve_text(user_input, mode)

        st.subheader("✨ Improved Text:")
        st.write(result["improved_text"])

        st.code(result["improved_text"])