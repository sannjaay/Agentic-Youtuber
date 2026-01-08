from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")

def generate_script(state):
    prompt = f"""
Write ONLY the spoken text for a YouTube Shorts script (50–55 seconds).

Rules:
- Output plain text only
- No asterisks (*)
- No sound effects
- No stage directions
- No narrator labels
- No emojis
- No formatting
- Just sentences a person would speak

Topic:
{state["topic"]}
"""

    script = llm.invoke(prompt).strip()

    return {
        **state,
        "script": script
    }
