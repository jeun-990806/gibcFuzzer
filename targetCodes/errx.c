//errx
#include <err.h>
#include <stdint.h>
int target(uint8_t **data) {
	errx(data[0][0], data[1]);
	return 0;
}