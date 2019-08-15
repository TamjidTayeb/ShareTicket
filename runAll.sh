#!/bin/bash
# $1 is number of tickets to generate
# $2 is the file to store json data in and to create DB from

# Generate JSON data
python generate-tickets.py $1 $2

# Generate DB and populate with JSON data
python generate-db.py $2

# Run Queries on DB
sqlite3 < queries.sql


