#!/bin/bash

# Check if the number of arguments provided is exactly one
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <number_of_attempts>"
    exit 1
fi

# Extract the number of attempts from the command line argument
n=$1

# Define the URL
URL="https://idvyhe1tuh.execute-api.us-west-2.amazonaws.com/default/triggerFARGATE"

# ec2
# URL="https://xw3pp220xd.execute-api.us-west-2.amazonaws.com/default/triggerECSTask"

# Loop to curl the URL 'n' times
for ((i=1; i<=n; i++))
do
    echo "Curling $URL - Attempt $i"
    curl -s "$URL"
    echo ""
done
