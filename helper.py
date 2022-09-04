import streamlit as st


def get_predictions(
        co_here,
        prompt,
        max_tokens=100,
        temperature=0.7) -> str:
    """
    A function to generate text.

    Parameters:
    ----------------------------
    co_here: cohere.Client -> client to connect cohore.ai

    API_KEY: str -> api key

    prompt: str -> prompt to the model

    max_tokens: int -> max tokens to output , default=30

    temperature: float -> randomness in the model,\
    the higher the value the greater the randomness, default=0.7
    """
    response = co_here.generate(model="xlarge",
                                prompt=prompt, max_tokens=max_tokens,
                                temperature=temperature, stop_sequences=["\n"])
    return response.generations[0].text


def open_files(filename):
    """Read a file and returns lines"""
    with open(filename, "r") as file:
        lines = file.read()
        return lines


def prompt_engine(
        prompt,
        max_chars,
        height):
    """A funtion that returns text area

    Parameters
    -----------

    prompt: str -> prompt to display

    max_chars: int -> maximum number of chars user can input

    height: int -> height of the text-area field

    """
    prompt_input = st.text_area(
        prompt,
        max_chars=max_chars,
        height=height
    )

    return prompt_input


def update_history(
        user_input,
        predictions
):
    """A function that updates the history of streamlit chat


    Parameters
    ----------


    user_input: str -> the user input to the model

    predictions: str -> the output of the model

    """

    st.session_state.history.append({
        "message": user_input, "is_user": True
    })
    st.session_state.history.append({
        "message": predictions,
        "is_user": False
    })
