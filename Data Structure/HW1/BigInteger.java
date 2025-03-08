import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.StringReader;
import java.util.Arrays;
import java.util.regex.Matcher;
import java.util.regex.Pattern;




public class BigInteger
{
    public static final String QUIT_COMMAND = "quit";
    public static final String MSG_INVALID_INPUT = "Wrong Input";
  
    // implement this
    public static final Pattern EXPRESSION_PATTERN = Pattern.compile("");


    //field
    public int[] Int=new int[220];

    //find if positive of negative
    //true->positive false->negative
    public boolean ifpos;

    //length of number
    public int length;

    public BigInteger(String s) throws IllegalArgumentException
    {
        //연산자 뒤에 또다른 연산자가 있을때 처리, 100*+100꼴
        char ifop =s.charAt(0);


        //숫자 앞에 + - 부호 오는지 확인
        if( ifop == '+' || ifop == '-'){
            ifpos = (ifop=='+');
            s=s.substring(1);
        }
        else{
            //특별한 부호가 제시되어 있지 않으면 양수로 파악
            ifpos = true;
        }

        //주어진 문자열을 저장
        int len= s.length();
        length=len;
        
        //문자열을 반대로 저장해서 연산할때 편하게 만들자
        for(int index=len-1,reverseindex=0;index>=0;reverseindex++,index--){
            char check = s.charAt(index);
            if(check<'0' || check>'9'){
                throw new IllegalArgumentException();
            }
            Int[reverseindex]=(check-'0');
        }
    }

    public BigInteger(boolean pos, int[] Int){
        this.ifpos = pos;
        this.Int = Int.clone();
        this.length=220;
    }

    public BigInteger(boolean pos, int[] Int,int length){//change()후 length가 필요할 때 호출하는 용도
        this.ifpos = pos;
        this.Int = Int.clone();
        this.length = length;
    }

    //method

    //숫자 +- 바꾸기 100+-100, 100--100같은 상황을 대비
    public BigInteger change(){
        this.ifpos= !this.ifpos;
        return new BigInteger(this.ifpos,this.Int,this.length);
    }
  
    public BigInteger add(BigInteger big)
    {
        int[] newInt = new int[220];

        if(this.ifpos){
            if(big.ifpos){
            }
            else{//this:양수 big:음수
                return this.subtract(big.change());
            }
        }
        else{
            //this:음수 big:양수
            if(big.ifpos){
                return big.subtract(this.change());
            }
            else{//양수+양수로 계산후 부호 바꾸기
                return this.change().add(big.change()).change();
            }
        }

        //7+6시 1 (넘어가는 숫자)
        int carry=0;

        for(int index=0; index<newInt.length; index++) {
            int num = this.Int[index] + big.Int[index] + carry;
            if (10 <= num) {
                carry = 1;
                num = num - 10;
            } else {
                carry = 0;
            }
            newInt[index] = num;
        }
        return new BigInteger(true, newInt);
    }
  
    public BigInteger subtract(BigInteger big)
    {
        int[] newInt = new int[220];

        if(this.ifpos){
            if(big.ifpos){
            }
            else{//this:양수 big:음수
                //양수+양수 꼴로 생각
                return this.add(big.change());
            }
        }
        else{
            //this:음수 big:양수
            if(big.ifpos){//음수-양수==음수+음수
                //양수+양수 후 음수 전환으로 생각
                return big.add(this.change()).change();
            }
            else{//음수1-음수2==양수2-양수1
                return big.change().subtract(this.change());
            }
        }

        //둘다 양수일때 뺄샘 계산이다.
        //case1 두 양수가 같을때
        if(Arrays.equals(this.Int,big.Int)){
            return new BigInteger("0");
        }
        if(this.length>big.length){//case2 this>big
        }
        else if(this.length==big.length){//case2 this>big
            for(int i=this.length-1;i>=0;i--){
                if(this.Int[i]>big.Int[i]){
                    break;
                }
                else if(this.Int[i]==big.Int[i]){
                    continue;
                }
                else{
                    return big.subtract(this).change();
                }
            }
        }
        else{//case3 this<big
            return big.subtract(this).change();
        }
        //this>big 인 경우에 대해서만 뺼샘을 고려
        //13-7 -> digit 6 carry 1
        //이럴 경우 결과 70 -> 바꿀시 07나오니까 나중에 0 제거 함수 만들자
        int carry=0;

        for(int index=0; index<newInt.length; index++) {
            int num = this.Int[index] - big.Int[index] - carry;
            if (num < 0) {
                carry = 1;
                num = num + 10;
            } else {
                carry = 0;
            }
            newInt[index] = num;
        }
        return new BigInteger(true, newInt);
    }
  
