//pthread_setconcurrency
#include <pthread.h>
#include <stdint.h>
int target(uint8_t **data) {
	pthread_setconcurrency(data[0][0]);
	return 0;
}