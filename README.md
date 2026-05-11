# 🛢️ Circle & Cylinder Using Inheritance in Python

## 📌 Description

This Python program demonstrates **inheritance** using a `Circle` class and a derived `Cylinder` class.
The `Cylinder` class inherits properties and methods of `Circle` and adds functionality for:

* Volume calculation
* Surface area calculation

---

## 🚀 Features

* Demonstrates **single inheritance**
* Uses `super()` constructor
* Calculates:

  * Area of circle
  * Circumference of circle
  * Volume of cylinder
  * Surface area of cylinder

---

## 🛠️ How It Works

### 1️⃣ Parent Class – `Circle`

Contains:

* `rad` → radius

Methods:

* `input_radius()`
* `area()`
* `circumference()`

---

### 2️⃣ Child Class – `Cylinder`

```python id="j4k9pl"
class Cylinder(Circle)
```

👉 Inherits all methods and variables from `Circle`

Adds:

* `ht` → height

Methods:

* `input_height()`
* `volume()`
* `surface_area()`

Uses:

```python id="a2m8qx"
super().__init__()
```

to initialize parent class constructor.

---

## 💻 Code

```python id="w7x3mz"
import math


class Circle:
    def __init__(self):
        self.rad = 0

    def input_radius(self):
        self.rad = float(input("Enter the radius : "))

    def area(self):
        a = math.pi * self.rad * self.rad
        print("Area of circle :", a)

    def circumference(self):
        c = 2 * math.pi * self.rad
        print("Circumference :", c)


class Cylinder(Circle):   # Inheriting Circle class
    def __init__(self):
        super().__init__()
        self.ht = 0

    def input_height(self):
        self.ht = float(input("Enter the height : "))

    def volume(self):
        v = math.pi * self.rad * self.rad * self.ht
        print("Volume :", v)

    def surface_area(self):
        sa = 2 * math.pi * self.rad * self.ht
        print("Surface area :", sa)


class Inh3:
    @staticmethod
    def main():
        c = Cylinder()

        c.input_radius()
        c.input_height()

        print("\nBase of Cylinder")
        print("------------------------")
        c.area()
        c.circumference()

        print("\nBody of Cylinder")
        print("------------------------")
        c.volume()
        c.surface_area()


Inh3.main()
```

---

## ▶️ Example Output

```id="z3m7qa"
Enter the radius : 5
Enter the height : 10

Base of Cylinder
------------------------
Area of circle : 78.53981633974483
Circumference : 31.41592653589793

Body of Cylinder
------------------------
Volume : 785.3981633974483
Surface area : 314.1592653589793
```

---

## 📐 Formulas Used

### Circle

genui{"math_block_widget_always_prefetch_v2":{"content":"A = \pi r^2"}}

genui{"math_block_widget_always_prefetch_v2":{"content":"C = 2\pi r"}}

### Cylinder

genui{"math_block_widget_always_prefetch_v2":{"content":"V = \pi r^2 h"}}

SA = 2\pi rh

---

## 🧠 Key Concepts

### ✔ Inheritance

`Cylinder` inherits:

* radius
* area()
* circumference()

from `Circle`.

---

### ✔ `super()` Keyword

```python id="q8k1pt"
super().__init__()
```

👉 Calls constructor of parent class.

---

### ✔ Code Reusability

No need to rewrite:

* area()
* circumference()

---

## 📚 Concepts Used

* Class & Object
* Single Inheritance
* Constructor Inheritance
* `super()` method
* Mathematical calculations
* `math` module

---

## ⚠️ Note About Surface Area

Your code calculates:

```python id="v2m9xl"
2 * π * r * h
```

which is actually the **Curved Surface Area (CSA)** of a cylinder.

👉 Full Total Surface Area formula is:

TSA = 2\pi r(h+r)

---

## 🔧 Future Improvements

* Add total surface area calculation
* Validate negative input
* Add cone and sphere classes
* Create menu-driven geometry calculator

---

## 📄 License

This project is open-source and free to use.
