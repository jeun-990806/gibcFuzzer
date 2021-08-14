//sched_get_priority_max
#include <sched.h>
#include <stdint.h>
int target(uint8_t **data) {
	sched_get_priority_max(data[0][0]);
	return 0;
}