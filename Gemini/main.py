import gemini_api
import google.generativeai as genai
import streamlit as st
from PIL import Image
api=gemini_api.var1
genai.configure(api_key=api)
st.title("My Chatbot")
model=genai.GenerativeModel('gemini-pro')
# vision=genai.GenerativeModel('gemini-pro-vision')
chat=model.start_chat(history=[])
def get_response(text):
    return chat.send_message(text).text
# text=input('enter text')
# print(get_response(text))
if 'lst' not in st.session_state:                   # whnever make a change the  session change can add into this to save# key value
    st.session_state.lst=[]                         # this step is to keep the history of the data as thelis as keyvalue pairs

user_text=st.text_input('You: ')
button=st.button('Send')
if user_text and button:
    res=get_response(user_text)
    st.write(res)
    st.session_state.lst.append(('user',user_text))
    st.session_state.lst.append(('Bot',res))
view_hist=st.button('View History')
if view_hist:
    for name,text in st.session_state.lst:
        st.write(f'{name}: {text}')
clear=st.button('Clear History')
if clear:
    st.session_state.lst.clear()