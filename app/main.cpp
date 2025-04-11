#include "log.h"
#include "feed_protocol.h"
#include "feed_manage.h"
#include "hello_world.h"

int main()
{
    hello_word();

    fun_feed_manage_init();

    while (1)
        ;
    return 0;
}