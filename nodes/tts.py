import subprocess
import os
import re

VOICE = "en_US-lessac-medium"

def clean_text(text: str) -> str:
    # remove non-ascii / problematic unicode
    text = text.encode("ascii", "ignore").decode("ascii")

    # collapse whitespace
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def generate_voice(state):
    os.makedirs("assets/audio", exist_ok=True)
    output = "assets/audio/voice.wav"

    safe_script = clean_text(state["script"])

    subprocess.run(
        [
            "piper",
            "--model", VOICE,
            "--output_file", output
        ],
        input=safe_script.encode("utf-8"),
        check=True
    )

    return {
        **state,
        "audio": output
    }
