cmd_/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o := gcc -Wp,-MD,/usr/src/openvswitch-1.4.0/datapath/linux/.flex_array.o.d  -nostdinc -isystem /usr/lib/gcc/i686-linux-gnu/4.6/include -I/usr/src/openvswitch-1.4.0/include -I/usr/src/openvswitch-1.4.0/datapath/linux/compat -I/usr/src/openvswitch-1.4.0/datapath/linux/compat/include  -I/usr/src/linux-headers-3.2.0-55-generic-pae/arch/x86/include -Iarch/x86/include/generated -Iinclude  -include /usr/src/linux-headers-3.2.0-55-generic-pae/include/linux/kconfig.h -Iubuntu/include  -D__KERNEL__ -Wall -Wundef -Wstrict-prototypes -Wno-trigraphs -fno-strict-aliasing -fno-common -Werror-implicit-function-declaration -Wno-format-security -fno-delete-null-pointer-checks -O2 -m32 -msoft-float -mregparm=3 -freg-struct-return -mpreferred-stack-boundary=2 -march=i686 -mtune=generic -maccumulate-outgoing-args -Wa,-mtune=generic32 -ffreestanding -fstack-protector -DCONFIG_AS_CFI=1 -DCONFIG_AS_CFI_SIGNAL_FRAME=1 -DCONFIG_AS_CFI_SECTIONS=1 -pipe -Wno-sign-compare -fno-asynchronous-unwind-tables -mno-sse -mno-mmx -mno-sse2 -mno-3dnow -Wframe-larger-than=1024 -Wno-unused-but-set-variable -fno-omit-frame-pointer -fno-optimize-sibling-calls -pg -Wdeclaration-after-statement -Wno-pointer-sign -fno-strict-overflow -fconserve-stack -DCC_HAVE_ASM_GOTO -DVERSION=\"1.4.0\" -I/usr/src/openvswitch-1.4.0/datapath/linux/.. -I/usr/src/openvswitch-1.4.0/datapath/linux/.. -DBUILDNR=\"\" -g -include /usr/src/openvswitch-1.4.0/datapath/linux/kcompat.h  -DMODULE  -D"KBUILD_STR(s)=\#s" -D"KBUILD_BASENAME=KBUILD_STR(flex_array)"  -D"KBUILD_MODNAME=KBUILD_STR(openvswitch)" -c -o /usr/src/openvswitch-1.4.0/datapath/linux/.tmp_flex_array.o /usr/src/openvswitch-1.4.0/datapath/linux/flex_array.c

source_/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o := /usr/src/openvswitch-1.4.0/datapath/linux/flex_array.c

deps_/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o := \
  /usr/src/openvswitch-1.4.0/datapath/linux/kcompat.h \
  include/linux/version.h \

/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o: $(deps_/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o)

$(deps_/usr/src/openvswitch-1.4.0/datapath/linux/flex_array.o):
