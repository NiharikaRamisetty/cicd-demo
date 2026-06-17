from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <title>CI/CD Automation Dashboard</title>

    <style>
        body{
            font-family: Arial, sans-serif;
            background:#f4f6f9;
            text-align:center;
            padding:50px;
        }

        .container{
            background:white;
            width:70%;
            margin:auto;
            padding:30px;
            border-radius:10px;
            box-shadow:0px 0px 10px gray;
        }

        h1{
            color:#2c3e50;
        }

        .success{
            color:green;
            font-size:22px;
            font-weight:bold;
        }

        .card{
            display:inline-block;
            width:180px;
            margin:10px;
            padding:15px;
            background:#ecf0f1;
            border-radius:8px;
        }

        .status{
            color:green;
            font-weight:bold;
        }

        button{
            background:#3498db;
            color:white;
            border:none;
            padding:10px 20px;
            border-radius:5px;
            cursor:pointer;
        }

        button:hover{
            background:#2980b9;
        }
    </style>

</head>

<body>

    <div class="container">

        <h1>CI/CD Automation Dashboard</h1>

        <p class="success">
            Application Successfully Deployed
        </p>

        <h3>Pipeline Status</h3>

        <div class="card">
            <h4>GitHub</h4>
            <p class="status">Connected</p>
        </div>

        <div class="card">
            <h4>GitHub Actions</h4>
            <p class="status">Passed</p>
        </div>

        <div class="card">
            <h4>Docker Build</h4>
            <p class="status">Success</p>
        </div>

        <div class="card">
            <h4>Deployment</h4>
            <p class="status">Live</p>
        </div>

        <br><br>

        <button onclick="alert('CI/CD Pipeline Executed Successfully!')">
            Check Pipeline
        </button>

    </div>

</body>
</html>
"""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)