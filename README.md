# Exercise
## 1. Overview of the solution
For the development of the exercise I used the Python programming language, since it is easy for me to handle files, and it is not as strict as other programming languages.

Apart from the classes created, I created a python file called main where I take care of importing all the classes created for their respective instantiation and making use of the methods that I create.

In addition, I did the unit tests to check if the result of the functions that I had created was correct and in this way continue with the development of the exercise.

## 2. Explanation of the architecture
For the development of the exercise I used the MVC architecture pattern in which I organized all the python files necessary to solve it together with an extra folder of tests.

Inside the model folder, not having a database such as MongoDB, MySQL, MariaDB, among others, I stored the two test .txt.

Inside the view folder I stored the final method to print the results obtained.

And inside the controller folder I stored all the operations necessary to perform the proper procedure and in this way get the proper response.

## 3. Explanation of the approach and Methodology
The approach that I gave to the exercise was through an object-oriented programming because I find that this type of programming is simple, effective and more organized.

Although at the beginning I chose to use TDD (Test Driven Development), I did not know very well what libraries to use for use in Python, since I have practiced this type of development in React Native, for this reason, I first began to develop the classes together with their methods and once they were done I began to test them using unit tests to check if they worked as I expected and once I verified that the methods worked correctly I proceeded to occupy them in the main, however, there were two methods that I could not test them, hence I had to test them by trial and error when executing the main.

## 4. Instructions 
1. Clone the repository to a local folder using the following command: **git clone https://github.com/kjduy/Exercise.git**
2. Open the project in any text editor, preferably Visual Studio Code.
3. Once the project is open, open a terminal and go to the address where the project is located, if it is within Visual Studio Code and in the Windows operating system, the key combination **Ctrl + Shift + P** will allow you to create a terminal within the application itself automatically located in the project.
4. To run the project it is necessary to have python installed and using the following command: **py main.py** will run the application.
5. There it will ask for the name of the file to perform the test so it will be necessary to type **1stWeek.txt** to test the first example or **2ndWeek.txt** to test the second example.
6. If you want to test the unit tests it is necessary to move to the test folder, if a Windows OS is managed with the **cd test** command it is enough and there select the test to test, such as: **testFileOperator.py**
