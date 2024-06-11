from typing import Any

from airflow.models.baseoperator import BaseOperator

from .hook import BrawlStatsHook


class BrawlStatsOperator(BaseOperator):
    def __init__(
            self,
            player_tag: str,
            conn_id: str = 'brawl_stats_conn_id',
            **kwargs) -> None:
        super().__init__(**kwargs)
        self.conn_id = conn_id
        self.player_tag = player_tag

    def execute(self, context: Any) -> str:
        """
        Get player trophies from BrawlStatsHook

        :param context:
        :return:
        """
        api = BrawlStatsHook(self.conn_id)
        return api.get_trophies(self.player_tag)
