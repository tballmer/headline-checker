from flask import Flask, redirect, render_template, render_template_string, request, redirect, url_for
from forms import Todo
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import openai
import numpy as np
from decouple import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'password'


@app.route('/name/<string:content>')
def name(content):
    return f'{content}'

@app.route('/', methods=['GET','POST'])
def todo():
    todo_form = Todo()
    if todo_form.validate_on_submit():
        matplotlib.use('agg')
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
            return {'reliable': percentyes, 'unreliable': percentno, 'unknown': unknown}
            
        stats = GPT3Call(todo_form.content.data)

        def pie(data):
            if data['unknown'] < 0.0001:
                labels = ['unreliable', 'unknown', 'reliable']
                sizes = [abs(data['unreliable']), abs(data['unknown']), abs(data['reliable'])]
                fig1, ax1 = plt.subplots()
                colors = ['#ff9999','#66b3ff','#99ff99']
            else:
                labels = ['unreliable', 'reliable']
                sizes = [abs(data['unreliable']), abs(data['reliable'])]
                fig1, ax1 = plt.subplots()
                colors = ['#ff9999','#99ff99']
            plt.figure(facecolor='#9E9E9E')
            explode = (0.05,0.05,0.05)
            plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85)
            centre_circle = plt.Circle((0,0),0.70,fc='#9E9E9E')
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)
            ax1.axis('equal')
            plt.tight_layout()
            fig = plt
            buf = BytesIO()
            fig.savefig(buf, format="png")
            data = base64.b64encode(buf.getbuffer()).decode("ascii")
            return f"<img src='data:image/png;base64,{data}'/>"

        piegraph = pie(stats)
        print(stats['reliable'])  
        return render_template('todo.html', form=todo_form, results= "reliable: "+ str(stats['reliable'])[:12] + '%\n unreliable: '  + str(stats['unreliable'])[:12] + "%", piegraph=piegraph)

    return render_template('todo.html', form=todo_form)


if __name__ == '__main__':
    app.run()