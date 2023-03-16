#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 02:54:21 2023

@author: haeyuel
"""

import openai
import streamlit as st
openai.api_key = password
model_engine = 'davinci'
text = st.text_input("say something")
st.write(text)

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

response = generate_text(text)
st.write(response)