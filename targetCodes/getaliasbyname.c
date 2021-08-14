//getaliasbyname
#include <aliases.h>
#include <stdint.h>
int target(uint8_t **data) {
	getaliasbyname(data[0]);
	return 0;
}