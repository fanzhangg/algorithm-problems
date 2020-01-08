from deque import Deque

def is_palindrome(string: str)->bool:
    deq = Deque()
    for c in string:
        deq.add_front(c)

    while True:
        if deq.is_empty():  # even length
            return True
        
        c1 = deq.remove_front()
        
        if deq.is_empty():  # Odd length
            return True

        c2 = deq.remove_rear()

        if not c1 == c2:
            return False
