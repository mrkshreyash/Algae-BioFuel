import streamlit as st
import pickle

TITLE = "Novel Smart Algae Bio Panel and It's Growth Forecasting using ML-A Sustainable Solution"

st.set_page_config(
    page_title = TITLE,
    layout = "wide"
)

st.write("---")
st.title(TITLE.upper() + ":test_tube:")
st.write("---")

# st.header("THEME NAME : AGRICULTURAL ANIMAL HUSBANDRY")
st.header("Theme Name : Agricultural Animal Husbandry :rocket:")
st.write("---")

with st.container():
    left, mid, right = st.columns(3)

    with mid:
        day = st.number_input(label="DAY", min_value=1)

        ph_value = st.number_input(label="PH VALUE", min_value=0.0)

        st.write("---")

        submit = st.button("SUBMIT")

        st.write("---")

        if submit:
            # ------------------------------------------------------------------------------------------
            ml_inputs = [[day, ph_value]]

            if ml_inputs == [[1, 0]]:
                st.warning("Please, enter the values. The above fields should not be empty.")
            else:
                ml_model = pickle.load(open('algae_model.pkl', 'rb'))
                prediction = ml_model.predict(ml_inputs)

                st.success(f"The algae growth per volume litre: {round(prediction[0], 6)}")

                copyright = "This program is created by Mr. Shreyash A. Kamble. for enquiry contact : shreyash261020@gmail.com :"
            # -----------------------------------------------------------------------------------------



with st.container():
    st.write("---")
    img1, img2, img3, img4 = st.columns(4)

    with img1:
        st.image(r"assets/images/img 1.jpg")
    with img2:
        st.image(r"assets/images/img 2.png")
    with img3:
        st.image(r"assets/images/img 3.jpg")
    with img4:
        st.image(r"assets/images/img 4.jpg")

    st.write("---")


