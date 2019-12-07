import os

from roboter import roboko

if __name__ == '__main__':
    roboko = roboko.Roboko()
    roboko.customer_name_check()
    roboko.recommend()
    roboko.hearing()
    roboko.say_goodbye()