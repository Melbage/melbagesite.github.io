
    #!/bin/bash
    # 
    cd /Users/paulcarter/Documents/melbageWebsite/Live/melbagesite.github.io/mgaData/RAW
    #ListOfFile = `wcl -l *.htm`
    for i in `ls *.htm`
    do 
        if [`wc -l <$i` == 224 ] 
        then
            echo "$i is 224"
            mv $i 224
        elif [`wc -l <$i` -eq 223 ] 
        then
            echo "$i is 233"
            mv $i 223
        else 
            echo "$i Other"
            mv $i other
        fi
    done
