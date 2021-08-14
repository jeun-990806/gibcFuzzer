//sem_unlink
#include <semaphore.h>
#include <stdint.h>
int target(uint8_t **data) {
	sem_unlink(data[0]);
	return 0;
}