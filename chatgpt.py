import streamlit as st
import openai

st.title('Connect ChatGPT with python')


#setup infor of model
model='text-davinci-003'
with open('apikey.txt', 'r') as f: #lấy apikey
    openai.api_key=f.readline()

#hàm để gọi tới chatgpt
def get_response_from_chatgpt(user_question):
    response = openai.Completion.create(  #completion: chat gpt sinh ra text dựa vào câu hỏi của người dùng, dựa vào đó để hoàn thiện câu trả lời
        engine = model, 
        prompt = user_question, #chuyền vào user query để mồi giúp chatgpt sinh ra text
        max_tokens = 1024, # độ dài câu trả lời 
        n = 1, # số lượng câu trả lời
        temperature = 0.5 
    )

    response_text = response.choices[0].text # response chứa câu tra lời và chỉ lấy câu trả lời đầu tiên thui
    return response_text

#control interface streamlit
def main():
    user_question = st.text_input("Type your question in here: ")
    if st.button('chat with gpt'):
        response_text = get_response_from_chatgpt(user_question)
        return st.write(f'{user_question} {response_text}')

main()