import sqlite3

# Connect to an in-memory SQLite database
conn = sqlite3.connect(':memory:')

# Create a table named 'Roster'
conn.execute("""CREATE TABLE Roster
                (Name TEXT, Species TEXT, IQ INT)""")

# Populate the table with values
conn.execute("INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)",
             ('Jean-Baptiste Zorg', 'Human', 122))
conn.execute("INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)",
             ('Korben Dallas', 'Meat Popsicle', 100))
conn.execute("INSERT INTO Roster (Name, Species, IQ) VALUES (?, ?, ?)",
             ("Ak'not", 'Mangalore', -5))

# Update the Species of Korben Dallas to be Human
conn.execute("UPDATE Roster SET Species = 'Human' WHERE Name = 'Korben Dallas'")

# Display the names and IQs of everyone classified as Human
result = conn.execute("SELECT Name, IQ FROM Roster WHERE Species = 'Human'")
for row in result:
    print("Name: ", row[0])
    print("IQ: ", row[1])
    print("--------------------")

# Close the database connection
conn.close()
