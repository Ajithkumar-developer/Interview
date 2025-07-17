# Singleton
Singleton is a design pattern that ensures a class has only one instance, and provides a global access point to that instance.

### The Singleton pattern is used when:

- You need exactly one instance of a class.

- The instance should be accessible globally.

- That instance controls access to a shared resource (like a database, config, logger, etc.).

```python
class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()
print(a is b)  # True
```
