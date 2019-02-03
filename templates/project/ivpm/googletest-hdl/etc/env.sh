#****************************************************************************
#* {{name}}_env.sh
#*
#* Environment setup script for {{name}}
#****************************************************************************
{% set filename = "etc/{{name}}_env.sh" %}

etc_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd)"
rootdir=`cd $etc_dir/.. ; pwd`

{% if rootvar != "" %}
{{rootvar}}=${rootdir}
export {{rootvar}}
{% endif %}

# Add a path to the simscripts directory
export PATH=$rootdir/packages/simscripts/bin:$PATH

# Force the PACKAGES_DIR
export PACKAGES_DIR=$rootdir/packages

