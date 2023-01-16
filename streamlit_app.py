import streamlit
#streamlit.title('Hello, Harish here..')
#streamlit.header('List of My Hobbies:')
#streamlit.text('Playing Cricket')
#streamlit.text('Hiking')

streamlit.title('My New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥗Omega 3 & Blueberry Oatmeal')
streamlit.text('🧋Kale, Spinach & Rocket Smoothie')
streamlit.text('🥚Hard-Boiled Free-Range Egg')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
