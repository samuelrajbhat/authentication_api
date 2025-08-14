import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello, Streamlit!")

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
    })
st.table(pd.DataFrame({
    'first':[34,35,54,23],
    'second': [100,200,300,400],
    'third': [3, 0,0,0]
}))

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(chart_data)

x= st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Type something", "Type here...", key="input")

st.write(st.session_state.input)

st.checkbox('Show dataframe')

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

('You selected: ', option)

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)


add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# if add_selectbox == 'Email':
#     st.write('You selected Email')
# elif add_selectbox == 'Home phone':
#     st.write('You selected Home phone')
# elif add_selectbox == 'Mobile phone':
#     st.write('You selected Mobile phone')

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")