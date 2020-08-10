from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/success',methods=['POST'])
def success():
    if request.method=='POST':
        email=request.form["emailname"]
        height=request.form["heightname"]
        print(email,height)
        return render_template("success.html")



if __name__ == "__main__":
    app.run(debug=True)
