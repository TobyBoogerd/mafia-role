#Developed by Toby Boogerd

import streamlit as st
import random
import time

# Function to initialize or reset roles
def initialize_roles():
    st.session_state.roles = ["Sheriff", "Doctor", "Mafia", "Mafia", "Villager", "Villager"]
    st.session_state.selected_role = None

# Initialize roles if not already done
if 'roles' not in st.session_state:
    initialize_roles()

# Streamlit interface
st.title("Mafia Role Picker")

# Button to pick a role
if st.button("Pick a Role"):
    if st.session_state.roles:
        st.session_state.selected_role = random.choice(st.session_state.roles)
        st.session_state.roles.remove(st.session_state.selected_role)
    else:
        st.write("All roles have been picked!")

# Display the selected role and automatically hide it after 3 seconds
role_display = st.empty()

if st.session_state.selected_role:
    role_display.write(f"You picked: **{st.session_state.selected_role}**")
    time.sleep(3)
    st.session_state.selected_role = None
    role_display.empty()  # Clear the display

# Reset button to start a new game
if st.button("Reset Game"):
    initialize_roles()
    st.write("The game has been reset!")

