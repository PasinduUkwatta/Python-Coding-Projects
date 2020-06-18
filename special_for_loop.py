#in this code aslo every object is saved in same memory space
#when new object come to the memory , old object replced by the new object
def special_loop(iterable):
    iterator = iter(iterable)
    while True:
        try :
            print(iterator)
            print(next(iterator)*2)

        except StopIteration:
            print(StopIteration)
            break
            
            
            
special_loop([1,2,3,4,5,6])