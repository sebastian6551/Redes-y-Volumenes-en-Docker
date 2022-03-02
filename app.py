import pymysql

from flask import Flask
app = Flask(__name__)

class DataBase:
    def __init__(self):
      self.connection = pymysql.connect(
        host = 'mysql-db',
        user = 'root',
        password = '2022',
        db = 'deportes'
      )

      self.cursor = self.connection.cursor()

    def get_hits(self):
      instruccion1 = 'SELECT nombre FROM sports'
      try:
        self.cursor.execute(instruccion1)
        dato = self.cursor.fetchone()
        self.connection.commit()
        self.connection.close()
        return '{} is a popular sport.\n'.format(dato[0])

      except Exception as exc:
        raise exc

@app.route('/')
def hello():
  database = DataBase()
  return database.get_hits()
