# CSI2470_project
    Simple Client-Server Application
 **** Overview: 
This project demonstrates a basic Client-Server application using Java's TCP socket programming. The server accepts multiple client connections and echoes messages in uppercase.

 **** How to Compile and Run:

		1. Requirements
Java Development Kit (JDK) installed (JDK 8 or higher recommended).
Any text editor or IDE (e.g., VS Code, IntelliJ, or Eclipse).
Terminal/Command Prompt for execution.

	****	2. Instructions
	Step 1: Compile the Code
Save the Server and Client code in separate .java files:
Server.java
Client.java
Open a terminal or command prompt.
Navigate to the directory where the files are saved.
Compile the code using the following commands:
bash
Copy code
javac Server.java
javac Client.java

		Step 2: Run the Server
Start the server by running:
bash
Copy code
java Server
The server will begin listening for client connections on port 1234.

		Step 3: Run the Client
Open another terminal or command prompt.
Start the client by running:
bash
Copy code
java Client
The client will connect to the server on localhost (default) at port 1234.


	*****	3. Testing the Application
Once the client connects to the server, type a message in the client's terminal and press Enter.
The server will process the message and send it back in uppercase.
The client will display the server's response.

	*****	4. Notes
Ensure the server is running before starting the client.
For multiple clients, open separate terminals and run the client program in each.
To change the server port or address:
Update the port variable in both Server.java and Client.java.
Change the serverAddress variable in Client.java to the desired IP address.

	*****	Common Issues
Port Already in Use:
Make sure no other application is using port 1234.
Change the port in the code if needed.
Connection Refused:
Ensure the server is running before starting the client.
Check for firewall restrictions if running on different machines.
