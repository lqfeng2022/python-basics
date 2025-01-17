# A PAGE NAVIGATION EXAMPLE:
# 1)Define an empty list
pages = []

# 2)Add pages to the list
pages.append("page_1")
pages.append("page_2")
pages.append("page_3")
print(pages)

# 3)Pop pages from the end of list
last = pages.pop()
print(last)
print(pages)

# 4)Back to the previous page
print("redirect", pages[-1])

# 5)check the stack is empty or not
if not pages:
    print("disable")
