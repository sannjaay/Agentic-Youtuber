import os
import requests
import urllib.parse

IMAGE_DIR = "assets/images"

def load_existing_images():
    if not os.path.exists(IMAGE_DIR):
        return []

    files = [
        os.path.join(IMAGE_DIR, f)
        for f in os.listdir(IMAGE_DIR)
        if f.lower().endswith((".png", ".jpg", ".jpeg"))
    ]

    return sorted(files)


def generate_images(state):
    os.makedirs(IMAGE_DIR, exist_ok=True)
    image_paths = []

    try:
        for i, prompt in enumerate(state["image_prompts"]):
            encoded = urllib.parse.quote(prompt)
            url = f"https://image.pollinations.ai/prompt/{encoded}"

            response = requests.get(url, timeout=60)
            response.raise_for_status()

            path = os.path.join(IMAGE_DIR, f"{i}.png")
            with open(path, "wb") as f:
                f.write(response.content)

            image_paths.append(path)

        print("IMAGES GENERATED SUCCESSFULLY")

    except Exception as e:
        print("IMAGE GENERATION FAILED:", e)
        print("FALLING BACK TO EXISTING IMAGES")

        image_paths = load_existing_images()

        if not image_paths:
            raise RuntimeError("No existing images available for fallback")

        print(f"USING {len(image_paths)} EXISTING IMAGES")

    return {
        **state,
        "images": image_paths
    }
