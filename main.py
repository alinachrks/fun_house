import hydralit as hy
from components import about, analytics, bot, development
import hydralit_components as hc
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import streamlit as st

app = hy.HydraApp(title='My App', navbar_sticky=True, sidebar_state='collapsed')

# Вставьте этот код в начало вашего файла
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F7F8; /* Цвет фона */
        color: #202021; /* Цвет текста */
        font-family: sans-serif; /* Шрифт */
    }
    .css-1aumxhk {
        background-color: #ECEBE5; /* Второй цвет фона */
    }
    .css-1aumxhk select {
        color: #202021; /* Цвет текста в выпадающем меню */
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# option_data = [
#    {'icon': "bi bi-hand-thumbs-up", 'label':"about"},
#    {'icon':"fa fa-question-circle",'label':"analytics"},
#    {'icon': "bi bi-hand-thumbs-down", 'label':"bot"},
# ]

# # override the theme, else it will use the Streamlit applied theme
# over_theme = {'txc_inactive': 'white','menu_background':'purple','txc_active':'yellow','option_active':'blue'}
# font_fmt = {'font-class':'h2','font-size':'150%'}

# # display a horizontal version of the option bar

# # display a version version of the option bar
# op2 = hc.option_bar(option_definition=option_data,title='Feedback Response',key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=False)

@app.addapp(is_home=True)
def home():
    return about.app()

@app.addapp(title='Bot')
def app2():
    return bot.app()

@app.addapp(title='Analytics')
def app3():
    return analytics.app()

@app.addapp(title='Development')
def app4():
    return development.app()

app.run()
