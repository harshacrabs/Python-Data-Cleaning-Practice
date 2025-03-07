import streamlit as st

#Text

st.title("Streamlit Basics")


#Header
st.header("This is a Header")

#Sub-Header
st.subheader("This is a subheader")

#text
st.text("This is simple Text")

#write dimension

st.write("This is write dimension")

#Markdown

st.markdown("[Google](hhtps://www.google.com)")

st.markdown("https://www.google.com")

#HTML 

html_page = """
<div style="background-color:blue;padding:50px">
<p style="color:yellow;font-size:50px">Welcome to Streamlit Basics!</p>
</div>
"""
st.markdown(html_page, unsafe_allow_html=True)

# Colored Text boxes

st.success("Success")

st.info("Information")

st.warning("This is a warning")

st.error("This is an error")

#Image
from PIL import Image
img = Image.open("media/YT_Channel.png")
st.image(img, width=500, caption="Youtube Channel")

# Video

video_file = open("media/aws_video.mp4", "rb")
video_bytes = video_file.read()
st.video(video_bytes)

#Videos with links

st.video("https://youtu.be/pdR5KRCd198?feature=shared")


# Audio files

audio_file = open("media/city_vibes.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

# Button

st.button("Play")

# Button with condition

if st.button("Welcome"):
    st.text("Hello World!")

# Checkbox

if st.checkbox("Checkbox"):
    st.text("Checkbox Selected")


# Radio Button

radio_button = st.radio("Your Selection", ["A", "B"])
if radio_button == "A":
    st.info("You Selected A")
else:
    st.info("You Selected B")

# Select Box

city = st.selectbox("Your Country", ["India", "USA", "UK", "Japan"])

# Multi-Select Widget

occupation = st.multiselect("Your Occupation", ["Programmer", "Data Scientist", "Data Analyst ", "Data Engineer"])

# Input Text and Numbers

name = st.text_input("Your Name", "Write Something..")
st.text(name)


# Text Area

message = st.text_area("Your Message", "Write something...")

# Input Numbers
age = st.number_input("Input a Number")


# Slider

select_value = st.slider("Select a value", 1,20)

#Baloons


#Image
from PIL import Image
img = Image.open("media/YT_Channel.png")
st.image(img, width=500, caption="Youtube Channel")


if st.button("Balloons"):
    st.balloons()

