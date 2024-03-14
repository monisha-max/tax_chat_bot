import openai
import gradio as gr

openai.api_key = "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"
chat_history = []
def CustomChatGPT(user_input, chat_history):
    if chat_history is None:
        chat_history = []
    
    if user_input.strip().lower() == "who are you":
        return "I am a chatbot that answers tax-related queries.", chat_history

    chat_history.append({"role": "user", "content": user_input})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    chat_history.append({"role": "assistant", "content": ChatGPT_reply})

    return ChatGPT_reply, chat_history
css = """
body, html {
    height: 100%;
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    background: #0E2954;
}
body {
    font-family: 'Arial', sans-serif;
    color: #ffffff;
    text-align: center;
}

.gradio_container {
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    background-color: #AD88C6;
    border-radius: 15px;
    overflow: hidden; 
    margin: 20px;
    transition: transform 0.3s ease;
}
.gradio_container:hover {
    transform: translateY(-5px);
}

.gradio_content {
    padding: 2rem; 
}

.input_text, .output_text, textarea, label, button {
    font-size: 1rem;
    border-radius: 5px;
    border: 2px solid #0b3d91;
    padding: 0.5rem;
    margin-top: 0.5rem; 
}

.output_text, label {
    color: #1b2948;
    font-weight: bold;
}

button {
    background-color: #0b3d91;
    color: white;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
}

button:hover {
    background-color: #1c1d67;
}

.title, .description {
    margin-bottom: 2rem;
}

.title {
    font-size: 2rem;
    color: #333333;
}

.description {
    font-size: 1.2rem;
    color: #555555;
}

"""

demo = gr.Interface(
    fn=CustomChatGPT,
    inputs=["text", gr.State()], 
    outputs=["text", gr.State()], 
    title="IntelliTax",
    description="This is an AI-powered tax assistant. Feel free to ask any tax-related questions!",
    css=css
)

demo.launch(share=True)
