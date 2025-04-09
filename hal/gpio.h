#ifndef HAL_GPIO
#define HAL_GPIO

#ifdef __cplusplus
extern "C"{
#endif

int hal_gpio_init();
int hal_gpio_get();
int hal_gpio_pull();

#ifdef __cplusplus
}
#endif

#endif