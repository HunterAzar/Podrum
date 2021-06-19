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

import asyncio
import importlib
import json
import os
import sys
from version import version
from zipfile import ZipFile

class plugin_manager:
    def __init__(self, server: object) -> None:
        self.server: object = server
        self.plugins: dict = {}
        
    def load(self, path: str) -> None:
        plugin_file = ZipFile(path, "r")
        plugin_info: dict = json.loads(plugin_file.read("info.json"))
        if plugin_info["name"] in self.plugins:
            self.server.logger.alert(f"A plugin with the name {plugin_info['name']} already exists.")
            return
        if plugin_info["api_version"] != version.podrum_api_version:
            self.server.logger.alert(f"A plugin with the name {plugin_info['name']} could not be loaded due to incompatible api version ({plugin_info['api_version']}).")
            return
        self.server.logger.info(f"Loading {plugin_info['name']}...")
        sys.path.append(path)
        main: str = plugin_info["main"].rsplit(".", 1)
        module: object = importlib.import_module(main[0])
        main_class: object = getattr(module, main[1])
        self.plugins[plugin_info["name"]]: object = main_class()
        self.plugins[plugin_info["name"]].server: object = self.server
        self.plugins[plugin_info["name"]].path: str = path
        self.plugins[plugin_info["name"]].version: str = plugin_info["version"] if "version" in plugin_info else ""
        self.plugins[plugin_info["name"]].description: str = plugin_info["description"] if "description" in plugin_info else ""
        self.plugins[plugin_info["name"]].author: str = plugin_info["author"] if "author" in plugin_info else ""
        if hasattr(main_class, "on_load"):
            self.plugins[plugin_info["name"]].on_load()
        self.server.logger.success(f"Successfully loaded {plugin_info['name']}.")
        
    async def load_all(self, path: str) -> None:
        for top, dirs, files in os.walk(path):
            for file_name in files:
                full_path: str = os.path.abspath(os.path.join(top, file_name))
                if full_path.endswith(".pyz") or full_path.endswith(".zip"):
                    self.load(full_path)
                asyncio.sleep(0.0001)
        
    def unload(self, name: str) -> None:
        if name in self.plugins:
            if hasattr(self.plugins[name], "on_unload"):
                self.plugins[name].on_unload()
            del self.plugins[name]
            self.server.logger.info(f"Unloaded {name}.")
            
    async def unload_all(self) -> None:
        for name in dict(self.plugins):
            self.unload(name)
            asyncio.sleep(0.0001)
                                   
    def reload(self, name: str) -> None:
        if name in self.plugins:
            path: str = self.plugins[name].path
            self.unload(name)
            self.load(path)
                                   
    async def reload_all(self) -> None:
        for name in dict(self.plugins):
            self.reload(name)
            asyncio.sleep(0.0001)
