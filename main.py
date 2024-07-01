import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Rishil Shah")
    content = """
    As a dedicated and highly motivated Computer Science student at the University of South Florida, 
    I have consistently excelled in my academic pursuits, with a Major GPA of 3.58 and recognition on the Dean's List of
    Scholars in 2021 and 2022. My skills encompass a wide range of programming languages and technologies, including 
    Python, C, SQL, Swift, HTML, CSS, and more. In my professional experience, I've had the opportunity to work on 
    meaningful projects, such as developing MuleSoft APIs to streamline processes at the University and enhancing
    facial outline technology accuracy during my internship at Galileo Group Inc. I'm also an active leader, having 
    served as Treasurer for Women in Computer Science and Engineering and in various other leadership roles. 
    My passion for technology, problem-solving skills, and commitment to personal and professional growth make me a 
    valuable asset to any team or organization.
    """
    st.info(content)