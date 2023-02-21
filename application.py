from flask import Flask, request, render_template
import boto3


application = Flask(__name__)

app = application
s3 = boto3.client('s3')
bucket_name = 'vehicle-logs-uploader'

# Define a route to display the table in three columns
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload():
    try:
        file = request.files['file']
        s3.upload_fileobj(file, bucket_name, file.filename)
        return 'File uploaded successfully!'
    except Exception as e:
        print(e)
        return 'File upload failed'


if __name__ == "__main__":
    app.run()