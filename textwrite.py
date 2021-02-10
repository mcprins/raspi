from datetime import datetime
import os

#test
def textwrite():
    now = str(datetime.now())

    file_name = now[0:10] + "_" + now[11:13] + ".txt"

    # Create file if it doesnt exist
    text =  open(file_name, 'a+')
    text.close()

    # Read file content
    f = open(file_name,'r')
    content = f.read()
    f.close()

    # Check if file content is empty, 
    if len(content) == 0:
        content = 0
    else:
        content = int(content)

    # Prepare new content
    new_number = str(content + 1)

    # # Write new content
    f = open(file_name, 'wt')
    f.write(new_number)
    f.close()
    
