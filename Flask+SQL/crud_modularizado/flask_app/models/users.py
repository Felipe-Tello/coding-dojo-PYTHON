from flask_app.config.mysqlconnection import connectToMySQL

class User:

    # //////////////////////////////////////////////////////////////////////////
    # ////////////////////////////// OBJETO ////////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////

    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    # //////////////////////////////////////////////////////////////////////////
    # /////////////////////////// C CREATE-CREAR ///////////////////////////////
    # //////////////////////////////////////////////////////////////////////////

    @classmethod
    def guardar(cls, formulario):
        #data = {"first_name": "C", "last_name": "X", "email": "c@cd.com"}
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s)"
        result = connectToMySQL('crud_m').query_db(query, formulario)
        return result

    # //////////////////////////////////////////////////////////////////////////
    # /////////////////////////// R READ-LEER //////////////////////////////////
    # //////////////////////////////////////////////////////////////////////////

    @classmethod
    def muestra_usuarios(cls):
        query = "SELECT * FROM users"
        results = connectToMySQL('crud_m').query_db(query)
        # [
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        #     {"id": "1","first_name":"Cynthia", "last_name": "Apellido", "email":"c@cd.com", "created_at": "2002-02", "updated_at"}
        # ]
        users = []
        for u in results:
            usr = cls(u)
            users.append(usr)
        return users
    
    @classmethod
    def mostrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "SELECT * FROM users WHERE users.id = %(id)s"
        result = connectToMySQL('crud_m').query_db(query, formulario)
        # [
        #     {'3','Juana','De Arco','juana@codingdojo.com','2022-03-09 14:50:58','2022-03-09 14:50:58'}
        # ]
        usr = result[0]
        user = cls(usr)
        print(result)
        return user

    # //////////////////////////////////////////////////////////////////////////
    # /////////////////////// U UPDATE-ACTUALIZAR //////////////////////////////
    # //////////////////////////////////////////////////////////////////////////

    @classmethod
    def actualizar(cls, formulario):
        #formulario = {"id": "1", "first_name": "C", "last_name": "X", "email": "c@cd.com"}
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id=%(id)s"
        result = connectToMySQL('crud_m').query_db(query, formulario)
        return result

    # //////////////////////////////////////////////////////////////////////////
    # /////////////////////////// D DELETE-BORRAR ///////////////////////////////
    # //////////////////////////////////////////////////////////////////////////

    @classmethod
    def borrar(cls, formulario):
        #formulario = {"id": "1"}
        query = "DELETE FROM users WHERE id = %(id)s"
        result = connectToMySQL('crud_m').query_db(query, formulario)
        return result
