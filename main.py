import streamlit as st
import os
from engine import models
from engine import pipeline
st.markdown("<h1 style='text-align: center; color: black;'>Neural Search Engine</h1>", unsafe_allow_html=True)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from engine.genrator import generator,querygen,find_match
local_css("main.css")
way = st.text_input("Image Directory")
imgem=None
filelist=None

imgem,filelist=generator(way)
query=[st.text_input(" ")]
quem=querygen(query)
rs=find_match(imgem,quem,1)
for i in rs:
   st.image(filelist[i])

