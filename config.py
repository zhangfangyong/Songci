# coding: UTF-8
batchSize = 200

learningRateBase = 0.001
learningRateDecayStep = 1000
learningRateDecayRate = 0.95

epochNum = 200          # train epoch
generateNum = 1                 # number of generated poems per time

type ="水调歌头"               # dataset to use, shijing, songci, etc

trainPoems = "D:/Download/Chinese_poem_generator-master/dataset/songci/" + type + ".txt" # training file location
checkpointsPath = "D:/Download/Chinese_poem_generator-master/checkpoints/"+type # checkpoints location
evaluateCheckpointsPath = "D:/Download/Chinese_poem_generator-master/checkpoints/"+type


saveStep = 100                # save model every savestep

# evaluate
trainRatio = 0.95                   # train percentage
