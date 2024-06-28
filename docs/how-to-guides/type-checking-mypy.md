# Static Type Checking

!!! example "Using ChatGPT to Assist with Static Typing"

    Consider a Retrieval-Augmented Generation (RAG) Q&A system. Here's a function without type annotations:

    ```plaintext
    I have a Python function that processes user queries and retrieves 
    relevant documents in a RAG Q&A system. The `query` parameter is a 
    string. The `retrieve_documents` function returns a list of 
    dictionaries with `id` and `text` as strings. The `process_query` 
    function should return a list of document texts. Here is the function:

    def process_query(query, retrieve_documents):
        documents = retrieve_documents(query)
        return [doc['text'] for doc in documents]

    Can you add the appropriate type annotations to this function using 
    Mypy and explain your reasoning?
    ```

    #### Example Output

    ChatGPT might respond with:

    ```python
    from typing import Callable, List, Dict

    def process_query(query: str, retrieve_documents: Callable[[str], List[Dict[str, str]]]) -> List[str]:
        documents = retrieve_documents(query)
        return [doc['text'] for doc in documents]
    ```

    #### Reasoning:

    1. **`query: str`**: The `query` parameter is a string because it represents the user's question.
    2. **`retrieve_documents: Callable[[str], List[Dict[str, str]]]`**: The `retrieve_documents` parameter is a callable function that takes a string (`query`) and returns a list of dictionaries, each containing an `id` and `text` as strings.
    3. **`-> List[str]`**: The `process_query` function returns a list of strings, which are the texts of the retrieved documents.

    ### Best Practices for Using ChatGPT

    4. **Provide Context**: More context leads to better type annotations. Include sample inputs or describe expected outputs.
    5. **Ask for Explanations**: If unsure about an annotation, ask ChatGPT for an explanation.
    6. **Iterate**: Start with a basic function and gradually add complexity to ensure consistent and accurate annotations.


## Why Use Static Typing with Python?

Python's dynamic typing allows for flexible and rapid development but
comes with trade-offs. Understanding these trade-offs and the benefits
of static typing can help you decide to use tools like Mypy in your
Python projects.

### Dynamic Typing in Python

Python doesn't require explicit type declarations for variables or
function return values. The interpreter determines the type at runtime
based on the value assigned. This flexibility allows quick prototyping
but can lead to subtle and hard-to-diagnose bugs.

### Duck Typing

Python uses "duck typing," where an object's suitability is determined
by the presence of certain methods and properties rather than its type.
This makes code flexible but can make understanding and debugging
difficult in larger codebases. For example:

```python
def add(a, b):
    return a + b

result = add(3, "4")  # This will cause a runtime error
print(result)
```

Without explicit type annotations, it's hard to know what types `a` and
`b` should be, leading to potential runtime errors.

### Benefits of Static Typing

Static typing addresses these issues by making type expectations
explicit, providing several benefits:

- **Improved Readability**: Type annotations serve as documentation,
  making it easier for others to understand the code.
- **Early Error Detection**: Tools like Mypy can detect type errors
  before runtime.
- **Ease of Refactoring**: Knowing variable types makes refactoring
  safer and more predictable.
- **Enhanced IDE Support**: IDEs use type annotations for better code
  completion, navigation, and refactoring tools.

### Example: Explicit Type Annotations

#### Before: Without Type Checking

```python
def add(a, b):
    return a + b

result = add(3, "4")  # This will cause a runtime error
print(result)
```

#### After: With Type Checking

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 4)  # This will work
print(result)

# Uncommenting the line below will cause a type checking error with mypy
# result = add(3, "4")  # This will cause a mypy type error
```

Type annotations specify that `a` and `b` must be of type `int`. The
type checker will catch any type errors before runtime.

To check the code with `mypy`, save the "after" code in a file (e.g.,
`example.py`) and run:

```bash
mypy example.py
```

Mypy will report an error if you uncomment the line with the type
mismatch:

```plaintext
example.py:10: error: Argument 2 to "add" has incompatible type "str"; expected "int"
```

This ensures that type errors are caught early during development,
improving code robustness.

### Maintaining Type Annotations

Type annotations are automatically checked for correctness by tools like
Mypy, ensuring they remain accurate and up-to-date. This reduces the
risk of outdated documentation and improves code quality.

By incorporating static typing and using tools like Mypy, you can
enhance the robustness and maintainability of your Python code, making
it easier to understand, debug, and extend.

## Type Inference Using Mypy

### Introduction

Type inference lets the compiler or interpreter deduce types without
explicit annotations. In Python, mypy helps ensure type correctness by
using type inference.

### What is Type Inference?

Type inference allows the type checker to deduce variable and expression
types based on assigned values and operations, reducing the need for
explicit annotations and keeping the code clean and concise.

### How Mypy Performs Type Inference

#### Variable Type Inference

Mypy can infer the type of a variable based on the value assigned to it.
For example:

```python
x = 10  # mypy infers x as int
y = "Hello, world!"  # mypy infers y as str
z = 3.14  # mypy infers z as float
```

In this example, `mypy` infers that `x` is of type `int`, `y` is of type
`str`, and `z` is of type `float` based on the assigned values.

#### Function Return Type Inference

Mypy can also infer the return type of a function based on the return
statement:

```python
def add(a: int, b: int) -> int:
    return a + b

