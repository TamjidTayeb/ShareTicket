# Share Ticket Data Base Script

## Project Overview
This project is a series of scripts that will acheive the following:
+ Generate dummy data based on a the shareticket schema and save to a JSON file on disk
+ Generate a relational SQLite database based on the shareticket schema
+ Parse the JSON file and insert into the database
+ Execute queries on the database
+ Bash script to execute the above in one command

## How to run
To run this series of scripts change directory into the project folder and run the bash script with the following paramaters:
+ $1 : Number of data records to generate
+ $2 : Filename of JSON file to save to  

For example: sh runAll.sh 1000 data.json

