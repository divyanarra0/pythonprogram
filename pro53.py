def pangram(str1): 
    str1 = str1.lower() 
    str1 = set(str1) 
    alpha = [ ch for ch in str1 if ord(ch) in range(ord('a'), ord('z')+1)] 
    if len(alpha) == 26: 
        return 'yes'
    else: 
        return 'no'
if __name__ == "__main__": 
    str1 = 'The quick brown fox jumps over the lazy dog'
    print pangram(str1) 