result = add(3, 4)  # mypy infers result as int
print(result)

# Uncommenting the line below will cause a type checking error with mypy
# result = add(3, "4")  # This will cause a mypy type error
```

Here, `mypy` infers that the `add` function returns an `int` because it
adds two integers. Consequently, the variable `result` is inferred to be
of type `int`.

#### Collection Type Inference

When working with collections like lists and dictionaries, `mypy` can
infer the types of the elements:

```python
numbers = [1, 2, 3, 4]  # mypy infers numbers as List[int]
names = ["Alice", "Bob", "Charlie"]  # mypy infers names as List[str]

person = {
    "name": "Marcos",
    "age": 42
}  # mypy infers person as Dict[str, Union[str, int]]
```

In these examples, `mypy` infers the types of the lists and dictionaries
based on their contents. If you later try to add elements of a different
type to these collections, mypy will flag it as an error, ensuring type
consistency throughout your codebase.

#### Example: Complete Type Inference

```python
# example.py

def add(a: int, b: int):
    return a + b

def greet(name: str):
    return f"Hello, {name}!"

x = 10  # mypy infers x as int
y = 20  # mypy infers y as int
z = add(x, y)  # mypy infers z as int

message = greet("Marcos")  # mypy infers message as str

numbers = [1, 2, 3, 4]  # mypy infers numbers as List[int]
names = ["Alice", "Bob", "Charlie"]  # mypy infers names as List[str]

person = {
    "name": "Marcos",
    "age": 42
}  # mypy infers person as Dict[str, Union[str, int]]
```

To check the type inference with `mypy`, run:

```bash
mypy example.py
```

### Benefits of Type Inference

1. **Conciseness**: Reduces the need for explicit type annotations,
   making the code more concise.
2. **Readability**: Enhances code readability by inferring types based
   on context.
3. **Safety**: Ensures type correctness, reducing runtime errors.


## Guide to Using Union and Optionals with Mypy

### Introduction

Two important concepts in type annotations are `Union` and `Optional`.
These types enable developers to specify multiple possible types for a
variable or function return type, making the code more flexible and
expressive.


### Union

The `Union` type allows a variable to have multiple possible types. This
is useful when a variable or function parameter can accept different
types.

#### Syntax

```python
from typing import Union

def process(value: Union[int, str]) -> None:
    if isinstance(value, int):
        print(f"Processing an integer: {value}")
    elif isinstance(value, str):
        print(f"Processing a string: {value}")

# Example usage
process(42)
process("Hello")
```

In this example, the `process` function can accept both `int` and `str`
types for the `value` parameter. `mypy` will check that the code
correctly handles both types.

#### Example

```python
from typing import Union

def describe(value: Union[int, float, str]) -> str:
    if isinstance(value, int):
        return f"Integer: {value}"
    elif isinstance(value, float):
        return f"Float: {value}"
    elif isinstance(value, str):
        return f"String: {value}"

# Example usage
print(describe(10))     # Integer: 10
print(describe(3.14))   # Float: 3.14
print(describe("hello"))  # String: hello
```

In this example, the `describe` function can handle `int`, `float`, and
`str` types, providing a description for each.

### Optional

The `Optional` type is a shorthand for a `Union` with `None`. It
indicates that a variable can have a specific type or be `None`.

#### Syntax

```python
from typing import Optional

def greet(name: Optional[str]) -> str:
    if name is None:
        return "Hello, there!"
    else:
        return f"Hello, {name}!"

# Example usage
print(greet(None))        # Hello, there!
print(greet("Marcos"))    # Hello, Marcos!
```

In this example, the `greet` function can accept either a `str` or
`None` for the `name` parameter.

#### Example

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

# Example usage
print(find_user(1))  # Alice
print(find_user(3))  # None
```

In this example, the `find_user` function returns a `str` if the user is
found, otherwise it returns `None`.

### Combining Union and Optional

You can combine `Union` and `Optional` to specify complex types.

#### Example

```python
from typing import Union, Optional

def read_value(value: Union[int, float, Optional[str]]) -> str:
    if value is None:
        return "No value"
    elif isinstance(value, int):
        return f"Integer value: {value}"
    elif isinstance(value, float):
        return f"Float value: {value}"
    elif isinstance(value, str):
        return f"String value: {value}"

# Example usage
print(read_value(10))      # Integer value: 10
print(read_value(3.14))    # Float value: 3.14
print(read_value("text"))  # String value: text
print(read_value(None))    # No value
```

In this example, the `read_value` function can handle `int`, `float`,
`str`, and `None`.

Sure! Here is the updated section for Overloads with the corrected
example:

## Guide to Using Overloads and Generics with Mypy

### Introduction

Two advanced features in mypy are `Overloads` and `Generics`, which
provide more flexibility and expressiveness in type annotations.

### Overloads

Function overloading allows you to define multiple signatures for a
function, enabling different behaviors based on input types. The
`overload` decorator from the `typing` module is used to achieve this in
Python.

