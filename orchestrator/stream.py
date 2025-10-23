import polars as pl
import asyncio

class Stream:
    def __init__(self):
        self.mapping = {"csv":pl.read_csv, "json":pl.read_json,"excel":pl.read_excel}
        self.filter_mapping = {"equals":"==", "not_equals":"!=", "greater_than":">", "less_than":"<"}
       
    async def read_data(self, file_path: str) -> pl.DataFrame:
        file_ends_with = file_path.split(".")[-1]
        df = self.mapping[file_ends_with](file_path)
        return df
    async def filter_data(self,df,filter_column, filter_value , filter_type):
        df_str  = f"df.filter(pl.col('{filter_column}') {self.filter_mapping[filter_type]} {filter_value})"
        df = eval(df_str, {"df": df, "pl": pl})
        return df
    
if __name__ == "__main__":
    dataframe = {"name": [1, 2, 3], "age": [4, 5, 6],"city": ["a", "b", "c"]}
    stream = Stream()
    df = asyncio.run( stream.filter_data(pl.DataFrame(dataframe),"name",1,"less_than"))
    print(df)
