# f = open("file.txt")
# print(type(f))
# data = f.read()
# print(data)
# f.close()

# МЕНЕДЖЕР КОНТЕКСТА

# def is_closed(file_):
#     if file_.closed:
#         print("Файл закрыт")
#     else:
#         print("Файл открыт")
        # -------------------------------
# with open("file.txt") as p:
#     print(type(p))
#     data = p.read()
#     print(data)
#     is_closed(p)
# is_closed(p)

# with open("file.txt") as p:
#     data = p.read()
#     print(data)
# ------------
# data += '\nЕще одна строка'
# print(data)
# -----------
# with open("file.txt") as f:
#     print(f.readline())
#     print(f.readline())
# ------------------------
# with open("file.txt") as f:
#     lines = f.readlines()
#     print(type(lines))
#     print(len(lines))
#     print(lines[0])
# --------------------
# with open("file.txt") as f:
#     for line in f:
#         print(line.strip())
# --------------
# with open("file.txt") as f:
#     for idx, l in enumerate(f):
#         print(idx, l.strip())

# with open("file.txt", "w") as f:
#     f.write('Hello world')
# -------------
# путь к тек директории

# import os
# import time
# with open("file.txt", "w") as f:
#     f.write(f'{time.time()}')
# with open("file.txt", "r") as f:
#     print(f.read())
# print(os.getcwd())
# file_path = os.path.join(os.getcwd(), "text.txt")
# print(file_path)
