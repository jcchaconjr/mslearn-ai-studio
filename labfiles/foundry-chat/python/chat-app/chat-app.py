import os
from dotenv import load_dotenv

# import namespaces
from openai import OpenAI
from azure.identity import DefaultAzureCredential, get_bearer_token_provider



def main(): 
    # Clear the console
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        # Get configuration settings 
        load_dotenv()
        azure_openai_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
        model_deployment = os.getenv("MODEL_DEPLOYMENT")

        # Initialize the OpenAI client
        token_provider = get_bearer_token_provider(
            DefaultAzureCredential(), "https://ai.azure.com/.default"
        )

        openai_client = OpenAI(
            base_url=azure_openai_endpoint,
            api_key=token_provider
        )
        


        # Loop until the user wants to quit
        
        #######################################################################################
        # This line can be commented out if using the ChatCompletions API (SECTION 1)...
        # Track responses
        last_response_id = None
        #######################################################################################

        while True:
            input_text = input('\nEnter a prompt (or type "quit" to exit): ')
            if input_text.lower() == "quit":
                break
            if len(input_text) == 0:
                print("Please enter a prompt.")
                continue

            ########################################################################################################
            # Uncomment ONLY ONE section below, as it modifies the app to use the API as indicated in each section
            ########################################################################################################

            # Get a response
            # SECTION 1: This is the code for the ChatCompletions API...
            """completion = openai_client.chat.completions.create(
                model=model_deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful AI assistant that answers questions and provides information."
                    },
                    {
                        "role": "user",
                        "content": input_text
                    }
                ]
            )
            print(completion.choices[0].message.content) """

            # Get a response
            # SECTION 2: Code is Modified to use the Responses API...
            """ response = openai_client.responses.create(
                        model=model_deployment,
                        instructions="You are a helpful AI assistant that answers questions and provides information.",
                        input=input_text
            )
            print(response.output_text) """
            # Get a response
            # SECTION 3: Code is Modified again to include conversation tracking with the Responses API...
            """ response = openai_client.responses.create(
                        model=model_deployment,
                        instructions="You are a helpful AI assistant that answers questions and provides information.",
                        input=input_text,
                        previous_response_id=last_response_id,
            )
            print(response.output_text)
            last_response_id = response.id """
            # Get a response
            # SECTION 4: Code is Modified to enable streaming responses...
            stream = openai_client.responses.create(
                        model=model_deployment,
                        instructions="You are a helpful AI assistant that answers questions and provides information.",
                        input=input_text,
                        previous_response_id=last_response_id,
                        stream=True
            )
            for event in stream:
                if event.type == "response.output_text.delta":
                    print(event.delta, end="")
                elif event.type == "response.completed":
                    last_response_id = event.response.id
            print()
            

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()
