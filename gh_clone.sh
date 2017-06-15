ORG=COSC2325-001-SU17

declare -a labs=("homework"
                 "lab1-memory-unit"
                )


for l in "${labs[@]}"
do
    echo "$l"
done


while read -r  f l u; do
    mkdir -p "$f-$l"
    for a in "${labs[@]}"; do
        echo "$a-$u"
    done
done < repo_names.txt

