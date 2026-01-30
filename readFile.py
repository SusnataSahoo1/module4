# reading the file
try:
     with open('sample.txt') as fh:
       print(fh.read())
     fh.close()
except  FileNotFoundError as file_error:
   print(f"The file ""sample.txt was not found.")
   print(file_error)

