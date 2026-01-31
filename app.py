from flask import Flask, render_template, request
import re

app = Flask(__name__)

def add_commas_every_8(text):
    # 1. Clean the input: Remove ALL spaces, tabs, and newlines first
    clean_text = re.sub(r'\s+', '', text)
    
    # 2. Logic: Slice the string from i to i+8
    chunks = [clean_text[i:i+8] for i in range(0, len(clean_text), 8)]
    
    # 3. Join with a comma ONLY (no space after it)
    return ",".join(chunks)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = ""
    user_input = ""
    
    if request.method == 'POST':
        user_input = request.form.get('number_input', '')
        if user_input:
            result = add_commas_every_8(user_input)
            
    return render_template('index.html', user_input=user_input, result=result)

if __name__ == '__main__':
    app.run(debug=True)
