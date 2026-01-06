import streamlit as st
import time
import random
import pandas as pd

st.title("하이퍼파라미터 튜닝 시뮬레이터")

# [Session state] 실험 기록 저장소 초기화
# 페이지가 새로고침 되어도 리스트가 사리지지 않고, 유지됩니다.

if 'history' not in st.session_state:
    st.session_state.history = []
    
with st.form("trainig_form"):
    st.subheader("모델 파라미터 설정")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        learning_rate=st.slider("Learning Rate", 0.001, 0.1, 0.01)
    with col2:
        epch=st.slider("Epochs", 1,100, 10)
    with col3:
        batchsize=st.select_slider("batch size", options=[16, 32, 64, 128], value=32)
    
    submitted = st.form_submit_button("학습 시작")
    
if submitted:
    st.write(f"학습시작 LR:{learning_rate}, Epochs:{epch}")
    
    progress_bar=st.progress(0)
    status_text=st.empty()
    
    #가상의 학습과정 스뮬레이션
    for i in range(100):
        time.sleep(0.01)
        progress_bar.progress(i+1)
        status_text.text(f"Progress: {i+1}%")
        
    accuracy =random.uniform(0.70,0.99)
    loss =random.uniform(0.1, 0.5)
    
    st.success(f"학습완료 Accuracy:{accuracy}")
    
    st.session_state.history.append({
    "Learning Rate": learning_rate,
    "Epochs": epch,
    "Batch Size": batchsize,
    "Accuracy": accuracy,
    "Loss": loss
    
})

# 초기화 함수 정의
def clear_history():
    st.session_state.history = []

# 버튼 생성 (label은 문자열로, on_click에 함수 연결)
st.button("실험 기록 초기화", on_click=clear_history)

# 저장된 실험 기록 출력
if len(st.session_state.history) > 0:
    st.markdown("---")
    st.subheader("📝 실험 기록 (Session State 유지)")
    # 리스트를 데이터프레임으로 변환하여 표로 출력
    df_history=pd.DataFrame(st.session_state.history)
    st.dataframe(df_history)
    
st.line_chart(df_history['Accuracy'])