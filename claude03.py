# claude03.py, B. Harmon 11/25/2025
# See also ..\pyAI\claude02.py
# Usage: py claude03.py >do_it.py
#   Then edit do_it.py and run it

import anthropic

def do_it():
    """
    Uses Claude Opus 4.5 to do the prompt
    """
    # Initialize the Anthropic client
    # Make sure you have ANTHROPIC_API_KEY set as an environment variable
    #   .\anthropic_apikey.ps1
    client = anthropic.Anthropic()
    
    # Create the prompt
    prompt = """Write a python program to print on one line the fibonacci sequence to 10 terms.
    Provide only the recursive version.  Do not explain it.  Do provide a doc string."""
    
    # Call the Claude API
    message = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=1024,
        system = "You are a principal software engineer.",
        messages=[ 
            {"role": "user", "content": prompt}
        ]
    )
    
    # Extract and print the response
    response_text = message.content[0].text
    # print("Prompt:", prompt)
    # print("\nResponse:")
    print(response_text)

if __name__ == "__main__":
    do_it()

""" Result is below as edited and without doc string
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(' '.join(str(fibonacci(i)) for i in range(10)))
"""
