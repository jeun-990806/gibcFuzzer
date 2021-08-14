//getspnam
#include <shadow.h>
#include <stdint.h>
int target(uint8_t **data) {
	getspnam(data[0]);
	return 0;
}