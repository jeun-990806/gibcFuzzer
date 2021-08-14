//qfcvt_r
#include <stdlib.h>
#include <stdint.h>
int target(uint8_t **data) {
	qfcvt_r(data[0][0], data[1][0], data[2], data[3], data[4], data[5][0]);
	return 0;
}