# Force PyTorch to use CPU to avoid device conflicts
from dotenv import load_dotenv
import streamlit as st
import asyncio

from rag_agent import run_rag_agent

load_dotenv()

def main():
    st.title("ChromaDB Basic RAG AI Agent (Simple Version)")

    st.write("This is a simplified version that avoids async complexity.")

    # Chat input for the user
    user_input = st.chat_input("What do you want to know about Pydantic AI?")

    if user_input:
        # Display user prompt in the UI
        with st.chat_message("user"):
            st.markdown(user_input)

        # Display the assistant's response
        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    # Run the RAG agent
                    response = asyncio.run(run_rag_agent(user_input))

                st.markdown(response)

            except Exception as e:
                st.error(f"Error: {e}")
                st.markdown("Sorry, there was an error processing your request.")

if __name__ == "__main__":
    main()