This is a test package for debugging an issue with using X-Sendfile
over HTTPS with mod_wsgi.

## Installation

```
git clone https://github.com/jhpyle/testxsendfile
pip install --upgrade ./testxsendfile/
```

Sample Apache configuration:

```
<IfModule mod_ssl.c>
    <VirtualHost *:443>
        ServerAdmin webmaster@localhost
        ServerName test54.docassemble.org
        SSLEngine on
        SSLCertificateFile /etc/letsencrypt/live/test54.docassemble.org/fullchain.pem
        SSLCertificateKeyFile /etc/letsencrypt/live/test54.docassemble.org/privkey.pem 
        XSendFile on
        XSendFilePath /usr
        XSendFilePath /tmp
        WSGIDaemonProcess testxsendfile user=www-data group=www-data threads=5
        WSGIScriptAlias / /home/admin/testxsendfile/testxsendfile.wsgi
        <Directory /home/admin/testxsendfile>
            WSGIProcessGroup testxsendfile
            WSGIApplicationGroup %{GLOBAL}
            AllowOverride none
            Require all granted
        </Directory>
        ErrorLog /var/log/apache2/error.log
        CustomLog /var/log/apache2/access.log combined
    </VirtualHost>
</IfModule>
```

## Testing environment

Debian stretch:

```
/home/admin# cat /etc/os-release 
PRETTY_NAME="Debian GNU/Linux 9 (stretch)"
NAME="Debian GNU/Linux"
VERSION_ID="9"
VERSION="9 (stretch)"
ID=debian
HOME_URL="https://www.debian.org/"
SUPPORT_URL="https://www.debian.org/support"
BUG_REPORT_URL="https://bugs.debian.org/"
```

Single CPU:

```
/home/admin# cat /proc/cpuinfo 
processor	: 0
vendor_id	: GenuineIntel
cpu family	: 6
model		: 63
model name	: Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
stepping	: 2
microcode	: 0x36
cpu MHz		: 2400.112
cache size	: 30720 KB
physical id	: 0
siblings	: 1
core id		: 0
cpu cores	: 1
apicid		: 0
initial apicid	: 0
fpu		: yes
fpu_exception	: yes
cpuid level	: 13
wp		: yes
flags		: fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx rdtscp lm constant_tsc rep_good nopl xtopology eagerfpu pni pclmulqdq ssse3 fma cx16 pcid sse4_1 sse4_2 x2apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand hypervisor lahf_lm abm fsgsbase bmi1 avx2 smep bmi2 erms invpcid xsaveopt
bugs		:
bogomips	: 4800.12
clflush size	: 64
cache_alignment	: 64
address sizes	: 46 bits physical, 48 bits virtual
power management:
```

Apache 2.4.25:

```
/home/admin# apache2ctl -V
Server version: Apache/2.4.25 (Debian)
Server built:   2017-07-18T18:37:33
Server's Module Magic Number: 20120211:68
Server loaded:  APR 1.5.2, APR-UTIL 1.5.4
Compiled using: APR 1.5.2, APR-UTIL 1.5.4
Architecture:   64-bit
Server MPM:     event
  threaded:     yes (fixed thread count)
    forked:     yes (variable process count)
Server compiled with....
 -D APR_HAS_SENDFILE
 -D APR_HAS_MMAP
 -D APR_HAVE_IPV6 (IPv4-mapped addresses enabled)
 -D APR_USE_SYSVSEM_SERIALIZE
 -D APR_USE_PTHREAD_SERIALIZE
 -D SINGLE_LISTEN_UNSERIALIZED_ACCEPT
 -D APR_HAS_OTHER_CHILD
 -D AP_HAVE_RELIABLE_PIPED_LOGS
 -D DYNAMIC_MODULE_LIMIT=256
 -D HTTPD_ROOT="/etc/apache2"
 -D SUEXEC_BIN="/usr/lib/apache2/suexec"
 -D DEFAULT_PIDLOG="/var/run/apache2.pid"
 -D DEFAULT_SCOREBOARD="logs/apache_runtime_status"
 -D DEFAULT_ERRORLOG="logs/error_log"
 -D AP_TYPES_CONFIG_FILE="mime.types"
 -D SERVER_CONFIG_FILE="apache2.conf"
```
