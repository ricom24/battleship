from flask import *
from battleship import *
import random

grid = initialiseGrid() #2D array
ship_row = random.randint(0,3)
ship_col = random.randint(0,4)
won = False

app = Flask(__name__)

@app.route('/') #decorator
def root():
       global grid       
       lst = [] #1D list to store strings
       for row in grid: #traverse 2D array
              lst.append(" ".join(row)) #concatenate each row into a str
      
       return render_template("index.html", lst = lst)

@app.route('/calculate', methods = ["POST"])
def calculate():
       global won       
       data = request.form

       row = data["row"]
       if validateRow(row) == False:
              return root()
       
       col = data["col"]
       if validateCol(col) == False:
              return root()
              
       won = checkResult(grid, int(row), int(col), ship_row, ship_col, won)
       if won == True:
              return render_template("won.html")
       else:
              return root()   
         
if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 1234)


