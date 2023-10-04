
#
#삶의 서포터 만들기
#2023.10.0 v1
#

#env 환경변수 읽어 들이기(같은 폴더 "/.env"의 파일을 그대로 읽어옴)
#from dotenv  import load_dotenv
#load_dotenv()

##Complete Mode 테스트해보기
#from langchain.llms import OpenAI
#llm = OpenAI() #Complete mode
#result = llm.predict("내가 좋아하는 동물은?")
#print(f'Completemode====>{result}')

##Chat mode Mode 테스트해보기
from langchain.chat_models import ChatOpenAI
import streamlit as st


chat_model = ChatOpenAI() #Chat mode  

st.image('banner.jpg', use_column_width=True)
st.title('AI Supporter - StrengthRainbow')
st.subheader('항상 좋은 기운이 너의 주변에 가득하길 기원하며..'+'\n'+ 'from SP Division No.7 member StrengthRainbow', divider='rainbow')

title_name = st.text_input('너의 이름은?')  
title = st.text_input('StrengthRainbow가 온 세상의 좋은 기운을 모두 담아 너에게 전달해야 하는 상황을 말해줘!!')  

#st.button("Reset", type="primary")
if st.button('StrengthRainbow의 좋은 기운 받기'):
   with st.spinner('Wait for it...') :
      result = chat_model.predict("너는 지금부터 세상의 모든 좋은 기운을 가진 StrengthRainbow 입니다." + title_name + "님의 '"+  title + "' 라는 상황에 대해 StrengthRainbow 로서 좋은 기운을 전달하는 응원글을 작성해줘")
      st.write('StrengthRainboAI Supporter - StrengthRainbow가 ' + title_name + '님 에게 말하길 ~~!!\n', result)




