import random
import gradio as gr

def random_response(message, history):
    return random.choice(["Yes", "No"])

def same_auth(username, password):
    return username == password

demo = gr.ChatInterface(random_response)

demo.launch(auth=same_auth)

