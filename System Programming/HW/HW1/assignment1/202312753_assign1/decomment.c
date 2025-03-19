#include <stdio.h>
#include <assert.h>
#include <stdlib.h>

/* This is skeleton code for reading characters from 
standard input (e.g., a file or console input) one by one until 
the end of the file (EOF) is reached. It keeps track of the current 
line number and is designed to be extended with additional 
functionality, such as processing or transforming the input data. 
In this specific task, the goal is to implement logic that removes 
C-style comments from the input. */

int main(void)
{
  // ich: int type variable to store character input from getchar() (abbreviation of int character)
  int ich;
  // line_cur & line_com: current line number and comment line number (abbreviation of current line and comment line)
  int line_cur, line_com;
  // ch: character that comes from casting (char) on ich (abbreviation of character)
  char ch;

  line_cur = 1;
  line_com = -1;

  // This while loop reads all characters from standard input one by one

  //state
  enum state {ON, OFF};
  enum state checkComment = OFF; // 주석 내부인지 아닌지 확인
  enum state checkString = OFF; // 문자열 내부인지 아닌지 확인
  enum state checkChar = OFF; // 문자 내부인지 아닌지 확인
  

  while (1) {
    int got_eof = 0;

    ich = getchar();
    if (ich == EOF) 
      break;

    ch = (char)ich;
    // TODO: Implement the decommenting logic

    // 굳이 EOF를 이렇게 확인해야 되는지 잘 모르겠음, 주어진 변수니까 그냥 사용;;
    if(ch == EOF){
      got_eof = 1;
    }

    // 코드의 시작부분에 있는 String부분 확인
    // 문자열 상태를 3항 연산자로 전환
    // 문자열이 시작되는 부분이면 checkComment ON
    // 문자열이 끝나는 부분이면 checkComment OFF
    if((ch=='"'&&checkComment==OFF&&checkChar==OFF)){
      putchar(ch);
      checkString = (checkString == ON) ? OFF : ON; 
      continue;
    }
    
    // 코드의 시작부분에 있는 Char부분 확인
    // 문자 상태를 3항 연산자로 전환
    // 문자가 시작되는 부분이면 checkChar ON
    // 문자가 끝나는 부분이면 checkChar OFF
    if((ch=='\''&&checkComment==OFF&&checkString==OFF)){
      putchar(ch);
      checkChar = (checkChar == ON) ? OFF : ON; 
      continue;
    }

    // 코드의 시작부분에 있는 주석부분 확인
    if(ch=='/'&&checkString==OFF&&checkChar==OFF){
      ich= getchar();
      ch = (char)ich;
      // case1) //로 시작되는 주석
      // case2) /*로 시작되는 주석
      // case3) 주석이 아닌 경우
      if(ch=='/'){ 
        /* 
        case1)
        //로 시작되는 주석
        주석이 끝나는 부분까지 출력하지 않고 넘어가기
        while문 안에 while문이 있는 구조이지만 
        getchar()의 실행빈도는 switch case문 보다 적다.
        switch case의 경우 //로 시작하는 각주를 추출하기 위해서 
        getchar()를 2번 실행한다. 또한 state의 정의를 많이 만들어야 되서 error case빈도가 높을 수 있다.

        -ch = \n 일때 주석이 끝난다.
        -ch = EOF 일때 주석이 끝나지 않고 파일이 끝난다.
        -이후 /+* 각주가 끝나지 않을때 출력할 메세지를 위해 line_cur을 저장한다.
        */
        line_com = line_cur; 
        checkComment=ON;
        putchar(' ');
        while(1){  
          ich = getchar();
          ch = (char)ich;
          if(ch=='\n'){
            line_cur++;
            checkComment=OFF;
            putchar(ch); 
            break;
          }
        }
      }
      else if(ch=='*'){
      /* 
      case2)
      /+*로 시작되는 주석
      주석이 끝나는 부분까지 출력하지 않고 넘어가기
      
      -ch = \n 일때 주석이 끝나지 않는다.
      -ch = EOF 일때 주석이 끝나지 않고 파일이 끝난다.
      -이후 /+*각주가 끝나지 않을때 출력할 메세지를 위해 line_cur을 저장한다.

      case1] 주석이 끝나는 경우
      case2] 주석이 끝나지 않고 파일이 끝나는 경우 
      case2의 경우 error메세지를 출력하고 프로그램을 종료한다.
      */
        line_com = line_cur; // 주석이 시작되는 줄
        putchar(' ');
        checkComment=ON;
        while(checkComment==ON){
          ich = getchar();
          ch = (char)ich;
          if(ch=='\n'){ 
            // enter 출력 다만 주석은 계속된다.
            putchar('\n');
            line_cur++;
          } 
          if(ch=='*'){  
            // case1]
            // 주석이 끝나는지 확인
            ich = getchar();
            if(ich=='/'){
              checkComment=OFF;
            }
            else{
              ungetc(ich,stdin);
            }
          }
          if(ch==EOF){ 
            // case2]
            // 주석이 끝나지 않고 파일이 끝나는 경우
            got_eof = 1;
            fprintf(stderr, "Error: line %d: unterminated comment\n", line_com);//에러파일에 출력
            return (EXIT_FAILURE);
            break;
          }
        }
      }
      else{
        putchar('/');
        putchar(ch);
      }
    }
    else{
      // case3) 주석이 아닌 경우
      // 코드의 끝부분에 있는 enter와 eof부분 확인
      if (ch == '\n'){
        line_cur++;
      }
      if (got_eof){
        break;
      }
      putchar(ch);
    }
  }
  return(EXIT_SUCCESS);
}
