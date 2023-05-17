# SQL-Registration-System

This is a registration system for employees

## Video Demo 



## Interface
The user interface is developed used tkinter GUI toolkit
- The program allows to add a new employee to the database with an id, name, and phone number
- The program also allows user to update a given employee details based on id
- To delete an employee from system given the id
- The interface has a display where employee details show up as new employees are added, deleted, or updated 

The python script connects to an SQL database using the python package [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)

## Database
In order for the python script to work properly you must first create the local database on your machine. Running the script without instantiating the database 
will not allow for insert, update, delete, and display functionality

### instructions for database setup: 
- In a [MySQL Workbench](https://www.mysql.com/products/workbench/) local instance in your computer open the sql script `registration_system_sql_query.sql` included in this repository
- This will create a database named `registration_system` amongst your schemas
- It will also create a table called `employees` within that new database
- The `employees` table will be created with three columns, `id`, `name`, `phone`
- It will also insert three employees so that when the python script is run there is some initial data for the tkinter interface to display


## Running the Script

### Dependencies
Before running the script the following dependencies must be installed: 
1. `pip install mysql-connector-python` [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
2. `pip install tk`
- tkinter might already be installed if you have python installed in your system as it is a native python tool
- you can run `python -m tkinter` from command prompt to check and if a popup that displays `click me!` appears then tkinter is installed

### Database Connection
At the top of the python script there are 4 variables under the commented line `# mysql connection variables`
1. `host` set to `'localhost'`
2. `user` set to `'root'`
3. `password` set to `'password'`
4. `database` set to `'registration_system'`

These details are necessary to connect to the local database you are running on your machine in MySQL WorkBench
- If for some reason you have different credentials for local databases in your computer, edit those variables accordingly 
- It is important that the database is set to `registration_system` as that is the name for the database created by the `registration_system_sql_query.sql` script
- If you want to change the name of the database you can, but must make the changes in both the python script and the sql script

Once all is set, you are good to go, and can run the python script in your command line. 

### Alternatively
Alternatively you can try dowloading the main.exe file
- clicking on it should run automatically if you have python installed 

(doing this might run the app without having the need to install dependencies but I am not sure)

You could try both, first without installing the dependencies and then with if it does not work the first time

- This `.exe` file was created using the package [pyinstaller](https://pyinstaller.org/en/stable/) so it is safe to use (in case your machine gives you any warnings)
- however if you will make changes to the script (specifically database credentials), this option is not best as those changes will not be reflected in the `main.exe` file
- **And most importantly, you must always run the `sql` script first in order to instantiate the database in your local machine**
