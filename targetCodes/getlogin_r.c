//getlogin_r
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	getlogin_r(data[0], data[1][0]);
	return 0;
}