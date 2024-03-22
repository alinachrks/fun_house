import streamlit as st

def app():
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://i.ibb.co.com/3yVykRQ/Minimal-Photography-1-fotor-20240315111216.png");
    background-size: cover;
    }
    [data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
    }
    [data-testid="stToolbar"]{
    right: 2rem;
    background-image: url("https://cdn.iconscout.com/icon/free/png-256/hamburger-menu-462145.png");
    background-size: cover;
    }
    </style>
    """
    st.markdown(page_element, unsafe_allow_html=True)

    # Заголовок страницы
    st.markdown("<h1 style='text-align: center; color: white; font-family: \"Old Standard TT\", serif; font-size: 32px;'>About the App </h1>", unsafe_allow_html=True)



    if st.link_button('Для бизнеса', "https://ai-for-business.streamlit.app/"):
        pass  # Вы можете добавить дополнительный код, который выполнится после нажатия кнопки

    if st.link_button('АI-сценарии', "https://rudolf.streamlit.app/"):
        pass  # Дополнительный код для второй кнопки

    if st.link_button('Smart City', "https://urban-analysis-one.streamlit.app/"):
        pass  # Дополнительный код для третьей кнопки