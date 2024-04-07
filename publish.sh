if [ -z "$1" ]; then 
    echo "commit message is blank"
    exit 1
fi

rm -rf output/

pelican

ghp-import -p -m "\"$1\"" output/
