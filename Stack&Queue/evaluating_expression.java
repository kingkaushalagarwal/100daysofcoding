//Concept learned in java
// method equal in java =  equal(str1,str2)
//method 2 str1.equalsIgnoreCase(str2)
//Interview Bit java implementation

public class Solution {
    public int evalRPN(String[] A) {
    Stack<Integer> stack = new Stack<>();
    int first;
    int second;
    for(String str:A)
    {
        if(equal(str,"+"))
        {
            second = stack.pop();
            first = stack.pop();
            stack.push(first + second);
        }
        else if(equal(str,"-")){
            second = stack.pop();
            first = stack.pop();
            stack.push(first - second);

        }
        else if(equal(str,"*")){
            second = stack.pop();
            first = stack.pop();
            stack.push(first * second);

        }else if(equal(str,"/")){
            second = stack.pop();
            first = stack.pop();
            stack.push((int)(first / second));

        }
        else {
            int val = Integer.parseInt(str);
            stack.push(val);
        }


    }
    return stack.peek();

    }
    public boolean equal(String str1, String str2) {
	    return str1.equalsIgnoreCase(str2);
	}
}
