import sqlite3

# Create an in-memory SQLite database and sample users and orders tables
def setup_db():
    conn = sqlite3.connect(':memory:')  # In-memory database
    cursor = conn.cursor()
    
    # Create users table
    cursor.execute('''
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        email TEXT NOT NULL
    )
    ''')
    
    # Create orders table with a foreign key reference to users
    cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        user_id INTEGER,
        order_details TEXT,
        order_amount REAL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    # Insert sample data into users and orders tables
    cursor.executemany('''
    INSERT INTO users (username, email)
    VALUES (?, ?)
    ''', [
        ('admin', 'admin@example.com'),
        ('user1', 'user1@example.com'),
        ('user2', 'user2@example.com')
    ])
    
    cursor.executemany('''
    INSERT INTO orders (user_id, order_details, order_amount)
    VALUES (?, ?, ?)
    ''', [
        (1, 'Admin Order 1', 100.50),
        (1, 'Admin Order 2', 200.75),
        (2, 'User1 Order 1', 50.25),
        (3, 'User2 Order 1', 75.00),
    ])
    
    conn.commit()
    return conn

# Function to fetch user and their order data (vulnerable to SQL Injection)
def fetch_user_orders(conn, username):
    cursor = conn.cursor()
    
    # Insecure complex SQL query vulnerable to SQL Injection
    query = f"""
    SELECT u.username, u.email, o.order_id, o.order_details, o.order_amount
    FROM users u
    LEFT JOIN orders o ON u.id = o.user_id
    WHERE u.username = '{username}'
    """
    
    print(f"Executing query: {query}")
    
    cursor.execute(query)
    results = cursor.fetchall()
    
    # Display the results
    if results:
        for row in results:
            print(f"Username: {row[0]}, Email: {row[1]}, Order ID: {row[2]}, Order Details: {row[3]}, Amount: ${row[4]}")
    else:
        print("No user or orders found for that username.")

def main():
    conn = setup_db()
    
    # Ask for username input (user-controlled input)
    username = input("Enter username to search for orders: ")
    
    # Fetch and display user orders based on the input
    fetch_user_orders(conn, username)
    
    conn.close()

if __name__ == "__main__":
    main()
