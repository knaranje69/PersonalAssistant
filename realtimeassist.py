import openai
import requests
import datetime
import pytz

# Set your OpenAI API key
openai.api_key = "api-key"

# Set your OpenWeatherMap API key and base URL
weather_api_key = "api-key"
weather_base_url = "https://api.openweathermap.org/data/2.5/weather"

def display_current_date():
    # Get the current date
    current_date = datetime.date.today()
    formatted_date = current_date.strftime('%Y-%m-%d')
    return formatted_date

def display_current_time(timezone):
    try:
        # Get the current time in the specified timezone
        local_timezone = pytz.timezone(timezone)
        current_time = datetime.datetime.now(local_timezone)
        formatted_time = current_time.strftime('%H:%M:%S')
        return formatted_time
    except pytz.exceptions.UnknownTimeZoneError:
        return "Unknown timezone"

print("Hello Sir, I'm Jarsirlexa here! Happy to help")

# Generate a completion using the GPT-3.5 model
while True:
    print("\n<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
    question = input("\n\nHow can I help? (or 'q' to exit): ")
    
    if question.lower() == 'q':
        break
    
    # Handle weather queries
    if 'weather' in question.lower():
        city = input("Which city's weather would you like to know? ")
        weather_params = {
            'q': city,
            'appid': weather_api_key,
            'units': 'metric'
        }
        
        try:
            response = requests.get(weather_base_url, params=weather_params)
            if response.status_code == 200:
                weather_data = response.json()
                temperature = weather_data['main']['temp']
                description = weather_data['weather'][0]['description']
                weather_response = f"The weather in {city} is currently {description} with a temperature of {temperature}°C."
                print(weather_response)
            else:
                print(f"Failed to fetch weather data for {city}. Please try again.")
        except Exception as e:
            print(f"An error occurred while fetching weather data: {str(e)}")

        continue

    # Handle date and time queries
    if 'date' in question.lower():
        # Display the current date
        formatted_date = display_current_date()
        print(f"Today's date is {formatted_date}.")
        continue

    if 'time' in question.lower():
        # Ask for the timezone
        timezone = input("Please enter the timezone (e.g., 'America/New_York'): ")
        # Display the current time in the specified timezone
        formatted_time = display_current_time(timezone)
        if formatted_time != "Unknown timezone":
            print(f"The current time in {timezone} is {formatted_time}.")
        else:
            print("Invalid timezone. Please try again.")
        continue

    # Call OpenAI API for other questions
    try:
        response = openai.Completion.create(
            engine="gpt-3.5-turbo-instruct",
            prompt=question,
            max_tokens=1024,
            n=1,
            temperature=0.7
        )
        print(response.choices[0].text)
    except Exception as e:
        print(f"An error occurred while generating response from OpenAI: {str(e)}")
