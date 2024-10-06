import sqlite3

# Database setup
def setup_database():
    conn = sqlite3.connect('community_service.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT UNIQUE,
        password TEXT
    )''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS service_logs (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        hours INTEGER,
        description TEXT,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')

    conn.commit()
    conn.close()

# User Registration
def register_user(username, password):
    conn = sqlite3.connect('community_service.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        print("User registered successfully!")
    except sqlite3.IntegrityError:
        print("Username already taken.")
    
    conn.close()

# Log Service Hours
def log_service_hours(user_id, hours, description):
    conn = sqlite3.connect('community_service.db')
    cursor = conn.cursor()
    
    cursor.execute('INSERT INTO service_logs (user_id, hours, description) VALUES (?, ?, ?)', (user_id, hours, description))
    conn.commit()
    print("Service hours logged successfully!")
    
    conn.close()

# Main Function
def main():
    setup_database()
    print("Welcome to the Community Service Tracker!")
    
    while True:
        print("\n1. Register\n2. Log Service Hours\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
        elif choice == '2':
            user_id = int(input("Enter your user ID: "))
            hours = int(input("Enter hours of service: "))
            description = input("Enter a brief description: ")
            log_service_hours(user_id, hours, description)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
