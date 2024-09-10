from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Welcome to My App</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
        <div class="container text-center mt-5">
            <h1>Welcome to My Flask App</h1>
            <p class="lead">This is a simple, clean web page built using Python and Flask.</p>
            <a href="#" class="btn btn-primary">Learn More</a>
            <a href="#" class="btn btn-secondary">Contact Us</a>
        </div>
        <footer class="text-center mt-5">
            <p>&copy; 2024 My App. All Rights Reserved.</p>
        </footer>
    </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
