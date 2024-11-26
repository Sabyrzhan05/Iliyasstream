import streamlit as st
from Pages import home, project1, Project2, Project3
from streamlit_navigation_bar import st_navbar as navbar, st_navbar
import os
from PIL import Image
import pandas as pd
import numpy as np

# Загрузка фотки для лого
image = Image.open('img/logo.png')
st.set_page_config(initial_sidebar_state="collapsed", page_icon=image)

# путь к логотипу
logo_path = os.path.join(os.path.dirname(__file__), "img", "fc-barcelona-logo.svg")
pages = ["home", "project1", "Project2", "Project3"]

# Стили навигации
styles = {
    "nav": {
        "background-color": "red",
        "display": "flex",
        "justify-content": "center",
        "padding": "10px",
        "box-shadow": "0 2px 4px rgba(0, 0, 0, 0.1)"  # Лёгкая тень для объёма
    },
    "img": {
        "position": "absolute",
        "left": "15px",
        "top": "5px",
        "width": "90px",
        "height": "40px"
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "display": "block",
        "color": "white",
        "margin": "0 0.5rem",
        "padding": "0.6rem 1.2rem",
        "font-size": "16px",
        "font-weight": "500",
        "transition": "background-color 0.3s ease-in-out, color 0.3s ease-in-out",
    },
    "active": {
        "background-color": "blue",  # При активации синий цвет
        "color": "white",
        "font-weight": "bold",
    },
    "hover": {
        "background-color": "blue",  # При наведении синий цвет
        "color": "white",
    }
}


options = {
    "show_menu": False,
    "show_sidebar": True,
}


page = st_navbar(pages, styles=styles, logo_path=logo_path, options=options)

# Проверка активной страницы
if page == "home":
    home.home().app()
elif page == "project1":
    project1.project1().app()
elif page == "Project2":
    Project2.Project2().app()
elif page == "Project3":
    Project3.Project3().app()
else:
    home.home().app()






