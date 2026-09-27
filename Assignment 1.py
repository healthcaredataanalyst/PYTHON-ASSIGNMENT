greetings=["Hello"]
Name = input("Enter your name: ")
Result = f"hello, {Name} welcome to Python programming"
print(len(Result))
# slicing
# first character of string
print(Result[0:1])
print(Result[-1])
print(Result[0:5])
print(Result[-11:])
print(Result[::-1])
print(Result[23:29])
strM = "Python beginner tutorial"
print(strM.upper())
print(strM.lower())
print(strM.capitalize())
print(strM.count("t"))
strM = "Python beginner tutorial"
print(strM.replace("Python", "Machine Learning"))
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
t_combine = tuple1 + tuple2
print(t_combine)
print(t_combine * 3)
print(t_combine[2])
print(t_combine[0:3])
print(t_combine[-3:])