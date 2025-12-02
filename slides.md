---
marp: true
theme: custom-theme
paginate: true
footer: "Page: $page of $total"
---

<!--
This is a Marp presentation for IITM TDS GA.
Email: 23ds2000079@ds.study.iitm.ac.in
-->

<!-- Custom theme -->
<style>
section {
  font-family: "Segoe UI", sans-serif;
}
h1 {
  color: #2e86de;
}
.custom-box {
  border: 3px solid #2e86de;
  padding: 12px;
  border-radius: 8px;
  background: #eaf2fd;
}
</style>

# Product Documentation  
### Marp Presentation  
**Email:** 23ds2000079@ds.study.iitm.ac.in

---

# Custom Theme Example  
This slide uses a custom theme defined inside the markdown file.

<div class="custom-box">
This is a custom-styled box using Marp directives.
</div>

---

<!-- background image slide -->
![bg](https://images.unsplash.com/photo-1527443224154-c4a3942d3b59?auto=format&fit=crop&w=1200&q=60)

# Background Image Slide  
Marp supports full-slide backgrounds using `![bg](...)`.

---

# Algorithmic Complexity  

We can express algorithm performance mathematically:

\[
T(n) = O(n \log n)
\]

or:

\[
S(n) = \Theta(n^2)
\]

---

# Code Example (Markdown)

```python
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
