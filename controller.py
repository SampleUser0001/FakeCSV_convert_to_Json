# -*- coding: utf-8 -*-
import tempfile
import pandas as pd
from enums import TypeEnum

class FakeCsvReaderController():
    def __init__(self):
        self.origin_format = TypeEnum.get_empty_dict()

    def convert(self, filepath:str) -> dict:
        """ CSVもどきを読み込んで、Enumに対応するdictに変換する。
        Args:
            filepath (str): ファイルパス
        
        Returns:
            dict: Enumに対応するdict
        """
        return self._convert_origin(self._read_origin(filepath))

    def _read_origin(self, filepath:str) -> dict:
        """ CSVもどきを読み込んで、Enumに対応するdictに変換する。
        Args:
            filepath (str): ファイルパス
        
        Returns:
            dict: Enumに対応するdict
        """

        with open('data.csv', 'r', ) as file:
            read_flag = None
            for line in file:
                # 改行コードを削除
                line = line.strip()

                if line in [e.name for e in TypeEnum]:
                    # 次以降の行にどのパターンが来るかを判定するためのフラグ
                    read_flag = line
                else:
                    if read_flag is not None:
                        
                        # CSVのまま一度出力するので、split不要。
                        if self.origin_format[read_flag]["header"] is None:
                            self.origin_format[read_flag]["header"] = line
                        else:
                            self.origin_format[read_flag]["data"].append(line)
                    else:
                        # 想定外のパターン
                        raise ValueError("Invalid file format, " + line)

    def _convert_origin(self, origin_format:dict) -> dict:
        """read_originの結果を項目ごとのdictに変換する。
        Args:
            origin_format (dict): Enumに対応するdict
        
        Returns:
            dict: Enumに対応するdict
        """
        return_dict = {}
        for e in TypeEnum:
            with tempfile.NamedTemporaryFile() as fp:
                # 一時ファイル(CSV)作成
                with open(fp.name, 'w') as file:
                    file.write(self.origin_format[e.name]["header"] + '\n')
                    for line in self.origin_format[e.name]["data"]:
                        file.write(line + '\n')

                # 一時ファイル(CSV)を読み込んでdictに変換
                d = pd.read_csv(fp.name).to_dict(orient='records')

                return_dict[e] = d

        return return_dict
