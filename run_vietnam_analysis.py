#!/usr/bin/env python
"""
Script chạy phân tích dân số Vietnam sử dụng pypopRF
"""

import os
import sys
from pathlib import Path

# Set working directory
os.chdir(Path(__file__).parent / 'my_project')

# Chạy phân tích với config.yaml
if __name__ == '__main__':
    from pypoprf.utils.logger import get_logger
    import subprocess
    
    logger = get_logger()
    config_file = 'config.yaml'
    
    logger.info("="*60)
    logger.info("Chạy phân tích dân số Vietnam với pypopRF")
    logger.info("="*60)
    logger.info(f"Config file: {config_file}")
    logger.info(f"Working directory: {os.getcwd()}")
    
    # Chạy CLI command
    cmd = ['pypoprf', 'run', '-c', config_file, '-v']
    logger.info(f"Command: {' '.join(cmd)}")
    logger.info("="*60)
    
    result = subprocess.run(cmd)
    sys.exit(result.returncode)
