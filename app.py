from flask import Flask, render_template, url_for, request, jsonify
from model_prediction import *

app = Flask(__name__)

text=""
predicted_emotion=''
predicted_emotion_img_url=''
@app.route('/')
def home():
    entries=show_entry()
    return render_template('index.html',entries=entries)
 
@app.route('/predict-emotion', methods=["POST"])
def predict_emotion():
    
    # Get Input Text from POST Request
    input_text=request.json.get("text")
    
    if not input_text:
        # Response to send if the input_text is undefined
       response = {
           'status':'error',
           'message':'Please enter some text to predict emotion'
       }
       return jsonify(response)
   
    else:
        predicted_emotion,predict_emotion_img_url = predict(input_text)
        
        # Response to send if the input_text is not undefined
        response ={
           "status":"success",
           "data":{
              "predicted_emotion":predicted_emotion,
              "predicted_emotion_img_url":predict_emotion_img_url
           }
        }
        # Send Response         
        return jsonify(response)
       
#save entry
@app.route('/save-entry',methods=["POST"])
def save_entry():

    #get date, predicted emotion & enter by the user to save the entry
    date = request.json.get('date')
    emotion=request.json.get('emotion')
    save_text=request.json.get('text')

    save_text = save_text.replace('\n','')

    #CSV Entry
    entry = f'"{date}","{save_text}","{emotion}"\n'

    with open("./static/assets/data_files/data_entry.csv",'a') as f:
        f.write(entry)

    return jsonify("Success")

if __name__ == "__main__":
    app.run(debug=True)




    