#### Syntax

```python
from typing import overload

@overload
def process(value: int) -> int:
    ...

@overload
def process(value: str) -> str:
    ...

def process(value):
    if isinstance(value, int):
        return value * 2
    elif isinstance(value, str):
        return value.upper()

# Example usage
print(process(10))    # 20
print(process("hello"))  # HELLO
```

In this example, the `process` function has two overloaded signatures:
one for `int` and one for `str`. The implementation combines both cases
and returns different results based on the input type.

#### Example

```python
from typing import overload, Union

@overload
def add(a: int, b: int) -> int:
    ...

@overload
def add(a: float, b: float) -> float:
    ...

@overload
def add(a: str, b: str) -> str:
    ...

def add(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str]:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    elif isinstance(a, float) and isinstance(b, float):
        return a + b
    elif isinstance(a, str) and isinstance(b, str):
        return a + b
    else:
        raise TypeError("Unsupported types")

# Example usage
print(add(1, 2))        # 3
print(add(1.5, 2.5))    # 4.0
print(add("Hello, ", "World!"))  # Hello, World!
```

Here, the `add` function is overloaded to handle `int`, `float`, and
`str` types, each performing the appropriate addition operation. The
actual implementation uses type checks to ensure that the parameters are
of the correct type, and raises a `TypeError` if they are not.

Mypy will validate that the `add` function calls match one of the
overloaded signatures and ensure type consistency. This ensures that the
`add` function will correctly handle integers, floats, and strings and
that `mypy` can verify the type correctness.

### Generics

Generics allow you to write functions and classes that can operate on a
variety of types while maintaining type safety. The `TypeVar` class from
the `typing` module is used to define generic types.

#### Syntax

```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    return elements[0]

# Example usage
print(get_first_element([1, 2, 3]))         # 1
print(get_first_element(["a", "b", "c"]))   # "a"
```

In this example, the `get_first_element` function is generic and can
operate on a list of any type, returning an element of the same type.

#### Generic Classes

You can also create generic classes using `Generic`.

```python
from typing import TypeVar, Generic

T = TypeVar('T')

class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content

# Example usage
int_box = Box(123)
str_box = Box("Hello")

print(int_box.get_content())  # 123
print(str_box.get_content())  # Hello
```

In this example, the `Box` class is generic and can store content of any
type.

#### Example with Multiple Type Variables

```python
from typing import TypeVar, Generic

T = TypeVar('T')
U = TypeVar('U')

class Pair(Generic[T, U]):
    def __init__(self, first: T, second: U) -> None:
        self.first = first
        self.second = second

    def get_first(self) -> T:
        return self.first

    def get_second(self) -> U:
        return self.second

# Example usage
pair = Pair(1, "one")
print(pair.get_first())   # 1
print(pair.get_second())  # one
```

Here, the `Pair` class uses two type variables `T` and `U`, allowing it
to store and return two values of different types.

## Using ChatGPT to Assist with Static Typing in Python with Mypy

### Introduction

ChatGPT can help you add static typing to your Python code using Mypy,
improving code quality, readability, and safety.

### How ChatGPT Can Help

1. **Adding Type Annotations**: ChatGPT can analyze your code and add
   appropriate type annotations.
2. **Explaining Annotations**: ChatGPT can explain why specific types
   are chosen.
3. **Ensuring Consistency**: ChatGPT can ensure consistent types
   throughout your code.

### Example Prompt

Consider a Retrieval-Augmented Generation (RAG) Q&A system. Here's a
function without type annotations:

```plaintext
I have a Python function that processes user queries and retrieves relevant documents in a RAG Q&A system. The `query` parameter is a string. The `retrieve_documents` function returns a list of dictionaries with `id` and `text` as strings. The `process_query` function should return a list of document texts. Here is the function:

```python
def process_query(query, retrieve_documents):
    documents = retrieve_documents(query)
    return [doc['text'] for doc in documents]

Can you add the appropriate type annotations to this function using Mypy and explain your reasoning?
```

#### Example Output

ChatGPT might respond with:

```python
from typing import Callable, List, Dict

def process_query(query: str, retrieve_documents: Callable[[str], List[Dict[str, str]]]) -> List[str]:
    documents = retrieve_documents(query)
    return [doc['text'] for doc in documents]
```

#### Reasoning:

1. **`query: str`**: The `query` parameter is a string because it
   represents the user's question.
2. **`retrieve_documents: Callable[[str], List[Dict[str, str]]]`**: The
   `retrieve_documents` parameter is a callable function that takes a
   string (`query`) and returns a list of dictionaries, each containing
   an `id` and `text` as strings.
3. **`-> List[str]`**: The `process_query` function returns a list of
   strings, which are the texts of the retrieved documents.

### Best Practices for Using ChatGPT

1. **Provide Context**: More context leads to better type annotations.
   Include sample inputs or describe expected outputs.
2. **Ask for Explanations**: If unsure about an annotation, ask ChatGPT
   for an explanation.
3. **Iterate**: Start with a basic function and gradually add complexity
   to ensure consistent and accurate annotations.