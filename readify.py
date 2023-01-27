### PURPOSE
# Converts commands from terminal into a readable format

### MAIN
def TFormat(paragraph):
    ### VARS
    near = []
    newline = ''

    # for each line in the paragraph
    for line in paragraph:
        # for each char in the lines
        for each in line:
            if(each == ' '): #get rid of the formating spaces
                continue
            elif (each == '█'): #space out each network
                newline += '\n'
            else:
                newline += each #add to new string for the list of each network
        #formating for unneeded data
        goodbye = int(newline.find(':', 14, 15))
        newline = newline[goodbye: len(newline)]

        near.append(newline)
        newline = ""
    return(near)

def TRead(paragraph):
    for line in paragraph:
        print(line)