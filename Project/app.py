from flask import Flask, render_template, request
import pickle


app = Flask(__name__)

with open('model.pkl','rb') as handle:
	model = pickle.load(handle)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    article = request.get_data()
    pred = model.predict([article])
    pred1 = listToString(pred)
    return render_template('child.html',prediction_text = 'The News Article is "{}"'.format(pred1))     

def listToString(s):   
    str1 = ""         
    for ele in s:  
        str1 += ele        
    return str1      
   

if __name__ == '__main__':
    app.run()
    