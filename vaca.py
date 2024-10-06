from flask import Flask, render_template, request
import requests
import smtplib

my_email = "safrodanya@gmail.com"
password = "crgc paxx ynss ycun"

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods = ["GET", "POST"])
def contact():
    is_msg_sent = False
    if request.method == "POST":
        name = request.form.get("username")
        email = request.form.get("email")
        phone = request.form.get("phone")
        msg = request.form.get("message")
        message = (f"{name}\n{email}\n{phone}\n{msg}")
        is_msg_sent = True
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = my_email, password = password)

            connection.sendmail(from_addr = my_email, to_addrs = "rybakova_oksana@yahoo.com", msg = f"Subject: Information Form\n\n{message}")

    return render_template("contact.html", msg_sent = is_msg_sent)



@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)