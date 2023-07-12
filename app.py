import streamlit as st
import sys
import random

from defined.char_builder import character

output_file_path = "rand_character.txt"
sys.stdout = open(output_file_path, "w")

st.set_page_config(page_title="D&D Character Generator", layout="wide")

st.title("D&D Character Background Generator")
st.subheader("Fun project to create a randomly generated lvl 1  5e DnD character ")

new_char = character()

regen_button = st.button("Rerun")

if regen_button:
    # Call your Python function
    new_char = character()
    # Rerun the app
    st.experimental_rerun()

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Character details")
    #st.write("Name = ", new_char.name)
    st.write("Race = ",new_char.race)
    st.write("Class = ", new_char.characterClass)
    st.write("HP = ", new_char.hitPoints)
    st.write("Gender = ",new_char.gender)
    st.write("Age =  ",new_char.age)
    st.write("Alignment = ",new_char.alignment)

with col2:
    st.header("Character attributes")
    st.write("STR = ", new_char.abilityScores['STR'])
    st.write("DEX = ", new_char.abilityScores['DEX'])
    st.write("CON = ", new_char.abilityScores['CON'])
    st.write("INT = ", new_char.abilityScores['INT'])
    st.write("WIS = ", new_char.abilityScores['WIS'])
    st.write("CHA =", new_char.abilityScores['CHA'])

with col3:
    st.header("Character modifiers")
    st.write("STR = ", new_char.modifiers['STR'])
    st.write("DEX = ", new_char.modifiers['DEX'])
    st.write("CON =", new_char.modifiers['CON'])
    st.write("INT = ",new_char.modifiers['INT'])
    st.write("WIS = ", new_char.modifiers['WIS'])    
    st.write("CHA =", new_char.modifiers['CHA'])



