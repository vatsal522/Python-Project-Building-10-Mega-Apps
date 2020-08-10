from flask import Flask,render_template

app=Flask(__name__)

# if i write about in quotes like '/about/'

#then it will open that page only
# like I will not be able to open localhost:5000 and load content
# I will be able to do so when the URL is localhost:5000/about


@app.route('/') 
def home():
    return render_template('home.html')


@app.route('/about/') 
def about():
    return render_template('about.html')

#render template is used to pickup HTML templates and use them while coding in Python





if __name__=="__main__":
    app.run(debug=True)
