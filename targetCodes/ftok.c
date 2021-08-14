//ftok
#include <sys/ipc.h>
#include <stdint.h>
int target(uint8_t **data) {
	ftok(data[0], data[1][0]);
	return 0;
}