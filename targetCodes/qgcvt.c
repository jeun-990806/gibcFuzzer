//qgcvt
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	qgcvt(data[0][0], data[1][0], data[2]);
	return 0;
}