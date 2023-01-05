import streamlit 
streamlit.title("My Mom's new healthy diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")

import pandas
my_fruits_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list.set_index('Fruit', inplace=True)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
#new section to display  fruityvice api response
streamlit.header('Fruityvice Fruit Advice')
import requests
fruit_choice = streamlit.text_input('What fruit would you like more info about', 'Kiwi')
streamlit.write('The user entered', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
# streamlit.text(fruityvice_response.json())
#normalize the json version of the response and save to a dataframe
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#display the table/df in webapp
streamlit.dataframe(fruityvice_normalized)
