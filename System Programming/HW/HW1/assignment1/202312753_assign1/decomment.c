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
  enum DFAstate {START, CheckChar, CheckString, CheckCommentStart, CheckEscapeSequenceChar, 
    CheckEscapeSequenceString, Twobar_Comment, OneStar_Comment, CheckCommentEnd};
  enum DFAstate DFAstate = START;
  while (1) {
    //int got_eof = 0;

    ich = getchar();
    ch = (char)ich;
    // TODO: Implement the decommenting logic
    switch(DFAstate){
      // 코드의 시작부분
      // case START: 코드의 시작부분을 의미한다.
      // - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시킨다.
      // - ch가 '/'이면, CheckCommentStart로 상태를 변경한다.
      // - ch가 '"'이면, ch를 출력하고 CheckString으로 상태를 변경한다.
      // - ch가 '\''이면, ch를 출력하고 CheckChar로 상태를 변경한다.
      // - ch가 EOF이면, 프로그램을 종료한다.
      // - 그 외의 경우, ch를 출력한다.
      case START:
        if(ch == '\n'){
          putchar(ch);
          line_cur++;
        }
        else if(ch == '/'){
          DFAstate = CheckCommentStart;
        }
        else if(ch == '"'){
          putchar(ch);
          DFAstate = CheckString;
        }
        else if(ch == '\''){
          putchar(ch);
          DFAstate = CheckChar;
        }
        else if(ch == EOF){
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar(ch);
        }
        break;

      case CheckString:
      // 코드 내부의 문자열 부분
      // - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시킨다.
      // - ch가 '"'이면, ch를 출력하고 START로 상태를 변경한다.
      // - ch가 EOF이면, 프로그램을 종료한다.
      // - ch가 '\\'이면, ch를 출력하고 CheckEscapeSequence로 변경한다.
      // - 그 외의 경우, ch를 출력한다.
        if(ch == '\n'){
          line_cur++;
        }
        if(ch == '\\'){
          DFAstate = CheckEscapeSequenceString;
        }

        if(ch == '"'){
          putchar(ch);
          DFAstate = START;
        }
        else if(ch == EOF){
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar(ch);
        }
        break;

      case CheckChar:
      // 코드 내부의 문자 부분
      //  - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시킨다.
      //  - ch가 '\''이면, ch를 출력하고 START로 상태를 변경한다.
      //  - ch가 EOF이면, 프로그램을 종료한다.
      //  - ch가 '\\'이면, ch를 출력하고 CheckEscapeSequence로 변경한다.
      //  - 그 외의 경우, ch를 출력한다.
        if(ch == '\n'){
          line_cur++;
        }
        if(ch == '\\'){
          DFAstate = CheckEscapeSequenceChar;
        }

        if(ch == '\''){
          putchar(ch);
          DFAstate = START;
        }
        else if(ch == EOF){
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar(ch);
        }
        break;
      
      case CheckEscapeSequenceChar:
      // Char 안에 EscapeSequence가 오는지 확인하는 부분
        if(ch=='\n'){
          line_cur++;
          DFAstate = CheckString;
        }
        if(ch=='\\'){
          putchar(ch);
        }
        else if(ch==EOF){
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar(ch);
          DFAstate = CheckChar;
        }
        break;

      case CheckEscapeSequenceString:
      // String 안에 EscapeSequence가 오는지 확인하는 부분
        if(ch=='\n'){
          line_cur++;
          DFAstate = CheckString;
        }
        if(ch=='\\'){
          putchar(ch);
        }
        else if(ch==EOF){
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar(ch);
          DFAstate = CheckString;
        }
        break;

      case CheckCommentStart:
        if(ch == '/'){
          putchar(' ');
          line_com=line_cur;  
          DFAstate = Twobar_Comment;
        }
        else if(ch == '*'){
          putchar(' ');
          line_com=line_cur;
          DFAstate = OneStar_Comment;
        }
        else if(ch == '\n'){
          putchar('/');
          putchar(ch);
          line_cur++;
          DFAstate = START;
        }
        else if( ch == EOF){
          putchar('/');
          return(EXIT_SUCCESS);
          break;
        }
        else{
          putchar('/');
          putchar(ch);
          DFAstate = START;
        }
        break;
      
      case Twobar_Comment:
      // //로 시작하는 각주 부분
      // - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시키고 START로 상태를 변경한다.
      // - ch가 EOF이면, 프로그램을 종료한다.
      // - 그 외의 경우, DFAstate를 Twobar_Comment로 유지한다.
        if(ch == '\n'){
          putchar(ch);
          line_cur++;
          DFAstate = START;
        }
        else if(ch == EOF){
          return(EXIT_SUCCESS);
          break;
        }
        break;
      
      case OneStar_Comment:
      // /+*로 시작하는 각주 부분
      // - ch가 '*'이면, CheckCommentEnd로 상태를 변경한다.
      // - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시킨다.
      // - ch가 EOF이면, 프로그램을 종료한다.
      // - 그 외의 경우, DFAstate를 OneStar_Comment로 유지한다.
        if(ch == '*'){
          DFAstate = CheckCommentEnd;
        }
        else if(ch == '\n'){
          putchar(ch);
          line_cur++;
        }
        else if(ch == EOF){
          fprintf(stderr, "Error: line %d: unterminated comment\n", line_com);
          return(EXIT_FAILURE);
          break;
        }
        break;

      case CheckCommentEnd:
      // /+*로 시작된 각주가 끝나는지 확인하는 부분
      // - ch가 '/'이면, START로 상태를 변경한다.
      // - ch가 '*'이면, CheckCommentEnd로 상태를 유지한다.
      // - ch가 '\n'이면, ch를 출력하고 line_cur을 1 증가시킨다.
      // - ch가 EOF이면, 프로그램을 종료한다.
      // - 그 외의 경우, OneStar_Comment로 상태를 변경한다.
        if(ch == '/'){
          DFAstate = START;
        }
        else if(ch == '*'){
          DFAstate = CheckCommentEnd;
        }
        else if(ch == '\n'){
          putchar(ch);
          line_cur++;
        }
        else if(ch == EOF){
          fprintf(stderr, "Error: line %d: unterminated comment\n", line_com);
          return(EXIT_FAILURE);
          break;
        }
        else{
          DFAstate = OneStar_Comment;
        }
        break;

      default:
      // 혹시 모르는 경우를 대비해 default로 설정
        return(EXIT_FAILURE);
        break;
    }
  }
  return(EXIT_SUCCESS);
}
