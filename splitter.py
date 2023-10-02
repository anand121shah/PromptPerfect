def split_long_prompt(text, max_length=1500):
    words = text.split()
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk + word) <= max_length:
            current_chunk += " " + word
        else:
            chunks.append(current_chunk.strip())
            current_chunk = word

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

# Example usage
long_text = "This is a very long text that needs to be split into smaller chunks for processing."
max_length = 20  # Replace with the actual maximum length you need
chunks = split_long_prompt(long_text, max_length)

for i, chunk in enumerate(chunks):
    print(f"Chunk {i+1}: {chunk}")
