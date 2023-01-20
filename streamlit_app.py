import streamlit
import pandas

streamlit.title('My Parents new healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('1. Bread Omlette')
streamlit.text('2. Bulls Eye')
streamlit.text('3. Boiled Eggs')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

myfruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
myfruitlist = myfruitlist.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruitselected = streamlit.multiselect("Pick some fruits:", list(myfruitlist.index))

fruitToShow = myfruitlist.loc[fruitselected]

# Display the table on the page.
streamlit.dataframe(fruitToShow)
