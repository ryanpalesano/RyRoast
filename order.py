




class Order:
    db = "coffee_orders"
    def __init__(self, data):
        self.id = data['id']
        self.blend = data['blend']
        self.roast = data['roast']
        self.city = data['city']
        self.address = data['address']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO orders (blend, roast, city, address, user_id) VALUES (%(blend)s, %(roast)s, %(city)s, %(address)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = """SELECT * FROM orders
                JOIN users ON coffee_orders_id =
                users.id""";
        results = connectToMySQL(cls.db).query_db(query)
        all_orders = []
        for row in results:
            orders_row = cls(row)
            user_data = {
                'id': row['users.id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'password': row['password'],
                'created_at': row['users.created_at'],
                'updated_at': row['users.updated_at']
            }
            user1 = user.User(user_data)
            orders_row.creator = user1
            all_orders.append(orders_row)
        return all_orders


    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM orders WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query,data)

