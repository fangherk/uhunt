# Check the number of arguments

if [ $# -eq 0 ]
   then
     echo "No arguments supplied"
     exit 1;
elif [ $# -eq 1 ]
   then 
     mkdir $1  # make a directory
     touch $1/answer.py
     touch $1/input.txt
else
     echo "Too many arguments"
     exit 1;
fi

