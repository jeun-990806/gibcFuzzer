#include <fstab.h>
#include <stdint.h>
int target(uint8_t **data){
	getfsfile(data[0]);
	return 0;
}
char *targetInfo(void){ return "getfsfile";}