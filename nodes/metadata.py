import json
from langchain_ollama import OllamaLLM
def generate_metadata(state):
    llm = OllamaLLM(model="llama3")
    prompt = f"""
    Return JSON ONLY:
    {{
      "title": "",
      "description": "",
      "tags": []
    }}

    Based on script:
    {state["script"]}
    """

    result = llm.invoke(prompt)
    meta = json.loads(result)

    return {
        **state,
        "title": meta["title"],
        "description": meta["description"],
        "tags": meta["tags"]
    }
