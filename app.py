from doctest import OutputChecker
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('PrediksiEmisiSVM.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost='Perlu Cek')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    CO, HC, tahun = [x for x in request.form.values()]

    data = []

    data.append(float(CO))
    data.append(float(HC))
    data.append(int(tahun))
    
    prediction = model.predict([data])
    
    if prediction == [1]:
        output = 'Kurang Bagus'
    else:
        output = 'Bagus'
    
    return render_template('index.html', insurance_cost=output, CO=CO, HC=HC, tahun=tahun)


if __name__ == '__main__':
    app.run(debug=True)