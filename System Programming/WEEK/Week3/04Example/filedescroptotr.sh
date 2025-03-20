echo "#include <stdio.h>" | gcc -E - | grep -w _*t
# 1. `echo "#include <stdio.h>"`: 표준 출력에 `#include <stdio.h>`를 출력합니다.
# 2. `| gcc -E -`: 표준 입력에서 입력을 받아서 전처리기(preprocessor) 단계까지만 실행합니다.
#    - `gcc -E`: GCC 컴파일러를 사용하여 전처리기 단계까지만 실행합니다.
#    - `-`: 표준 입력에서 입력을 받도록 지정합니다.
# 3. `| grep -w _*t`: 전처리된 출력에서 `_`로 시작하고 `t`로 끝나는 단어를 검색합니다.
#    - `grep -w`: 단어 단위로 검색합니다.
#    - `_ * t`: `_`로 시작하고 `t`로 끝나는 패턴을 의미합니다.

echo "#include <stdio.h>" | gcc -E - | grep -w off_t
# 1. `echo "#include <stdio.h>"`: 표준 출력에 `#include <stdio.h>`를 출력합니다.
# 2. `| gcc -E -`: 표준 입력에서 입력을 받아서 전처리기(preprocessor) 단계까지만 실행합니다.
#    - `gcc -E`: GCC 컴파일러를 사용하여 전처리기 단계까지만 실행합니다.
#    - `-`: 표준 입력에서 입력을 받도록 지정합니다.
# 3. `| grep -w off_t`: 전처리된 출력에서 `off_t` 단어를 검색합니다.
#    - `grep -w`: 단어 단위로 검색합니다.
#    - `off_t`: `off_t` 타입을 의미합니다.

