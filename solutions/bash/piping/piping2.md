# Piping Exercises Part 1

[vsftpd.log](../../../exercises/bash/piping/vsftpd.log


## How many different IP-addresses have tried to connect?
```console
$ cut -d\" -f2 vsftpd.log | sort -u | wc -l
```

## From which IP-addresses where hacking attacks probably started?
```console
$ cut -d\" -f2 vsftpd.log | sort | uniq -c | sort -nr
```

## Which 2 usernames were most frequently used and how often?
```console
$ cut -d"[" -f3 vsftpd.log | cut -d"]" -f1 | sort | uniq -c | sort -nr | head -2
```

## How many failed logins were tried from 213.114.38.100?
```console
$ grep "FAIL.*213\.114\.38\.100" vsftpd.log | wc -l
```