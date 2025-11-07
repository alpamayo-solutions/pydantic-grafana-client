from ...models import (
    FolderCreateModel,
    FolderMoveModel,
    FolderPermissionsModel,
    FolderUpdateModel,
    FolderUserPermissionsModel,
)
from ..base import Base


class Folder(Base):
    def __init__(self, client):
        super(Folder, self).__init__(client)
        self.client = client

    async def get_all_folders(self, parent_uid=None):
        """

        :return:
        """
        path = "/folders"
        params = {}
        if parent_uid:
            params["parentUid"] = parent_uid
        return await self.client.GET(path, params=params)

    async def get_folder(self, uid):
        """

        :param uid:
        :return:
        """
        path = "/folders/%s" % uid
        return await self.client.GET(path)

    async def create_folder(self, title, uid=None, parent_uid=None):
        """

        :param title:
        :param uid:
        :param parent_uid:
        :return:
        """
        payload = FolderCreateModel.validate(
            {
                "title": title,
                "uid": uid,
                "parentUid": parent_uid,
            }
        ).to_payload()
        return await self.client.POST("/folders", json=payload)

    async def move_folder(self, uid, parent_uid):
        """
        Move a folder beneath another parent folder.

        This is relevant only if nested folders are enabled.

        :param uid:
        :param parent_uid:
        :return:
        """
        payload = FolderMoveModel.validate({"parentUid": parent_uid}).to_payload()
        path = "/folders/%s/move" % uid
        return await self.client.POST(path, json=payload)

    async def update_folder(self, uid, title=None, version=None, overwrite=False, new_uid=None):
        """

        :param uid:
        :param title:
        :param version:
        :param overwrite:
        :param new_uid:
        :return:
        """
        payload = FolderUpdateModel.validate(
            {
                "uid": new_uid,
                "title": title,
                "version": version,
                "overwrite": overwrite,
            }
        ).prepare_payload()

        path = "/folders/%s" % uid
        return await self.client.PUT(path, json=payload)

    async def delete_folder(self, uid):
        """

        :param uid:
        :return:
        """
        path = "/folders/%s" % uid
        return await self.client.DELETE(path)

    async def get_folder_by_id(self, folder_id):
        """

        :param folder_id:
        :return:
        """
        path = "/folders/id/%s" % folder_id
        return await self.client.GET(path)

    async def get_folder_permissions(self, uid):
        """

        :return:
        """
        path = "/folders/%s/permissions" % uid
        return await self.client.GET(path)

    async def update_folder_permissions(self, uid, items):
        """

        :param uid:
        :param items:
        :return:
        """
        payload = FolderPermissionsModel.validate({"items": items}).to_payload()
        update_folder_permissions_path = "/folders/%s/permissions" % uid
        return await self.client.POST(update_folder_permissions_path, json=payload)

    async def update_folder_permissions_for_user(self, uid, user_id, items):
        """

        :param uid:
        :param user_id:
        :param items:
            {"permission": "View"} or {"permission": "Edit"} or {"permission": ""}
        :return:
        """

        normalized = [FolderUserPermissionsModel.validate(item).to_payload() for item in items]
        update_folder_permissions_path_for_user = "/access-control/folders/%s/users/%s" % (uid, user_id)
        return await self.client.POST(update_folder_permissions_path_for_user, json=normalized)
