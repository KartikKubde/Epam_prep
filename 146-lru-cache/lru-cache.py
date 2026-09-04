class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add_to_front(self,node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1

        target_node = self.cache[key]
        self.remove(target_node)
        self.add_to_front(target_node)
        return target_node.value



    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            target_node = self.cache[key]
            target_node.value = value
            self.remove(target_node)
            self.add_to_front(target_node)

        else:
            new_node = Node(key,value)
            self.cache[key] = new_node
            self.add_to_front(new_node)

            if len(self.cache) > self.capacity :
                lru = self.tail.prev
                self.remove(lru)
                del self.cache[lru.key]
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

