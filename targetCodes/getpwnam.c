//getpwnam
#include <sys/types.h>
#include <pwd.h>
#include <stdint.h>
int target(uint8_t **data) {
	getpwnam(data[0]);
	return 0;
}