import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import os


class home:
    @staticmethod
    def app():
        st.title("Welcome to the BARCELONA HOME PAGE")



        def load_lottieurl(url):
            r = requests.get(url)
            if r.status_code != 200:
                return None
            return r.json()


        def local_css(file_name):
            with open(file_name) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


        css_path = os.path.join(os.path.dirname(__file__), "style", "style.css")
        if os.path.exists(css_path):
            local_css(css_path)


        lottie_coding = load_lottieurl("https://lottie.host/ef5c6fe8-c304-4f0b-a74e-4c80029a92d9/HvwLOSuiCr.json")
        img_contact_form = Image.open(r"D:\VSCODE\pythonProject\img\ol.png")
        img_lottie_animation = Image.open(r"D:\VSCODE\pythonProject\img\j.png")


        with st.container():
            st.subheader("Hi, I am Iliyas :wave:")
            st.title("I am student ")
            st.write("Arizona Alga!")


        with st.container():
            st.write("---")
            left_column, right_column = st.columns(2)
            with left_column:
                st.header("Barcelona")
                st.write("##")
                st.write(
                    """
                    Barcelona has won five UEFA Champions League titles, a record four UEFA Cup Winners' Cup titles, a record three Inter-Cities Fairs Cup titles (non-UEFA), a shared record of two Latin Cup titles, a shared record of five UEFA Super Cup titles and three FIFA Club World Cup titles. They are also second to Real Madrid in terms of overall official titles 98–99.
                    """
                )
            with right_column:
                if lottie_coding:
                    st_lottie(lottie_coding, height=300, key="coding")


        with st.container():
            st.write("---")
            st.header("My Projects")
            st.write("##")
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_lottie_animation)
            with text_column:
                st.subheader("Barcelona 2010-2011")
                st.write(
                    """
                    VISCA BARCA
                    """
                )

        with st.container():
            image_column, text_column = st.columns((1, 2))
            with image_column:
                st.image(img_contact_form)
            with text_column:
                st.subheader("Barcelona 2014-2015")
                st.write(
                    """
                   VISCA BARCA! BARCA ALGA!
                    """
                )


        with st.container():
            st.write("---")
            st.header("Write your contact")
            st.write("##")

            contact_form = """
            <form action="#" method="POST">
                <input type="hidden" name="_captcha" value="false">
                <input type="text" name="name" placeholder="Your name" required>
                <input type="email" name="email" placeholder="Your email" required>
                <textarea name="message" placeholder="Your message here" required></textarea>
                <button type="submit">Send</button>
            </form>
            """
            left_column, right_column = st.columns(2)
            with left_column:
                st.markdown(contact_form, unsafe_allow_html=True)
            with right_column:
                st.empty()


