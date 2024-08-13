from pathlib import Path
from typing import List

from pydantic import BaseModel, Field


class KgHgConfigurations(BaseModel):
    """
    Class for defining the kghg configurations in tool_specific_configurations field,
    within the input_dir config.yaml
    Args:
        environment (str): Environment to run kghg, i.e., local/docker (only local supported)
        path_to_kghg (str): File path to kghg.py 
        path_to_nodes (str): File path to monarch-kg_nodes.tsv
        path_to_edges (str): File path to monarch-kg_edges.tsv
    """

    environment: str = Field(...)
    path_to_kghg: str = Field(...)
    path_to_nodes: str = Field(...)
    path_to_edges: str = Field(...)