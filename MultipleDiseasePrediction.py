import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetic_model=pickle.load(open('trained_diabetic_model.sav','rb'))

heart_model=pickle.load(open('trained_heardisease_model.sav','rb'))

Parkinson_model=pickle.load(open('trained_ParkinsonsPrediction.sav','rb'))



with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=1)
    
if (selected=="Diabetes Prediction"):

    st.title('Diabetes Prediction using ML')

    col1,col2,col3=st.columns(3)

    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')

    with col2:
        Glucose=st.text_input('Gulcose level')
    
    with col3:
        BloodPressure=st.text_input('BLOOD PRESSURE LEVEL')

    with col1:
        SkinThickness=st.text_input('SKIN THICKNESS')
    with col2:
        Insulin=st.text_input('INSULIN LEVEL')
    with col3:
        BMI=st.text_input('BMI LEVEL')
    with col1:
        DiabetesPedigreeFunction=st.text_input('DiabetesPedigreeFunction')
    with col2:
        Age=st.text_input('AGE')


    diab_diagonsis=""
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetic_model.predict([[float(Pregnancies),float(Glucose),float(BloodPressure),float(SkinThickness),float(Insulin),float(BMI),float(DiabetesPedigreeFunction),int(Age)]])
        
        if diab_prediction[0]==1:
            diab_diagonsis="The person is Diabetic"
        else:
            diab_diagonsis="The person is not Diabetic"
    st.success(diab_diagonsis)


if (selected=='Heart Disease Prediction'):

    st.title('Heart Disease Prediction using ML')
    col1,col2,col3=st.columns(3)

    with col1:
        age=st.text_input("Enter the age")
    with col2:
        sex=st.text_input("Enter the sex")
    with col3:
        cp=st.text_input("Enter the cp")
    with col1:
        trestbps=st.text_input("Enter the trestbps")
    with col2:
        chol=st.text_input("Enter the chol")
    with col3:
        fbs=st.text_input("Enter the fbs")
    with col1:
        restecg=st.text_input("Enter the restecg")
    with col2:
        thalach=st.text_input("Enter the thalach")
    with col3:
        exang=st.text_input("Enter the exang")
    with col1:
        oldpeak=st.text_input("Enter the oldpeak")
    with col2:
        slope=st.text_input("Enter the slope")
    with col3:
        ca=st.text_input("Enter the CA")
    with col1:
        thal=st.text_input("Enter the Thal")

    heart_diagonsis=""
    if st.button('Heart Disease Test Result'):
        heart_prediction=heart_model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if heart_prediction[0]==1:
            heart_diagonsis="The person is Diabetic"
        else:
            heart_diagonsis="The person is not Diabetic"
    st.success(heart_diagonsis)



if (selected=='Parkinsons Prediction'):

    st.title('Parkinsons Prediction Using ML')

    col1,col2,col3,col4,col5=st.columns(5)

    with col1:
        fo=st.text_input('MDVP:FO')
    
    with col2:
        fhi=st.text_input('mdvp:fhi')
    with col3:
        flo=st.text_input('mdvp:flo')
    with col4:
        Jitter_present=st.text_input('Jitter')
    with col5:
        jitter_abs=st.text_input('jitter_abs')
    with col1:
        MDVP_RAP=st.text_input('MDVP:RAP')
    with col2:
        PPQ=st.text_input('PPQ')
    with col3:
        DDP=st.text_input('DDP')
    with col4:
        Shimmer=st.text_input('Shimmer')
    with col5:
        Shimmer_dB=st.text_input('Shimmer(dB)')
    with col1:
        Shimmer_APQ3=st.text_input('Shimmer:APQ3')
    with col2:
        Shimmer_APQ5=st.text_input('Shimmer:APQ5')
    with col3:
        MDVP_APQ=st.text_input('MDVP:APQ')
    with col4:
        Shimmer_DDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        DFA=st.text_input('DFA')
    with col4:
        spread1=st.text_input('spread1')
    with col5:
        spread2=st.text_input('spread2')
    with col1:
        D2=st.text_input('D2')
    with col2:
        PPE=st.text_input('PPE')


    Parkinson_diagosis=""
    if st.button('Parkinsons Test Result'):
        Parkinson_prediction=Parkinson_model.predict([[fo,fhi,flo,Jitter_present,jitter_abs,MDVP_RAP,PPQ,DDP,Shimmer,Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if Parkinson_prediction[0]==1:
            Parkinson_diagosis="The person is affected by parkinson disease"
        else:
            Parkinson_diagosis="The person is not parkinson disease"
    st.success(Parkinson_diagosis)
