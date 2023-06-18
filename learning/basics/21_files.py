# https://realpython.com/working-with-files-in-python/

from tempfile import TemporaryFile

with open('data.txt', 'w') as f:
    data = 'some data to be written to the file'
    f.write(data)

with open('data.txt', 'r') as f:
    data = f.read()
    print(data)

# Create a temporary file and write some data to it
fp = TemporaryFile('w+t')
fp.write('Hello universe!')

# Go back to the beginning and read data from file
fp.seek(0)
data = fp.read()

# Close the file, after which it will be removed
fp.close()

