//acct
#include <unistd.h>
#include <stdint.h>
int target(uint8_t **data) {
	acct(data[0]);
	return 0;
}