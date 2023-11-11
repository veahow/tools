#include <linux/init.h> 
#include <linux/module.h>

static int var = 0;
module_param(var, int, S_IRUGO|S_IWUSR);
MODULE_PARM_DESC(var, "demo test parameter");

static int __init demo_init(void)
{
	printk(KERN_ALERT "[%s %d] var:%d\n", 
		__FUNCTION__, __LINE__, var);

	return 0;
}
module_init(demo_init);

static void __exit demo_exit(void)
{
	printk(KERN_ALERT "[%s %d]\n", 
		__FUNCTION__, __LINE__);
}
module_exit(demo_exit);

MODULE_LICENSE("GPL");
MODULE_AUTHOR("veahow");
MODULE_DESCRIPTION("A Simple Demo Module");
MODULE_VERSION("1.0");