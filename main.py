### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''

import pickle
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

model = pickle.load(open('Peer_Reader.pkl', 'rb'))

@app.route('/')
def welcome():
    return render_template('index.html')
      


### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        abstract=request.form['science']


        prediction = model.predict([abstract])
        final = output(prediction)

    return render_template('extend.html', output = final)






def output(my_pred):

    if my_pred[0] == 0 :
       return 'We regret to inform that your paper is not accepted'
        
    else:
        return 'Congratulations your paper is accepted'



    



if __name__=='__main__':
    app.run(debug=True)