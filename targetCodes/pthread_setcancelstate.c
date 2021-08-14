//pthread_setcancelstate
#include <pthread.h>
#include <stdint.h>
int target(uint8_t **data) {
	pthread_setcancelstate(data[0][0], data[1]);
	return 0;
}