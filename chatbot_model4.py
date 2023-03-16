#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:26:58 2023

@author: haeyuel
"""

import openai
import googletrans
import streamlit as st

model_engine = 'davinci'
openai.api_key = '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'

def generate_text(prompt):
    response = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=20,
      n=1,
      stop="STOP",
      temperature=0.5,
    )
    raw_text = response.choices[0].text
    text = raw_text.strip()
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

try:
    text = st.text_input("대화를 입력하세요: ")
    en_text = ko_to_en(text)
    response = generate_text(en_text)
    ko_response = en_to_ko(response)
    st.write("당신: ",text)
    st.write("Chatbot: ", ko_response)
except:
    pass
