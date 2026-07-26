# Develop Generative AI Solutions in Azure

The exercises in this repo are designed to provide you with a hands-on learning experience in which you'll explore common tasks that developers perform when building generative AI solutions on Microsoft Azure.

> **Note**: To complete the exercises, you'll need an Azure subscription in which you have sufficient permissions and quota to provision the necessary Azure resources and generative AI models. If you don't already have one, you can sign up for an [Azure account](https://azure.microsoft.com/free). There's a free trial option for new users that includes credits for the first 30 days.

View the exercises in the [GitHub Pages site for this repo](https://go.microsoft.com/fwlink/?linkid=2310724).

> **Note**: While you can complete these exercises on their own, they're designed to complement modules on [Microsoft Learn](https://aka.ms/mslearn-generative-ai), in which you'll find a deeper dive into some of the underlying concepts on which these exercises are based.

## Reporting issues

If you encounter any problems in the exercises, please report them as **issues** in this repo.

## Personal Notes

This is **Lab 3** from the **Skillable Lab series** for **AI-103 certification**. The instructions for building the chat agent in Microsoft Foundry, along with the code details that were added to teh generic code sample, can be found in:
.\Instructions\Exercises\03-foundry-sdk.md

The code for this specific exercises creates both a synchronous Chat app and an asynchronous chat app via the two Python scripts provided.

Synchronous app (chat-app.py) -  the Lab guides you through 4 different ways that you can use the deployed model:

- Connecting via the ChjatCompletions API.
- Connecting via the Responses API.
- Using the Repsonses API with conversation tracking.
- Adding streaming responses to the conversation tracking example.

I have added the code for all 4 scenarios used in this lab. One AND ONLY ONE block should be uncommented when running the script.
 **NOTE:** The declaration of the variable last_response_id can be commented out when using the code block for SECTION 1 or 2. It is required if usiong the socde in sections 3 or 4.

 ## VS Code Environment Requirements

 To properly set up the VS Code development environment in Windows 11, I set up the following:

 - Python 3.13 (Download from the Microsoft Store app in Windows)
 - The Python Language Support extension from Micrsoft
 - Ensure that Python is set up to use env files (hit CTRL+, to open Settings, then enter python.envfile.useenvfile in the search bar to see the property - make sure it is checked)
 - Use the Windows Package Manager to load the Azure CLI (PowerShell command: *winget install -e --id Microsoft.AzureCLI*)
 - To ensure that Azure login authenticates via web browser, enter the following PowerShell command: *az config set core.allow_broker=false*
 - The OpenAI endpoint in the project .env file **MUST** be updated with the OpenAI endpoint generated after creating a project resource as indicated in the Lab 3 instructions. 

 In this case, I used the lab credentials locally after setting up the code and environment on my local machine. With the models deployed via the Skillable session, the model resource is accessible externally, as long as you have the model requirements (OpenAI endpoint, Model Deployment name) set up locally.


