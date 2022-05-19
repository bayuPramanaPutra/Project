import streamlit as st
import pickle
import pandas as pd
import numpy as np
import sklearn
import tensorflow as tf
import nltk

st.title('Hoax Tweet Detection Application')

st.header('Please input the tags and the tweet text below for false news checking')

col1, col2 = st.columns(2)
with col1:
    tags_a = st.text_input('Tags 0', value=" ")
    tags_b = st.text_input('Tags 1', value=" ")
    tags_c = st.text_input('Tags 2', value=" ")
    tags_d = st.text_input('Tags 3', value=" ")
    tags_e = st.text_input('Tags 4', value=" ")
with col2:
    text_a = st.text_input('Tweet 0', value=" ")
    text_b = st.text_input('Tweet 1', value=" ")
    text_c = st.text_input('Tweet 2', value=" ")
    text_d = st.text_input('Tweet 3', value=" ")
    text_e = st.text_input('Tweet 4', value=" ")

df = {'Tags':[tags_a, tags_b, tags_c, tags_d, tags_e],
    'Text':[text_a, text_b, text_c, text_d, text_e]}
df_inf = pd.DataFrame(data=df)
df_inf['feature'] = df_inf['Tags'] + ' ' + df_inf['Text']
df_inf = pd.DataFrame(df_inf.feature)
df = pd.DataFrame(data=df)

model_BEST = tf.keras.models.load_model('model_BEST.tf')

df_inf_pred = model_BEST.predict(df_inf)
df_inf_pred = (df_inf_pred.argmax(axis=1))
df_inf_result = df.copy()
df_inf_result['predicted_label'] = ''
df_inf_result['predicted_label'] = df_inf_pred

df_inf_result.predicted_label.replace(0, 'FALSE or barely true', inplace=True)
df_inf_result.predicted_label.replace(1, 'unknown (50:50)', inplace=True)
df_inf_result.predicted_label.replace(2, 'TRUE or mostly true', inplace=True)
df_inf_result.predicted_label = df_inf_result.predicted_label.astype('object')

if st.button('Click to see the prediction results'):
    st.dataframe(data=df_inf_result, width=None, height=None)
else:
    st.write(' ')