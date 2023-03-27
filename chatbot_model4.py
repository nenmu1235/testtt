import openai
import googletrans
import streamlit as st
import smtplib
from email.mime.text import MIMEText

model_engine = 'gpt-3.5-turbo'
openai.api_key = st.secrets['API_KEY']

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

def translate(text, lan):
    translator = googletrans.Translator()
    response = translator.translate(text, dest = lan).text
    return response
def ko_to_en(text):
    ja_text = translate(text, "ja")
    en_text = translate(ja_text, "en")
    return en_text
def en_to_ko(text):
    ja_text = translate(text, "ja")
    ko_text = translate(ja_text, "ko")
    return ko_text
if st.button('안녕!'):
    name = st.text_input('이름:')
else:
    st.write('안녕하세요!')
while type(name) == str:
    text = st.text_input("대화를 입력하세요: ")
    en_text = ko_to_en(text)
    response = generate_text(en_text)
    ko_response = en_to_ko(response)
    st.write("당신: ",text)
    st.write("Chatbot: ", ko_response)

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

        smtp.login('testuser7295@gmail.com', 'gqxqmblqkrjamqma')

        msg = MIMEText('내용 : 학교폭력 위험 신호 감지됨')
        msg['Subject'] = 'Chatbot으로부터 해당 시간에 학교폭력 위험 신호가 감지되었습니다. 이름: '+ name

        smtp.sendmail('testuser7295@gmail.com', 'zollida01@gmail.com', msg.as_string())

        smtp.quit()
