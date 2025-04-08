import Solver.*;
import Structures.*;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.PrintWriter;

public class Main {
    public static int MAXLEN = 5;

    public static void main(String[] args) throws IOException{
        Stack st = new Stack(MAXLEN);
        Queue q = new Queue(MAXLEN);
        Palindrome pal = new Palindrome(MAXLEN);

        BufferedReader input = new BufferedReader(new FileReader(args[0]));
        PrintWriter output = new PrintWriter(args[1]);
        for(int cnt = 0; ; cnt++){
            String line = input.readLine();
            if (line == null) break;

            String[] tokens = line.split(" ");
            String target = tokens[0];
            String command = tokens[1];
            
            int i = 0;
            switch(target){
                case "stack":
                    switch(command){
                        case "push":
                            i = Integer.parseInt(tokens[2]);
                            st.push(i);
                            output.println("stack push: " + i);
                            break;
                        case "pop":
                            i = st.pop();
                            output.println("stack pop: " + i);
                            break;
                        case "clear":
                            st.clear();
                            output.println("stack cleared");
                            break;
                        case "isempty":
                            if (st.isempty())
                                output.println("stack is empty");
                            else
                                output.println("stack is not empty");
                            break;
                        case "length":
                            i = st.length();
                            output.println("stack length: " + i);
                            break;
                    }
                    break;
                case "queue":
                    switch(command){
                        case "enqueue":
                            i = Integer.parseInt(tokens[2]);
                            q.enqueue(i);
                            output.println("queue enqueue: " + i);
                            break;
                        case "dequeue":
                            i = q.dequeue();
                            output.println("queue dequeue: "+i);
                            break;
                        case "clear":
                            q.clear();
                            output.println("queue cleared");
                            break;
                        case "isempty":
                            if (q.isempty())
                                output.println("queue is empty");
                            else
                                output.println("queue is not empty");
                            break;
                        case "length":
                            i = q.length();
                            output.println("queue length: " + i);
                            break;
                    }
                    break;
                case "palindrome":
                    output.println("palindrome: new sequence");
                    for (int n = 1; n < tokens.length; n++){
                        i = Integer.parseInt(tokens[n]);
                        if (i != 0) {
                            pal.newInt(i);
                            output.println("palindrome newInt: " + i);
                        } else {
                            output.println("palindrome Check: " + Boolean.toString(pal.palindromeCheck()) + " " + pal.length());
                        }
                    }
                    pal.clear();
                    break;
            }
        }
        input.close();
        output.close();
    }
}
