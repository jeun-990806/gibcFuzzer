//qfcvt
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	qfcvt(data[0][0], data[1][0], data[2], data[3]);
	return 0;
}