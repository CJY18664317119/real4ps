import pymysql

class SQLHandler:
    def __init__(self, db_config):
        self.db_config = db_config
        self.connection = None
        self.cursor = None
    
    def connect(self):
        try:
            self.connection = pymysql.connect(**self.db_config)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(f"Database connection error: {e}")
            return False
    
    def disconnect(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
    
    def execute_query(self, query, params=None):
        try:
            if not self.connect():
                return None
            
            self.cursor.execute(query, params or ())
            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return self.cursor.rowcount
        except Exception as e:
            print(f"Query execution error: {e}")
            return None
        finally:
            self.disconnect()
    
    # 问题定向相关方法
    def i_problem_orientation(self, a, b, c, d):
        query = "INSERT INTO problem_orientation (a, b, c, d) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (a, b, c, d))
    
    def get_problem_orientation(self):
        query = "SELECT * FROM problem_orientation"
        return self.execute_query(query)
    
    # 原理探究相关方法
    def i_principle_exploration(self, a, b, c, d):
        query = "INSERT INTO principle_exploration (a, b, c, d) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (a, b, c, d))
    
    def get_principle_exploration(self):
        query = "SELECT * FROM principle_exploration"
        return self.execute_query(query)
    
    # 工程实践相关方法
    def i_engineering_practice(self, a, b, c, d):
        query = "INSERT INTO engineering_practice (a, b, c, d) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (a, b, c, d))
    
    def get_engineering_practice(self):
        query = "SELECT * FROM engineering_practice"
        return self.execute_query(query)
    
    # 产品展示相关方法
    def i_product_display(self, a, b, c, d):
        query = "INSERT INTO product_display (a, b, c, d) VALUES (%s, %s, %s, %s)"
        return self.execute_query(query, (a, b, c, d))
    
    def get_product_display(self):
        query = "SELECT * FROM product_display"
        return self.execute_query(query)