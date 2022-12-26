from vega_datasets import data

def getDatasetNames() -> list:
    return data.list_datasets()

def getDataFrameByDatasetName(name: str):
    name = name.replace('-', '_')
    return getattr(data, name)()