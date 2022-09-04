import streamlit as st

from helper import open_files, get_predictions, update_history


def story_generation(
        lines,
        user_prompt,
        co_here,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """
    if st.button("Generate"):
        with st.spinner("Please wait"):
            predictions = get_predictions(
                co_here,
                lines,
                max_tokens,
                temperature
            )
            outputs = user_prompt + predictions
            st.text_area(value=outputs, label="Outputs(you can paste the outputs \
                                    above to generate longer stories)",
                         height=320)


def code_explanation(
        lines,
        user_prompt,
        co_here,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """
    if st.button("Explain"):
        if len(user_prompt) <= 2:
            st.error("Please input something meaningful.")
        else:
            with st.spinner("Please wait"):
                predictions = get_predictions(
                    co_here,
                    lines,
                    max_tokens,
                    temperature
                )
                st.write(predictions)


def machine_translation(
        lines,
        user_prompt,
        co_here,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """
    if st.button("Translate"):
        if len(user_prompt) <= 2:
            st.error("Please input something meaningful.")
        else:
            with st.spinner("Please wait"):
                predictions = get_predictions(
                    co_here,
                    lines,
                    max_tokens,
                    temperature
                )
                st.write(predictions)


def grammer_check(
        lines,
        user_prompt,
        co_here,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """
    if st.button("Grammer Check"):
        if len(user_prompt) <= 2:
            st.error("Please input something meaningful.")
        else:
            with st.spinner("Please wait"):
                predictions = get_predictions(
                    co_here,
                    lines,
                    max_tokens,
                    temperature
                )
                st.write(predictions)


def text_summarization(
        lines,
        user_prompt,
        co_here,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """
    if st.button("Summarize"):
        if len(user_prompt) <= 100:
            st.error(
                "Add more text. The length of the \
                text should be more than 100.")
        else:
            with st.spinner("Please wait"):
                predictions = get_predictions(
                    co_here,
                    lines,
                    max_tokens,
                    temperature
                )
                print(predictions)
                st.write(predictions)


def talk_to_the_bot(
        lines,
        co_here,
        user_prompt,
        max_tokens,
        temperature
):
    """
    Returns outputs

    Parameters:
    --------------
    lines: str -> full data to give to the model

    user_prompt: str -> user inputted data

    co_here: cohere.Client -> client to connect to api server

    max_tokens: int -> maximum number of tokens to use

    temperature: float -> the randomness in the model
    """

    if st.button("Send"):
        if len(user_prompt) <= 1:
            st.error(
                "Input something meaningful")
        else:
            predictions = get_predictions(
                co_here,
                lines,
                max_tokens,
                temperature
            )
            return predictions
