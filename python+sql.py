from mysql.connector import errorcode
import mysql.connector

from http.server import HTTPServer, BaseHTTPRequestHandler


class ConnectCheck:

    def __init__(self, db_user, db_pass, db_port, db_name, db_host):
        self.db_user = db_user
        self.db_pass = db_pass
        self.db_port = db_port
        self.db_name = db_name
        self.db_host = db_host

    def conn_db(self):
        self.conn = mysql.connector.connect(user=self.db_user, password=self.db_pass, host=self.db_host,
                                            port=self.db_port, database=self.db_name)
        self.cursor = self.conn.cursor()
        return self.cursor, self.conn

    def check_conn(self):
        try:
            pass
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            self.conn.close()

    def close_conn(self):
        self.cursor.close()
        self.conn.close()

    def sel_db(self):
        question1 = "y"
        while question1 == "y":
            query1 = input("Input your SELECT: ")
            type(query1)
            self.cursor.execute(query1)
            self.show_select()
            question1 = input("Something else?\ny/n:\n")
        return self.end_block()

    def show_select(self):
        for (name) in self.cursor:
            print(name)
            print(self.cursor)

    def end_block(self):
        print("Bye bye!!!")


#class HttpServer(BaseHTTPRequestHandler):

#    def do_get(self):
#        self.send_response(200)
#        self.send_header('content-type', 'text/html')
 #       self.end_headers()
 #       self.wfile.write("<html><body><h1>hi!</h1></body></html>")


#server = HTTPServer(("localhost", 8080), HttpServer)
#server.serve_forever()

query = ConnectCheck(input("Enter db user "), input("Enter db pass "), input("Enter db port "),
                     input("Enter db name "),
                     input("Enter db host "))
query.conn_db()
query.sel_db()
query.show_select()
query.close_conn()

#   def input_db(self):
#      query = ("SELECT * FROM humans;")
#        query1 = ("INSERT INTO humans VALUES(20, 'Crimson', 2003, 5, 2, 233);")
#        cursor.execute(query1, query)
#        return cursor
#    def close_ins(self):
#        conn.commit()
