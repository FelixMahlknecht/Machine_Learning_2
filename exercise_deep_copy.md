Understanding Assignment, Shallow Copy, and Deep Copy in Python

In Python, assignment (=), shallow copy (copy.copy), and deep copy (copy.deepcopy) are ways to duplicate or reference objects.

Assignment creates a reference to the original object, meaning both variables point to the same data.
Shallow Copy makes a new object but still references the original elements inside. For nested structures, changes to the inner objects affect both copies.
Deep Copy creates a fully independent copy of the object and all nested objects, ensuring that changes in one copy do not affect the other.
Understanding these distinctions is important for managing object behavior and memory efficiently in Python programming.