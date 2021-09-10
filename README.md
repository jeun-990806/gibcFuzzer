# pythonLibFuzzer

fuzzer (for glibc functions)
+ Automatically generate test code
+ (Also) Automatically generate and mutate new inputs
+ execution ftrace

---
## 사용법

sudo python3 main.py [targetCode] [targetFunction]  
(targetCode 내에 targetFunction이 정의되어 있어야 함.

---
## 설명

### 1. 실행 과정
 1. Fuzzing 하고자 하는 함수를 정의한 test code가 필요하다.  
    (atoi 함수의 test code 예)
 ```c
  #include <stdlib.h>
  
  int atoi(const char *nptr);
 ```
 2. 이 test code는 TargetFunctionScanner 클래스가 읽어, 함수의 정보를 바탕으로 .pro 파일을 생성한다. 이 파일은 target code를 빌드할 때, Fuzzer가 argument type에 맞는 Mutator 객체를 생성할 때 사용된다.   
    (atoi.pro 예시)
```buildoutcfg
NAME=atoi;
RETURN_TYPE=int;
HEADER_FILES=stdlib.h;
ARG1=const char*;
```
 3. 그리고 test code를 Builder 클래스가 다음의 코드로 변환한 뒤 빌드한다.  
    (atoi의 변환된 코드 예시)
```c
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
        
int setTrace = -1;
int marker = -1;

char ftracePath[256] = "/sys/kernel/debug/tracing/tracing_on";
char markerPath[256] = "/sys/kernel/debug/tracing/trace_marker";       
         
int openFtraceFiles(void){
	setTrace = open(ftracePath, O_WRONLY);
	marker = open(markerPath, O_WRONLY);
	return (setTrace > 0) && (marker > 0);
}
            
void ftraceStart(void){
	openFtraceFiles();
	if(setTrace != -1 && marker != -1){
		write(setTrace, "1", 1);
		write(marker, "start_ftrace\n", 14);
	}else{
		printf("cannot open ftrace files.\n");
	}
}
void ftraceStop(void){
	if(setTrace != -1 && marker != -1){
		write(marker, "stop_ftrace\n", 13);
		write(setTrace, "0", 1);
		close(marker);
		close(setTrace);
	}else{
		printf("cannot open ftrace files.\n");
	}
}

void target(const char *nptr){
    ftraceStart();
    atoi(nptr);
    ftraceStop();
}
```
4. 빌드가 완료되면, 빌드한 코드를 import하여 Fuzzing하는 Fuzzer Class의 객체를 생성한다. 
   1. *.pro 파일의 정보를 바탕으로 DataType 객체, Mutator 객체를 생성함  
  

5. executeWithMutationSequence()를 반복하여 실행한다.  
   1. Mutator 객체들이 만든 Mutation들을 하나의 List로 저장함 (MutationSequence)
   2. ptrace 프로세스를 생성함
   3. MutationSequence를 target() 함수에 전달함
   4. 새로운 system call set을 발견한 경우, ftrace log를 저장함
  
  
### 2. 파일 설명
 + fuzzer.py: Fuzzer class 정의
   + Class Fuzzer
     + setMutators(): 각 argument의 type에 맞는 Mutator 객체들을 생성함.
     + makeMutationSequence(): Mutator 객체들이 반환하는 Mutation들을 하나의 Mutation Sequence로 만듦.
     + executeWithMutationSequence(): 새로운 Mutation Sequence를 이용해 Test Code를 실행함. 
 + targetFunctionScanner.py: TargetFunctionScanner class 정의
   + Class TargetFunctionScanner
 + targetCodeBuilder.py: Builder class 정의
   + Class Builder
 + cDataMaker.py: CDataMaker class 정의
   + Class CDataMaker
     + castToCDataType(): bytearray를 원하는 c data type으로 캐스트함.
 + dataType.py: DataType class 정의
   + Class DataType
     + getMutator(): 객체의 data type에 맞는 mutator를 생성하여 반환함.
 + byteMutator.py: ByteMutator class 정의
   + Class ByteMutator
     + getMutation(): byte mutation을 생성하고 이를 반환함. 
 + structMutator.py: StructMutator class 정의 (미사용)