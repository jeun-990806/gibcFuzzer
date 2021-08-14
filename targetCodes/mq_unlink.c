//mq_unlink
#include <mqueue.h>
#include <stdint.h>
int target(uint8_t **data) {
	mq_unlink(data[0]);
	return 0;
}