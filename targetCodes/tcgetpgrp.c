//tcgetpgrp
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	tcgetpgrp(data[0][0]);
	return 0;
}