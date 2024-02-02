# -*- coding: utf-8 -*-
from controller import FakeCsvReaderController

import sys

if __name__ == "__main__":
    csv_path = sys.argv[1]
    print(FakeCsvReaderController().convert(csv_path))