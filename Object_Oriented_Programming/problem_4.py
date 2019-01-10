def f():
    try:
        print ("a")
        return         # similar to break
    except:
        print ("b")
    else:
        print ("c")
    finally:
        print ("d")

f()


# Result is:
# a
# d
