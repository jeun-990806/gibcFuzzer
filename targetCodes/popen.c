//popen
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	popen(data[0], data[1]);
	return 0;
}