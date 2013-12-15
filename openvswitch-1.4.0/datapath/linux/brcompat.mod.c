#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

MODULE_INFO(vermagic, VERMAGIC_STRING);

struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
 .name = KBUILD_MODNAME,
 .init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
 .exit = cleanup_module,
#endif
 .arch = MODULE_ARCH_INIT,
};

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0xc86911db, "module_layout" },
	{ 0xd0d8621b, "strlen" },
	{ 0xb7afe45f, "genl_unregister_family" },
	{ 0xc7a4fbed, "rtnl_lock" },
	{ 0xeb7b764c, "skb_clone" },
	{ 0xa7aaf700, "ovs_dp_ioctl_hook" },
	{ 0x55c09669, "mutex_unlock" },
	{ 0xee49c988, "nlmsg_notify" },
	{ 0x2bc95bd4, "memset" },
	{ 0xb86e4ab9, "random32" },
	{ 0xf97456ea, "_raw_spin_unlock_irqrestore" },
	{ 0x50eedeb8, "printk" },
	{ 0x2f287f0d, "copy_to_user" },
	{ 0xb4390f9a, "mcount" },
	{ 0x76c9efd9, "nla_put" },
	{ 0x16305289, "warn_slowpath_null" },
	{ 0x5d17121e, "mutex_lock" },
	{ 0x52669ef, "netlink_unicast" },
	{ 0x1dadad7c, "genl_register_family_with_ops" },
	{ 0xe1782b27, "init_net" },
	{ 0xc03ccf4a, "__dev_get_by_index" },
	{ 0xc6cbbc89, "capable" },
	{ 0xef06bf6f, "__alloc_skb" },
	{ 0x1c374d1c, "netlink_broadcast" },
	{ 0xf0fdf6cb, "__stack_chk_fail" },
	{ 0x4f391d0e, "nla_parse" },
	{ 0x62090a07, "kfree_skb" },
	{ 0xcb5789ff, "brioctl_set" },
	{ 0x21fb443e, "_raw_spin_lock_irqsave" },
	{ 0xafea97b4, "genl_register_mc_group" },
	{ 0x19a9e62b, "complete" },
	{ 0xda67bc21, "skb_put" },
	{ 0xb1d9523e, "wait_for_completion_timeout" },
	{ 0x362ef408, "_copy_from_user" },
	{ 0x6e720ff2, "rtnl_unlock" },
	{ 0xe914e41e, "strcpy" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=openvswitch";


MODULE_INFO(srcversion, "86F66FB9669D74FF0741D97");
