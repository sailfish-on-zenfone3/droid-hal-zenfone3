# These and other macros are documented in dhd/droid-hal-device.inc
# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device zenfone3
%define vendor asus

%define vendor_pretty Asus
%define device_pretty Zenfone 3

%define rpm_device zenfone3
%define installable_zip 1
%define droid_target_aarch64 1

# Entries migrated from the old rpm/droid-hal-hammerhead.spec
%define enable_kernel_update 1

%define straggler_files \
    /bugreports \
    /d \
    /dsp \
    /firmware \
    /plat_file_contexts \
    /plat_hwservice_contexts \
    /plat_property_contexts \
    /plat_seapp_contexts \
    /plat_service_contexts \
    /product \
    /sdcard \
    /vendor \
    /vendor_file_contexts \
    /vendor_hwservice_contexts \
    /vendor_property_contexts \
    /vendor_seapp_contexts \
    /vendor_service_contexts \
    /vndservice_contexts \
%{nil}

%define additional_post_scripts \
/usr/bin/groupadd-user media_rw || :\
%{nil}
 
%define android_config \
#define WANT_ADRENO_QUIRKS 1\
%{nil}

%define makefstab_skip_entries /dev/stune /dev/cpuset /sys/fs/pstore /dev/cpuctl

%include rpm/dhd/droid-hal-device.inc
