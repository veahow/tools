KERNEL_DIR ?=../kernel
PWD := $(shell pwd)
MODULE_NAME = demo
HEADER_DIR = ../project/release/include/

ccflags-y := -I$(HEADER_DIR)
obj-m += $(MODULE_NAME).o
obj-$(MODULE_NAME) += demo.c

modules:
	make -C $(KERNEL_DIR) -I $(HEADER_DIR) M=$(PWD) modules
	
clean:
	make -C $(KERNEL_DIR) M=$(PWD) clean

.PHONY: modules 

