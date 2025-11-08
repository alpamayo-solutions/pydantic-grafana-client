from typing import Any, Mapping, Union

from ...models import AlertRuleModel
from ..base import Base


class Alerting(Base):
    def __init__(self, client):
        super(Alerting, self).__init__(client)
        self.client = client

    async def get_alertrule(self, folder_name: str, alertrule_name: str) -> dict:
        """
        :param folder_name:
        :param alertrule_name:
        :return:
        """
        get_alertrule_path = "/ruler/grafana/api/v1/rules/%s/%s" % (folder_name, alertrule_name)
        return await self.client.GET(get_alertrule_path)

    async def get_managedalerts_all(self, datasource: str = "grafanacloud-prom") -> dict:
        """ """
        get_managedalerts_path = "/prometheus/%s/api/v1/rules" % datasource
        return await self.client.GET(get_managedalerts_path)

    async def create_alertrule(self, folder_name: str, alertrule: Union[AlertRuleModel, Mapping[str, Any]]) -> dict:
        """
        :param folder_name:
        :param alertrule:
        :return:
        """
        payload = AlertRuleModel.validate(alertrule).to_payload()
        create_alertrule_path = "/ruler/grafana/api/v1/rules/%s" % folder_name
        return await self.client.POST(create_alertrule_path, json=payload)

    async def update_alertrule(self, folder_name: str, alertrule: Union[AlertRuleModel, Mapping[str, Any]]) -> dict:
        """
        @param folder_name:
        @param alertrule:
        @return:
        """

        payload = AlertRuleModel.validate(alertrule).to_payload()
        update_alertrule_path = "/ruler/grafana/api/v1/rules/%s" % folder_name
        return await self.client.POST(update_alertrule_path, json=payload)

    async def delete_alertrule(self, folder_name: str, alertrule_name: str) -> dict:
        """
        :param folder_name:
        :param alertrule_name:
        @return:
        """

        delete_alertrule_path = "/ruler/grafana/api/v1/rules/%s/%s" % (folder_name, alertrule_name)
        return await self.client.DELETE(delete_alertrule_path)
