# 🧠 Learning some Fundamental Python:
This folder includes notes and exercises to help learn and practice fundamental Python.

## ✔ What I learned:
+ How to use two random methods: **random.choice()** and **random.choices()**.
  - `random.choice()`:
    * Return one random item from a list.
    * Output is a single value.

  - `random.choices()`:
    * Returns one or more random items from a list.
    * You can use the **k=** parameter to specify how many items to pick.
    * Output is always a list, even if you ask for only one item.
    * Allows duplicates.
    ```
    Example:
    import random
    fruits = ["Apple", "Banana", "Cherry"]
    print(random.choices(fruits, k=2))  
    # Output: ["Cherry", "Cherry"]
    ```
    
+ How to use **Nested List**: A list inside another list.
+ How to used list methods: **.insert(index, value)** and **split()**.

## 📌 Bonus Knowledge:
### ✅ 4 Points to keep track of when writing code:
+ سهل في الصيانة
+ سهل القراءة
+ سهل لاصلاح الاخطاء
+ الاداء
يجب عليك ان تقوم بالتوازن بين عدد اسطر الكود و قابليته للقراءة بسهولة
