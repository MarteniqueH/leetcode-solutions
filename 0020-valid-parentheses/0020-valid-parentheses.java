class Solution {
    public boolean isValid(String s) {
        // create HashMap

        HashMap <Character, Character> closeToOpen = new HashMap<>(); 

        // add the types of brackets to the hashmap
        closeToOpen.put(']', '[');
        closeToOpen.put(')', '(');
        closeToOpen.put('}', '{');

        // create a stack to keep the open braket 

        Stack<Character> stack = new Stack<>(); 

        // iterate over all of the characters in the string 

        for( char c: s.toCharArray()){
            // if the hashMap contains the current character c
            if(closeToOpen.containsKey(c)){
                // if the stack is empty 
                // OR 
                // if the top item on the stack does not match the the key:value pair set stored in the hashMap 
                if(stack.isEmpty() || stack.peek() != closeToOpen.get(c)){
                    // the parentheses are not correct based on the conditions
                    return false;
                }
                // if the stack is not empty and the current top item of the stack matches the hashmap key:value pair then remove that open braket from the top of the stack
                stack.pop();
            }else{
                // if the current chacater c that is being looked at in the iteration is a open bracket push it to the top of the stack
                stack.push(c);
            }
        }
            
        // This return true if the stack is empty.
        // for every close braket found their was the correct type found in the stack where the open brakets were pushed on to
        return stack.isEmpty(); 

            
    }
}