from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
import os

def compose_video(state):
    clips = []

    duration_per_image = 5

    for img in state["images"]:
        clip = ImageClip(img).set_duration(duration_per_image)
        clips.append(clip)

    video = concatenate_videoclips(clips, method="compose")

    audio = AudioFileClip(state["audio"])
    video = video.set_audio(audio)

    os.makedirs("assets/video", exist_ok=True)
    output = "assets/video/final.mp4"

    video.write_videofile(
        output,
        fps=24,
        codec="libx264",
        audio_codec="aac"
    )

    return {
        **state,
        "video": output
    }
