# Feedback-system-project
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
</head>

<body>

  <h1>Universal Feedback System</h1>

  <p>
        This project implements a universal feedback system using Flask for the backend, Render for deployment, and
        PostgreSQL for database storage. It provides a simple web-based interface for collecting feedback responses and
        storing them in a database.
    </p>
    <h2>Features</h2>
    <ul>
        <li>Web-based feedback form with customizable questions.</li>
        <li>Responses stored in a PostgreSQL database.</li>
        <li>Easy deployment on Render.</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Python (3.6 or higher)</li>
        <li>Flask (<code>pip install Flask</code>)</li>
        <li>Flask-SQLAlchemy (<code>pip install Flask-SQLAlchemy</code>)</li>
        <li>PostgreSQL</li>
    </ul>
    <h2>Setup</h2>
    <ol>
        <li><strong>Clone the Repository:</strong></li>
        <pre><code>[git clone https://github.com/yourusername/universal-feedback-system.git](https://github.com/ananya39mehta/Feedback-system-project-master.git)
cd universal-feedback-system
</code></pre>
        <li><strong>Install Dependencies:</strong></li>
        <pre><code>pip install -r requirements.txt
</code></pre>
        <li><strong>Configure Database:</strong></li>
        <ul>
            <li>Create a PostgreSQL database.</li>
            <li>Update the database URI in <code>app.py</code>:</li>
            <pre><code>app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@hostname:port/database_name'</code></pre>
        </ul>
        <li><strong>Run the Application:</strong></li>
        <pre><code>python app.py
</code></pre>
        <p>The application will start locally on <code>http://127.0.0.1:5000/</code>.</p>
    </ol>
    <h2>Deployment on Render</h2>
    <ol>
        <li><strong>Create a Render Account:</strong></li>
        <p>Sign up for an account on <a href="https://render.com/">Render</a>.</p>
        <li><strong>Create a New Web Service:</strong></li>
        <ul>
            <li>Click on "Create New" &gt; "Web Service".</li>
            <li>Choose GitHub as the repository source.</li>
            <li>Select your repository and configure the deployment settings.</li>
        </ul>
        <li><strong>Configure Environment Variables:</strong></li>
        <p>Set the <code>SQLALCHEMY_DATABASE_URI</code> environment variable to your PostgreSQL database URI.</p>
        <li><strong>Deploy the Application:</strong></li>
        <p>Click "Deploy" to deploy your application on Render.</p>
    </ol>
    <h2>Customization</h2>
    <ul>
        <li><strong>Customize Feedback Questions:</strong></li>
        <p>Update the <code>questions</code> list in <code>app.py</code> to customize the feedback questions displayed
            in the form.</p>
    </ul>
    <h2>Contributing</h2>
    <p>Contributions are welcome! If you have suggestions, enhancements, or bug fixes, feel free to submit a pull
        request.</p>
    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
    <h2>Author</h2>
    <p>Ananya Mehta</p>
    <hr>
    <p>Below are example images of the feedback form:</p>
</body>

</html>

![image](https://github.com/ananya39mehta/Feedback-system-project-master/assets/121433203/0e67b30b-b992-4727-93fe-b86000d688f1)

![image](https://github.com/ananya39mehta/Feedback-system-project-master/assets/121433203/0e67b30b-b992-4727-93fe-b86000d688f1)

![image](https://github.com/ananya39mehta/Feedback-system-project-master/assets/121433203/361cda00-3876-45fa-98a3-13c01ed485af)








