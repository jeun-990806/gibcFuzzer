//ttyname
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	ttyname(data[0][0]);
	return 0;
}