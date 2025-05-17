import geocoder
import streamlit as st

def get_coordinates():
    g = geocoder.ip('me')
    if g.latlng:
        latitude, longitude = g.latlng
        return latitude, longitude
    else:
        return None

coordinates = get_coordinates()
if coordinates:
    latitude, longitude = coordinates
    st.write(f"Latitude: {latitude}")
    st.write(f"Longitude: {longitude}")
else:
    st.write("Could not retrieve coordinates.")