//msgrcv
#include <sys/msg.h>
#include <stdint.h>
int target(uint8_t **data) {
	msgrcv(data[0][0], data[1], data[2][0], data[3][0], data[4][0]);
	return 0;
}