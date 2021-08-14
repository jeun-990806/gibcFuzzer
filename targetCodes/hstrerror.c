//hstrerror
#include <netdb.h>
#include <stdint.h>
int target(uint8_t **data) {
	hstrerror(data[0][0]);
	return 0;
}