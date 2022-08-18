import os
import sqlite3 as sq


class maclasse():
    def __init__(self,mabase):
        self.conn=sq.connect(f"{os.path.dirname(os.path.abspath(__file__))}/{mabase}")
        self.conn.row_factory=sq.Row


    def create_user(self,username:str,password:str,age:int):
        cur=self.conn.cursor()
        query=f"INSERT INTO Person(username,password,age) VALUES(?,?,?);"
        cur.execute(query,(username,password,age))
        cur.close()
        self.conn.commit()


    def verification_connexion(self,username:str):
        cur=self.conn.cursor()
        query=f"SELECT password FROM Person WHERE username= ?;"
        cur.execute(query,(username,))
        out=cur.fetchall()
        cur.close()
        return dict(out[0])["password"]
        
    
    def user_exists(self,username:str):
        #si l'utilisateur existe c'est qu'il y a des donnes en sont nom dans la table
        cur=self.conn.cursor()
        query=f"SELECT * FROM Person WHERE username=?;"
        cur.execute(query,(username,))  
        out=cur.fetchall()
        cur.close
        return len(out) == 1

    def affichage(self):
        cur=self.conn.cursor()
        query=f"SELECT * FROM Person;"
        cur.execute(query)  
        out=cur.fetchall()
        out=map(dict,out)
        cur.close()
        return out

    def change_password(self,username:str,new_password:str):
        cur=self.conn.cursor()
        query=f"UPDATE Person SET password=?,nbPasswordChange=nbPasswordChange+1 WHERE username=?;"
        cur.execute(query,(new_password,username))
        cur.close()  
        self.conn.commit()      