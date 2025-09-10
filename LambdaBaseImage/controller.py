#!/usr/bin/env python
import sys
import importlib
import importlib.util

def lazy_load_module(module_name:str):
    spec = importlib.util.find_spec(module_name)
    assert spec is not None
    assert spec.loader is not None
    loader = importlib.util.LazyLoader(spec.loader)
    spec.loader = loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    loader.exec_module(module)
    return module

def module_has_function(module, function_name):
    return hasattr(module, function_name)

def main():
    user_module = lazy_load_module('user')
    has_handler = module_has_function(user_module, 'handler')
    assert has_handler
    handler_function = user_module.handler
    handler_function()
    ...

if __name__ == '__main__':
    main()