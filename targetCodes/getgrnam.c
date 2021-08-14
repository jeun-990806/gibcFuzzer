//getgrnam
#include <sys/types.h>
#include <grp.h>
#include <stdint.h>
int target(uint8_t **data) {
	getgrnam(data[0]);
	return 0;
}