    public BigInteger multiply(BigInteger big)
    {
        int[] newInt = new int[220];
        //100*100 연산뒤 나오는 자리는 최대 201자리이지만 혹시 모르니 조금 더 넉넉하게 220으로 설정

        int carry=0;

        for(int index=0; index<210; index++) {
            int sum=0;
            sum=sum+carry;//

            for(int j=0; j<=index; j++) {
                //곱의 자릿수가 일정하도록 설정
                //1*100+10*10+100*1
                sum+=this.Int[j]*big.Int[index-j];
            }
            //carry 연산
            carry=sum/10;
            newInt[index]=sum%10;
        }

        //부호 확인
        boolean pos;

        if(this.ifpos==big.ifpos){
            pos=true;
        }
        else{
            pos=false;
        }
        return new BigInteger(pos, newInt);
    }
  
    @Override
    public String toString()
    {
        //append 사용하기 위해서 Stringbuffer도입
        StringBuffer tostring= new StringBuffer("");

        //숫자 앞에 오는 0을 무시
        //07->7
        boolean leadingZero = true;
        for (int i = this.length - 1; i >= 0; i--) {
            //만일 자릿수가 1이 나오게 되면 원래 값이 0이었던 것
            if (this.length == 1) {
                return "0"; // Special case for -0
            }
            if (this.Int[i] != 0 ) {
                leadingZero = false;
                this.length = i + 1;
                break;
            }
            if(i==0){//끝까지0이면 0*1000꼴의 입력값 -> 0으로 출력
                if(this.Int[0]==0){
                    return "0";
                }
            }
        }

        //음수인지 확인
        if(!this.ifpos){
            tostring.append('-');
        }
        //수 다시 원래대로 만들어서 대입
        for(int i=this.length-1;i>=0;i--){
            tostring.append(this.Int[i]);
        }

        return tostring.toString();
    }
  
    static BigInteger evaluate(String input) throws IllegalArgumentException{
        // implement here
        // parse input
        // using regex is allowed
        //입력값의 공백을 모두 제거한 후 String으로 생각

        String result="";
        for(int i=0; i<input.length();i++){
            if(input.charAt(i)!=' '){
                result +=input.charAt(i);
            }
        }

        int wantindex=1;
        for(int checkindex=1;checkindex<203;checkindex++){
            if( result.charAt(checkindex)=='+'|| result.charAt(checkindex)=='-'|| result.charAt(checkindex)=='*'){
                wantindex=checkindex;
                break;
            }
        }
        String arg1= result.substring(0,wantindex);
        String arg2= result.substring(wantindex+1);

        //check operator
        char operator= result.charAt(wantindex);

        // One possible implementation
        // BigInteger num1 = new BigInteger(arg1);
        // BigInteger num2 = new BigInteger(arg2);
        // BigInteger result = num1.add(num2);

        BigInteger num1 = new BigInteger(arg1);
        BigInteger num2 = new BigInteger(arg2);

        switch (operator) {
            case ('+'): return num1.add(num2);
            case ('-'): return num1.subtract(num2);
            case ('*'): return num1.multiply(num2);
            default: throw new IllegalArgumentException();
        }

        // return result;
    }
  
    public static void main(String[] args) throws Exception
    {
        try (InputStreamReader isr = new InputStreamReader(System.in))
        {
            try (BufferedReader reader = new BufferedReader(isr))
            {
                boolean done = false;
                while (!done)
                {
                    String input = reader.readLine();
  
                    try
                    {
                        done = processInput(input);
                    }
                    catch (IllegalArgumentException e)
                    {
                        System.err.println(MSG_INVALID_INPUT);
                    }
                }
            }
        }
    }
  
    static boolean processInput(String input) throws IllegalArgumentException
    {
        boolean quit = isQuitCmd(input);
  
        if (quit)
        {
            return true;
        }
        else
        {
            BigInteger result = evaluate(input);
            System.out.println(result.toString());
  
            return false;
        }
    }
  
    static boolean isQuitCmd(String input)
    {
        return input.equalsIgnoreCase(QUIT_COMMAND);
    }
}