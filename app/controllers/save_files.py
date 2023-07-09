from dataclasses import dataclass
from datetime import datetime
import re
import os


@dataclass
class Backup:
    name: str
    path: str
    data: datetime
    ...
    
    
