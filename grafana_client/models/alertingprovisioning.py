from .base import GrafanaBaseModel


class AlertRuleModel(GrafanaBaseModel):
    pass


class AlertRuleGroupModel(GrafanaBaseModel):
    pass


class ContactPointModel(GrafanaBaseModel):
    pass


class NotificationPolicyModel(GrafanaBaseModel):
    pass


class MuteTimingModel(GrafanaBaseModel):
    pass


class TemplateModel(GrafanaBaseModel):
    pass


__all__ = [
    "AlertRuleModel",
    "AlertRuleGroupModel",
    "ContactPointModel",
    "NotificationPolicyModel",
    "MuteTimingModel",
    "TemplateModel",
]
