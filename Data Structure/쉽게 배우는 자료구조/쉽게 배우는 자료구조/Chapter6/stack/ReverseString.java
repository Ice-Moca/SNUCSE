package stack;

public class ReverseString {
    private static String reverse(String s){
        ArrayStack<Character> st = new ArrayStack<>(s.length());
        //스택에서 char을 하나의 객체로 사용한다. 따라서 String말고 <E>를 이용해 작성.
        for(int i=0; i<s.length();i++){
            st.push(s.charAt(i));
        }
        String output= "";
        while (!st.isEmpty()) {
            output=output+st.pop();
        }
        return output;
    } 

    public static void main(String[] args){ //Test code
        String input = "Test Seq 12345";
        String output = reverse(input);
        System.out.println("Input String: " + input);
        System.out.println("Reversed String: " + output);
    }
}
