# 🔺 Pascal's Triangle Generator (Python)

This Python script generates the first `n` rows of **Pascal's Triangle**, a common problem in algorithm interviews and coding challenges.

---

## 📘 Problem Statement

Given an integer `num_rows`, generate the first `num_rows` of Pascal's Triangle.

Each number is the sum of the two numbers directly above it.  
The triangle starts with `[1]`, and each row has one more element than the previous row.

---

## 🧠 Approach

- Initialize the triangle with the first row as `[1]`.
- For each new row:
  - The first and last elements are always `1`.
  - The inner elements are the sum of two adjacent elements from the previous row.
- Use two pointers (`left_pointer`, `right_pointer`) to access adjacent values from the previous row.
