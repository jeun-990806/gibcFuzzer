//strxfrm
#include <string.h>
#include <stdint.h>
int target(uint8_t **data) {
	strxfrm(data[0], data[1], data[2][0]);
	return 0;
}