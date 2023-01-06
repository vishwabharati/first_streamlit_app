import streamlit 
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Mom's new healthy diner")

streamlit.header("Breakfast Favorites")
streamlit.text("🥣 Omega 3 and Blueberry Oatmeal")
streamlit.text("🥗 Kale, Spinach and Rocket Smoothie")
streamlit.text("🐔 Hard-boiled Free-Range Egg")
streamlit.text("🥑🍞 Avocado Toast")


streamlit.header("🍌🥭 Build Your Own Fruit Smoothie 🥝🍇")


my_fruits_list = pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
my_fruits_list.set_index('Fruit', inplace=True)
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruits_list.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruits_list.loc[fruits_selected]

streamlit.dataframe(fruits_to_show)
#new section to display  fruityvice api response
streamlit.header('Fruityvice Fruit Advice')

#add a function
def get_fruityvice_data(this_fruit_choice):
   fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
   fruityvice_normalized =pandas.json_normalize(fruityvice_response.json())
   return fruityvice_normalized 

try:
  fruit_choice = streamlit.text_input('What fruit would you like more info about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    
    # streamlit.write('The user entered', fruit_choice)
#     fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    # streamlit.text(fruityvice_response.json())
    #normalize the json version of the response and save to a dataframe
#     fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    #display the table/df in webapp
#     streamlit.dataframe(fruityvice_normalized)
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
   
except URLError as e:
  streamlit.error()
  

streamlit.header("The fruit load list contains")
def get_fruit_load_list():   
   with my_cnx.cursor() as my_cur:
      my_cur.execute("select * from fruit_load_list")
      return my_cur.fetchall()
   
if streamlit.button('Get Fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list()
   streamlit.dataframe(my_data_rows)
   
streamlit.stop()
add_my_fruit = streamlit.text_input('What fruit would you like to add','jackfruit')
streamlit.write("Thanks for adding", add_my_fruit)
my_cur.execute("insert into fruit_load_list values ('from_streamlit')")
