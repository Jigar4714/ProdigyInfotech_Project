# ProdigyInfotech_Project 

Task 1:- “Implement Caesar Cipher Tool”

• Objective:-
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.

•	Implementation:-
1.	Make the python script & Run
2.	Save the Python Script in kali linux.
3.	Open a text editor (e.g., nano, vim, gedit, or any other editor).
4.	Copy the Python code provided above into the editor.
5.	Save the file with a .py extension 
Nano Ceaser¬_cipher_tool.py
 
5.	Make the Script Executable 
6.	Give execute permissions to the script file:
chmod +x Ceaser_cipher_tool.py

7.	Now you can run it :
Python3 Ceaser_cipher_tool.py
 
• Conclusion:-

•	The Caesar Cipher Tool is implemented successfully, providing functionality for both encryption and decryption of text using a user-defined shift value. The program ensures accurate results and offers a user-friendly experience.



#Task 2:-  Password Strength Checker

• Objective: Build a Python program to evaluate password strength.
• Tools Required: Python, kali linux, Pycharm

✅ Steps to follow:
1. Check Password Criteria
We will check the following conditions:
•	At least 8 characters long.
•	Contains both uppercase and lowercase letters.
•	Contains at least one numeric character.
•	Contains at least one special character (e.g., !@#$%^&*()).
________________________________________
2. Provide Feedback
•	Weak: If the password doesn't meet most of the criteria (e.g., less than 8 characters).
•	Moderate: If the password meets some of the criteria but not all.
•	Strong: If the password meets all criteria.
________________________________________
3. Save Output in a Log File
We will log the password evaluation (including feedback) in a file for record-keeping.


•	Implementation:-
1.	Make the python script in pycharm 
 
2.	Install Python
First, make sure you have Python installed on your Linux machine. Most Linux distributions come with Python pre-installed, but you can verify this by running the following command in the terminal:
‘python3 –version’

If Python isn't installed, you can install it using the package manager for your distribution:
•	For kali linux:
sudo apt update
sudo apt install python3
 
3.	Save the Python Script
4.	Open a text editor (e.g., nano, vim, gedit, or any other editor).
5.	Copy the Python code provided above into the editor.
6.	Save the file with a .py extension 
Nano password_strength_checker.py
 
7.	Make the Script Executable 
8.	Give execute permissions to the script file:
chmod +x password_strength_checker.py
 
9.	Now you can run it :
Python3 password_strength_checker.py
 
10.	Check the Saved Output in a File using command
Nano password_stregth_log.txt
 
•Conclusion:-
•The Password Strength Checker is a practical tool for evaluating password robustness. By analyzing passwords against predefined criteria, it encourages users to adopt stronger, more secure practices. The inclusion of a feedback system and logging ensures better security awareness and record-keeping, making it a valuable addition to personal and organizational cybersecurity measures.
________________________________________


Task-04 :- Simple Keylogger

•	Objective:-  

•	Create a basic keylogger program that records and logs keystrokes 
•	Focus on logging the keys pressed and saving them to a file. Note:
•	mEthical considerations and permissions are crucial for projects involving keyloggers.

Here's a simple keylogger written in Python using the pynput library. This script will record keystrokes and save them to a file.
 Ethical Considerations:
•	Do NOT use this for malicious purposes.
•	Obtain explicit consent from users before running this script on any system.
•	Ensure compliance with local laws and regulations regarding monitoring and privacy.
This script will log all keypresses into a file called keylog.txt.
How It Works:
1.	Uses pynput.keyboard.Listener to listen for keypresses.
2.	Logs every keystroke to keylog.txt.
3.	Stops logging when the ESC key is pressed.
________________________________________
Installation & Usage:
1.	Install the pynput library if you haven't already: 
     -  pip install pynput
2.	 Run the script: 
     -  python keylogger.py
3.	 Press ESC to stop recording.
•	Implementation:-
1.	Make the python script in pycharm and run the script. 
 
2.	Saved file keylog.txt 
 





•	Conclusion:- 

•	The keylogger project provided valuable insights into system monitoring and cyber security. It offered practical experience in keystroke logging, data management, and software reliability. Ethical considerations were a key focus, emphasizing the importance of legal compliance and privacy protection. By using Python and libraries like pynput and logging, we enhanced both functionality and security. Future enhancements could involve real-time monitoring and advanced security measures. Overall, this project was a valuable learning experience in responsible software development.

________________________________________



Task-05 :- Network Packet Analyzer

	Objective:-
•	Develop a packet sniffer tool that captures and analyzes network packets. Display relevant     information such as source and destination IP addresses, protocols, and payload data.
Ensure the ethical use of the tool for educational purposes.



•	Implementation:-
1.	Make the python script in pycharm
 

2.	Save the Python Script in kali linux.
a)	Open a text editor (e.g., nano, vim, gedit, or any other editor).
b)	Copy the Python code provided above into the editor.
c)	Save the file with a .py extension 
Nano Packet_Analyzer.py
 
3.	Make the Script Executable 
a)	Give execute permissions to the script file:
 chmod +x Packet_Analyzer.py
 
4.	Now you can run it :
            Python3 Packet_Analyzer.py
 
5.	Check the Saved Output in a File using command
-ls
-cat packet_log.txt
 

	Conclusion:-

•	The network packet analyzer captures and analyzes network traffic, displaying key details like source and destination IPs, protocols, and payload data. It enhances understanding of network communication and cyber security. When used ethically for educational or security purposes, it aids in network monitoring and troubleshooting. 

________________________________________
