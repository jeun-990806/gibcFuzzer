//catopen
#include <nl_types.h>
#include <stdint.h>
int target(uint8_t **data) {
	catopen(data[0], data[1][0]);
	return 0;
}