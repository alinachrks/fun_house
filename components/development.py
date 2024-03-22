import streamlit as st

def app():
    # Заголовок страницы
    st.markdown("<h1 style='text-align: center; color: white; font-family: \"Old Standard TT\", serif; font-size: 32px;'>Gallery </h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    # Первая строка
    with col1:
        st.image("img/1.jpg")
    with col2:
        st.image("img/2.jpg")
    with col3:
        st.image("img/3.jpg")

    # Вторая строка
    with col1:
        st.image("img/4.jpg")
    with col2:
        st.image("img/5.jpg")
    with col3:
        st.image("img/6.jpg")

    # Третья строка
    with col1:
        st.image("img/7.jpg")
    with col2:
        st.image("img/8.jpg")
    with col3:
        st.image("img/9.png")
    # Последний столбец оставляем пустым, если число изображений не кратно трем
