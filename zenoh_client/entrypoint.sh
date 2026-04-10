#!/bin/ash
#Current_Wifi=$( iwgetid -r )

#case "$Current_Wifi" in
#    "LINKS-GUEST")

	./zenoh-bridge-ros2dds -c /zenoh_config_links_guest.json

#        ;;
#    "zeppelin-test" | "pattern3")
#
#	./zenoh-bridge-ros2dds -c /zenoh_config_zeppelin.json

#        ;;
#    *)
#        ;;
#esac


