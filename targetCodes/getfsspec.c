//getfsspec
#include <fstab.h>
#include <stdint.h>
int target(uint8_t **data) {
	getfsspec(data[0]);
	return 0;
}