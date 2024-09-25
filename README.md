Step-by-Step Guide to Run the Flask App
Step 1: Set Up Your Environment
Make sure you have Python and Flask installed on your machine. If not, follow these instructions:

Install Python:

Ensure you have Python installed on your machine. If you don't, download and install it from python.org.
Check the installation by typing this command in your terminal:
bash
Copy code
python --version
Install Flask: Open a terminal or command prompt and run:

bash
Copy code
pip install Flask
Step 2: Organize the Project Structure
Create a directory to store your project files. Inside that directory, create two folders: one for your Flask app (app.py) and another for HTML templates (templates/). The structure will look like this:

graphql
Copy code
my_flask_app/
│
├── app.py              # The Flask Python script you uploaded
├── twitter_201904.tsv   # Your dataset (place this in the same directory as app.py)
└── templates/
    └── index.html       # The HTML template you uploaded
app.py: Your main Python Flask application script.
twitter_201904.tsv: Place your dataset in the same directory as app.py.
templates/index.html: HTML template (the one you uploaded should be inside the templates/ directory).
Step 3: Add Your app.py and index.html
Here’s how your files should look:

app.py: (Assuming it is the one you provided, place this file inside the my_flask_app directory)

index.html: (The HTML template you've provided will look like this)

html
Copy code
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tweet Analyzer</title>
</head>
<body>
    <h1>Tweet Analyzer</h1>
    <form method="post">
        <label for="term">Search Term:</label>
        <input type="text" id="term" name="term" required>
        <button type="submit">Analyze</button>
    </form>

    {% if result %}
        <h2>Analysis Results</h2>
        <ul>
            <li><strong>Daily Counts:</strong> {{ result.daily_counts }}</li>
            <li><strong>Unique Users:</strong> {{ result.unique_users }}</li>
            <li><strong>Average Likes:</strong> {{ result.average_likes }}</li>
            <li><strong>Place IDs:</strong> {{ result.place_ids }}</li>
            <li><strong>Times of Day:</strong> {{ result.times_of_day }}</li>
            <li><strong>Most Active User:</strong> {{ result.most_active_user }}</li>
        </ul>
    {% endif %}
</body>
</html>
Make sure index.html is in the templates/ directory, so Flask can correctly render it when the app is running.

Step 4: Run the Flask App
Open a Terminal: Navigate to your project directory (my_flask_app) using the terminal.

Run Flask:

Make sure you're in the directory containing app.py and run:
bash
Copy code
python app.py
Expected Output: If everything works correctly, you should see output like this in your terminal:

csharp
Copy code
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
Open Browser:

Now open your browser and go to http://127.0.0.1:5000/.
You should see the form where you can enter a search term and get the analysis results.
Step 5: Analyze and Troubleshoot
If the Application Doesn’t Load:

Make sure the terminal where Flask is running does not show any errors.
If the browser still shows "connection refused", verify that Flask is running with the correct port and the server is not blocked by any firewall or security software.
If You Encounter Parsing Issues:

If there are any memory-related errors (as seen earlier with pandas), ensure the dataset size is manageable or read it in chunks as previously discussed.
Step 6: Close the Flask Server
When you're done testing the web app, you can stop the Flask server by pressing CTRL+C in the terminal where it's running.

Summary of Steps
Set Up Environment: Install Python and Flask.
Organize Files: Set up a directory structure with app.py and templates/index.html.
Run the Application: Execute python app.py to start the web server.
Test the Application: Visit http://127.0.0.1:5000/ in your browser to interact with the app.
If any part of this process doesn’t work or if you encounter further errors, let me know, and I’ll assist you further!
