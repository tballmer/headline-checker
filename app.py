from flask import Flask, redirect, render_template, request, redirect, url_for
from forms import Todo
import openai
import numpy as np
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'

'''
@app.route('/', methods=['GET','POST'])
def hello_world():
    request_method = request.method
    if request.method == 'POST':
        content = request.form['content']
        return redirect(url_for('name',content=content))
    return render_template('hello.html',request_method=request_method)
'''
@app.route('/name/<string:content>')
def name(content):
    return f'{content}'

@app.route('/', methods=['GET','POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        print(todo_form.content.data)

        openai.api_key = config('TRUTH_TELLER_API_KEY')

        def GPT3Call(prompt):
            response = openai.Completion.create(
                model="curie:ft-personal-2022-01-16-04-34-35",
                prompt=f'{prompt}\nReliable: ',
                logprobs = 2,
                max_tokens = 1
                )
            try:
                percentno = 100 * np.e ** response.choices[0]['logprobs']['top_logprobs'][0]['no']
            except:
                percentno = 0
            try:
                percentyes = 100 * np.e ** response.choices[0]['logprobs']['top_logprobs'][0]['yes']
            except:
                percentyes = 0
            unknown = 100 - (percentyes + percentno)
            return {'relibale': percentyes, 'unreliable': percentno, 'unknown': unknown}
            
        stats = GPT3Call(todo_form.content.data)
        print(stats['relibale'])
        

    return render_template('todo.html', form=todo_form)

if __name__ == '__main__':
    app.run(debug=True)