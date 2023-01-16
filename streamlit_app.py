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

streamlit.header('🍎🍏 Build Your Own Fruit Smoothie 🍏🍎')
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index))
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
