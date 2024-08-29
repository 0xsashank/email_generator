import ollama

client = ollama.Client()

def generate_email(industry, recipient_role, company_details, tone):
    prompt = f"""
    Generate a personalized cold outreach email based on the following details:
    Industry: {industry}
    Recipient's Role: {recipient_role}
    Company Details: {company_details}
    Desired Tone: {tone}

    The email should be concise, engaging, and tailored to the recipient's industry and role.
    Ensure the content is relevant and compelling to increase engagement and conversion rates.
    """
    
    response = client.generate(model='llama3', prompt=prompt)
    return response['response']

def email_genie(industry, recipient_role, company_details, tone):
    # Your email generation logic here
    generated_email = f"Generated email for {industry} industry, {recipient_role}, with {tone} tone."
    return generated_email
