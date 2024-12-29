def _if(bool, func1, func2):
    func1() if bool else func2()

def truthy(): 
    print("Test success")
  
def falsey(): 
    print("Test failed")

_if(True, truthy, falsey)
# prints 'Test sucess' to the console