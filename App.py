import streamlit as st
from Pages import home
from Pages import project1, Project2, Project3
from pygments.styles.dracula import background
from streamlit_navigation_bar import st_navbar as navbar


st.set_page_config(initial_sidebar_state="collapsed")

pages = ["home","project1", 'Project2','Project3']


styles = {
    "nav": {
      "background-color": "rgb(123, 209, 146)",
    },
    "div": {
        "max-width": "32rem",
    },
    "span": {
        "border-radius": "0.5rem",
        "color": "rgb(49, 51, 63)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
    },
    "active": {
        "background-color": "rgba(105, 114, 255, 0.25)",
    },
    "hover": {
        "background": "rgba(255, 255, 255,0.35)",
    },
}

page = navbar(pages, styles = styles)

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



