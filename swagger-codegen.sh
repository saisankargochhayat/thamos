#!/usr/bin/env bash
# Generate swagger client from Thoth's swagger specification for Thamos.
# Fridolin Pokorny <fridolin.pokorny@gmail.com>
#
# This file automates generation of the swagger client and makes it reproducible. Run this
# file to automatically generate Python swagger client for interacting with Thoth from Thamos.

set -ex

THOTH_SWAGGER_YAML=${1:-'https://raw.githubusercontent.com/thoth-station/user-api/master/thoth_user_api/swagger.yaml'}

function die() {
    echo $@ 1>&2
    exit 1
}

which which > /dev/null || die "Please install which command to continue"
which git > /dev/null   || die "Please install git to continue"
which mvn > /dev/null   || die "Please install maven to continue"
which java > /dev/null  || die "Please install java to continue"
which find > /dev/null  || die "Please install find utility to continue"


if [ ! -d 'swagger-codegen' ]; then
    git clone https://github.com/swagger-api/swagger-codegen
    pushd swagger-codegen
    mvn clean package
    popd
fi


rm -rf swagger-codegen-output/
java -jar swagger-codegen/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar generate \
    -i "${THOTH_SWAGGER_YAML}" \
    -l python \
    -o swagger-codegen-output/ \
    -c swagger-codegen.json

rm -rf thamos/swagger_client
cp -r swagger-codegen-output/thamos/swagger_client/ thamos/swagger_client
# There is a bug in swagger-codegen - it does not respect sub-package for some files, this is a simple workaround.
find swagger-codegen-output/thamos.swagger_client/ -iname '*.py' -exec sed -i 's/^from thoth/from thamos.swagger_client.thoth/' {} \+
cp -r swagger-codegen-output/thamos.swagger_client/* thamos/swagger_client
cp -r swagger-codegen-output/docs Documentation
