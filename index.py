import streamlit as st 
import pandas

st.set_page_config(layout="wide")




# st.title("Hi, I’m Nomaan Shaik 👋")
col2, col3 = st.columns(2)
with col2:
    st.image("image/shaik.png" )
    #st.write("nomaan")

with col3:
    st.title("Hi, I’m Nomaan Shaik 👋")
    contant ="""
I am an Artificial Intelligence and Data Science (AI-DS) engineering student with a strong interest in Python development, backend technologies, and problem-solving. I enjoy building practical, real-world applications and understanding how systems work behind the scenes rather than just focusing on outputs.

I have hands-on experience in Python programming and backend development using Flask and Django. I have built projects that involve form handling, database integration, authentication, APIs, and basic automation. Alongside backend development, I am comfortable with frontend technologies such as HTML, CSS, JavaScript, and Bootstrap, which allows me to build complete full-stack applications.

Currently, I am actively learning **Data Structures and Algorithms using Python**, focusing on writing efficient, readable, and optimized code. My DSA journey includes topics like arrays, strings, stacks, queues, linked lists, trees, recursion, greedy algorithms, dynamic programming, and optimization techniques. This has helped me improve my logical thinking, problem-solving skills, and interview readiness.

In parallel, I am starting my **AI & Machine Learning learning path**, where my goal is to build a strong foundation in core concepts such as data handling, basic machine learning algorithms, and practical implementation using Python. As an AI-DS student, I aim to combine my backend development skills with AI/ML to build intelligent and scalable applications in the future.

I strongly believe in learning by doing. I regularly work on mini-projects, backend systems, and coding challenges, and I maintain my work on GitHub to track my progress and continuously improve. My focus is on clean code, proper structure, and understanding the “why” behind every concept I learn.

I am eager to work in environments where I can learn from real-world projects, collaborate with experienced developers, and grow as a software and AI engineer.

              """
    st.info(contant)
contant2="""Below are some app i bulit by using python"""
st.write(contant2)

col4,empty_col, col5 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")

with col4:
    for index, row in df[:9].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row['url']})")

with col5:
    for index, row in df[9:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("image/"+ row["image"])
        st.write(f"[source code]({row['url']})")
