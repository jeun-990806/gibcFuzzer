//shmdt
#include <sys/shm.h>
#include <stdint.h>
int target(uint8_t **data) {
	shmdt(data[0]);
	return 0;
}