# pythonLibFuzzer

fuzzer (for glibc functions)
+ Automatically generate test code
+ (Also) Automatically generate and mutate new inputs
+ execution ftrace

---
## 사용법

main.py [targetCode]  
target code가 directory인 경우, directory 내의 전체 파일에 대해 fuzzing을 
