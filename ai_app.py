"""Python app created with streamlit and Cohere API"""

import os

import cohere
from dotenv import load_dotenv

import streamlit as st
from streamlit_chat import message as st_message


from helper import update_history, open_files, prompt_engine
from utils import story_generation, code_explanation, machine_translation, text_summarization, grammer_check, talk_to_the_bot


load_dotenv()
API_KEY = os.environ['API_KEY']

CLIENT = cohere.Client(f"{API_KEY}")


def clear_cache():
    for key in st.session_state.keys():
        del st.session_state[key]


def main():
    """A main function to return output based on user input"""
    st.title("An AI app that can do everything.")

    activities = ['Chatbot', 'Text Summarizer',
                  'Grammer Check', 'Translation',
                  'Story Generation', 'Code Explanation']
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == 'Story Generation':
        clear_cache()
        prompt_input = "Please input a starter and choose theme for a story."
        prompt = prompt_engine(
            prompt=prompt_input,
            max_chars=2000,
            height=320
        )
        theme = ["Sci-Fi", "Horror", "Dystopian",
                 "Time-Loop", "Mystery", "Simple Story", "Mythology"]
        theme_choice = st.selectbox("Pick a theme", theme)
        lines = open_files("story_generation.txt").replace(
            "<<STORY>>", prompt).replace("<<THEME>>", theme_choice)
        story_generation(lines=lines,
                         user_prompt=prompt,
                         co_here=CLIENT, max_tokens=50,
                         temperature=0.5)

    elif choice == "Code Explanation":
        clear_cache()
        prompt_input = "Please input code to get Explanation."
        prompt = st.text_area(
            prompt_input,
            max_chars=2000,
            height=320)
        lines = open_files("code_explanation.txt").replace(
            "<<CONTENT>>", prompt)
        code_explanation(
            lines=lines,
            user_prompt=prompt,
            co_here=CLIENT, max_tokens=40,
            temperature=0.5
        )

    elif choice == "Translation":
        clear_cache()
        prompt_input = "Please input text to translate."
        prompt = st.text_area(
            prompt_input,
            max_chars=2000,
            height=320)
        languages = ['English', 'Japanese',
                     'Chinese', 'French', 'Espanyol', 'Hindi', 'Russian']
        source = st.selectbox("Pick Source Language", languages)
        target = st.selectbox("Pick Target Language", languages)
        lines = open_files("translation.txt").replace(
            "<<SOURCE>>", source) \
            .replace("<<TARGET>>", target).replace("<<CONTENT>>", prompt)

        machine_translation(
            lines=lines,
            user_prompt=prompt,
            co_here=CLIENT,
            max_tokens=len(lines) + 20,
            temperature=0.6
        )

    elif choice == "Grammer Check":
        clear_cache()
        prompt_input = "Please input text."
        prompt = st.text_area(
            prompt_input,
            max_chars=2000,
            height=320)
        lines = open_files("grammer_checker.txt").replace(
            "<<CONTENT>>", prompt)

        grammer_check(
            lines=lines,
            user_prompt=prompt,
            co_here=CLIENT,
            max_tokens=len(prompt) + 50,
            temperature=0.4
        )

    elif choice == "Text Summarizer":
        clear_cache()
        prompt_input = "Enter Text(The language should be English)."
        prompt = st.text_area(
            prompt_input,
            max_chars=4000,
            height=320)
        lines = open_files("text_summarizer.txt").replace(
            "<<CONTENT>>", prompt
        )
        print(lines)
        text_summarization(
            lines=lines,
            user_prompt=prompt,
            co_here=CLIENT,
            max_tokens=150,
            temperature=0.5
        )

    elif choice == "Chatbot":
        predictions = None
        st.header("Hello Chatbot")

        if 'generated' not in st.session_state:
            st.session_state['generated'] = []

        if 'past' not in st.session_state:
            st.session_state['past'] = []

        if "chat" not in st.session_state:
            st.session_state['chat'] = []
            st.session_state.chat.append("""You are a chatbot.
                                         You love talking with humans.
                                         You are intelligent,
                                         smart and loving bot.""")
        st.text_area("Talk to the Bot", key="input_text")
        prompt = st.session_state.input_text
        lines = ""
        if len(st.session_state.chat) >= 1:
            lines += st.session_state.chat[-1].strip()
        else:
            lines = st.session_state.chat[0].strip()

        lines += f"\nPerson A: {prompt}\nchatbot:"

        predictions = talk_to_the_bot(
            co_here=CLIENT,
            lines=lines,
            user_prompt=prompt,
            max_tokens=50,
            temperature=0.5
        )
        if predictions:
            input_and_predictions = f"{predictions}"
            lines = lines + input_and_predictions
            st.session_state.chat.append(lines)
        st.session_state.past.append(prompt)
        st.session_state.generated.append(predictions)

        if st.session_state['generated']:
            for i in range(len(st.session_state['generated'])-1, -1, -1):
                st_message(st.session_state["generated"][i], key=str(i))
                st_message(st.session_state['past'][i],
                           is_user=True, key=str(i) + '_user')


main()
