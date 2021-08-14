//pthread_exit
#include <pthread.h>
#include <stdint.h>
int target(uint8_t **data) {
	pthread_exit(data[0]);
	return 0;
}