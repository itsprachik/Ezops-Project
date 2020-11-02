# Ezops-Project

Here is the assignment that was given to me previously. I was told not to do challenge 5A and 6A. I was unsure how to show D3 on github so I don't have it here but it is something I can do.
Also I had hosted my flask application on AWS but since it started charging me for having the instance running I shut it down. But if need I will happily demo it on AWS again.
## DevOps
When done, provide a link to your GitHub and to the running AWS server with instructions too  review your challenge.

# Challenge D1 - Basic Python Skills

Create a python script that  reads the titanic data set from Kaggle and performs the following actions
Read the file and write it two files, the first reversing the order of the columns, the second creates a file that contains every other columns
Create a python script that pulls data from https://www.alphavantage.co/ calling the API, https://www.alphavantage.co/query. to get a time series of daily quotes for Microsoft and creates a xlsx file that you can open in excel
create a python flask server that implements a UI for  #2 and #3

# Challenge D2 - Basic Devops Skills
On AWS create a CENTOS 7 server with Docker installed
Create a docker container for the flask server created in Python Skills Section and  deploy it on the CENTOS server

# Challenge D3 - Basic Java Skills
Create a hello world application in java and set it up in Eclipse
Demo how to set a break point in eclipse
Add an option to force it to throw and exception and explain how you would find the line causing the exception from the stack trace

# Challenge D4 - Shell Scripting Skills
create an ec2 micro instance on aws
Create a shell script that does the same steps as D1 Python script steps 1-3 and in addition create a file that reverse the text in every 3rd column.

# Challenge D5 - SQL Basic Skills
Create an EMPLOYEE table and a DEPARTMENT table and populate them with data. Include a SALARY column in the EMPLOYEE table and a CITY column in the DEPARTMENT table. Write a query that lists the average employee salary for each city.
Write a query to print the current date and time on the server.



# Challenge D5A - SQL Advanced Skills
Produce a query plan and explain it for time 1 in D5
Revise the design to support millions of rows or explain why your current design will scale based on the plan
Oracle Only:  Query to report number of rows in each table for you  current schema

# Challenge D6 - Basic Docker Skills
Create the following running in docker, MYSQL DB, Tomcat, IBM MQ
Create a docker compose file to start a Tomcat, have the container run a simple web site with a single helloworld.html file from the local filesystem
Create a docker compose file to start the 3 services above with these setting, MYSQL DB, override default  port, delay starting until MQ  is running
Demonstrate debugging skills by starting the MYSQL image locally to create a temporary container that is running bash interactively

# Challenge D6A - Advanced Docker Skills
Create a docker compose to start MYSQL, Tomcat & IBM MQ
IBM MQ IMAGE in a docker compose file, add a file to the file system called /ezops.txt that contains the text "HELLO EZOPS" and Cat the file ezops.txt before starting IBMMQ
Using the Tomcat image add a server call cmdTest that runs a 'pwd' and 'ls' command then stops
Change the default network name  in the docker compose to EZOPS_CHALLENGE
Run the docker-compose in a swarm with to instances of tomcat and 1 of the DB & MQ
