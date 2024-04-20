from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Set your OpenAI API key
openai.api_key = "api-key"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user's query
        query = request.form['query']

        # Use the OpenAI API to generate a response
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=f"Search query: {query}",
            max_tokens=4000,
            n=1,
            stop=None,
            temperature=0.7,
        )

        # Extract the generated text from the API response
        generated_text = response.choices[0].text.strip()

        return render_template('index.html', query=query, response=generated_text)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)