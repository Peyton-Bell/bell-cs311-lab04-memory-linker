# Lab 4 Questions

## Part A

### Question 1

For a back/forwards browsing history, a doubly linked list is important so we can move forwards and backward between pages. If we had a singly linked list we wouldn't be able to go back if the user wanted to. In order for a singly linked list to go back it needs to restart from the home page again, O(n) time complexity. With doubly linked lists moving backwards is only O(1) time complexity.

### Question 2

1. head<->[A]<->tail
2. head<->[A]<->[B]<->tail
3. head<->[Z]<->[A]<->[B]<->tail
4. head(None)<->[Z]<->[A]<->[B]<->[C]<->tail(None)

### Question 3

1. A <-> B <-> C
2. A -> B <-> C (B.prev = None)
3. A -> B <- C (B.next = None)
4. head <-> A <-> None <-> C <-> tail

The first two operations remove B's pointers so it is no longer pointing to anything. Then, when you try to set A.next = B.next and C.prev = B.prev it will break up the list completely losing B. Since you removed it's pointers B.prev and B.next are both = None. So, now all the pointers for A, B, and C are all pointing to None. This makes B and C "clobbered" from the list since there is no longer a direct path to them.

### Question 4

- first base case is when the linked list is empty: node == None -> return None and don't do an recursion
- second base case is when it reaches the end of the linked list or the tail: node.next == None -> return None and stop recursion

If we omit the base cases and let it run for an empty list and a single-node list separately they will both result in an AttributeError crashing the program. None doesn't have any attributes, so when we try to call something like None.next it will crash the program. This is why we need the base cases to handle when the reverse() gets to None.
