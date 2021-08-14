//getttynam
#include <ttyent.h>
#include <stdint.h>
int target(uint8_t **data) {
	getttynam(data[0]);
	return 0;
}