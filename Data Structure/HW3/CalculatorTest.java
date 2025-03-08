import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class CalculatorTest {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {
            String input;
            while (!(input = br.readLine()).equals("q")) {
                command(input);
            }
        } catch (Exception e) {
            System.out.println("입력이 잘못되었습니다. 오류 : " + e);
        }
    }

    private static void command(String input) {
        String parsedInput = parseInput(input);
        String postfix = toPostfix(parsedInput);
        String result = calculate(postfix);
        
        if (!"ERROR".equals(parsedInput) && !"ERROR".equals(postfix) && !"ERROR".equals(result)) {
            System.out.println(postfix);
            System.out.println(result);
        } else {
            System.out.println("ERROR");
        }
    }

    private static int better(char a, char b)
	{
        int result;
		switch(a)
		{
			case ')':
				result=(b==')')?0:1;
				return result;
			case '~':
                result=((b==')')||(b=='^'))?-1:((b == '~')?0:1);
				return result;
			case '^':
                result=(b==')')?-1:((b == '^')?0:1);
				return result;
			case '*':
			case '%':
			case '/':
                result=((b==')')||(b=='~')||(b=='^'))?-1:((b=='+')||(b=='-')||(b=='(')?1:0);
				return result;
			case '+':
			case '-':
                result=((b=='+')||(b=='-'))?0:((b=='(')?1:-1);
				return result;
			case '(':
                result=(b=='(')?0:-1;
                return result;
			default:
				throw new IndexOutOfBoundsException();
		}
	}

    private static String parseInput(String input)
	{
		String result = "";
		boolean lastisnum = false;
		boolean needtojump = true;


		for(int i = 0; i < input.length(); i++){
			char check = input.charAt(i);
			if((check != ' ')&&(check != 9)){
				if((48 <= check)&&(check <= 57)&&needtojump&&lastisnum){
						result = "ERROR";
                        return result;
				}
                lastisnum=((48 <= check)&&(check <= 57)?true:false);
                result += check;
			}
            needtojump=((check == ' ')||(check == 9)?true:false);
		}
		return result;
	}
    
    
    private static String toPostfix(String input) {
        StringBuilder result = new StringBuilder();
        Stack<Character> opstack = new Stack<>();
    
        boolean isUnary = true; 
        boolean spaceAfterNum = false;
        int parenthesisCount = 0; 
        boolean specialErrorChecker = false;
    
        if (input.equals("ERROR")) return input;
    
        for (int i = 0; i < input.length(); i++) {
            char check = input.charAt(i);
            
            if (Character.isDigit(check)) {
                specialErrorChecker = false; 
                result.append(spaceAfterNum && result.length() > 0 ? " " : "").append(check);
                spaceAfterNum = false;
                isUnary = false;
            } else {
                spaceAfterNum = true;
    
                if (specialErrorChecker && check == ')') return "ERROR";
    
                if (check != '(' && check != ')') specialErrorChecker = true;
    
                if (check == '(') {
                    opstack.push(check);
                    parenthesisCount++;
                    continue;
                }
    
                if (check == ')') {
                    if (parenthesisCount > 0) {
                        while (opstack.peek() != '(') {
                            result.append(" ").append(opstack.pop());
                        }
                        opstack.pop(); // Remove '('
                        parenthesisCount--;
                    } else {
                        return "ERROR"; // Parenthesis mismatch
                    }
                    continue;
                }
    
                if (check == '-') check = isUnary ? '~' : check;
    
                isUnary = true; 
    
                while (!opstack.empty()) {
                    int pr = better(check, opstack.peek());
                    if (pr > 0 || (check == '^' && pr == 0) || (check == '~' && pr == 0)) {
                        opstack.push(check);
                        break;
                    } else {
                        if (result.length() > 0) result.append(' ');
                        result.append(opstack.pop());
                    }
                }
                if (opstack.empty() || better(check, opstack.peek()) > 0) opstack.push(check);
            }
        }
    
        while (!opstack.empty()) {
            result.append(" ").append(opstack.pop());
        }
    
        return result.toString().trim(); // Trim to remove leading space
    }
    
    
	private static String calculate(String input) {
		Stack<Long> dish = new Stack<>();
		String term = ""; 

		if (input.equals("ERROR")) return "ERROR";

		for (int i = 0; i < input.length(); i++) {
			char target = input.charAt(i);

			if (Character.isDigit(target)) {
				term += target;
				continue;
			}
			
			if (target == ' ') {
				if (!term.isEmpty()) {
					dish.push(Long.parseLong(term));
					term = "";
				}
				continue;
			}
			
			if (target == '~') {
				if (dish.empty()) return "ERROR";
				dish.push(-dish.pop());
				continue;
			}
			
			if (dish.size() < 2) return "ERROR";
			long num1 = dish.pop();
			long num2 = dish.pop();
			long res;

			if (target == '+') {
				res = num2 + num1;
			} else if (target == '-') {
				res = num2 - num1;
			} else if (target == '*') {
				res = num2 * num1;
			} else if (target == '/') {
				if (num1 == 0) return "ERROR";
				res = num2 / num1;
			} else if (target == '%') {
				if (num1 == 0) return "ERROR";
				res = num2 % num1;
			} else if (target == '^') {
				if (num1 < 0 && num2 == 0) return "ERROR";
				res = (long) Math.pow(num2, num1);
			} else {
				return "ERROR"; // Handle unknown operator
			}

			dish.push(res);
		}

		return (dish.size() == 1) ? String.valueOf(dish.pop()) : "ERROR";
	}


}
