from langgraph.graph import StateGraph

from nodes.topic import generate_topic
from nodes.script import generate_script
from nodes.tts import generate_voice
from nodes.visuals import generate_visual_context
from nodes.image_gen import generate_images
from nodes.video import compose_video
from nodes.metadata import generate_metadata
from nodes.upload import upload_video
from nodes.logger import log_status

graph = StateGraph(dict)


graph.add_node("topic", generate_topic)
graph.add_node("script", generate_script)
graph.add_node("tts", generate_voice)
graph.add_node("visuals", generate_visual_context)
graph.add_node("images", generate_images)
graph.add_node("video", compose_video)
graph.add_node("meta", generate_metadata)
graph.add_node("upload", upload_video)
graph.add_node("log", log_status)

graph.set_entry_point("topic")

graph.add_edge("topic", "script")
graph.add_edge("script", "tts")
graph.add_edge("tts", "visuals")
graph.add_edge("visuals", "images")
graph.add_edge("images", "video")
graph.add_edge("video", "meta")
graph.add_edge("meta", "upload")
graph.add_edge("upload", "log")

app = graph.compile()


def run_graph():
    app.invoke({})
