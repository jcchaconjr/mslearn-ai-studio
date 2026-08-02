# Develop Generative AI Solutions in Azure

The exercises in this repo are designed to provide you with a hands-on learning experience in which you'll explore common tasks that developers perform when building generative AI solutions on Microsoft Azure.

> **Note**: To complete the exercises, you'll need an Azure subscription in which you have sufficient permissions and quota to provision the necessary Azure resources and generative AI models. If you don't already have one, you can sign up for an [Azure account](https://azure.microsoft.com/free). There's a free trial option for new users that includes credits for the first 30 days.

View the exercises in the [GitHub Pages site for this repo](https://go.microsoft.com/fwlink/?linkid=2310724).

Original Repository Link: [MSLearn-AI-Studio](https://github.com/MicrosoftLearning/mslearn-ai-studio).

> **Note**: While you can complete these exercises on their own, they're designed to complement modules on [Microsoft Learn](https://aka.ms/mslearn-generative-ai), in which you'll find a deeper dive into some of the underlying concepts on which these exercises are based.

## Reporting issues

If you encounter any problems in the exercises, please report them as **issues** in this repo.

## Personal Notes

**DISCLAIMER:** This is a personal fork of the Microsoft provided lab resources indicated above, with my personal notes indicating what I have updated in the project. If you'd like to work with the original Repo as provided by MSLearn, you can clone it yourself from the link provided above, or below in the Lab Notes.

## VS Code Environment Requirements

 To properly set up the VS Code development environment in Windows 11, I set up the following:

 - Python 3.13 (Download from the Microsoft Store app in Windows)
 - The Python Language Support extension from Microsoft
 - Ensure that Python is set up to use env files (hit CTRL + the comma key to open Settings) - enter python.envfile.useenvfile in the Settings search bar to see the property - make sure it is checked.
 - Use the Windows Package Manager to load the Azure CLI (PowerShell command: *winget install -e --id Microsoft.AzureCLI*)
 - After the CLI is installed, to ensure that Azure login authenticates via web browser, enter the following PowerShell command: *az config set core.allow_broker=false*
 - The OpenAI endpoint in the project's .env file **MUST** be updated with the OpenAI endpoint generated after creating a project resource as indicated in the Lab 3 instructions. 

 In this case, I used the lab credentials locally after setting up the code and environment on my local machine. With the models deployed via the Skillable session, the model resource is accessible externally, as long as you have the model requirements (OpenAI endpoint, Model Deployment name) set up locally.

 ## Lab 3 Notes

**Lab 3** from the **Skillable Lab series** for **AI-103 certification**, uses the code in this github: **https://github.com/MicrosoftLearning/mslearn-ai-studio**. The instructions for building the chat agent in Microsoft Foundry, along with the code details that were added to the generic code sample, can be found in:
.\Instructions\Exercises\03-foundry-sdk.md

The code for this specific exercises creates both a synchronous Chat app and an asynchronous chat app via the two Python scripts provided. The following app files for this lab are in:
.\labfiles/foundry-chat/python/chat-app. 

**Synchronous app (chat-app.py)** -  the Lab guides you through 4 different ways that you can use the deployed model:

- Connecting via the ChatCompletions API.
- Connecting via the Responses API.
- Using the Repsonses API with conversation tracking.
- Adding streaming responses to the conversation tracking example.

I have added the code for all 4 scenarios used in this lab. One AND ONLY ONE block should be uncommented when running the script.
 **NOTE:** The declaration of the variable last_response_id can be commented out when using the code block for SECTION 1 or 2. It is required if using the code in sections 3 or 4.

 **Asynchronous App (chat-async.py)** - This app is straghtforward enough. It replicates the objective, but calls the response object using await for asynchronous responses.

 In all cases, the instructions for using the chatbot provided above will include prompts that you can use to try the chatbot and validate its appropriate responses.

## Lab 4 Notes

**Lab 4** from the **Skillable Lab series** for **AI-103 certification**, uses the code at the following github: **https://github.com/MicrosoftLearning/mslearn-ai-studio**. The instructions for building the chat agent in Microsoft Foundry, along with the code details that were added to the generic code sample, can be found in:
.\Instructions\Exercises\04a-use-own-data.md

The application will load, vectorize, and upload the vectorized PDF files in the "brochures" subfolder to teh Model. Once loaded, The objective is to query the model for data based in the documents, from which the Model will provide answers. The code base is simple enough, as it is not modified several times like Lab 3 was. Just prmompt the model the questions as suggested in the instrcutions to complete the exercise.

## The Other Lab Exercises

There are a total of 6 Lab Exercises in this repository, but only Labs 3 and 4 make use of code projects. The Exercises for the other labs can all be done inside of the Azure portal (**ai.azure.com**), as you are pretty much working in the portal's provided sandboxes with the resources created.

## Cleanup

Also as noted, DON"T FORGET to clean up any and all Azure resources after you complete a lab! As the labs typically As you to Create the lab projects inside of a Resource Group named "ResourceGroup1", the fastest way to clean up is by going into the Azure portal site (portal.azure.com) then deleting that resource group after bringing up the Resource Groups list. Just select the Resource Group, then from teh detail view for the Group, select "Delete Resource group" from the top, and follow the instructions. It should take about a minute to clean them up.
