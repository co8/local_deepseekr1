from ollama import chat
import sys

#text input
prompt = input("Enter prompt (press enter for 'surprise me'): ") or "surprise me"
print(f"Prompt: {prompt}")

stream = chat(
    model='deepseek-r1:8b',
    messages=[{'role': 'user', 'content': prompt}],
    stream=True,
)

reasoning_content = ""
content = ""

for chunk in stream:
    if chunk and 'message' in chunk and chunk['message'].content:
        # Get the content from the chunk
        chunk_content = chunk['message'].content
        
        # Print the content immediately, without newline
        sys.stdout.write(chunk_content)
        sys.stdout.flush()
        
        # Store in appropriate buffer
        if chunk_content.startswith('<think>'):
            in_thinking = True
        elif chunk_content.startswith('</think>'):
            in_thinking = False
        else:
            if 'in_thinking' in locals() and in_thinking:
                reasoning_content += chunk_content
            else:
                content += chunk_content

print("\n\nReasoning:", reasoning_content)
print("\nFinal Answer:", content)
