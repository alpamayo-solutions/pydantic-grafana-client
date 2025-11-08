from typing import Any, Mapping, Union

from ...models import (
    AdminChangePassword,
    AdminChangePermissions,
    AdminCreateUser,
    AdminPauseAlerts,
)
from ..base import Base


class Admin(Base):
    def __init__(self, client):
        super(Admin, self).__init__(client)
        self.client = client

    async def settings(self):
        """

        :return:
        """
        path = "/admin/settings"
        return await self.client.GET(path)

    async def stats(self):
        """

        :return:
        """
        path = "/admin/stats"
        return await self.client.GET(path)

    async def create_user(self, user: Union[AdminCreateUser, Mapping[str, Any]]) -> dict:
        """

        :param user:
        :return:
        """
        payload = AdminCreateUser.validate(user).to_payload()
        create_user_path = "/admin/users"
        return await self.client.POST(create_user_path, json=payload)

    async def change_user_password(self, user_id: int, password: str) -> dict:
        """

        :param user_id:
        :param password:
        :return:
        """
        payload = AdminChangePassword.validate({"password": password}).to_payload()
        change_user_password_path = "/admin/users/%s/password" % user_id
        return await self.client.PUT(change_user_password_path, json=payload)

    async def change_user_permissions(self, user_id: int, is_grafana_admin: bool) -> dict:
        """

        :param user_id:
        :param is_grafana_admin:
        :return:
        """
        payload = AdminChangePermissions.validate({"isGrafanaAdmin": is_grafana_admin}).to_payload()
        change_user_permissions = "/admin/users/%s/permissions" % user_id
        return await self.client.PUT(change_user_permissions, json=payload)

    async def delete_user(self, user_id: int) -> dict:
        """

        :param user_id:
        :return:
        """
        delete_user_path = "/admin/users/%s" % user_id
        return await self.client.DELETE(delete_user_path)

    async def pause_all_alerts(self, pause: Union[bool, str]) -> dict:
        """

        :param pause:
        :return:
        """
        payload = AdminPauseAlerts.validate({"paused": pause}).prepare_payload()
        change_user_permissions = "/admin/pause-all-alerts"
        return await self.client.POST(change_user_permissions, json=payload)

    async def set_user_enabled(self, user_id: int, enabled: bool) -> dict:
        """

        :param user_id:
        :param enabled:
        :return:
        """
        action = "enable" if enabled else "disable"
        set_user_enabled = "/admin/users/%s/%s" % (user_id, action)
        return await self.client.POST(set_user_enabled)
