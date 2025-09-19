# bruteforce
How to Run the Program

Step 1: Set Up the Environment

Verify that Python 3 is installed on your computer.

To create the graph, run the matplotlib library installation in the terminal:
pip install matplotlib

Step 2: Start the Project

Place the bruteforce.py file in a directory on your computer.

In Visual Studio Code, open that folder.

Step 3: Run the Script

Access the bruteforce.py file through VSCode.

Press the "Play" button or the run arrow, located in the top-right corner of the editor.

Step 4: Examine the Results

The program will display the following in the VSCode integrated terminal:

The password found.

The total number of attempts.

The total duration in seconds. Step 5: Modify Parameters

Change test password:
password = "cumA"

Change maximum test length:
max_length = 4
When you run the script, the terminal only displays the password found, how many attempts it took, and how long it took.

You can change the test password, such as password = "cumA," or set a different maximum length, such as max_length = 4.

For example:

Password found: cumA

Total attempts: 6876

Time: 0.8231 seconds

The graph shows how the time increases as more attempts are required.

Honestly, the longer and more complex a password is (with capital letters, numbers, and symbols), the more difficult it will be. Even the fastest computers would take years or centuries to crack a truly strong password. This makes you realize the importance of using strong passwords. In addition to not having a very good computer, the computer can get stuck when trying to enter a password with many characters, that is, more than 8. In addition, this method is very bad for decrypting a password because I believe it is detectable and very slow.
