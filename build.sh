#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

mkdir -p ./{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cp stub_http_server.js stub_http_server.service SOURCES
spectool -g -C SOURCES stub_http_server.spec
rpmbuild --quiet --define "_topdir `pwd`" -bb stub_http_server.spec
