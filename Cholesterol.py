
import streamlit  as st
import joblib
import pandas as pd
import sklearn 

model = joblib.load('pipline.h5')
Inputs = joblib.load('input.h5')



def predict(age, gender, height, weight, ap_hi, ap_lo, gluc, smoke,alco, active, cardio) :
    test_df = pd.DataFrame(columns = Inputs)
    test_df.at[0,'age'] = age
    test_df.at[0,'gender'] = gender
    test_df.at[0,"height"] = height
    test_df.at[0,"weight"] = weight
    test_df.at[0,"ap_hi"] = ap_hi
    test_df.at[0,"ap_lo"] = ap_lo
    test_df.at[0,"gluc"] = gluc
    test_df.at[0,"smoke"] = smoke
    test_df.at[0,"alco"] = alco
    test_df.at[0,"active"] = active
    test_df.at[0,"cardio"] = cardio
    result = model.predict(test_df)[0]
    return result

def main () :
    st.title('Estimate your Cholesterol') 
    age = st.slider("age" , min_value=10 , max_value=90 , value=25 , step=1)
    gender = st.selectbox("gender" ,[0, 1])
    height = st.slider("height" , min_value=0.0 , max_value= 200.0 , value=25.0 , step=0.2)
    weight = st.slider("weight" , min_value=0.0 , max_value=110.0 , value=25.0 , step=0.2)
    ap_hi = st.slider("ap_hi" , min_value=0.0 , max_value=180.0 , value=25.0 , step=0.2)
    ap_lo = st.slider("ap_lo" , min_value=0.0 , max_value=110.0 , value=25.0 , step=0.2)
    smoke = st.selectbox("smoke",[1,0])
    alco = st.selectbox("alco",[1,0])
    gluc = st.selectbox("gluc" ,[ 1, 2, 3] )
    active = st.selectbox("active",[0, 1])
    cardio = st.selectbox("cardio",[1,0])
    
    if st.button('Predict') :
        result = predict(age, gender, height, weight, ap_hi, ap_lo, gluc, smoke,alco, active, cardio)
        st.write('your cholesterol level is {}'.format(result))
                  

        
        
if __name__ == '__main__' :
    main()
    
  
