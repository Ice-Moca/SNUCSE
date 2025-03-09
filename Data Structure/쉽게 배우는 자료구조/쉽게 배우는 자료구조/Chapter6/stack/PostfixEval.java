package stack;

public class PostfixEval {
    private static int evaluate(String postfix){
        int A, B;
        LinkedStack<Integer> s = new LinkedStack<>();
        boolean digitPreviously = false;
        for(int i=0; i<postfix.length();i++){
            char ch = postfix.charAt(i);
            if(Character.isDigit(ch)){//들어오는 입력 값의 부분이 숫자일 경우처리
                if(digitPreviously==true){ // 숫자 인식
                    int tmp= s.pop();
                    tmp = 10*tmp + (ch-'0'); 
                    //ch-'0': char type data> int type data 전환을 위한 연산
                    s.push(tmp);
                }
                else{
                    s.push(ch-'0');
                }
                digitPreviously=true;
            }
            else if(isOperator(ch)){
                A = s.pop();
                B = s.pop();
                int val = operation(A,B,ch);
                s.push(val);
                digitPreviously=false;
            }
            else{
                digitPreviously=false;
            }
        }
        return s.pop();
    }

    public static int operation(int a, int b, char ch){
        int val=0;
        switch (ch) {
            case '*':
                val=b*a;
                break;
            case '/':
                val=b/a;
                break;
            case '+':
                val= b+a;
                break;
            case '-':
                val=b-a;
                break;
        }
        return val;
    }

    private static boolean isOperator(char ch){
        return (ch=='+'||ch=='-'||ch=='+'||ch=='-') ;
    }

    public static void main(String[] args){//Test code
        String postfix = "700 3 47 + 6 * - 4 /";
        System.out.println("Input String: "+ postfix);
        int answer = evaluate(postfix);
        System.out.println("Ans: "+ answer);
    }
}
