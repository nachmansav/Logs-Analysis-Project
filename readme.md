#Project overview:
This is a project for the Udacity Full Stack Web Developer nanodegree program and is aimed at increasing the student's proficiency with SQL.
##Details:
Python is used to interact with a large SQL database containing over a million rows from a news website.
The goal is to build and refine complex queries and use them to draw business conclusions from the data. It will use a single SQL statement to answer each one of the following three questions about the site.

1. What are the three most popular articles based on the number of views?
2. Who are the most popular contributors to the site based on page views?
3. On what date did more than 1% of connection attempts lead to errors?

This code uses PostgreSQL and python. It uses a sigle SQL select statement to get results from the database and returns the result as a python list that is then displayed.

##Instructions for running the code:
1. Download and install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/).
2. Download the following Udacity [folder](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) which contains preconfigured vagrant settings.
3. Clone this repository.
5. Navigate to the Udacity folder using the command line interface and inside that, cd into the vagrant directory.
6. Launch the virtual machine with the command 'vagrant up'.
7. Once Vagrant installs the necessary files use 'vagrant ssh' to connect to the virtual machine.
8. Cd into the '/vagrant' folder.
9. Copy the contents of this repository to this directory.
10. Load the database with the command 'psql -d news -f newsdata.sql'.
11. Run the database with the command 'psql -d news'.
12. Use the command 'python logs.py' to run the python program and display the query results.

