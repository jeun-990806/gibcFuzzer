//getpass
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	getpass(data[0]);
	return 0;
}