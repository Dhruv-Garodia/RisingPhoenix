from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    
    uid : str
    iid : str
    r_ui : int
        
# loading the saved model
fed_model = pickle.load(open('/Users/dhruvjyotigarodia/Documents/GitHub/bd_project/RisingPhoenix/estore/fed_model.sav', 'rb'))

@app.post('/fed_prediction')
def fed_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    uid= input_dictionary['uid']
    iid = input_dictionary['iid']
    r_ui = input_dictionary['r_ui']
    
    
    input_list = [iid,uid,r_ui]
    
    # prediction = fed_model.predict([input_list])
    
    prediction = fed_model.predict(uid = input_list[0],iid = input_list[1],r_ui=input_list[-1])
    print(prediction)

    if (prediction[0]):
        s = "The predicted product id : "
        s = s + prediction[0]
        return s 
    else:
        return 'Error in prediction'
    