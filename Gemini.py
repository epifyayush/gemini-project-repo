import requests

GEMINI_API_KEY = "YOUR_AP_KEY"
url= f"COPY THE CURL URL UPTO {GEMINI_API_KEY}"

headers = {"Content-Type": "application/json"}

def get_gemini_responses(user_input):
    #prepare the request payload
    data={"contents":[{"parts":[{"text":user_input}]}]}
    #making the POST request
    response= requests.post(url, headers=headers, json=data)

    #Checking if successful or not
    if response.status_code == 200:
        response_data=response.json()

        #Extracting the response from the backend
        if response_data.get("candidates"):
            bot_response=response_data["candidates"][0]["content"]["parts"][0]["text"]
            return bot_response
        else:
            return "Model Failed"
        


def chat():
    print("Welcome to the Gemini AI model. Type exit to exit the model")

    while True:
        #Get user input
        user_input= input("You:")

        if user_input.lower()== "exit":
            print("Goodbye! Have a great day!")
            break

        bot_response= get_gemini_responses(user_input)

        print("Bot: ", bot_response)


if __name__ == "__main__":
    chat()
