def fun1():
    print("fun() called")

def fun2():
    print("Before fun1()")
    fun1()
    print("After fun1()")

print("Before fun2()")
fun2()
print("After fun2()")
