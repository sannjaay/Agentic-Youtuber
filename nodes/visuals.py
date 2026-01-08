from langchain_ollama import OllamaLLM
def generate_visual_context(state):
    llm = OllamaLLM(model="llama3")
    prompt = f"""
    Break this script into 5 image prompts:
    {state['script']}
    """
    visuals = llm.invoke(prompt)
    prompts = visuals.split("\n")
    return {**state, "image_prompts": prompts}
