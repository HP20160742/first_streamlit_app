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
fruits_selected=streamlit.multiselect("Pick Some Fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('Fruityvice Fruit Advice!')
fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)



# take the json version of the response and normalize it  
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# output it the screen as table 
streamlit.dataframe(fruityvice_normalized)

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT * from fruit_load_list ")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)


add_my_fruit = streamlit.text_input('What fruit would you like to add?')
streamlit.write('Thanks for adding ', add_my_fruit)
