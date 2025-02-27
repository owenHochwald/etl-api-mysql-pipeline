import mysql.connector
import os
from dotenv import load_dotenv

# load env variables
load_dotenv()
user = os.environ['USER']
password = os.environ['PASSWORD']

mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  password=password
)

print(mydb)
