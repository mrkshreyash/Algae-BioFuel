import streamlit as st
import pickle
import math

# brake_power = (2 * pi * n * t)/60
# n == speed (1500 fix)
# t == torque == load * 9.81 * arm_length

TITLE = "DIESEL ENGINE PERFORMANCE"

st.set_page_config(
    page_title = TITLE,
    layout = "wide"
)

st.write("---")
st.title(TITLE.upper())
st.write("---")

with st.container():
    left, mid, right = st.columns(3)

    with mid:
        SPEED = 1500

        DIVIDE_CONSTANT = 600

        LOAD = st.text_input(label="LOAD")

        ARM_LENGTH = st.text_input(label="ARM LENGTH")


        st.write("---")

        submit = st.button("SUBMIT")

        st.write("---")

        

        if submit:
            if LOAD == "" or ARM_LENGTH == "":
                st.error("The above fields cannot be empty.")

            else:                    
                # ------------------------------------------------------------------------------------------
                # Find Torque:
                ARM_LENGTH = float(ARM_LENGTH)
                LOAD = float(LOAD)        
                TORQUE = LOAD * 9.81 * ARM_LENGTH


                BRAKE_POWER = (2 * math.pi * SPEED * TORQUE) / DIVIDE_CONSTANT
                st.success(f"TORQUE: {TORQUE}")
                st.success(f"BRAKE POWER: {round(BRAKE_POWER, ndigits=5)}")
                

            #         copyright = "This program is created by Mr. Shreyash A. Kamble. for enquiry contact : shreyash261020@gmail.com :"
            #     # -----------------------------------------------------------------------------------------
                