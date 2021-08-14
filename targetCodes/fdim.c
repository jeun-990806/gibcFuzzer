//fdim
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	fdim(data[0][0], data[1][0]);
	return 0;
}