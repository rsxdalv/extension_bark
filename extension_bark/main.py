import gradio as gr
from extension_bark.bark_tab import bark_ui
from extension_bark.voices.voices_tab import voices_tab
from extension_bark.settings_tab_bark import settings_tab_bark
from extension_bark.vocos_tab_bark import vocos_tab_bark

def ui():
    with gr.Tabs():
        with gr.Tab("Generation"):
            bark_ui()
        # tab_voice_clone()

        voices_tab()
        settings_tab_bark()
        vocos_tab_bark()

def extension__tts_generation_webui():
    ui()
    return {
        "package_name": "extension_bark",
        "name": "Bark",
        "version": "0.0.1",
        "requirements": "git+https://github.com/rsxdalv/extension_bark@main",
        "description": "Bark: A text-to-speech model",
        "extension_type": "interface",
        "extension_class": "text-to-speech",
        "author": "Suno",
        "extension_author": "rsxdalv",
        "license": "MIT",
        "website": "https://github.com/suno-ai/bark",
        "extension_website": "https://github.com/rsxdalv/extension_bark",
        "extension_platform_version": "0.0.1",
    }




if __name__ == "__main__":
    if "demo" in locals():
        locals()["demo"].close()
    with gr.Blocks() as demo:
        ui()
    demo.launch()
