import streamlit as st
import random
import time

# Function to initialize or reset roles based on the number of players
def initialize_roles(num_players):
    if num_players == 4:
        st.session_state.roles = ["Sheriff", "Doctor", "Mafia", "Villager"]
    elif num_players == 5:
        st.session_state.roles = ["Sheriff", "Doctor", "Mafia", "Mafia", "Villager"]
    elif num_players == 6:
        st.session_state.roles = ["Sheriff", "Doctor", "Mafia", "Mafia", "Villager", "Villager"]
    st.session_state.selected_role = None

# Initialize roles if not already done
if 'roles' not in st.session_state:
    st.session_state.num_players = 4  # Default to 4 players
    initialize_roles(st.session_state.num_players)

# Streamlit interface
st.title("Mafia Role Picker")

# Input for the number of players
num_players = st.number_input("Enter the number of players (4-6):", min_value=4, max_value=6, value=st.session_state.num_players)

# Update roles if the number of players changes
if num_players != st.session_state.num_players:
    st.session_state.num_players = num_players
    initialize_roles(st.session_state.num_players)

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
    time.sleep(2)
    st.session_state.selected_role = None
    role_display.empty()  # Clear the display

# Reset button to start a new game
if st.button("Reset Game"):
    initialize_roles(st.session_state.num_players)
    st.write("The game has been reset!")

# Add footer
st.markdown("---")
st.markdown("**Developer: Toby Boogerd**")
