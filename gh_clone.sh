#~/bin/env bash
ORG=https://github.com/ACC-COSC2325-001-SU17

declare -a labs=("homework"
                 "lab1-memory-unit"
                 "lab2-alu-unit"
                 "lab3-control-unit"
                 "lab4-numberconversion"
                )

while read -r  f l u; do
    if [[ $f = *[!\ ]* ]]; then
        mkdir -p "$f-$l"
            for a in "${labs[@]}"; do
                git clone "$ORG/$a-$u" "_repos/$f-$l/$a-$u"
            done
    fi
done < repo_names.txt

