# pythonLibFuzzer

fuzzer (for glibc functions)
+ Automatically generate test code
+ (Also) Automatically generate and mutate new inputs
+ execution strace

---
## 사용법

start.sh을 실행합니다. start.sh는 무작위로 10개의 glibc function을 뽑아, 각각 5번 생성된 mutation과 함께 실행하여 결과를 저장한다. (별도의 옵션 없음)
