//mlockall
#include <sys/mman.h>
#include <stdint.h>
int target(uint8_t **data) {
	mlockall(data[0][0]);
	return 0;
}