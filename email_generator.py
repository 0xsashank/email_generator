import ollama

client = ollama.Client()

def generate_email(recipient_name, recipient_role, company_name, industry, company_details, key_points, tone):
    prompt = f"""
    Generate a personalized cold outreach email based on the following details:
    Recipient's Name: {recipient_name}
    Recipient's Role: {recipient_role}
    Company Name: {company_name}
    Industry: {industry}
    Company Details: {company_details}
    Key Points to Cover: {key_points}
    Desired Tone: {tone}

    The email should be concise, engaging, and tailored to the recipient's name, role, and company.
    Ensure the content is relevant and compelling, incorporating the key points provided.
    Use the specified tone throughout the email.
    """
    
    response = client.generate(model='llama3', prompt=prompt)
    return response['response']

def email_genie(recipient_name, recipient_role, company_name, industry, company_details, key_points, tone):
    email = generate_email(recipient_name, recipient_role, company_name, industry, company_details, key_points, tone)
    return f"Here's your personalized email:\n\n{email}"
