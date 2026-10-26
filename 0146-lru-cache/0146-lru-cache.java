// hashmap will provide fast access to the items using their key
import java.util.HashMap;
// the interface that the hashmap implements 
import java.util.Map;

class LRUCache {
    // create a class node 

    class Node {
        // stores the key
        int key;
        // stores the value associated with each of the key
        int value;
        //points to the prev node
        Node prev;
        // points to the next node 
        Node next;
        // constructor the run when a new node is created 
        Node(int key, int value) {
            // saves the key in the node
            this.key = key;
            // saves the value in the node
            this.value = value;
        }
    }
    // declare cache variables 
    // the max number of items allows
    private final int capacity;
    // maps the each integer key to its node
    private final Map<Integer, Node> cache;
    //makres the begining of the linked list
    private final Node head;
    // marks the tail of the linked list 
    private final Node tail;

    public LRUCache(int capacity) {
        // Initalizing the cache
        //remebers how much the cache can hold 
        this.capacity = capacity;
        // creates and empty hashmap
        this.cache = new HashMap<>();
        //creates a dummynode at thebegining 
        head = new Node(0, 0);
        //creates a dummynode at the end 
        tail = new Node(0, 0);
        //connects the head to the tail
        head.next = tail;
        // connects the tail back to the head 
        tail.prev = head;
    }

    public int get(int key) {
        // checks if the key exist 
        if (!cache.containsKey(key)) {
            return -1;
        }
        // retrives the node  since it does exist 
        Node node = cache.get(key);
        //removes the node from the current position
        remove(node);

        //moves it to the end of the linked list
        addToTail(node);
        // returns the value of the key value pair
        return node.value;
    }

    public void put(int key, int value) {
        // if the key already exist update it 
        if (cache.containsKey(key)) {
            Node node = cache.get(key);
            node.value = value;

            remove(node);
            addToTail(node);

            // if the keydoes not exist create a new node 
        } else {
            Node node = new Node(key, value);

            cache.put(key, node);
            addToTail(node);
        }
        // checks wheather the cache is over capacity
        if (cache.size() > capacity) {
            Node lru = head.next;

            remove(lru);
            cache.remove(lru.key);
        }
    }
    // helper function that removes the nodes from the linked list 
    private void remove(Node node) {
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }
    // helper method that inserts a node acter the dummy tail node 
    private void addToTail(Node node) {
        Node last = tail.prev;

        last.next = node;
        node.prev = last;

        node.next = tail;
        tail.prev = node;
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */