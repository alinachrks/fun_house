import hydralit as hy
from components import about, analytics, bot, development
import hydralit_components as hc
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
import streamlit as st

app = hy.HydraApp(title='My App', navbar_sticky=True, sidebar_state='collapsed')

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

@app.addapp()
def app2():
    return bot.app()

@app.addapp(title='The Best', icon="🥰")
def app3():
    return analytics.app()

app.run()
