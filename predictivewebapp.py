# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pickle
import streamlit as st

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.pexels.com/photos/261181/pexels-photo-261181.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
background-size: 120%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}



</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)



# loading the saved model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'Resort Hotel'
    else:
      return 'City Hotel'
  
    
  
def main():
    
    
    # giving a title
    #st.title('Hotel Prediction Web App')
    st.markdown("<h1 style='text-align: center; color: white;'>Hotel Prediction Web App</h1>", unsafe_allow_html=True)
    
    # getting the input data from the user
    
    form = st.form("Form 1")

    choice_meal_list = {-1:"Select Option", 0: "BB", 1: "FB", 2: "HB", 3: "SC", 4: "Undefined"}
    
    def drop_func(meal):
        return choice_meal_list[meal]

    meal = form.selectbox('Select Meal Type', options=list(choice_meal_list.keys()), format_func=drop_func)
    
    choice_market_segment = {-1:"Select Option", 0: "Direct", 1: "Corporate", 2: "Online TA", 3: "Offline TA/TO", 4: "Complementary", 5: "Groups", 6: "Aviation"}

    def drop_func2(segment):
        return choice_market_segment[segment]
    
    market_segment = form.selectbox('Select Marcket Segment', options=list(choice_market_segment.keys()), format_func=drop_func2)
    
    choice_reserved_room_type_list = {-1:"Select Option", 1: "C", 2: "A", 3: "D", 4: "E", 5: "G", 6: "F", 7: "H", 8: "L", 9: "B"}
    
    def drop_func3(room):
        return choice_reserved_room_type_list[room]

    reserved_room_type_list = form.selectbox('Select Room Type', options=list(choice_reserved_room_type_list.keys()), format_func=drop_func3)
  
    col1,col2 = form.columns(2)
    stays_in_weekend_nights = col1.text_input('Weekend Nights')
    
    stays_in_week_nights = col2.text_input('Weekday Nights')
    
    col3,col4,col5 = form.columns(3)
    adults = col3.text_input('No of Adults')   
    children = col4.text_input('No of Childrens')
    babies = col5.text_input('No of Babies')
    
    col6,col7 = form.columns(2)
    adr= col6.text_input('adr')
    
    required_car_parking_spaces = col7.text_input('Required Car Parking Spaces')
    
    
    # code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    btnsubmit = form.form_submit_button('Hotel Result')
    
    if btnsubmit:
        if stays_in_weekend_nights == '':
            col1.error("Pleace enter no of weekend nights.")
            st.stop()
    
    if btnsubmit:
        if stays_in_week_nights == '':
            col2.error("Pleace enter no of weekday nights.")
            st.stop()
            
    if btnsubmit:
        if adults == '':
            col3.error("Pleace enter no of adults.")
            st.stop()
            
    if btnsubmit:
        if children == '':
            col4.error("Pleace enter no of childrens.")
            st.stop()
    
    if btnsubmit:
        if babies == '':
            col5.error("Pleace enter no of babies.")
            st.stop()
            
    if btnsubmit:
        if adr == '':
            col6.error("Pleace enter adr.")
            st.stop()
    
    if btnsubmit:
        if required_car_parking_spaces == '':
            col7.error("Pleace enter required car parking spaces.")
            st.stop()
            
    if btnsubmit:
        try:
            int(stays_in_weekend_nights)
            
        except ValueError:
           col1.error("Pleace enter Integer values.")
           st.stop()
    
    if btnsubmit:
        try:
            int(stays_in_week_nights)
            
        except ValueError:
           col2.error("Pleace enter Integer values.")
           st.stop()
           
    if btnsubmit:
        try:
            int(adults)
            
        except ValueError:
           col3.error("Pleace enter Integer values.")
           st.stop()
           
    if btnsubmit:
        try:
            int(children)
            
        except ValueError:
           col4.error("Pleace enter Integer values.")
           st.stop()
    
    if btnsubmit:
        try:
            int(babies)
            
        except ValueError:
           col5.error("Pleace enter Integer values.")
           st.stop()
           
    if btnsubmit:
        diagnosis = diabetes_prediction([meal, market_segment, reserved_room_type_list, stays_in_weekend_nights, stays_in_week_nights, adults, children, babies, adr, required_car_parking_spaces])
        
        
    form.success(diagnosis)
    
    
    
    
    
if __name__ == '__main__':
    main()