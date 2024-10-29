import asyncio

from core.solvers import *
from utils import load_config, FileOperations

config = load_config()

# Initialize the captcha solver based on the selected captcha module
captcha_solver = (
    TwoCaptchaImageSolver(config.two_captcha_api_key)
    if config.captcha_module == "2captcha"
    else AntiCaptchaImageSolver(config.anti_captcha_api_key)
)

file_operations = FileOperations()
semaphore = asyncio.Semaphore(config.threads)
