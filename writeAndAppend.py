#Step 1:Write user input
user_text=input("Enter the text to write to file")
fh = open("output.txt","wt")
fh.write(user_text)
fh.write("\n")
print("Data successfully written to output.txt")
#step 2:append additional input
extra_text=input("Enter additional text to append to file")
fh = open("output.txt","at")
fh.write(extra_text)
print("Data successfully appended to output.txt")
#Step 3:read the final content
fh = open("output.txt","rt")
print("\n Final contents of output.txt:")
print(fh.read())
fh.close()
