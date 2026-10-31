
import streamlit as st

from knowledge import (
    load_documents,
    retrieve,
    ollama_generate,
    extractive_answer
)


st.set_page_config(
    page_title="Cynbit Knowledge Copilot",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Cynbit Knowledge Copilot")

st.write(
    "Ask questions about Cynbit using the provided "
    "company information documents."
)

with st.sidebar:

    st.header("Settings")

    use_ollama = st.checkbox(
        "Use local Ollama model",
        value=False
    )

    model = st.text_input(
        "Ollama model",
        value="qwen2.5:3b"
    )

    top_k = st.slider(
        "Number of retrieved passages",
        min_value=1,
        max_value=5,
        value=3
    )

    st.divider()

    st.write("No paid LLM API is used.")

    st.caption(
        "Without Ollama, the application displays "
        "relevant document passages."
    )


records = load_documents()

st.success(
    f"Loaded {len(records)} document passages."
)

question = st.text_input(
    "Enter your question",
    placeholder="Example: What services does Cynbit provide?"
)


if st.button(
    "Ask Question",
    type="primary",
    disabled=not question.strip()
):

    with st.spinner("Searching documents..."):

        passages = retrieve(
            question,
            records,
            top_k=top_k
        )

    if not passages:

        st.warning(
            "I cannot find relevant information "
            "in the provided documents."
        )

    else:

        if use_ollama:

            try:

                with st.spinner(
                    "Generating answer with local Ollama..."
                ):

                    answer = ollama_generate(
                        question,
                        passages,
                        model=model
                    )

                if not answer:
                    answer = extractive_answer(passages)

            except Exception as error:

                st.error(
                    f"Ollama failed: {error}"
                )

                st.info(
                    "Using the extractive fallback instead."
                )

                answer = extractive_answer(passages)

        else:

            answer = extractive_answer(passages)

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Retrieved Sources")

        for passage in passages:

            title = (
                f"{passage['source']} | "
                f"Passage {passage['chunk']} | "
                f"Similarity: {passage['score']:.3f}"
            )

            with st.expander(title):

                st.write(passage["text"])


st.divider()

st.caption(
    "Assessment prototype. Use only approved documents. "
    "Verify generated answers against their sources."
)
