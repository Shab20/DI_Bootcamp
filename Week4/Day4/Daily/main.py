secret_msg = "7i3\n\
    Tsi\n\
    h%x\n\
    i #\n\
    sM \n\
    $a \n\
    #t%\n\
    ^r!"

msg_lines_list = secret_msg.split("\n")
msg_lines_list = [
    line.strip() for line in msg_lines_list
]  

print(f"The lines list contains: {msg_lines_list}")
msg_lines_len_list = [
    len(line) for line in msg_lines_list
]
max_line_len = max(msg_lines_len_list) 

rotated_msg = ""
for x in range(max_line_len):  
    for line in msg_lines_list:  
        if x >= len(
            line
        ):  
            break
        elif line[x].isalpha():  
            rotated_msg += line[x]
        else:  
            rotated_msg += " "

print(f"The raw rotated message is: {rotated_msg}")

rotated_msg = rotated_msg.strip()

while "  " in rotated_msg:
    rotated_msg = rotated_msg.replace("  ", " ")

print(f"The clean rotated message is: {rotated_msg}")