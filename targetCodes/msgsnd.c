//msgsnd
#include <sys/msg.h>
#include <stdint.h>
int target(uint8_t **data) {
	msgsnd(data[0][0], data[1], data[2][0], data[3][0]);
	return 0;
}