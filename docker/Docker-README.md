# Docker file for VTC based on a pytorch image

following the instructions at `https://github.com/LAAC-LSCP/VTC/blob/main/README.md`

This is an experiment to see if I can get an interactive version working, followed by a set of scripts that throw inference data at the model.

### build the container

        docker build -t test.2 .

### run the container interactively

        docker run -it -v /media/joe/slepnir1/Datasets/ALSSA/VanDam-5minute/WAV:/home/inference/inputs \
         -v /media/joe/slepnir1/Datasets/ALSSA/VanDam-5minute/VTC-inferred:/home/inference/outputs --name VTC2 test.2 



