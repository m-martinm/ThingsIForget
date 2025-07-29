import re
from pathlib import Path
from typing import Union, List
from dataclasses import dataclass


@dataclass
class RecordLayout:
    @dataclass
    class Element:
        element_type: str
        offset: int
        data_type: str
        layout: str | None
        access: str | None

    name: str
    elements: List[Element]


@dataclass
class Characteristic:
    identifier: str
    long_identifier: str
    characteristic_type: str
    ecu_address: int
    record_layout: str
    max_diff: float
    conversion_method: str
    lower_limit: float
    upper_limit: float


class A2LExtractor:
    CHARACTERISTIC_BODY = re.compile(
        r"/\s*begin\s+CHARACTERISTIC(.*?)/\s*end\s+CHARACTERISTIC",
        re.DOTALL,
    )
    RECORD_LAYOUT_BODY = re.compile(
        r"/\s*begin\s+RECORD_LAYOUT(.*?)/\s*end\s+RECORD_LAYOUT",
        re.DOTALL,
    )

    CHARACTERISTIC_PARTS = re.compile(
        r"\s*(?P<identifier>[^\s]+)"
        r"\s+\"(?P<long_identifier>[^\"]*)\""
        r"\s+(?P<characteristic_type>\w+)"
        r"\s+(?P<ecu_address>(?:0x|0X)[0-9a-fA-F]+)"
        r"\s+(?P<record_layout>\w+)"
        r"\s+(?P<max_diff>-?\d+(?:\.\d+)?)"
        r"\s+(?P<conversion_method>\w+)"
        r"\s+(?P<lower_limit>-?\d+(?:\.\d+)?)"
        r"\s+(?P<upper_limit>-?\d+(?:\.\d+)?)"
    )

    RECORD_LAYOUT_NAME = re.compile(r"\s*(\w+)\s+")

    RECORD_LAYOUT_ELEMENT = re.compile(
        r"\s*(?P<element_type>\w+)"
        r"\s+(?P<offset>\d+)"
        r"\s+(?P<data_type>UBYTE|SBYTE|UWORD|SWORD|ULONG|SLONG|A_UINT64|A_INT64|FLOAT32_IEEE|FLOAT64_IEEE)"
        r"(?:\s+(?P<layout>INDEX_INCR|COLUMN_DIR|ROW_DIR))?"
        r"(?:\s+(?P<access>DIRECT|LOOKUP))?"
    )

    def __init__(self, filepath: Union[str, Path]) -> None:
        self.filepath = filepath
        self.record_layouts = dict()
        self.characteristics = dict()

    def parse(self):
        fp = open(self.filepath, "r", errors="ignore")
        content = fp.read()
        fp.close()

        self._parse_record_layouts(content)
        self._parse_characteristics(content)

    def _parse_record_layouts(self, content: str):
        for body in re.finditer(self.RECORD_LAYOUT_BODY, content):
            body = body.group(1)
            name = re.search(self.RECORD_LAYOUT_NAME, body)
            if name is not None:
                name, left = name.group(1), name.span(1)
                body = body[left[1] :]
                elements = list(
                    filter(
                        lambda e: e is not None,
                        map(
                            lambda m: m.groupdict() if m is not None else None,
                            (map(lambda line: re.search(self.RECORD_LAYOUT_ELEMENT, line), body.strip().splitlines())),
                        ),
                    )
                )
                self.record_layouts[name] = elements

    def _parse_characteristics(self, content: str):
        for body in re.finditer(self.CHARACTERISTIC_BODY, content):
            body = body.group(1)
            parts = re.search(self.CHARACTERISTIC_PARTS, body)
            if parts is not None:
                entry = parts.groupdict()
                name = entry.pop("identifier")
                self.characteristics[name] = entry
