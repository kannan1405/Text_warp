import textwrap
def wrap(string, max_width):
    t=0
    l=len(string)
    
    for i in range(max_width,l,max_width):
        print(string[t:i])
        t=i
    
    if (len(string) % max_width != 0): 
        rem=len(string) % max_width
      
        print(string[t:t+rem])
   
    
    return  "\n"

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
