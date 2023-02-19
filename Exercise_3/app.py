from flask import Flask, render_template, request, redirect

app = Flask(__name__)

STUDENT_ORGANIZATIONS = ["Sports & Recreation", "Academic Clubs", "Cultural Clubs", "Community Service", "Political Clubs"]

registered_students = {}

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        organization = request.form["organization"]
             
        if not name or not organization:
            return render_template("index.html", error="Please enter both name and organization.", organizations=STUDENT_ORGANIZATIONS)
        
        if organization not in STUDENT_ORGANIZATIONS:
            return render_template("index.html", error="Invalid organization selected.", organizations=STUDENT_ORGANIZATIONS)
        
        if name in registered_students:
            return render_template("index.html", error="Name already registered.", organizations=STUDENT_ORGANIZATIONS)
        
        registered_students[name] = organization
        
        return redirect("/users")
    
    return render_template("index.html", organizations=STUDENT_ORGANIZATIONS)

@app.route("/users")
def users():
    return render_template("users.html", users=registered_students)

if __name__ == "__main__":
    app.run(debug=True)