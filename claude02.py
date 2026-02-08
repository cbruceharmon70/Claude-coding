# claude02.py, B. Harmon 11/5/2025

import anthropic

def summarize_emma():
    """
    Uses Claude 3.5 Haiku to summarize the novel Emma
    """
    # Initialize the Anthropic client
    # Make sure you have ANTHROPIC_API_KEY set as an environment variable
    client = anthropic.Anthropic()
    
    # Create the prompt
    prompt = "Summarize the novel Emma in 100 words"
    
    # Call the Claude API
    message = client.messages.create(
        model="claude-3-5-haiku-20241022",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    
    # Extract and print the response
    response_text = message.content[0].text
    print("Prompt:", prompt)
    print("\nResponse:")
    print(response_text)
    
    return response_text

if __name__ == "__main__":
    summarize_emma()