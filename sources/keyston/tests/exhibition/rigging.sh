# source ${0%/*}/rigging.sh || exit 70
__top=${0%/*}/../..
export PATH="${__top}/check/bin:${__top}/bin:$PATH"
exe=exhibition
name=${0##*/} ; name=${name%.test}
