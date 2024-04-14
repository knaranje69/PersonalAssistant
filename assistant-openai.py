import openai
import emoji
# Set your OpenAI API key
api_key = "api-key"
openai.api_key = api_key

# Define the user input
#user_input = input()

#conversation_history = []

print(f"Hello Sir, I'm Jarsirlex here! Happy to help", "\U0001F600") 
#print(emoji.emojize('thumbs_up:'))

# Generate a completion using the GPT-3.5 model
while True:
	print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
	question = input("\n\nHow can I help? (or 'q' to exit): ")
	
	if question.lower() == 'q':
		break
	
	#conversation_history.append(f"Human: {question}")	

	#prompt = "\n".join(conversation_history)	

	response = openai.Completion.create(
    		engine="gpt-3.5-turbo-instruct",
    		prompt=question,   # for history-> prompt=prompt
		max_tokens=1024,
		n=1,
		temperature=0.7
	)

# Print the generated response
	print(response.choices[0].text)