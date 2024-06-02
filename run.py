#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# vim: set et sw=4 ts=4 sts=4 ff=unix fenc=utf8:
# Author: Binux<roy@binux.me>
#         http://binux.me
# Created on 2014-11-24 23:11:49

from pyspider.run import main

if __name__ == '__main__':
    # import cProfile
    # import pstats
    # import sys
    # profiler = cProfile.Profile()
    # try:
    #     profiler.enable()
    #     main()
    # except KeyboardInterrupt:
    #     pass
    # finally:
    #     profiler.disable()
    #     stats = pstats.Stats(profiler).sort_stats('cumtime')
    #     stats.dump_stats('profile.stats')
    #     print("Профильные данные сохранены в 'profile.stats'")

    main()