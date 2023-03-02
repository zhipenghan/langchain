"""Util that calls Graph Search.

"""
from typing import Dict, List

import requests
from pydantic import BaseModel, Extra, root_validator

from langchain.utils import get_from_dict_or_env


class GraphSearchAPIWrapper(BaseModel):
    """Wrapper for Graph Search API.

    https://developer.microsoft.com/en-us/graph/graph-explorer
    """

    graph_search_key: str
    graph_search_url: str

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def _graph_search_results(self) -> any:
        headers = {"Authorization": f"Bearer {self.graph_search_key}"}
        response = requests.get(
            self.graph_search_url, headers=headers, params=None  # type: ignore
        )
        response.raise_for_status()
        search_results = response.json()

        return search_results["displayName"]

    @root_validator(pre=True)
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and endpoint exists in environment."""
        graph_search_key = get_from_dict_or_env(
            values,
            "graph_search_key",
            "GRAPH_SEARCH_KEY"
        )
        values["graph_search_key"] = graph_search_key

        graph_search_url = get_from_dict_or_env(
            values,
            "graph_search_url",
            "GRAPH_SEARCH_URL",
            default="https://graph.microsoft.com/v1.0/me/people",
        )
        values["graph_search_url"] = graph_search_url

        return values

    def run_manager(self, peo: str) -> str:
        """Run query through BingSearch and parse result."""
        snippets = []
        result = self._graph_search_results()
        if len(result) == 0:
            return "Xuan Li"

        return result

    def results(self, query: str, num_results: int) -> List[Dict]:
        """Run query through BingSearch and return metadata.

        Args:
            query: The query to search for.
            num_results: The number of results to return.

        Returns:
            A list of dictionaries with the following keys:
                snippet - The description of the result.
                title - The title of the result.
                link - The link to the result.
        """
        metadata_results = []
        results = self._bing_search_results(query, count=num_results)
        if len(results) == 0:
            return [{"Result": "No good Bing Search Result was found"}]
        for result in results:
            metadata_result = {
                "snippet": result["snippet"],
                "title": result["name"],
                "link": result["url"],
            }
            metadata_results.append(metadata_result)

        return metadata_results
