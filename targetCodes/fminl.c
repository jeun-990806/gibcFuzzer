//fminl
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	fminl(data[0][0], data[1][0]);
	return 0;
}