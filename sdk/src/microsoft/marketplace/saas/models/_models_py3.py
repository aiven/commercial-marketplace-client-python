# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
from typing import List, Optional, Union

import msrest.serialization

from ._metering_api_enums import *


class UsageEvent(msrest.serialization.Model):
    """UsageEvent.

    :param resource_id: Subscription ID for the event.
    :type resource_id: str
    :param quantity: Number of units consumed.
    :type quantity: long
    :param dimension: Dimension identifier.
    :type dimension: str
    :param effective_start_time: Time in UTC when the usage event occurred.
    :type effective_start_time: ~datetime.datetime
    :param plan_id: Plan associated with the purchased offer.
    :type plan_id: str
    """

    _attribute_map = {
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
        'dimension': {'key': 'dimension', 'type': 'str'},
        'effective_start_time': {'key': 'effectiveStartTime', 'type': 'iso-8601'},
        'plan_id': {'key': 'planId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        resource_id: Optional[str] = None,
        quantity: Optional[int] = None,
        dimension: Optional[str] = None,
        effective_start_time: Optional[datetime.datetime] = None,
        plan_id: Optional[str] = None,
        **kwargs
    ):
        super(UsageEvent, self).__init__(**kwargs)
        self.resource_id = resource_id
        self.quantity = quantity
        self.dimension = dimension
        self.effective_start_time = effective_start_time
        self.plan_id = plan_id


class UsageEventBadRequestResponse(msrest.serialization.Model):
    """UsageEventBadRequestResponse.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    :param details:
    :type details: list[~microsoft.marketplace.saas.models.UsageEventBadRequestResponseDetail]
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
        'details': {'key': 'details', 'type': '[UsageEventBadRequestResponseDetail]'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        details: Optional[List["UsageEventBadRequestResponseDetail"]] = None,
        **kwargs
    ):
        super(UsageEventBadRequestResponse, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target
        self.details = details


class UsageEventBadRequestResponseDetail(msrest.serialization.Model):
    """UsageEventBadRequestResponseDetail.

    :param code:
    :type code: str
    :param message:
    :type message: str
    :param target:
    :type target: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'target': {'key': 'target', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        message: Optional[str] = None,
        target: Optional[str] = None,
        **kwargs
    ):
        super(UsageEventBadRequestResponseDetail, self).__init__(**kwargs)
        self.code = code
        self.message = message
        self.target = target


class UsageEventConflictResponse(msrest.serialization.Model):
    """UsageEventConflictResponse.

    :param code:
    :type code: str
    :param additional_info:
    :type additional_info:
     ~microsoft.marketplace.saas.models.UsageEventConflictResponseAdditionalInfo
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'str'},
        'additional_info': {'key': 'additionalInfo', 'type': 'UsageEventConflictResponseAdditionalInfo'},
    }

    def __init__(
        self,
        *,
        code: Optional[str] = None,
        additional_info: Optional["UsageEventConflictResponseAdditionalInfo"] = None,
        **kwargs
    ):
        super(UsageEventConflictResponse, self).__init__(**kwargs)
        self.code = code
        self.additional_info = additional_info


class UsageEventConflictResponseAdditionalInfo(msrest.serialization.Model):
    """UsageEventConflictResponseAdditionalInfo.

    :param usage_event_id: Unique identifier associated with the usage event.
    :type usage_event_id: str
    :param status: Accepted|NotProcessed|Expired. Possible values include: "Accepted",
     "NotProcessed", "Expired".
    :type status: str or
     ~microsoft.marketplace.saas.models.UsageEventConflictResponseAdditionalInfoStatus
    :param message_time: Time this message was created in UTC.
    :type message_time: ~datetime.datetime
    :param resource_id: Identifier of the resource against which usage is emitted.
    :type resource_id: str
    :param quantity:
    :type quantity: long
    :param dimension: Dimension identifier.
    :type dimension: str
    :param effective_start_time: Time in UTC when the usage event occurred.
    :type effective_start_time: ~datetime.datetime
    :param plan_id: Plan associated with the purchased offer.
    :type plan_id: str
    """

    _attribute_map = {
        'usage_event_id': {'key': 'usageEventId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'message_time': {'key': 'messageTime', 'type': 'iso-8601'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
        'dimension': {'key': 'dimension', 'type': 'str'},
        'effective_start_time': {'key': 'effectiveStartTime', 'type': 'iso-8601'},
        'plan_id': {'key': 'planId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        usage_event_id: Optional[str] = None,
        status: Optional[Union[str, "UsageEventConflictResponseAdditionalInfoStatus"]] = None,
        message_time: Optional[datetime.datetime] = None,
        resource_id: Optional[str] = None,
        quantity: Optional[int] = None,
        dimension: Optional[str] = None,
        effective_start_time: Optional[datetime.datetime] = None,
        plan_id: Optional[str] = None,
        **kwargs
    ):
        super(UsageEventConflictResponseAdditionalInfo, self).__init__(**kwargs)
        self.usage_event_id = usage_event_id
        self.status = status
        self.message_time = message_time
        self.resource_id = resource_id
        self.quantity = quantity
        self.dimension = dimension
        self.effective_start_time = effective_start_time
        self.plan_id = plan_id


class UsageEventOkResponse(msrest.serialization.Model):
    """UsageEventOkResponse.

    :param usage_event_id: Unique identifier associated with the usage event.
    :type usage_event_id: str
    :param status: Status of the operation. Possible values include: "Accepted", "Expired",
     "Duplicate", "Error", "ResourceNotFound", "ResourceNotAuthorized",
     "InvalidDimension|BadArgument".
    :type status: str or ~microsoft.marketplace.saas.models.UsageEventStatusEnum
    :param message_time: Time this message was created in UTC.
    :type message_time: ~datetime.datetime
    :param resource_id: Identifier of the resource against which usage is emitted.
    :type resource_id: str
    :param quantity: Number of units consumed.
    :type quantity: long
    :param dimension: Dimension identifier.
    :type dimension: str
    :param effective_start_time: Time in UTC when the usage event occurred.
    :type effective_start_time: ~datetime.datetime
    :param plan_id: Plan associated with the purchased offer.
    :type plan_id: str
    """

    _attribute_map = {
        'usage_event_id': {'key': 'usageEventId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'message_time': {'key': 'messageTime', 'type': 'iso-8601'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'quantity': {'key': 'quantity', 'type': 'long'},
        'dimension': {'key': 'dimension', 'type': 'str'},
        'effective_start_time': {'key': 'effectiveStartTime', 'type': 'iso-8601'},
        'plan_id': {'key': 'planId', 'type': 'str'},
    }

    def __init__(
        self,
        *,
        usage_event_id: Optional[str] = None,
        status: Optional[Union[str, "UsageEventStatusEnum"]] = None,
        message_time: Optional[datetime.datetime] = None,
        resource_id: Optional[str] = None,
        quantity: Optional[int] = None,
        dimension: Optional[str] = None,
        effective_start_time: Optional[datetime.datetime] = None,
        plan_id: Optional[str] = None,
        **kwargs
    ):
        super(UsageEventOkResponse, self).__init__(**kwargs)
        self.usage_event_id = usage_event_id
        self.status = status
        self.message_time = message_time
        self.resource_id = resource_id
        self.quantity = quantity
        self.dimension = dimension
        self.effective_start_time = effective_start_time
        self.plan_id = plan_id
