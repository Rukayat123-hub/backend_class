
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
from pymysql.constants import CLIENT  # Enables MULTI_STATEMENTS for MySQL

# -----------------------------------
# 1️⃣ Load environment variables
# -----------------------------------
load_dotenv()

# Get credentials from .env file
db_user = os.getenv('dbuser')
db_password = os.getenv('dbpassword')
db_host = os.getenv('dbhost')
db_port = os.getenv('dbport')
db_name = os.getenv('dbname')

# -----------------------------------
# 2️⃣ Create database connection URL
# -----------------------------------
db_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# -----------------------------------
# 3️⃣ Create SQLAlchemy engine & session
# -----------------------------------
engine = create_engine(
    db_url,
    connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
)

Session = sessionmaker(bind=engine)
db = Session()

# -----------------------------------
# 4️⃣ Define SQL queries to create tables
# -----------------------------------

create_users = text("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
);
""")

create_courses = text("""
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    level VARCHAR(100) NOT NULL
);
""")

create_enrollments = text("""
CREATE TABLE IF NOT EXISTS enrollments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT,
    courseId INT,
    FOREIGN KEY (userId) REFERENCES users(id),
    FOREIGN KEY (courseId) REFERENCES courses(id)
);
""")

# -----------------------------------
# 5️⃣ Execute table creation
# -----------------------------------
try:
    db.execute(create_users)
    db.execute(create_courses)
    db.execute(create_enrollments)
    db.commit()
    print("✅ Tables have been created successfully.")

except Exception as e:
    print("❌ Error creating tables:", e)
    db.rollback()

# -----------------------------------
# 6️⃣ Insert sample data
# -----------------------------------
try:
    insert_user = text("""
    INSERT INTO users (name, email, password)
    VALUES (:name, :email, :password)
    """)

    insert_course = text("""
    INSERT INTO courses (title, level)
    VALUES (:title, :level)
    """)

    db.execute(insert_user, {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "12345"
    })

    db.execute(insert_course, {
        "title": "Python Basics",
        "level": "Beginner"
    })

    db.commit()
    print("✅ Sample data inserted successfully.")

except Exception as e:
    print("❌ Error inserting data:", e)
    db.rollback()

finally:
    db.close()
    print("🔒 Database session closed.")





# # #    
# from sqlalchemy import create_engine, text
# from sqlalchemy.orm import sessionmaker
# from dotenv import load_dotenv
# import os
# from pymysql.constants import CLIENT  # for MULTI_STATEMENTS

# # Load environment variables
# load_dotenv()

# # Build the database connection URL
# db_url = (
#     f"mysql+pymysql://{os.getenv('dbuser')}:{os.getenv('dbpassword')}"
#     f"@{os.getenv('dbhost')}:{os.getenv('dbport')}/{os.getenv('dbname')}"
# )

# # Create engine
# engine = create_engine(
#     db_url,
#     connect_args={"client_flag": CLIENT.MULTI_STATEMENTS}
# )

# # Create a session
# Session = sessionmaker(bind=engine)
# db = Session()

# # SQL for creating the users table
# create_users = text("""
# CREATE TABLE IF NOT EXISTS users (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100) NOT NULL,
#     email VARCHAR(100) NOT NULL,
#     password VARCHAR(100) NOT NULL
# );
# """)

# # SQL for creating the courses table
# create_courses = text("""
# CREATE TABLE IF NOT EXISTS courses (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     title VARCHAR(100) NOT NULL,
#     level VARCHAR(100) NOT NULL
# );
# """)

# # SQL for creating the enrollments table
# create_enrollment = text("""
# CREATE TABLE IF NOT EXISTS enrollments (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     userId INT,
#     courseId INT,
#     FOREIGN KEY (userId) REFERENCES users(id),
#     FOREIGN KEY (courseId) REFERENCES courses(id)
# );
# """)

# # Execute table creation
# try:
#     db.execute(create_users)
   
   