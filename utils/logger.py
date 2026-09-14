import logging

def get_logger(name: str = "scanner", level: int = logging.INFO, log_file: str = None) -> logging.Logger:
    """
    Configure and return a logger instance.

    Args:
        name (str): Name of the logger (default: "scanner").
        level (int): Logging level (default: logging.INFO).
        log_file (str): Optional file path to also log messages.

    Returns:
        logging.Logger: Configured logger object.
    """
    logger = logging.getLogger(name)

    if not logger.handlers:  # Prevent duplicate handlers if called multiple times
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Console handler
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Optional file handler
        if log_file:
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)

        logger.setLevel(level)

    return logger


