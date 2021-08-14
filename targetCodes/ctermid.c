//ctermid
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	ctermid(data[0]);
	return 0;
}