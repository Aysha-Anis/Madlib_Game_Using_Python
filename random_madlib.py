from sample_madlib import bird , dragon , fairy , princess
import random

def main():
    choose = random.choice([bird,dragon,fairy,princess])
    choose.display()



if __name__=='__main__':
    main()