#Name:Pratik Singh
#Student id: 1001670417


import sqlite3 
conn = sqlite3.connect("Players.db")

print ("Player Manager\n")
print ("COMMAND MENU")
print("view - View players")
print("add - Add a player")
print('update - update a player')
print("del - Delete a player")
print("exit - Exit program\n")




def view():
	q2 = '''SELECT *
               FROM Player ORDER BY win desc '''
 
	cursor = conn.execute(q2)

	print("{:15}{:>3} {:>15} {:>15} {:>15}".format("Name","Wins", "Losses", "Ties", "Games"))
	print("---------------------------------------------------------------------------")
       
	for row in cursor:
		print("{:15}{:>3} {:>15} {:>15} {:>15}".format(row[0],row[1], row[2], row[3], (row[1]+row[2]+row[3])))
	
	print()
	select()

def delete():
	name = input("Name: ")

	conn.execute('DELETE from Player where name=?;',(name,))
	conn.commit()
	if conn.total_changes != 0:
		print(name, " was deleted from database.")
	select()


def update():
    name = input("Enter a name you want to update : ")
    win = int(input('Wins :'))
    losses = int(input('Losses :'))
    ties = int(input('Ties :'))
    conn.execute('UPDATE Player set win = ?, losses = ?, ties = ? where name=?', (win,losses,ties,name))
    select()

def add():
    
	name = input("Name: ")
	win = int(input("Wins: "))
	losses = int(input("Losses: "))
	ties = int(input("Ties: "))
	print(name,"was added to the Database")

	q1 = '''INSERT INTO Player (name, win, losses, ties) 
            VALUES (?, ?, ?, ?)'''
	conn.execute(q1, (name, win, losses, ties))
	conn.commit()

	select()
def select():
        print ("Player Manager\n")
        print ("COMMAND MENU")
        print("view - View players")
        print("add - Add a player")
        print('update - update a player')
        print("del - Delete a player")
        print("exit - Exit program\n")

        main()


def quit():
    print('Bye!')
    
def main():
    choice = input('Command :')
    if choice == "view":
	    view()        	
    elif choice == "add":
	    add()             
    elif choice == "del":
	    delete()
    elif choice == "update":
            update()
    elif choice == "exit":
            quit()

conn = sqlite3.connect("Players.db") 

conn.execute('''
        CREATE TABLE if not exists Player
        (       
          
			name             TEXT		NOT NULL,
			win		INTEGER		NOT NULL,
			losses		INTEGER		NOT NULL,
			ties		INTEGER		NOT NULL
        )         
        ''')  
main()




    



