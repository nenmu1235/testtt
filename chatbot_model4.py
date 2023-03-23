#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:26:58 2023

@author: haeyuel
"""

import openai
import googletrans
import streamlit as st

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

text = st.text_input("대화를 입력하세요: ")
en_text = ko_to_en(text)
response = generate_text(en_text)
ko_response = en_to_ko(response)
st.write("당신: ",text)
st.write("Chatbot: ", ko_response)

#추가
word_list = ['Bullying', 'bully', 'bullied', 'bullies', 'Harassment', 'harass', 'harassed', 'harasses', 'Intimidation', 'intimidate', 'intimidated', 'intimidates', 'Verbal abuse', 'verbally abuse', 'verbally abused', 'verbally abuses', 'Physical abuse', 'physically abuse', 'physically abused', 'physically abuses', 'Cyberbullying', 'cyberbully', 'cyberbullied', 'cyberbullies', 'Social exclusion', 'exclude', 'excluded', 'excludes', 'Victim', 'victimize', 'victimized', 'victimizes', 'Aggressor', 'aggress', 'aggressed', 'aggresses', 'Peer pressure', 'pressure', 'pressured', 'pressures', 'Hazing', 'haze', 'hazed', 'hazes', 'Name-calling', 'call names', 'called names', 'calls names', 'Taunting', 'taunt', 'taunted', 'taunts', 'Threatening', 'threaten', 'threatened', 'threatens', 'Blackmail', 'blackmail', 'blackmailed', 'blackmails', 'Coercion', 'coerce', 'coerced', 'coerces', 'Homophobia', 'homophobe', 'homophobic', 'homophobes', 'Xenophobia', 'xenophobe', 'xenophobic', 'xenophobes', 'Racism', 'racist', 'racial', 'racists', 'Discrimination', 'discriminate', 'discriminated', 'discriminates', 'Bias', 'biased', 'biasing', 'biases', 'Stereotyping', 'stereotype', 'stereotyped', 'stereotypes', 'Prejudice', 'prejudiced', 'prejudicing', 'prejudices', 'Inequality', 'unequal', 'inequality', 'inequalities', 'Oppression', 'oppress', 'oppressed', 'oppresses', 'Power dynamics', 'power', 'powered', 'powers', 'Bullying prevention', 'prevent bullying', 'prevented bullying', 'prevents bullying', 'Conflict resolution', 'resolve conflict', 'resolved conflict', 'resolves conflict', 'Restorative justice', 'restore justice', 'restored justice', 'restores justice', 'Counseling', 'counsel', 'counseled', 'counsels', 'Mental health', 'mental', 'health', 'mental health', 'Trauma', 'traumatize', 'traumatized', 'traumatizes', 'Anxiety', 'anxious', 'anxiety', 'anxieties', 'Depression', 'depress', 'depressed', 'depresses', 'Suicide', 'suicidal', 'suicide', 'suicides', 'Self-harm', 'self-harm', 'self-harmed', 'self-harms', 'Substance abuse', 'abuse substances', 'abused substances', 'abuses substances', 'Academic performance', 'perform academically', 'performed academically', 'performs academically', 'Attendance', 'attend', 'attended', 'attends', 'Truancy', 'truant', 'truanted', 'truants', 'Dropouts', 'dropout', 'dropped out', 'dropouts', 'Suspension', 'suspend', 'suspended', 'suspends', 'Expulsion', 'expel', 'expelled', 'hit', 'violence']
if en_text.endswith("?"):
    enc_text = en_text.strip("?")
else:
    enc_text = en_text
for item in enc_text.split():
    if item in word_list:
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 465
        smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT)
        EMAIL_ADDR = 'testu7295'
        EMAIL_PASSWORD = 'gawakfxfrkfmsmtr'
        smtp.login(EMAIL_ADDR, EMAIL_PASSWORD)
        message = EmailMessage()
        message.set_content('이메일 본문')
        message["Subject"] = "warning from chatbot"
        message["From"] = EMAIL_ADDR  #보내는 사람의 이메일 계정
        message["To"] = 'testu7295@gmail.com'
        smtp.send_message(message)
        smtp.quit()
