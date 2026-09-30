2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Locking]]

# Spinlock Interrupt Variants

Spinlock interrupt variants combine [[SpinLock]] acquisition with disabling local interrupt or bottom-half processing. They prevent an interrupt handler on the same CPU from preempting the holder and trying to acquire the identical lock, which would spin forever because the interrupted holder cannot resume.

The correct variant matches the contexts that share the data: ordinary locking, bottom-half exclusion, interrupt disabling, or interrupt-state save and restore. Disabling local interrupts alone does not serialize another CPU, so the spinlock remains necessary on multiprocessor systems.

# References

[[linuxkernelprogramming_secondedition.pdf]]
