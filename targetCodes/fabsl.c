//fabsl
#include <math.h>
#include <stdint.h>
int target(uint8_t **data) {
	fabsl(data[0][0]);
	return 0;
}