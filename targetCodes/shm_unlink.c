//shm_unlink
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdint.h>
int target(uint8_t **data) {
	shm_unlink(data[0]);
	return 0;
}