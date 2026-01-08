from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def generate_topic(state):
    topic = llm.invoke(
        "Give 1 random fun fact topic for a YouTube Shorts video."
    )

    return {
        **state,
        "topic": topic
    }
