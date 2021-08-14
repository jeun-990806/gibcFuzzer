//setmntent
#include <stdio.h>
#include <mntent.h>
#include <stdint.h>
int target(uint8_t **data) {
	setmntent(data[0], data[1]);
	return 0;
}