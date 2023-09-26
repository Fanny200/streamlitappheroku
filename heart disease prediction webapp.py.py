# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 04:38:53 2023

@author: DELL
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

loaded_model = pickle.load(open('C:/Users/DELL/Desktop/heart disease/saved model/heart_disease_model.sav','rb'))

with st.sidebar:
    
    selected = option_menu('Heart Disease Prediction System',
                          
                          ['Home',
                           'Heart Disease Prediction',
                           'More Info About Status',
                           'Tips To Healthy Heart'
                           ],
                          icons=['activity','heart','activity','person'],
                          default_index=0)
    
    
# Diabetes Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction Web App')
    st.write("""### We Need the Following information about you so we can help you.""")
    
    def main():
        
        #giving a title
       
        
        #about getting input data from user
        
        
        age = st.number_input('Age')
        sex = st.number_input('Sex')
        cp = st.number_input('Chest Pain types(cp),Typical angina(0), ATypical angina(1), Non angina(2), Asymptomatic(3)')
        trestbps = st.number_input('Resting Blood Pressure(trestbps)')
        chol = st.number_input('Serum Cholestoral in mg/dl(chol)')
        fbs = st.number_input('Fasting Blood Sugar (fbs)')
        restecg = st.number_input('Resting Electrocardiographic results(restecg)')
        thalach = st.number_input('Maximum Heart Rate achieved(thalach)')
        exang = st.number_input('Exercise Induced Angina(exang)')
        oldpeak = st.number_input('ST depression induced by exercise(oldpeak)')
        slope = st.number_input('Slope of the peak exercise ST segment(slope)')
        ca = st.number_input('Major vessels colored by flourosopy(ca)')
        thal = st.number_input('Thalassemia(thal): 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
        
        #code for prediction
        heart_diagnosis = ''
        
        #creating a button for prediction
        if st.button('Heart Disease Test Result'):
            heart_diagnosis = heart_disease_prediction([age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal])
            
        st.success(heart_diagnosis)
        
    def heart_disease_prediction(input_data):
        

        # change the input data to a numpy array
         input_data_as_numpy_array= np.asarray(input_data)

        # reshape the numpy array as we are predicting for only on instance
         input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

         prediction = loaded_model.predict(input_data_reshaped)
         print(prediction)

         if (prediction[0]== 0):
          return 'The Person does not have a Heart Disease'
         else:
          return 'The Person has Heart Disease'
      
        
        

    if __name__=='__main__':
        main()
    

                         


#creating a function for prediction

if (selected == 'Home'):
    
    # page title
    st.title('Welcome to A Heart Disease prediction Web App')
    st.write("""##### 
             The heart is a very vital part of the human body and 
             statistics have shown that many indivuals die due to 
             heart diseases, this part of a Human Body, Supplies nutrients 
             and oxygen rich blood to all the body parts, including itself.
             
             The Heart Disease prediction Web App is here to help 
             individuals know thier heart status without necessarily going 
             directly to the hospital, at the comfort of your home you can 
             know exactly what is wrong this will help most of us to reduce 
             cost of consultation and
             even save us alot of time.
             
             with just about 13 input and a click you get to know if your
             are at risk for free in less than no time, how fascinating will it be to 
             have that service at your disposal.
             No more excuses cause you have a solution now, Check yourself.""")
    
if (selected == 'More Info About Status'):
    
    # page title
    st.title('Get a little idea of how you can know your status on each attribute')
    
    st.write("""### 1. Chest Pain Type""")
    st.write("""#### There are types of chain pain, just check the symptoms to know which type you have""")
    st.write("""#####
             Typical angina(0): is the type that is precipitaed by physical exertion or emotional
             stress and relived with rest nitroglycerin.
             Chest, arm or jaw pain described as dull, heavy, tight or crushing""")
    st.write("""#####
             ATypical angina(1): This is common is women
             Back pain or epigastric or pain described as burning, stabbing or 
             indigestion""")
    st.write("""#####
             Non angina(2): This is a recurring pain in your chest, typically behind your breast
             bone or near your heart, it is the pain caused by heart disease.
             Painful, squeezing or tightness in your chest or pressure or heaviness 
             particularly
             behind your sternum.""")
    st.write("""#####
             Asymptomatic(3): This is the transient alteration in myocardial perfusion in 
             the absence of chest pain or usual angina.
            You have a flu, indigestion, sore muscle in chest or upper back.""")
            
    st.write("""### 2. Resting Blood Pressure(fbs)""")
    st.write("""#### This is how you can measure you blood pressure by yourself at your home""")
    st.write("""#####
             Using the sphygmomanometer(blood pressure cuff)
             sit up right in a chair
             your back against the chair
             rest your feet
             relax your hand make sure you do not make a fist
             just relax and place the cuff around your arm and start.
             
             between 90/60mmHg and 120/80mmHg is considered normal
             140/90mmHg or higher is considered as high B.P
             120/80mmHg is considered heart disease""")
    st.write("""### 3. Cholesterol Level(chol)""")
    st.write("""#### This is how you can check your Cholesterol by yourself at your home""")            
    st.write("""#####
             using the kit curoL5 cholesterol test kit meter and test strips or any other.
             pock your finger with the Lancet to draw blood
             place the blood sample in a test trip
             insert the test trip into the meter provided to measure
             
             less than 100mg/dl(Low-density Lipoproteins(LDL)) is considered Bad
             greater or equal to 60mg/dl(high-density Lipoprotein(HDL)) is considered as good
             less than 150mg/dl(triglycerides) this is fat n the blood stream that give 
             the body energy, increase in it increase a persons risk for heart attack.
             """) 
    st.write("""### 4. Blood sugar Level(""")
    st.write("""#### This is how you can check your blood sugar level by yourself""")
    st.write("""#####
             using the kit A Glucometer
             use the lancet from the kit to pock your finger and get blood.
             put the blood sample in the test strips 
             insert the test strips into the meter and wait for sometime for results
             
             less than 100mg/dl is normal
             100 to 125mg/dl is considered prediabetes
             126mg/dl or higher on is considered diabetic""")
             
    st.write("""### 5. Resting Electrocardiography(restecg)""")
    st.write("""##### 
             using the Alivecor's kardiaMobile 6L
             ECG is a non-invasive test that can detect abnormalities including
             arrhythmais, evidence of coronary heart disease, left venticular 
             hypertrophy and bundle branch blocks
             
             shows your heart is beating at an even rate 60 to 100beats per minute is normal.
             abnormal heart rate, irregular rhythm abnormal waveforms or intervals""")
             
    st.write("""### 5. maximum heart rate(thalach)""")
    st.write("""#### This is how you canknow your max heart rate""")
    st.write("""#####
             Max heart rate is the number of beats your beats your heart can
             functionally make blood pump around the body faster
             
             to obtain this you can simply subtract your age from 220
             or you can use a Stethoscope """)
    st.write("""### 6. Exercise Induced Angina(exang)""")
    st.write("""#####
             It occurs during or after exercise. It is caused 
             by a narrowing of the coronary arteries, which supply blood to the heart.
             Exercise test: This is a test that measures the heart's response to exercise.
             The test is typically done on a treadmill or stationary bike. The patient 
             starts at a low level of exercise and gradually increases the intensity 
             until they experience chest pain or other symptoms.
             
             0 for normal 
             1 for exercise induced angina""")
    
    st.write("""### 7. ST depression induced by exercise(oldpeak)""")
    st.write("""##### 
             Oldpeak is the amount of ST depression that occurs during exercise 
             relative to the resting ST segment on an electrocardiogram (ECG).
             
             To measure Oldpeak, look for the point at which
             the ST segment returns to the baseline at rest. The difference 
             between this point and the ST segment at peak exercise is the Oldpeak value.
             
             Oldpeak can be measured on a standard ECG, but it is more accurately 
             measured on an exercise stress test. An exercise stress test is a test 
             that measures the heart's response to exercise. The patient starts at a 
             low level of exercise and gradually increases the intensity until they 
             reach their target heart rate.""")
    st.write("""### 7. Slope of the peak exercise ST segment(slope)""")
    st.write("""##### 
             The slope of the peak exercise ST segment (slope) is a
             measurement used to assess the severity of coronary artery disease (CAD).
             It is measured by comparing the ST segment at rest to the ST segment at 
             peak exercise. The ST segment is the part of the electrocardiogram (ECG)
             that follows the QRS complex. The QRS complex is the part of the ECG that 
             represents the electrical activity of the heart muscle.
             
             Oldpeak is measured by comparing the ST segment at rest to the ST segment at peak exercise.
             
             To measure the slope of the peak exercise ST segment, 
             will look for the point at which the ST segment returns to the baseline at rest.
             The difference between this point and the ST segment at peak exercise is the slope.
             The slope of the peak exercise ST segment is graded on a scale of 1 to 4, 
             with 1 being the most severe. A slope of 1 or 2 is considered mild, 
             a slope of 3 is considered moderate, and a slope of 4 is considered severe.""")
    st.write("""### 8. Thalassemia(Thal)""")
    st.write("""##### 
             Thalassemia is a group of inherited blood disorders that affect the
             production of hemoglobin, the protein in red blood cells that carries oxygen. 
             There are many different types of thalassemia, but they all share the common 
             feature of decreased or abnormal hemoglobin production.
             
             Thalassemia is measured by a blood test called a complete blood count (CBC).
             The CBC measures the number of red blood cells, white blood cells, 
             and platelets in the blood. It also measures the hemoglobin level 
             and the hematocrit, which is the percentage of blood that is made 
             up of red blood cells.""")
    
    
if (selected == 'Tips To Healthy Heart'):  
    
    #page title
    st.title('How To Maintain A Healthy Heart')
    st.write("""##### 
             Eat a healthy diet: This means eating plenty of fruits, vegetables, and whole grains. 
             It also means limiting processed foods, sugary drinks, and unhealthy fats.
             
             Get regular exercise: Aim for at least 30 minutes of moderate-intensity exercise most
             days of the week.
             
             Maintain a healthy weight: Being overweight or obese is a major risk factor for heart disease.
             
             Quit smoking: Smoking damages the heart and blood vessels. If you smoke, quitting is 
             the best thing you can do for your heart health.
             
             Manage your blood pressure: High blood pressure is a major risk factor for heart disease. 
             If you have high blood pressure, work with your doctor to control it.
             
             Manage your cholesterol: High cholesterol is another major risk factor for heart disease.
             If you have high cholesterol, work with your doctor to control it.
             
             Manage your blood sugar: High blood sugar can damage the heart and blood vessels. 
             If you have diabetes, work with your doctor to control your blood sugar.
             
             Get regular checkups: Your doctor can check your risk factors for heart disease 
             and make sure you are getting the preventive care you need.
             Get enough sleep: When you don't get enough sleep, your body produces more stress hormones,
             which can damage the heart. Aim for 7-8 hours of sleep each night.
             
             Manage stress: Stress can also damage the heart. Find healthy ways to manage stress, 
             such as exercise, yoga, or meditation.
             
            Stay social: Social isolation can increase your risk of heart disease. 
            Make an effort to stay connected with friends and family.
            
            Have a positive outlook: A positive attitude can help you stay motivated to 
            make healthy lifestyle changes.""")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    