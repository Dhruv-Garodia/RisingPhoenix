from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    product_id : int
    user_id : int
    rating : int
    time_stamp : int
        
# loading the saved model
fed_model = pickle.load(open('fed.sav', 'rb'))

@app.post('/fed_prediction')
def fed_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    
    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]
    
    prediction = fed_model.predict([input_list])
    
    if (prediction[0]):
        s = "The predicted product id : "
        s = s + prediction[0]
        return s 
    else:
        return 'Error in prediction'
    