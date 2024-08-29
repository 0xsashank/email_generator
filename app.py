import gradio as gr
from email_generator import generate_email
from chat_handler import chat

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# EmailGenie: AI-Powered Cold Email Generator")
    
    with gr.Tab("Chat"):
        chatbot = gr.Chatbot()
        msg = gr.Textbox()
        clear = gr.Button("Clear")

        msg.submit(chat, [msg, chatbot], [msg, chatbot])
        clear.click(lambda: None, None, chatbot, queue=False)

    with gr.Tab("Email Generator"):
        industry = gr.Textbox(label="Industry")
        recipient_role = gr.Textbox(label="Recipient's Role")
        company_details = gr.Textbox(label="Company Details")
        tone = gr.Dropdown(["Formal", "Friendly", "Professional"], label="Tone")
        generate_button = gr.Button("Generate Email")
        output = gr.Textbox(label="Generated Email")

        generate_button.click(generate_email, inputs=[industry, recipient_role, company_details, tone], outputs=output)

if __name__ == "__main__":
    demo.launch()