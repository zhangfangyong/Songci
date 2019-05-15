# coding: UTF-8
import data
import model

import argparse

Str = ""
def defineArgs():
    """define args"""
    parser = argparse.ArgumentParser(description = "Chinese_poem_generator.")
    parser.add_argument("-m", "--mode", help = "select mode by 'train' or test or head",
                        choices = ["train", "test", "head"], default = "test")
    return parser.parse_args()

def main(trainPoems,checkpointsPath):
    global Str
    args = defineArgs()
    trainData = data.POEMS(trainPoems)
    MCPangHu = model.MODEL(trainData)
    if args.mode == "train":
        MCPangHu.train()
    else:
        if args.mode == "test":
            poems = MCPangHu.test(checkpointsPath)
            Str = MCPangHu.Get_Str()
        else:
            characters = input("please input chinese character:")
            poems = MCPangHu.testHead(characters)

def main_Get_str():
    global Str
    return Str