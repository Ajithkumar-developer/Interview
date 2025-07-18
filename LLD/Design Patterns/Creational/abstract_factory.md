# Abstract Factory
Abstract Factory is a creational design pattern that provides an interface for creating families of related or dependent objects without specifying their concrete classes.

It’s like a factory of factories. Each factory is responsible for creating related objects.

### Pros:
- Ensures consistency among related objects
- Easy to switch product families
- Encapsulates object creation
- Promotes scalability for new themes/platforms

### Cons:
- Adds complexity
- Hard to add new product types (need to update all factories)
- Can feel over-engineered for small apps

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
```
