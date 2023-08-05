import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

def same_auth(username, password):
    return username == password

iface = gr.ChatInterface(random_response)

iface.launch(auth=same_auth, server_name="0.0.0.0", server_port=7860)

