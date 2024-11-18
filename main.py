from flask import Flask, request, jsonify,render_template
import pandas as pd
import pickle

app = Flask(__name__)
placement_model1 = pickle.load(open('RandomForestClassifier.pkl', 'rb'))
placement_model2= pickle.load(open('GaussianNB.pkl', 'rb'))
#Defines a route for the home page
@app.route('/')
def home():
    return render_template('input.html')

# Route for uploading CSV file
@app.route('/upload', methods=['POST'])
def upload_csv():    
    csv_file = request.files['file']
    if csv_file:
        data = pd.read_csv(csv_file)       
        response_final_rfc=placement_model1.predict(data)
        response_final_gnb=placement_model2.predict(data)
        p_status_rfc='Heart is Healthy' if response_final_rfc[0]==0 else 'Heart is Defect'
        p_status_gnb='Heart is Healthy' if response_final_gnb[0]==0 else 'Heart is Defect'
        return render_template('input.html',prediction_text_rfc='Patient Report = {}'.format(p_status_rfc),prediction_text_gnb='Patient Report = {}'.format(p_status_gnb))        
    else:
        return jsonify({'error': 'No file uploaded'})

if __name__ == '__main__':
    app.run(debug=True)
