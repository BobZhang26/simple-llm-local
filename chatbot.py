from transformers import AutoModelForCausalLM, AutoTokenizer

# Load GPT-2 model and tokenizer
model_name = "gpt2"  # You can replace this with another model like 'gpt2-medium'
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequences=1)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

# Main chatbot loop
if __name__ == "__main__":
    print("Chatbot is ready! Type 'exit' to end the chat.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        # Generate response
        response = generate_response(user_input)
        print(f"Chatbot: {response}")