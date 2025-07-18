# Factory Method
The Factory Method defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
### Pros
- Decouples object creation from usage.
- Promotes consistency in object creation.
- Encourages Single Responsibility Principle (each class handles one concern).
### Cons
- Adds more classes and complexity.
- Might be overkill for simple object creation logic.
### Use Cases
- GUI toolkits where buttons, windows, etc. need platform-specific implementations (e.g., MacOS vs Windows).
- Notification systems (e.g., create EmailNotification, SMSNotification).
- Database connectors that vary based on the database type (e.g., MySQL vs PostgreSQL).
- Game development: create enemy units based on level or terrain.

```python
# 1. Product Interfaces
# 2. Concrete products
# 3. Factory Interface
# 4. Concrete Factories
# 5. Client

# Factory for different Database systems

# 1. Product interface
class DatabaseConnection:
    def connect(self):
        pass

class QueryExecutor:
    def execute_query(self, query: str):
        pass


# 2. Products
class MySQLConnection(DatabaseConnection):
    def connect(self):
        return "MySQL Database connected successfully"

class MySQLQueryExecutor(QueryExecutor):
    def execute_query(self, query: str):
        return f"Executed my sql query : {query}"

class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        return "Postgre SQL connected successfully"

class PostgreSQLExecutor(QueryExecutor):
    def execute_query(self, query: str):
        return f"Executed postgre sql query : {query}"


# 3. Factory interface
class DatabaseFactory:
    def create_connection(self) -> DatabaseConnection:
        pass

    def create_execute_query(self) -> QueryExecutor:
        pass


# 4. Concrete Factories
class MySQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return MySQLConnection()

    def create_execute_query(self) -> QueryExecutor:
        return MySQLQueryExecutor()

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self) -> DatabaseConnection:
        return PostgreSQLConnection()

    def create_execute_query(self) -> QueryExecutor:
        return PostgreSQLExecutor()

# 5. Client

class DatabaseApplication:
    def __init__(self, factory: DatabaseFactory):
        self.factory = factory

    def establish_connection(self):
        connect = self.factory.create_connection()
        execute = self.factory.create_execute_query()

        print(connect.connect())
        print(execute.execute_query("Hello world!"))


print()
mySql_app = DatabaseApplication(MySQLFactory())
mySql_app.establish_connection()
print()
postgre_app = DatabaseApplication(PostgreSQLFactory())
postgre_app.establish_connection()


# Alternate Code

class DataBase:
    def connect(self):
        pass

    def execute_query(self, query):
        pass

class MySQL(DataBase):
    def connect(self):
        return "MySQL Database connected successfully."

    def execute_query(self, query):
        return f"MySQL Query : {query}"

class PostgresSQL(DataBase):
    def connect(self):
        return "PostgresSQL connected successfully."

    def execute_query(self, query):
        return f"Postgres Query : {query}"

class DataBaseApplication:
    def __init__(self, factory):
        db_dict = {
            'MySQL': MySQL(),
            'PostgresSQL':PostgresSQL()
        }
        self.factory = db_dict[factory]

    def establish_connection(self):
        connect = self.factory.connect()
        execute = self.factory.execute_query("Query")

        print(connect)
        print(execute)


print()
db = DataBaseApplication('MySQL')
db.establish_connection()
print()
db1 = DataBaseApplication('PostgresSQL')
db1.establish_connection()
print()
```
