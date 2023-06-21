import streamlit
streamlit.title("My Parents New Healthy Diner")
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/Avocado")
streamlit.text(fruityvice_response)
streamlit.header("Fruityvice Fruit Advice!")
fruits_to_show = streamlit.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
