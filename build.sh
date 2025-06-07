#!/bin/bash
rm -rf build dist renaming.spec
pyinstaller --onefile renaming.py
