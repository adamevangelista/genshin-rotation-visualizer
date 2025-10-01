Genshin Rotation Visualizer

A web-based tool that visualizes optimized Genshin Impact team rotations. This project turns complex, text-based rotation notation into clean, intuitive timelines to help players play their team comps optimally.

Demo Video

[![Genshin Rotation Visualizer Demo](/static/demo/thumbnail.png)](https://youtu.be/TK5-j3Flofw)

Core Functionality

This programs core function is a dynamic parser that reads custom .gsim rotation files to extract character actions, timings, and descriptive labels. The processed data is then rendered as an interactive timeline displayed on a bar chart, which shows each character's actions in a sequential flow. To accommodate a growing library of teams, the user interface is designed to be highly scalable, organizing rotations by their main DPS character in a two-tier dropdown system. Furthermore, the application is built to be self-contained, with all character icons and rotation data hosted locally.

The Backend (Python & Flask)

The backend is composed of a web server built with the Flask framework, which serves the main index.html file and provides a simple API endpoint for the frontend to request rotation data. The backend logic is in the gsim_parser.py. When the API is called, this script reads the requested .gsim text file, separates actions from comments, and extracts the character, action type, total duration, and a tooltip label. It then constructs a structured list of action objects in JSON format and returns it to the Flask server, which sends the data to the frontend.

The Frontend (HTML, JavaScript, Chart.js)

The frontend is what the user sees and interacts with in their browser. The user interface is a single HTML file formatted using Tailwind CSS. A dedicated JavaScript file, character_db.js, contains a database of all characters and the paths to their locally stored icons, which keeps the main HTML file clean and easy to manage. The primary script in index.html handles all user interactions. It populates the "Select a Team" dropdown based on the chosen character and sends a fetch request to the backend's API when the user wishes to generate a visualization. Upon receiving the JSON data from the server, it uses the Chart.js library to dynamically render the final, easy-to-read timeline.

Scalability and Maintenance

Adding a new character with multiple new teams is easy. First, a new .gsim data file must be created for each team, formatted with one action per line and including # duration= and # label= comments. Next, the Python parser must be updated by adding the new character names to its CHARACTER_NAME_MAP dictionary. Finally, the frontend needs to be updated by adding the new character to the dropdown menu and their teams to the TEAM_DATA object in index.html, and placing their icon in the /static folder.
Local Installation and Execution

To run this application on a local machine, please follow the steps below.

    Clone the repository:

    git clone <https://github.com/adamevangelista/genshin-rotation-visualizer>
    cd genshin-rotation-visualizer

    Install dependencies:

    python3 -m pip install -r requirements.txt

    Run the Flask server:

    python3 app.py
