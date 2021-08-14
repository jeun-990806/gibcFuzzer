//mq_open
#include <fcntl.h>
#include <sys/stat.h>
#include <mqueue.h>
#include <stdint.h>
int target(uint8_t **data) {
	mq_open(data[0], data[1][0]);
	return 0;
}