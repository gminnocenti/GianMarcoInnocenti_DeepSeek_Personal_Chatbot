# GianBOT Deep Seek Personal Chatbot

Welcome to the **GianBOT Deep Seek Personal Chatbot** repository. This project is a demonstration of how to integrate and fine-tune large language models (LLMs) for small, targeted tasks, showcasing advanced API integrations and prompt engineering techniques.

## Overview

**GianBOT** is an AI-powered chatbot built on the Deep Seek model (derived from LLaMA 70B). It is fine-tuned to provide detailed and accurate information about Gian Marco Innocenti by leveraging a carefully curated dataset. The chatbot uses a streamlined API-based approach, making it an excellent example of adapting powerful LLMs to specific, context-driven applications.

## Key Features

- **Deep Seek Model**: Utilizes a fine-tuned LLaMA 70B-based model to deliver precise and context-specific answers.
- **API Integration**: Demonstrates robust API usage to interact with the LLM, ensuring smooth and reliable communication.
- **Streamlit Interface**: Features a dynamic, conversational interface built with Streamlit for an intuitive user experience.
- **Custom Prompt Engineering**: Leverages effective prompt design to ensure responses are both accurate and context-aware.
- **Lightweight & Focused**: Designed for targeted tasks, showcasing how big models can be fine-tuned for small, personal projects.

## Project Structure

```plaintext
GianBOT-DeepSeek-Chatbot/
├── data.txt             # Source data for context-specific responses
├── app.py              # Main Streamlit application code
├── requirements.txt     # List of required Python packages
├── README.md            # Project documentation
└── .env                 # Environment variables (e.g., API keys)

## Deployment Instructions

Follow these steps to deploy your own version of the GianBOT Deep Seek Personal Chatbot:

1. **Create an Account and Get an API Key:**
   - Visit [Groq - Fast AI Inference](https://groq.com) and sign up for a free account.
   - After registration, obtain your free API key.

2. **Create a `.env` File:**
   - In the root directory of the project, create a file named `.env`.
   - Copy your API key into this file using the following format:

     ```env
     key=YOUR_API_KEY_HERE
     ```

3. **Set Up Your Virtual Environment:**
   - Create a virtual environment for the project. For example:

     ```bash
     python -m venv venv
     ```

   - Activate the virtual environment:
     - On macOS/Linux:

       ```bash
       source venv/bin/activate
       ```

     - On Windows:

       ```bash
       venv\Scripts\activate
       ```

4. **Install Dependencies:**
   - Install the required Python packages using:

     ```bash
     pip install -r requirements.txt
     ```

5. **Run the Chatbot Application:**
   - Launch the Streamlit app by running:

     ```bash
     streamlit run app.py
     ```

   - The application will open in your default web browser, and you can start interacting with GianBOT.

## Create Your Own Data

This chatbot uses a simple, data-driven approach to generate responses based on user inputs. The core idea is to define "tags" that represent different intents or topics. For each tag, you specify:

- **Tag**: A unique identifier for the intent (e.g., `greeting`, `goodbye`, `thanks`).
- **Patterns**: A list of example phrases or questions that users might input.
- **Responses**: A list of potential responses that the chatbot can provide when it detects a matching pattern.
- **Context**: (Optional) Additional context or information that may help refine the response.

To add your own data, follow these steps:

1. Open the data file (e.g., `data.txt`) used by the chatbot.
2. Add a new block using the following format:

   ```yaml
   Tag: your_tag_name
   Patterns:
     - pattern example 1
     - pattern example 2
   Responses:
     - response example 1
     - response example 2
   Context:
     - optional context information
