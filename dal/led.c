#include "led.h"

#include "gpio.h"
#include "log.h"

int dal_led_init()
{
    hal_gpio_init();
    hal_gpio_pull();

    LOG("dal_led_init\n");
    return 0;
}