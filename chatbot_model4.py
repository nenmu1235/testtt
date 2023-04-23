import openai
import streamlit as st
import smtplib
import time
from email.mime.text import MIMEText

model_engine = 'gpt-3.5-turbo'
openai.api_key = st.secrets['API_KEY']
password = st.secrets['password']
def generate_text(prompt):
    response = openai.ChatCompletion.create(
      model=model_engine,
      messages=[
        {"role": "system", "content": "You are a freind of user."},
        {"role": "user", "content": prompt}
        ]
    )
    text = response['choices'][0]['message']['content']
    return text

def determine_text(prompt):
    response = openai.ChatCompletion.create(
      model=model_engine,
      messages=[
        {"role": "system", "content": "Figure out if the prompt is related to school bullying. Determine only by Yes or No. The output should only by 'Yes' or 'No'. You should not answer to the prompt. You just determine by saying 'Yes' or 'no'."},
        {"role": "user", "content": prompt}
        ]
    )
    text = response['choices'][0]['message']['content']
    return text

if 'chat' not in st.session_state:
    st.session_state.chat = ''

def submit():
    st.session_state.chat = st.session_state.widget
    st.session_state.widget = ''

name = st.text_input('이름:')
st.text_input('대화를 입력하세요', key='widget', on_change=submit)
text = st.session_state.chat
response = generate_text(text)
if name == '':
    st.write("당신" + ": " + text)
else:
    st.write(name + ": " + text)
st.write("토닥이: ", response)
st.write(determine_text(text))
    
#추가
word_list = ['괴롭힘','괴롭', '협박', '폭력', '차별', '성희롱', '가해자', '피해자', '사이버 폭력', '인신공격', '피해자 지원', '피해자보호 정책', '선생님 폭력', '학교폭력 보고서', '학교폭력 증거보존', '학교폭력 법적 대응', '선도교사', '학교 내 고립', '학교 내 대인관계', '권리 침해', '가정 내 폭력', '부모교육', '학교폭력 예방 봉사활동', '초등학교 폭력', '중학교 폭력', '고등학교 폭력', '대학교 폭력', '초등학교 폭력 예방', '중학교 폭력 예방', '고등학교 폭력 예방', '대학교 폭력 예방', '학생회 폭력', '체육 대회 폭력', '학교 내 성소수자 차별', '학교 폭력 피해 심리', '학교폭력 관련 법률', '학교폭력 예방 위원회', '학교폭력 예방 자료', '학교폭력 예방 가이드라인', '학교폭력 예방 사례', '불완전한 가정']
if text.endswith("?"):
    textt = text.strip("?")
else:
    textt = text
for item in textt.split():
    if item in word_list:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)

        smtp.ehlo()

        smtp.starttls()

        smtp.login('testuser7295@gmail.com', password)
        server_time = time.strftime('%c', time.localtime(time.time()))
        msg = MIMEText('Chatbot으로부터 해당 시간에 학교폭력 위험 신호가 감지되었습니다. 이름: '+ name + 'keyword: ' + item + '시간: ' + server_time)
        msg['Subject'] = '학교폭력 위험 신호 감지됨 -By keyword detecting'
        smtp.sendmail('testuser7295@gmail.com', 'zollida01@gmail.com', msg.as_string())

        smtp.quit()
if determine_text(text) == "Yes.":
    smtp = smtplib.SMTP('smtp.gmail.com', 587)

    smtp.ehlo()

    smtp.starttls()

    smtp.login('testuser7295@gmail.com', password)
    server_time = time.strftime('%c', time.localtime(time.time()))
    msg = MIMEText('Chatbot으로부터 해당 시간에 학교폭력 위험 신호가 감지되었습니다. 이름: '+ name + 'text: ' + text + '시간: ' + server_time)
    msg['Subject'] = '학교폭력 위험 신호 감지됨 -By Openai detecting'
    smtp.sendmail('testuser7295@gmail.com', 'zollida01@gmail.com', msg.as_string())

    smtp.quit()
