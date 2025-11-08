from ...models import DatasourcePermissionUpdateModel, TeamRoleAssignmentModel, TeamRolesReplaceModel
from ..base import Base


class Rbac(Base):
    def __init__(self, client):
        super(Rbac, self).__init__(client)
        self.client = client

    async def get_rbac_roles_all(self):
        """
        The Rbac is only available in Grafana Enterprise.

        :return:
        """
        roles_path = "/access-control/roles"
        return await self.client.GET(roles_path)

    async def add_rbac_role_team(self, team_id, role_uid):
        """
        The Rbac is only available in Grafana Enterprise.

        :param team_id:
        :param role_uid:
        :return:
        """
        payload = TeamRoleAssignmentModel.validate({"roleUid": role_uid}).to_payload()
        role_team_path = "/access-control/teams/%s/roles" % team_id
        return await self.client.POST(role_team_path, json=payload)

    async def add_rbac_roles_team(self, team_id, role_uids):
        """
        The Rbac is only available in Grafana Enterprise.

        :param team_id:
        :param role_uids:
        :return:
        """
        payload = TeamRolesReplaceModel.validate({"roleUids": role_uids}).to_payload()
        role_team_path = "/access-control/teams/%s/roles" % team_id
        return await self.client.PUT(role_team_path, json=payload)

    async def remove_rbac_role_team(self, team_id, role_uid):
        """
        The Rbac is only available in Grafana Enterprise.

        :param team_id:
        :param role_uid:
        :return:
        """
        role_team_path = "/access-control/teams/%s/roles/%s" % (team_id, role_uid)
        return await self.client.DELETE(role_team_path)

    async def get_rbac_datasources(self, datasource_uid):
        """
        Gets all existing permissions for the data source with the given uid

        The Rbac is only available in Grafana Enterprise.
        This API works only with grafana version > 10.2.3.

        :param datasource_uid:
        :return:
        """
        datasource_path = "/access-control/datasources/%s" % datasource_uid
        return await self.client.GET(datasource_path)

    async def set_rbac_datasources_teams(self, datasource_uid, team_id, permission):
        """
        Sets team permission for the data source with the given uid.

        the values allowed for the permission argument are :
        Query, Edit, or Admin.
        To remove a permission, set the permission argument to an empty string.
        The Rbac is only available in Grafana Enterprise.
        This API works only with grafana version > 10.2.3.

        :param datasource_uid:
        :param team_id:
        :param permission:
        :return:
        """
        payload = DatasourcePermissionUpdateModel.validate({"permission": permission}).to_payload()
        datasource_path = "/access-control/datasources/%s/teams/%s" % (datasource_uid, team_id)
        return await self.client.POST(datasource_path, json=payload)

    async def set_rbac_datasources_builtin_roles(self, datasource_uid, builtin_role, permission):
        """
        Sets permission for the data source with the given uid to all users who
        have the specified basic role.

        the values allowed for the builtin_role argument are :
        Admin, Editor or Viewer
        the values allowed for the permission argument are :
        Query, Edit, or Admin.
        To remove a permission, set the permission argument to an empty string.
        The Rbac is only available in Grafana Enterprise.
        This API works only with grafana version > 10.2.3.

        :param datasource_uid:
        :param builtin_role:
        :param permission:
        :return:
        """
        payload = DatasourcePermissionUpdateModel.validate({"permission": permission}).to_payload()
        datasource_path = "/access-control/datasources/%s/builtInRoles/%s" % (datasource_uid, builtin_role)
        return await self.client.POST(datasource_path, json=payload)
