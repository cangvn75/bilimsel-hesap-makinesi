import sqlite3

class DBManager:

    def __init__(self,dbname):
        self.dbname = dbname
        print(self.dbname)

        self.conn = sqlite3.connect(self.dbname)
        """
        if there is no db with named dbname.db here.
            self.create_db()

        """
        

    def add(self,*args):
        print("Add..")
        pass

    def delete(self,arg):
        pass

    def create_db(self):
        pass

    def __enter__(self):
        # Open db process
        self.conn = sqlite3.connect(self.dbname)

        return self

    def __exit__(self,exc_type,exc_value,tb):
        # Exit db connection
        if tb is None:
            # No exception
            # commit db
            self.conn.close()
            print("Exitted...")
        else:
            # Exception occurred
            print(exc_type)
            print(exc_value)
            print(tb)
                    
        
# fill inside this class bashir.
class CalculatorDBManager(DBManager):

    def __init__(self, dbname):
        super().__init__(dbname)
        self.create_db()
    
    def create_db(self):
        self.conn.execute("""
        CREATE TABLE IF NOT EXISTS Formulas(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        formula TEXT NOT NULL,
        type TEXT NOT NULL)""")
        self.conn.close()
        return super().create_db()

    def add(self, *args):
        print(*args)
        print(args)
        self.conn.execute("INSERT INTO Formulas(formula,type) VALUES('{0}','{1}')".format(*args))
        self.conn.commit()
        return super().add(*args)

    def delete(self, arg):
        self.conn.execute("DELETE FROM Formulas WHERE id={0}".format(arg))
        self.conn.commit()
        return super().delete(arg)

   
db_conn = CalculatorDBManager("formula.db")
with db_conn as db:
    db.delete(2)