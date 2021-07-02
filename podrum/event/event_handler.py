#########################################################                        
#  ____           _                                     #
# |  _ \ ___   __| |_ __ _   _ _ __ ___                 #
# | |_) / _ \ / _` | '__| | | | '_ ` _ \                #
# |  __/ (_) | (_| | |  | |_| | | | | | |               #
# |_|   \___/ \__,_|_|   \__,_|_| |_| |_|               #
#                                                       #
# Copyright 2021 Podrum Team.                           #
#                                                       #
# This file is licensed under the GPL v2.0 license.     #
# The license file is located in the root directory     #
# of the source code. If not you may not use this file. #
#                                                       #
#########################################################


from typing import Callable

class event_handler:
    events: dict = {}
  
    @staticmethod
    def register_listener(event_name: str, listener: Callable) -> None:
        event_handler.events[event_name].append(listener)
        
    @staticmethod
    def remove_listener(listener: Callable) -> None:
        event_handler.events[event_name].remove(listener)
        
    @staticmethod
    def get_listeners(event_name: str) -> list
        return event_handler.events[event_name]
