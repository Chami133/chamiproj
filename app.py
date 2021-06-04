from flask import Flask, render_template,request
# import server.py
app = Flask(__name__, template_folder='templates')


@app.route("/",methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route("/dropdown", methods=['POST'])
def dropdown():
    global selectValue
    selectValue = request.form.get('val', None)
    print(selectValue)
    if selectValue == None:
        print("No value")
        return render_template("index.html",selectValue=selectValue)
    return selectValue


if __name__ == '__main__':
    app.run()

value = "LK"
