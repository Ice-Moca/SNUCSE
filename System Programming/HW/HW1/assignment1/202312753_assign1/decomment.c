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
    if((ch=='"'&&checkComment==OFF&&checkChar==OFF)){
      putchar(ch);
      if(checkString == ON){//문자열이 끝나는 부분
        checkString = OFF;
      }
      else if(checkString == OFF){
        checkString = ON;
      }
    }
    // 코드의 시작부분에 있는 Char부분 확인
    else if((ch=='\''&&checkComment==OFF&&checkString==OFF)){
      putchar(ch);
      if(checkChar == ON){
        checkChar = OFF;
      }
      else if(checkChar == OFF){
        checkChar = ON;
      }
    }
    // 코드의 시작부분에 있는 주석부분 확인
    else if(ch=='/'&&checkString==OFF&&checkChar==OFF){
      ich= getchar();
      ch = (char)ich;
      if(ch=='/'){ // 주석이 시작되는 부분
        line_com = line_cur; // 주석이 시작되는 줄
        checkComment=ON;
        putchar(' ');
        while(1){  // 주석이 끝나는 부분까지 출력하지 않고 넘어가기
          ich = getchar();
          ch = (char)ich;
          if(ch=='\n'){
            line_cur++;
            checkComment=OFF;
            putchar(ch); // enter 출력
            break;
          }
        }
      }
      else if(ch=='*'){ // 주석이 시작되는 부분
        line_com = line_cur; // 주석이 시작되는 줄
        putchar(' ');
        checkComment=ON;
        while(checkComment==ON){
          ich = getchar();
          ch = (char)ich;
          if(ch=='\n'){ // enter 출력 다만 주석은 계속된다.
            putchar('\n');
            line_cur++;
          } 
          if(ch=='*'){  // 주석이 끝나는지 확인
            ich = getchar();
            if(ich=='/'){// 주석이 끝나는 부분
              checkComment=OFF;
            }
            else{
              ungetc(ich,stdin);
            }
          }
          if(ch==EOF){ // 주석이 끝나지 않고 파일이 끝나는 경우
            got_eof = 1;
            fprintf(stderr, "Error: line %d: unterminated comment\n", line_com);//에러파일에 출력
            break;
          }
        }
      }
      else{
        putchar('/');
        putchar(ch);
      }
    }
    else{// 주석이 아닌 경우
      // 코드의 끝부분에 있는 enter와 eof부분 확인인
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
