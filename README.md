# AI-ChatBot
## Project Overview: Chatbot Application with Generative AI
Purpose:
The project aims to create an interactive chatbot using the Gemini API and Streamlit. This chatbot leverages generative AI models to engage in natural language conversations with users.

## Key Components and Features:
## Gemini API Integration:

The Gemini API is utilized to access generative AI models capable of understanding and generating human-like responses.
An API key (api) is configured to authenticate and interact with Gemini's AI services.
## Streamlit User Interface:

Streamlit framework is employed to build a web-based user interface (UI) for the chatbot application.
The UI includes a title (st.title) to label the chatbot interface as "My Chatbot".
## GenerativeModel Initialization:

A GenerativeModel object (model) is instantiated from Gemini's platform to facilitate chatbot functionalities.
The specific model used ('gemini-pro') suggests high-capacity generative AI capabilities tailored for interactive conversational use cases.
## User Interaction:

Users interact with the chatbot through a text input widget (st.text_input) labeled "You:".
A send button (st.button) triggers the chatbot's response generation upon user input.
## Chatbot Response Handling:

The get_response function utilizes the chatbot model (model) to generate responses based on user input (user_text).
Responses are displayed using Streamlit's st.write function, showing the chatbot's reply to the user's input.
## Session State Management:

Streamlit's session state (st.session_state) is utilized to manage and persist conversation history (lst).
Each interaction (user input and Bot response) is stored as tuples in lst, facilitating chat history viewing and management.
## Additional Features:

History Viewing: Users can view the chat history by clicking on a "View History" button (view_hist), which iterates through lst to display previous interactions.
History Clearing: An option (clear button) is provided to clear the chat history stored in st.session_state.lst.
## Technical Skills Demonstrated:
API Integration: Proficiency in integrating external APIs (Gemini) for AI-driven applications.
User Interface Development: Experience in creating interactive web interfaces using Streamlit.
State Management: Effective use of session state in Streamlit for data persistence and dynamic UI updates.
Natural Language Processing (NLP): Application of generative AI models for real-time text-based interactions.
## Future Improvements:
Enhance chatbot capabilities with advanced NLP features like sentiment analysis or context awareness.
Integrate multimedia capabilities (images, videos) using Gemini's vision models ('gemini-pro-vision').
Implement user authentication and personalized user experiences.
