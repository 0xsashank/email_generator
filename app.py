import gradio as gr
from email_generator import email_genie

# Create the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# EmailGenie: AI-Powered Cold Email Generator")
    
    with gr.Tab("Email Generator"):
        recipient_name = gr.Textbox(label="Recipient's Name")
        recipient_role = gr.Textbox(label="Recipient's Role")
        company_name = gr.Textbox(label="Company Name")
        industry = gr.Textbox(label="Industry")
        company_details = gr.Textbox(label="Company Details")
        key_points = gr.Textbox(label="Key Points to Cover", lines=3)
        tone = gr.Dropdown(["Formal", "Friendly", "Professional"], label="Tone")
        generate_button = gr.Button("Generate Email")
        output = gr.Textbox(label="Generated Email")

        generate_button.click(
            email_genie, 
            inputs=[recipient_name, recipient_role, company_name, industry, company_details, key_points, tone], 
            outputs=output
        )

if __name__ == "__main__":
    demo.launch()