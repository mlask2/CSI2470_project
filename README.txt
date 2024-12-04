README: How to run: Client-Server Text Application for Visual Studio Code

How to Compile and Run in Visual Studio Code (VS Code) on Windows:
1. Prerequisites
	STEP ONE:
Python installed (version 3.6 or later). Link: https://www.python.org/downloads/ 
	STEP TWO:
Download Visual Studio Code. Link: https://code.visualstudio.com/
	STEP THREE:
Install the Python Extension in VS Code:
Open VS Code, go to Extensions (Ctrl+Shift+X), and search for Python.
Install it.

2. Setting Up the Files
	STEP ONE:
Open VS Code.
	STEP TWO
Make sure the Server.py and Client.py are downloaded
	STEP THREE:
Open the Server.py and Client.py in two individual windows by clicking the files. (Should open in VS code)

3. Running the Application
	STEP ONE:
Run the server and the client
Use Ctrl+Shift+D OR click "Run and Debug" on the left hand sidebar. View the code in the terminal below. (Bottom of screen)

4. Using the Application
Server will ask the client for a NICKNAME. Enter the name you wish in the terminal
Server will ask for the password. The password is "password"
Type a message in the client terminal and press Enter.
The server will process the message and echo it back
Repeat the process to test additional messages.
 * Can have multiple client connections at once
To test multiple clients:
Open additional terminals in VS Code and run python client.py in each.
