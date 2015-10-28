def is_palindrome(text):
    return text == text[::-1]

def my_longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    low_text = text.lower()
    #print low_text
    start = 0
    end   = 0
    max_length = -1
    max_start  = 0
    max_end    = 0
    for start,start_letter in enumerate(low_text):
        if True: # start == #
            #if start == 7: print "START = 7"
            #print "New for iteration"
            #print start,start_letter
            end = start # slice is not inclusive
            while end < (len(low_text)): # extract to a variable
                #print "********"
                #print end
                #print len(low_text)-1
                #print text[start:end+1]
                if is_palindrome(low_text[start:end+1]): # is indexing off                    
                    #print "Palindrome"
                    #print text[start:end+1]
                    #print "start = "+str(start)
                    #print "end = "+str(end)
                    #print "max_length = "+str(max_length)
                    if (end-start+1) > max_length:
                        #print "NEW_MAX"
                        max_length = end-start+1
                        max_start  = start
                        max_end    = end+1
                    #print "Increment end"
                    end += (end-start+1) # is this correct, or should it be minus one
                else:
                    end += 1
    #print "end"
    #print max_start, max_end
    #print low_text[max_start:max_end]
    return (max_start,max_end)

# i dont understand the slice that is happening below. is it a tuple input?
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    if text == '': return (0,0)
    def length(slice): a,b = slice; return b-a
    candidates = [grow(text, start, end) # list of tuples
                  for start in range(len(text))
                  for end in (start,start+1)] # start is for odd case, start+1 for even case
    return max(candidates, key=length)

def grow(text, start, end):
    "Start with a 0- or 1- length palindrome; try to grow a bigger one"
    while (start > 0 and end < len(text)
           and text[start-1].upper() == text[end].upper()):
        start -= 1; end +=1
    return (start,end)
    
                    
def test():
    L = longest_subpalindrome_slice

    assert L('Race carr') == (7, 9)

    assert L('xxbxx') == (0, 5)
    assert L('xxxxx') == (0, 5)

    #return 'tests pass'

    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Mad am I ma dam.') == (0, 15)

    return 'tests pass'

print test()

#print is_palindrome("the")
#print is_palindrome("abba")
#longest_subpalindrome_slice("abba")
#longest_subpalindrome_slice("abbaab") # just abba
#longest_subpalindrome_slice("abbaabba")
#longest_subpalindrome_slice("abbaabbaabbaabba")

#longest_subpalindrome_slice("cabba")
#longest_subpalindrome_slice("abcdabba")
