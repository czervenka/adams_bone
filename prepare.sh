url="www.adamova-kost.cz"
title="Adamova kost"
slug="kost"
package="kost"

cd "$(dirname $0)"

for itm in url title slug package; do
    searchfor="adams_bone_$itm"
    eval replaceby="\$$itm"
    find -type f -a \( -name '*.py' -o -name '*.html' -o -name '*.json' \) -exec sed -i "s|$searchfor|$replaceby|g" {} \;
done
