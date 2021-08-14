//fdopen
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	fdopen(data[0][0], data[1]);
	return 0;
}