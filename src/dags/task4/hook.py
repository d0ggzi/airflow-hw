import requests
from airflow.exceptions import AirflowException
from airflow.hooks.base import BaseHook


class BrawlStatsHook(BaseHook):
    def __init__(self, bs_conn_id: str):
        super().__init__()
        self.conn_id = bs_conn_id

    def get_trophies(self, player_tag: str) -> str:
        """
        Get player's trophies by player tag.

        :param player_tag:
        :return: amount of trophies
        """
        host = self._get_host()
        api_key = self._get_api_key()
        url = f"{host}/players/%23{player_tag}"
        response = requests.get(url, headers={'Authorization': f"Bearer {api_key}"})
        response.raise_for_status()
        return response.json()['trophies']

    def _get_api_key(self) -> str:
        """
        Get API-key from airflow connections.

        :return: API-key
        """
        conn = self.get_connection(self.conn_id)
        if not conn.password:
            raise AirflowException('Missing API key (password) in connection settings')
        return conn.password

    def _get_host(self) -> str:
        """
        Get host from airflow connections.

        :return: API host
        """
        conn = self.get_connection(self.conn_id)
        if not conn.host:
            raise AirflowException('Missing HOST in connection settings')
        return conn.host
