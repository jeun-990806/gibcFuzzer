//create_module
#include <linux/module.h>
#include <stdint.h>
int target(uint8_t **data) {
	create_module(data[0], data[1][0]);
	return 0;
}