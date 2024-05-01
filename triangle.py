"""
n = 3
--*-- 1 [0] [2]
-***- 3 [1] [1]
***** 5 [2] [0]


n = 5

----*---- 1 [0] [4]
---***--- 3 [1] [3]
--*****-- 5 [2] [2]
-*******- 7 [3] [1]
********* 9 [4] [0]

"""
def triangle(rows):
    outp=""
    row_length = rows*2 - 1
    for a in range(rows):
        empty_half = rows - a - 1
        full_half = row_length - empty_half*2
        for j in range(empty_half): outp += " "
        for j in range(full_half): outp += "*"
        for j in range(empty_half): outp += " "
        outp += "\n"
    print(outp)

rows = int(input("Number of triangle rows: "))
triangle(rows)



"""
n = 4
---**---  - 2  [3]  [0]
--****--  - 4  [2]  [1]
-*******- - 6  [1]  [2]
********* - 8  [0]  [3]

n = 5
----**---- - 2 [0]  [4]
---****--- - 4 [1]  [3]
--******-- - 6 [2]  [2]
-********- - 8 [3]  [1]
********** - 10 [4] [0]
"""

# def almost_triangle(n):
#     outp=""
#     row_length = n*2
#     for a in range(n):
#         empty_half = n-a-1
#         full_half = row_length - (empty_half*2)
#         for j in range(empty_half): outp+=" "
#         for j in range(full_half): outp+="*"
#         for j in range(empty_half): outp+=" "
#         outp+="\n"
#     print(outp)

# n = int(input("Number of (almost) triangle rows: "))
# almost_triangle(n)

