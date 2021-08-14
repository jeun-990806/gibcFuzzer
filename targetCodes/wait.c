//wait
#include <sys/wait.h>
#include <stdint.h>
int target(uint8_t **data) {
	wait(data[0]);
	return 0;
}