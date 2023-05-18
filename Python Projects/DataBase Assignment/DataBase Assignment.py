import sqlite3

# List of file names
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# Create a database connection
conn = sqlite3.connect('file_database.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("CREATE TABLE IF NOT EXISTS tbl_files (id INTEGER PRIMARY KEY AUTOINCREMENT, filename TEXT)")

# Iterate over the file list and add the qualifying text files to the database
for filename in fileList:
    if filename.endswith(".txt"):
        # Insert the filename into the database
        cursor.execute("INSERT INTO tbl_files (filename) VALUES (?)", (filename,))

# Commit the changes to the database
conn.commit()

# Retrieve and print the qualifying text files from the database
cursor.execute("SELECT filename FROM tbl_files WHERE filename LIKE '%.txt'")
results = cursor.fetchall()

for row in results:
    print(row[0])

# Close the database connection
conn.close()
