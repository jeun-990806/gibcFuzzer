//putchar_unlocked
#include <stdio.h>
#include <stdint.h>
int target(uint8_t **data) {
	putchar_unlocked(data[0][0]);
	return 0;
}