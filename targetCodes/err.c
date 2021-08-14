//err
#include <err.h>
#include <stdint.h>
int target(uint8_t **data) {
	err(data[0][0], data[1]);
	return 0;
}